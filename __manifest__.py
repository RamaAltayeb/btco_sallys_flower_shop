# -*- coding: utf-8 -*-
{
    'name': "BTCO Sally's Flower Shop",

    'summary': """
    """,

    'description': """
    """,

    'author': 'Rama Altayeb',
    'website': '',
    'category': '',
    'version': '16.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['product', 'stock', 'sale', 'website_sale'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/flower_product_product_record_rules.xml',
        'security/ir.model.access.csv',

        'data/paper_format.xml',
        'data/server_actions.xml',

        'views/flower.xml',
        'views/product_product.xml',
        'views/product_template.xml',
        'views/sale_order.xml',
        'views/stock_lot.xml',

        'views/templates.xml',

        'reports/sale_order_flowers.xml',
    ],
}
