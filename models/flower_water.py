from odoo import fields, models


class FlowerWater(models.Model):
    _name = 'flower.water'
    _description = 'Flower Water'
    _order = 'water_datetime desc'

    water_datetime = fields.Datetime()
    serial_id = fields.Many2one('stock.lot')
