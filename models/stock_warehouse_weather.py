from odoo import fields, models


class StockWarehouseWeather(models.Model):
    _name = 'stock.warehouse.weather'
    _description = 'Stock Warehouse Weather'
    _order = 'capture_time desc'

    stock_warehouse_id = fields.Many2one('stock.warehouse')
    temperature = fields.Float()
    pressure = fields.Float()
    humidity = fields.Float()
    wind_speed = fields.Float()
    rain_volume = fields.Float()
    capture_time = fields.Datetime()
