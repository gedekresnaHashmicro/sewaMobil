# -*- coding: utf-8 -*-
# from odoo import http


# class SewaMobil(http.Controller):
#     @http.route('/sewa_mobil/sewa_mobil/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sewa_mobil/sewa_mobil/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sewa_mobil.listing', {
#             'root': '/sewa_mobil/sewa_mobil',
#             'objects': http.request.env['sewa_mobil.sewa_mobil'].search([]),
#         })

#     @http.route('/sewa_mobil/sewa_mobil/objects/<model("sewa_mobil.sewa_mobil"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sewa_mobil.object', {
#             'object': obj
#         })
