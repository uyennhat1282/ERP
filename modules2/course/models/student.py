from odoo import api, fields, models

class student(models.Model):
    _inherit = "res.partner"


    #ngay_sinh = fields.Date("Ngày sinh")
    #gioi_tinh = fields.Char("Giới tính")