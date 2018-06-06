# coding=utf-8

import xlrd
import odoorpc
import ssl
import os


ROOT_PATH = '/Users/zhengxiang/Desktop/Library/CAD/'


def connect_odoo(url, port, db, login, password, protocol):
    # 获取实例连接参数
    # 跟进ssl参数，使用相应协议进行连接
    ssl._create_default_https_context = ssl._create_unverified_context
    # protocol = 'jsonrpc+ssl' if config.getboolean(section, 'ssl') else 'jsonrpc'
    # 连接数据库
    odoo = odoorpc.ODOO(url, port=port, protocol=protocol, version='9.0', timeout=1000)
    # 登录远程系统:数据库/用户名/密码
    odoo.login(db, login, password)
    return odoo


def get_field_values(filename, index, field_map):
    wb = xlrd.open_workbook(filename)
    sheet = wb.sheet_by_index(index)

    values = []
    for row in range(1, sheet.nrows):
        values.append([sheet.cell(row, column).value for column in range(sheet.ncols)])

    field_values = []
    for value in values:
        field_value = {}
        for index, field in enumerate(field_map):
            if not field or not value[index]:
                continue

            if field in field_value:
                if not isinstance(field_value[field], (list, tuple)):
                    field_value[field] = [field_value[field]]

                field_value[field].append(value[index])
            else:
                field_value[field] = value[index]

        field_values.append(field_value)

    return field_values


def get_model_maps(odoo, model, key, value):
    model_values = odoo.env[model].search_read([], [key, value])

    maps = {}
    for model_value in model_values:
        maps[model_value[key]] = model_value[value]

    return maps


def get_map_ids(name_id_maps, code_name_maps, codes):
    if not codes:
        return []

    if not isinstance(codes, (list, tuple)):
        codes = [codes]

    res = []
    for code in codes:
        name = code_name_maps.get(code.strip(), '').strip()
        id = name_id_maps.get(name)

        if not id:
            print 'Error Get', code, name
        else:
            res.append(id)

    return res


def get_file_content(path, root_path=None):
    path = path.replace('\\', '/')
    full_path = os.path.join(root_path or ROOT_PATH, path)
    if not os.path.exists(full_path):
        print 'File Not Exists', path
        return '', ''
    else:
        with open(full_path, 'r') as fp:
            content = fp.read()

        return os.path.basename(full_path), content

