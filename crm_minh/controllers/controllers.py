# -*- coding: utf-8 -*-
# from odoo import http


# class CrmReview(http.Controller):
#     @http.route('/crm_review/crm_review', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/crm_review/crm_review/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('crm_review.listing', {
#             'root': '/crm_review/crm_review',
#             'objects': http.request.env['crm_review.crm_review'].search([]),
#         })

#     @http.route('/crm_review/crm_review/objects/<model("crm_review.crm_review"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('crm_review.object', {
#             'object': obj
#         })
