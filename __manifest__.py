# -*- coding: utf-8 -*-
{
    'name': "Paint & Decor Store Management",
    'summary': "Manage custom properties for paints, wallpapers, and decor products",
    'description': """
Paint & Decor Store Management Module for Odoo 17
=================================================
* Color codes and HEX management for paint and wallpaper products.
* Coverage rate calculation per liter.
* Classification and categorisation for painting tools and equipment.
    """,
    'author': "Sara Claket",
    'category': 'Sales/Sales',
    'version': '17.0.1.0.0',
    'license': 'LGPL-3',
    'depends': ['base', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
}