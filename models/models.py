# -*- coding: utf-8 -*-

from odoo import models, fields, api


class sewa_mobil(models.Model):
    _name = 'sewa_mobil.sewa_mobil'
    _description = 'sewa_mobil.sewa_mobil'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
