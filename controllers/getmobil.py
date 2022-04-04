from odoo import http, fields, models
from odoo.http import request
import json


class MobilController(http.Controller):
    @http.route(['/mobil','/mobil/<int:idnya>'],auth='public',methods=['GET'], csrf=True,type='json')
    def getMobil(self, idnya=None,**kwargs):
        mobil = request.env['mobil.list'].search([])
        value=[]
        if not idnya:
            for m in mobil:
                value.append({
                    "id":m.id,
                    "plat":m.plat,
                    "tipe":m.tipe,
                    "harga":m.harga,
                    "transmisi":m.transmisi,
                    "brand":m.brand,
                    "disewa":m.disewa,
                })
            return json.dumps(value)
        else:
            mobil_id = request.env['mobil.list'].search([('id','=',idnya)])
            for m in mobil_id:
                value.append({
                    "id":m.id,
                    "plat":m.plat,
                    "tipe":m.tipe,
                    "harga":m.harga,
                    "transmisi":m.transmisi,
                    "brand":m.brand,
                    "disewa":m.disewa,
                })
            return json.dumps(value)

    @http.route('/createmobil',auth='user', methods=['POST'],type='json')
    def createMobil(self, **kw):
        if request.jsonrequest:
            if kw['tipe']:
                vals={
                    "plat":kw['plat'],
                    "tipe":kw['tipe'],
                    "harga":kw['harga'],
                    "transmisi":kw['transmisi'],
                    "brand":kw['brand'],
                    "disewa":kw['disewa'],
                }
                mobil_baru = request.env['mobil.list'].create(vals)
                args = {'success':True, 'ID':mobil_baru.id}
                return args

    @http.route(['/deletemobil','/deletemobil/<int:idnya>'],auth='user',methods=['DELETE'],type='json')
    def deleteMobil(self, idnya=None, **kw):
        if idnya:
            mobil_id = request.env['mobil.list'].search([('id','=',idnya)]).unlink()
            return mobil_id