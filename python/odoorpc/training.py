from utils import *
from pprint import pprint
import base64

training_field_map = [
    'title',
    'attachment',
    'name'
]

ROOT_PATH = '/Users/zhengxiang/Desktop/Training/'

training_values = get_field_values('training.xlsx', 0, training_field_map)

odoo = connect_odoo('thermo.peoplus.cn', 443, 'thermo', 'system', 'S57peopluS', 'jsonrpc+ssl')
# odoo = connect_odoo('thermouat.peoplus.cn', 443, 'thermo_uat', 'system', 'admin', 'jsonrpc+ssl')
# odoo = connect_odoo('localhost', 8888, 'uat0517', 'system', 'admin', 'jsonrpc')

course_ids = odoo.env['course.arrangement'].search([])
odoo.env['course.arrangement'].write(course_ids, {'state': 'released'})

# course_ids = odoo.env['course.management'].search([])
# odoo.env['course.management'].write(course_ids, {'state_id': 2})

# index = 0
# 44-46 47
# for training in training_values[54:]:
#     print '--------index--------', index
#     index += 1
#     management = odoo.env['course.management'].search([('name', '=', training['title'])])
#
#     filename, content = get_file_content(training['attachment'], root_path=ROOT_PATH)
#
#     content = base64.b64encode(content)
#     attachment_id = odoo.env['web.video'].save_file('course.arrangement', filename, content)
#
#     employee_ids = odoo.env['hr.employee'].search([])
#
#     vals = {
#         'course_id': management[0],
#         'name': training['name'],
#         'course_start_time': '2018-05-20',
#         'course_end_time': '2019-05-21',
#         'attachment_ids': [[6, 0, [attachment_id]]],
#         'employee_ids': [[6, 0, employee_ids]],
#         'state': 'released',
#     }
#
#     odoo.env['course.arrangement'].create(vals)

# for training in training_values:
#     file_name, content = get_file_content(training['attachment'], root_path=ROOT_PATH)
#
#     print file_name, len(content)
