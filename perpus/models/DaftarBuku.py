from odoo import api, fields, models


class DaftarBuku(models.Model):
    _name = 'perpus.daftarbuku'
    _description = 'New Description'

    name = fields.Char(string='Judul')
    pengarang = fields.Char(string='Pengarang')
    penerbit = fields.Char(string='Penerbit')
    jumlah_buku = fields.Integer(string='Stok')
    kategoribuku_id = fields.Many2one(comodel_name='perpus.kategoribuku', string='Kategori Buku', ondelete='cascade')
    distributor_id = fields.Many2many(comodel_name='perpus.distributor', string='Distributor')