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
        'security/ir.model.access.csv',
        'views/flower.xml',
        'views/product_product.xml',
        'views/product_template.xml',
        'views/sale_order.xml',
        'views/templates.xml',
    ],
}
