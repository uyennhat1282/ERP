{
    'name': "Course",
    'summary': """Management""",
    'description': """App Quản lý khóa học""",
    'author': "nhom1",

    'category': 'Uncategorized',
    'version': '1.1',
    'depends': [
        "sale",
        'product',
        "base",
    ],
    'data': [
        'views/course_information.xml',
        'views/khoahoc.xml',
         'views/sale.xml',
        'views/student.xml',
        'views/teacher.xml',
        'views/feedback.xml',
        'views/report_view.xml',
        # 'security/ir.model.access.csv',
        #'report/report.xml',
    ],
    'demo': [

    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}