from odoo import api, fields, models

class feedback(models.Model):
    _name = "feedback"
    _description = "course feedback"

    name = fields.Char("Tên học viên", required=True)
    id_name = fields.Char("Tên khóa học", required=True)
    id_cart = fields.Char("CCCD/CMND", required=True)
    fb = fields.Text("Phản hồi")

