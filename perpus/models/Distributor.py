from odoo import api, fields, models


class Distibutor(models.Model):
    _name = 'perpus.distributor'
    _description = 'New Description'

    name = fields.Char(string='Nama Distributor')
    alamat = fields.Char(string='Alamat')
    no_telp = fields.Char(string='No. Telepon')
    daftarbuku_id = fields.Many2many(comodel_name='perpus.daftarbuku', string='Buku')