# -*- coding: utf-8 -*-
# from odoo import http


# class OdooAndroidSync(http.Controller):
#     @http.route('/odoo_android_sync/odoo_android_sync/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_android_sync/odoo_android_sync/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_android_sync.listing', {
#             'root': '/odoo_android_sync/odoo_android_sync',
#             'objects': http.request.env['odoo_android_sync.odoo_android_sync'].search([]),
#         })

#     @http.route('/odoo_android_sync/odoo_android_sync/objects/<model("odoo_android_sync.odoo_android_sync"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_android_sync.object', {
#             'object': obj
#         })
