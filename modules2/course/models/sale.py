from odoo import api, fields, models

class Sale(models.Model):
    _inherit = "sale.order"
    id_cart = fields.Char("CCCD/CMND", required=True)
    phone = fields.Char("Số điện thoại", required=True)



