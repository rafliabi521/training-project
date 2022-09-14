from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'New Description'

    is_anggota = fields.Boolean(string='Is Anggota')
    level = fields.Char(string='Member')