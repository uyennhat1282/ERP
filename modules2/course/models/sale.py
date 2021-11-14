from odoo import api, fields, models

class Sale(models.Model):
    _inherit = "sale.order"
    target = fields.Text("Mục tiêu đăng kí", required=True)



