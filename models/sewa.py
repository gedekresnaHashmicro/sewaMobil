
from odoo import api, fields, models
from .mobil import Mobil


class Sewa(models.Model):
    _name = 'mobil.sewa'
    _description = 'Form sewa mobil'

    name = fields.Char(string='Name')

    mobil_ids = fields.One2many(comodel_name='mobil.sewadetail', inverse_name='sewa_id', string='Pilih Tipe mobil')

    pemesan = fields.Many2one(comodel_name='res.partner', string='pemesanan', domain=[('is_customernya','=',True)],store=True)

    tgl_sewa = fields.Date(string='Tanggal Sewa')

    lama_sewa = fields.Integer(string='Lama Sewa')

    total = fields.Float(compute='_compute_total', string='Total')

    @api.depends('mobil_ids')
    def _compute_total(self):
        for record in self:
            record.total = record.mobil_ids.harga * record.lama_sewa

    @api.model
    def create(self, values):
        record =  super(Sewa, self).create(values)
        if record.mobil_ids:
            self.env['mobil.list'].search([('id','=',record.mobil_ids.mobil_tipe_id.id)]).write({'sedang_disewa':True})
            return record  
  
class SewaDetail(models.Model):
    _name = 'mobil.sewadetail'
    _description = 'New Description'

    sewa_id = fields.Many2one(comodel_name='mobil.sewa', string='Sewa')
  
    mobil_tipe_id = fields.Many2one(comodel_name='mobil.list', string='Tipe Mobil',domain=[('sedang_disewa','!=',True)])

    name = fields.Char(string='Name')

    harga = fields.Float(compute='_compute_harga', string='harga')
    
    @api.depends('mobil_tipe_id')
    def _compute_harga(self):
        for record in self:
            record.harga = record.mobil_tipe_id.harga

   
    

    

  
    
    
   


   
    
    