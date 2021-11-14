from odoo import api, fields, models

class teacher(models.Model):
    _inherit = "hr.employee"

    chung_chi = fb = fields.Text("Kinh nghiệm")