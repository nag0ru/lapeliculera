# -*- coding: utf-8 -*-
# from odoo import http


# class Lapeliculera(http.Controller):
#     @http.route('/lapeliculera/lapeliculera', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lapeliculera/lapeliculera/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('lapeliculera.listing', {
#             'root': '/lapeliculera/lapeliculera',
#             'objects': http.request.env['lapeliculera.lapeliculera'].search([]),
#         })

#     @http.route('/lapeliculera/lapeliculera/objects/<model("lapeliculera.lapeliculera"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lapeliculera.object', {
#             'object': obj
#         })
