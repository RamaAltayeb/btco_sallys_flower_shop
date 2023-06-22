from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_flower = fields.Boolean()
    flower_id = fields.Many2one('flower', compute='_compute_flower', inverse='_set_flower')

    @api.depends('product_variant_ids.flower_id')
    def _compute_flower(self):
        self.flower_id = False
        for template in self:
            variant_count = len(template.product_variant_ids)
            if variant_count == 1:
                template.flower_id = template.product_variant_ids.flower_id
            elif variant_count == 0:
                archived_variants = template.with_context(active_test=False).product_variant_ids
                if len(archived_variants) == 1:
                    template.flower_id = archived_variants.flower_id

    def _set_flower(self):
        variant_count = len(self.product_variant_ids)
        if variant_count == 1:
            self.product_variant_ids.flower_id = self.flower_id
        elif variant_count == 0:
            archived_variants = self.with_context(active_test=False).product_variant_ids
            if len(archived_variants) == 1:
                archived_variants.flower_id = self.flower_id