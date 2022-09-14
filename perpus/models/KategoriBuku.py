from odoo import api, fields, models


class KategoriBuku(models.Model):
    _name = 'perpus.kategoribuku'
    _description = 'New Description'

    name = fields.Selection([
        ('karya umum', 'Karya Umum'),
        ('teknologi', 'Teknologi'),
        ('filsafat', 'Filsafat'),
        ('ilmu murni', 'Ilmu Murni'),
        ('sejarah', 'Sejarah'),
    ], string='Nama Kategori')
    kode_kategori = fields.Char(string='Kode Kategori Buku')

    @api.onchange('name')
    def _onchange_kode_kategori(self):
        if self.name == 'karya umum':
            self.kode_kategori = 'KU01'
        elif self.name == 'teknologi':
            self.kode_kategori = 'TEK02'
        elif self.name == 'filsafat':
            self.kode_kategori = 'FIL03'
        elif self.name == 'ilmu murni':
            self.kode_kategori = 'ILNI04'
        elif self.name == 'sejarah':
            self.kode_kategori = 'SEJ05'

    kode_rak = fields.Char(string='Kode Rak')
    daftarbuku_ids = fields.One2many(comodel_name='perpus.daftarbuku', inverse_name='kategoribuku_id', string='Daftar Buku')
    jml_judul = fields.Char(compute='_compute_jml_judul', string='Jumlah Judul')

    @api.depends('daftarbuku_ids')
    def _compute_jml_judul(self):
        for record in self:
            a = self.env['perpus.daftarbuku'].search([('kategoribuku_id', '=', record.id)]).mapped('name')
            b = len(a)
            record.jml_judul = b
            record.daftar = a
    
    daftar = fields.Char(string='Daftar Isi')