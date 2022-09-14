from odoo import models, fields


class PartnerXlsx(models.AbstractModel):
    _name = 'report.perpus.report_distributor_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    tgl_laporan = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, distributor):
        sheet = workbook.add_worksheet('Daftar Distributor')
        sheet.write(0, 0, str(self.tgl_laporan))
        sheet.write(1, 0, 'Nama Distributor')
        sheet.write(1, 1, 'Alamat')
        sheet.write(1, 2, 'No. Telepon')
        sheet.write(1, 3, 'Buku')
        
        row = 2
        col = 0
        for obj in distributor:
            col = 0
            sheet.write(row, col, obj.name)
            sheet.write(row, col + 1, obj.alamat)
            sheet.write(row, col + 2, obj.no_telp)

            for item in obj.daftarbuku_id:
                sheet.write(row, col + 3, item.name)
                col += 1
            row += 1