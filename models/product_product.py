from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    def _get_gardeners_domain(self):
        return [('id', 'in', self.env.ref('btco_sallys_flower_shop.gardner_user').users.ids)]

    flower_id = fields.Many2one('flower')
    need_watering = fields.Boolean(compute='_compute_need_watering')
    sequence_id = fields.Many2one('ir.sequence', 'Serial Sequence')
    gardeners_ids = fields.Many2many('res.users', domain=_get_gardeners_domain)

    def _compute_need_watering(self):
        for record in self:
            record.need_watering = False
            if record.is_flower and record.flower_id:
                lots = record.stock_quant_ids.filtered(lambda x: x.quantity > 0).mapped('lot_id')
                if any(lots.mapped('need_watering')):
                    record.need_watering = True