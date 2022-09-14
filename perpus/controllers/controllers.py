from crypt import methods
import json

from odoo import http, models, fields
from odoo.http import request


class Perpus(http.Controller):
    @http.route('/perpus/getdaftarbuku', auth='public', method=['GET'])
    def getDaftarBuku(self, **kw):
        daftarbuku = request.env['perpus.daftarbuku'].search([])
        items = []

        for item in daftarbuku:
            items.append({
                'Judul Buku': item.name,
                'Pengarang': item.pengarang,
                'Penerbit': item.penerbit,
                'Jumlah Buku': item.jumlah_buku
            })
        
        return json.dumps(items)

    @http.route('/perpus/getdistributor', auth='public', method=['GET'])
    def getDistributor(self, **kw):
        distributor = request.env['perpus.distributor'].search([])
        items = []

        for item in distributor:
            items.append({
                'Nama Distributor': item.name,
                'Alamat': item.alamat,
                'No. Telepon': item.no_telp,
                'Daftar Buku': item.daftarbuku_id[0].name
            })
        
        return json.dumps(items)