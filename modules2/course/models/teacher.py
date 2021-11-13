from odoo import api, fields, models

class teacher(models.Model):
    _inherit = "res.partner"
    #gioi_tinh = fields.Selection([
     #   ('male', 'Male'),
      #  ('female', 'Female')
  #  ], default='male', string='Giới tính')