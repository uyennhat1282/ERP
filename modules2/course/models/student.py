from odoo import api, fields, models

class student(models.Model):
    _inherit = "res.partner"

    #id_cart = fields.Char("CCCD/CMND", required=True,)
    #ngay_sinh = fields.Date("Ngày sinh")
    #gioi_tinh = fields.Selection([
     #   ('nam', 'Nam'),
     #   ('nu', 'Nữ'),
      #  ('khac','Khác'),
  #  ], default='nam', string='Giới tính')