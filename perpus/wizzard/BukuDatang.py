from odoo import api, fields, models


class BukuDatang(models.TransientModel):
    _name = 'perpus.bukudatang'

    daftarbuku_id = fields.Many2one(comodel_name='perpus.daftarbuku', string='Nama Buku', required=True)
    jumlah = fields.Integer(string='Jumlah', required=False)

    def button_buku_datang(self):
        for line in self:
            self.env['perpus.daftarbuku'].search([('id', '=', line.daftarbuku_id.id)]).write(
                {'jumlah_buku': line.daftarbuku_id.jumlah_buku +  line.jumlah}
            )