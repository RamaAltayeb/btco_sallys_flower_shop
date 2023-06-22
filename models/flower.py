from odoo import fields, models


class Flower(models.Model):
    _name = 'flower'
    _description = 'Flower'

    name = fields.Char(required=True)
    scientific_name = fields.Char()
    season_date_start = fields.Date()
    season_date_end = fields.Date()
    watering_frequency = fields.Integer(help='Should be watered once every x days')
    watering_amount = fields.Float(help='In milliliters')

    def name_get(self):
        return [(record.id, '%s (%s)' % (record.name, record.scientific_name)) for record in self]