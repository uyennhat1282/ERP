from odoo import api, fields, models

class courseinformation(models.Model):
    _name = "course.information"
    _description = "course management"

    name = fields.Char("Tên khóa học", required=True)

    type_course = fields.Selection([
        ('online', 'Online'),
        ('offline', 'Offline')
    ], default='online', string='Hình thức học')
    course_image = fields.Binary("course Image", attachment=True, help="course Image")
    teacher = fields.Char("Người dạy")
    day = fields.Date("Ngày học")
    time = fields.Char("Giờ học")
    tuition = fields.Float("Học phí")

