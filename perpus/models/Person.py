from odoo import api, fields, models


class Person(models.Model):
    _name = 'perpus.person'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    alamat = fields.Char(string='Alamat')
    tgl_lahir = fields.Date(string='Tanggal Lahir')


class Pustakawan(models.Model):
    _name = 'perpus.pustakawan'
    _inherit = 'perpus.person'
    _description = 'New Description'

    id_pustakawan = fields.Char(string='ID Pustakawan')
