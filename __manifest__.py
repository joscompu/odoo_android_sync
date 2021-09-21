# -*- coding: utf-8 -*-
{
    'name': "odoo_android_sync",

    'summary': """
        Module to sync assistance information from an Android App """,

    'description': """
        Module to sync assistance information from an Android App
    """,

    'author': "Jose Calderon",
    'website': "http://www.osm-soft.io",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr_attendance'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
