from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError

class Peminjaman(models.Model):
    _name = 'perpus.peminjaman'
    _description = 'Peminjaman'

    name = fields.Char(string='No. Nota')
    nama_peminjam = fields.Char(string='Nama Peminjam')
    tgl_peminjaman = fields.Datetime(
        string='Tanggal Peminjaman',
        default=fields.Datetime.now())
    total_buku = fields.Integer(
        string='Total Buku',
        compute='_compute_totalbuku')
    detailpeminjaman_ids = fields.One2many(
        comodel_name='perpus.detailpeminjaman',
        inverse_name='peminjaman_id',
        string='Detail Peminjaman')

    @api.depends('detailpeminjaman_ids')
    def _compute_totalbuku(self):
        for line in self:
            result = sum(self.env['perpus.detailpeminjaman'].search(
                [('peminjaman_id', '=', line.id)]).mapped('qty'))
            line.total_buku = result
    
    @api.ondelete(at_uninstall=False)
    def __ondelete_peminjaman(self):
        if self.detailpeminjaman_ids:
            peminjaman = []
            for line in self:
                peminjaman = self.env['perpus.detailpeminjaman'].search(
                    [('peminjaman_id', '=', line.id)])
                print(peminjaman)

            for ob in peminjaman:
                print(ob.daftarbuku_id.name + ' ' + str(ob.qty))
                ob.daftarbuku_id.jumlah_buku += ob.qty
    
    def write(self, vals):
      for line in self:
          data_asli = self.env['perpus.detailpeminjaman'].search([('peminjaman_id', '=', line.id)])
          print(data_asli)

          for data in data_asli:
              print(str(data.daftarbuku_id.name) + " " + str(data.qty) + ' ' + str(data.daftarbuku_id.jumlah_buku))
              data.daftarbuku_id.jumlah_buku += data.qty
      
      line = super(Peminjaman, self).write(vals)
      
      for line in self:
          data_setelah_edit = self.env['perpus.detailpeminjaman'].search([('peminjaman_id', '=', line.id)])
          print(data_asli)
          print(data_setelah_edit)

          for data_baru in data_setelah_edit:
              if data_baru in data_asli:
                  print(data_baru.daftarbuku_id.name + " " + str(data_baru.qty) + ' ' + str(data_baru.daftarbuku_id.jumlah_buku))
                  data_baru.daftarbuku_id.jumlah_buku -= data_baru.qty
              else:
                  pass

      return line

    _sql_constraints = [
        ('no_nota_unik', 'unique (name)', 'Nomor Nota tidak boleh sama!')
    ]


class DetailPeminjaman(models.Model):
    _name = 'perpus.detailpeminjaman'
    _description = 'Detail'

    name = fields.Char(string='Nama')
    peminjaman_id = fields.Many2one(
        comodel_name='perpus.peminjaman',
        string='Detail Peminjaman')
    daftarbuku_id = fields.Many2one(
        comodel_name='perpus.daftarbuku',
        string='List Buku')
    qty = fields.Integer(string='Quantity')

    @api.depends('qty')
    def _compute_qty(self):
        for line in self:
            line.qty

    @api.onchange('daftarbuku_id')
    def _onchange_daftarbuku_id(self):
        if self.daftarbuku_id:
            self.daftarbuku_id
    
    @api.model
    def create(self, vals):
        line = super(DetailPeminjaman, self).create(vals)
        if line.qty:
            self.env['perpus.daftarbuku'].search(
                [('id', '=', line.daftarbuku_id.id)]
            ).write({'jumlah_buku': line.daftarbuku_id.jumlah_buku - line.qty})

        return line

    @api.constrains('qty')
    def check_quantity(self):
        for line in self:
            if line.qty < 1:
                raise ValidationError('Jumlah peminjaman harus minimal 1, silahkan input dengan benar.')
            elif line.daftarbuku_id.jumlah_buku < line.qty:
                raise ValidationError('Stok yang tersedia tidak mencukupi.')