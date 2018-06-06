from utils import *
from pprint import pprint
import base64

# message_field_map = [
#     'title',
#     'category_ids',
#     'image',
#     '',
#     '',
#     'label_ids',
#     'label_ids',
#     'label_ids',
#     'label_ids',
#     'label_ids',
#     'label_ids',
#     'label_ids',
#     'details',
#     'attachments'
# ]
#
# category_field_map = [
#     '',
#     'first_name',
#     'second_name',
#     '',
#     'third_name',
#     '',
#     'code'
# ]
#
# label_field_map = [
#     'code',
#     'name'
# ]

# message_values = get_field_values('library.xlsx', 0, message_field_map)
# category_values = {
#     value['code']: '/'.join(map(lambda item: item.strip(), filter(lambda item: item, [value.get('first_name'), value.get('second_name'), value.get('third_name')])))
#     for value in get_field_values('library.xlsx', 1, category_field_map)
# }
#
# label_values = {
#     value['code']: value['name']
#     for value in get_field_values('library.xlsx', 2, label_field_map)
# }
#
odoo = connect_odoo('thermo.peoplus.cn', 443, 'thermo', 'system', 'S57peopluS', 'jsonrpc+ssl')

message = odoo.env['library.message'].search([('state', '=', 'draft')])

print message

odoo.env['library.message'].write(message, {"state": "publish"})

# odoo = connect_odoo('thermouat.peoplus.cn', 443, 'thermo_uat', 'system', 'admin', 'jsonrpc+ssl')
# odoo = connect_odoo('localhost', 8888, 'uat0517', 'system', 'admin', 'jsonrpc')
#
# category_maps = get_model_maps(odoo, 'library.category', 'display_complete_name', 'id')
# label_maps = get_model_maps(odoo, 'product.brochure.label', 'name', 'id')
#
# index = 0
# for message in message_values[100:]:
#     print '-------------------------------------index: %s-----------------------------' % index
#     index += 1
#
#     vals = {
#         'title': message['title'],
#         'category_ids': [[6, 0, get_map_ids(category_maps, category_values, message.get('category_ids'))]],
#         'label_ids': [[6, 0, get_map_ids(label_maps, label_values, message.get('label_ids'))]],
#         'details': message.get('details') or '',
#     }
#
#     if message.get('image'):
#         _, image = get_file_content(message.get('image'))
#         if image:
#             vals['image'] = base64.b64encode(image)
#
#     if message.get('attachments'):
#         filename, content = get_file_content(message.get('attachments'))
#         if not filename:
#             continue
#
#         attachment_vals = {
#             'name': filename,
#             'datas_fname': filename,
#             'res_model': 'library.message',
#             'res_id': 0,
#             'datas': base64.encodestring(content)
#         }
#
#         attachment_id = odoo.env['ir.attachment'].create(attachment_vals)
#         vals['attachments'] = [[6, 0, [attachment_id]]]
#
#     odoo.env['library.message'].create(vals)

# for value in message_values:
#     if value.get('category_ids'):
#         name = category_values.get(value['category_ids']).strip()
#         if not category_maps.get(name):
#             print name, category_maps.get(name)

    # if value.get('label_ids'):
    #     labels = value['label_ids']
    #     if not isinstance(labels, (list, tuple)):
    #         labels = [labels]
    #
    #     for label in labels:
    #         label = label.strip()
    #         if label:
    #             name = label_values.get(label).strip()
    #             if not label_maps.get(name):
    #                 print name, label_maps.get(name)

