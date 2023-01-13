# -*- coding: utf-8 -*-
# from odoo import http


# class Task1(http.Controller):
#     @http.route('/task_1/task_1', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/task_1/task_1/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('task_1.listing', {
#             'root': '/task_1/task_1',
#             'objects': http.request.env['task_1.task_1'].search([]),
#         })

#     @http.route('/task_1/task_1/objects/<model("task_1.task_1"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('task_1.object', {
#             'object': obj
#         })
