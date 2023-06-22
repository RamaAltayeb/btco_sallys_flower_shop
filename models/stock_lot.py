from odoo import fields, models, api
from datetime import datetime, timedelta

class StockLot(models.Model):
    _inherit = 'stock.lot'

    flower_water_ids = fields.One2many('flower.water', 'serial_id')
    is_flower = fields.Boolean(related='product_id.is_flower')
    flower_id = fields.Many2one(related='product_id.flower_id')

    def action_water_flower(self):
        for record in self.filtered(lambda x: x.is_flower and x.flower_id):
                watering_frequency = record.flower_id.watering_frequency
                if not record.flower_water_ids or \
                   record.flower_water_ids[-1].water_datetime + timedelta(days=watering_frequency) <= datetime.now():
                    self.env['flower.water'].create({'water_datetime': datetime.now(),
                                                     'serial_id': record.id})


