from odoo import api, fields, models

class courseinformation(models.Model):
    _name = "course.information"
    _description = "course management"

    name = fields.Char("Tên khóa học")
    description = fields.Text("Mô tả khóa học")
    type_course = fields.Selection([
        ('online', 'Online'),
        ('offline', 'Offline')
    ], default='online', string='Hình thức học')
    course_image = fields.Binary("course Image", attachment=True, help="course Image")
    day = fields.Date("Ngày học")
    time = fields.Text("Giờ học")
    tuition = fields.Float("Học phí")

