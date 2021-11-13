from odoo import fields, models


class ProductTemplateInherit(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    description = fields.Text("Mô tả khóa học")
    teacher = fields.Char("Người dạy")
    day = fields.Date("Ngày học")
    time = fields.Char("Giờ học")
