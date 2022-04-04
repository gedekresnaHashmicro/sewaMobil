from odoo import api, fields, models


class Mobil(models.Model):
    _name = 'mobil.list'
    _description = 'Data tentang mobil dan harganya'

    _rec_name = "tipe"

    plat = fields.Char(string='Plat Nomor')
    
    tipe = fields.Char(string='Tipe')
    harga = fields.Integer(string='Harga per hari')

    transmisi = fields.Selection([
        ('manual', 'Manual'),('matic','Matic')
    ], string='Transmisi')
    
    brand = fields.Selection([
        ('honda', 'Honda'),('toyota','Toyota'),('mitsubishi','Mitsubishi'),('suzuki','Suzuki'),('daihatsu','Daihatsu')
    ], string='brand')

    sedang_disewa = fields.Boolean(string='Sedang Disewa',default=False)
    
    
    
