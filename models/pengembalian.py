from odoo import api, fields, models


class Pengembalian(models.Model):
    _name = 'mobil.pengembalian'
    _description = 'New Description'

    name = fields.Char(string='Name')

    sewa_id = fields.Many2one(comodel_name='mobil.sewa', string='No. Order',domain=[('sudah_kembali','!=',True)])

    tgl_pengembalian = fields.Date(string='Tanggal Pengembalian', default=fields.Date.today())
 
    nama_penyewa = fields.Char(compute='_compute_nama_penyewa', string='nama_penyewa')


    @api.depends('sewa_id')
    def _compute_nama_penyewa(self):
        for record in self:
            record.nama_penyewa = record.sewa_id.pemesan.name

    
    tagihan = fields.Integer(compute='_compute_tagihan', string='Tagihan')

    @api.depends('sewa_id')
    def _compute_tagihan(self):
        for record in self:
            record.tagihan = record.sewa_id.total

    @api.model
    def create(self, values):
        record =  super(Pengembalian, self).create(values)
        if record.tgl_pengembalian:
            self.env['mobil.sewa'].search([('id','=',record.sewa_id.id)]).write({'sudah_kembali':True})
            self.env['mobil.list'].search([('id','=',record.sewa_id.mobil_ids.mobil_tipe_id.id)]).write({'sedang_disewa':False})
            self.env['mobil.akunting'].create({'kredit': record.tagihan,'name':record.name})
            return record
    
    def unlink(self):
        for record in self:
            self.env['mobil.sewa'].search([('id','=',record.sewa_id.id)]).write({'sudah_kembali':False})
        record = super(Pengembalian, self).unlink()
    