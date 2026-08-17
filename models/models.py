# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductTemplateDecor(models.Model):
    _inherit = 'product.template'

    main_section = fields.Selection([
        ('paint', 'Paints'),
        ('tools', 'Tools & Equipment'),
        ('wallpaper', 'Wallpaper'),
        ('decor', 'Other Decor'),
    ], string="Main Section", default='paint')

    tool_type = fields.Selection([
        ('brush', 'Paint Brush'),
        ('roller', 'Paint Roller'),
        ('tape', 'Masking Tape'),
        ('spray', 'Spray Gun'),
        ('other', 'Other'),
    ], string="Tool Type")

    color_code = fields.Char(string="Color Code")
    color_hex = fields.Char(string="Color HEX Code")

    coverage_per_liter = fields.Float(string="Coverage per Liter (sqm/L)")