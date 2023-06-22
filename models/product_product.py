from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    flower_id = fields.Many2one('flower')