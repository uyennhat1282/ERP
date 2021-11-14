from odoo import fields, models


class ProductTemplateInherit(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    description = fields.Text("Mô tả khóa học")
    teacher = fields.Many2one('hr.employee', 'Giảng viên',  required=True,)
    day = fields.Date("Ngày bắt đầu học", required=True,)
    day_time = fields.Char("Thời gian học", required=True,)
    time = fields.Char("Giờ học", required=True,)
