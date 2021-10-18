# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class course(models.Model):
    _name = "Course"
    _description = "Course model"

    name = fields.Char('Course Name', required=True)
    nickname = fields.Char('Nickname')
    description = fields.Text('Course Description')
    dob = fields.Date('DOB', required=False)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender', default='male')
    couse_image = fields.Binary("course Image", attachment=True, help="course Image")
    owner_id = fields.Many2one('res.partner', string='Owner')
    product_ids = fields.Many2many(comodel_name='product.product',
                                string="Related Products",
                                relation='course_product_rel',
                                column1='col_course_id',
                                column2='col_product_id')