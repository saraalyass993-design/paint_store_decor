# -*- coding: utf-8 -*-
from odoo import http


class PaintStoreDecorController(http.Controller):

    @http.route('/paint_store/calculator', type='json', auth='public', website=True)
    def calculate_paint_needed(self, area_sqm, coverage_per_liter=10, **kw):
        area = float(area_sqm or 0)
        coverage = float(coverage_per_liter or 10)

        if area <= 0 or coverage <= 0:
            return {'status': 'error', 'message': 'Invalid area or coverage value.'}

        liters_needed = area / coverage
        return {
            'status': 'success',
            'area': area,
            'liters_needed': round(liters_needed, 2),
        }