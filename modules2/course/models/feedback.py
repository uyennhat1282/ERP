from odoo import api, fields, models

class feedback(models.Model):
    _name = "feedback"
    _description = "course feedback"


    id_name =fields.Many2one('product.template', 'Tên khóa học',  required=True,)
    name = fields.Char('Tên học viên', required=True, )
    fb = fields.Text("Phản hồi")

