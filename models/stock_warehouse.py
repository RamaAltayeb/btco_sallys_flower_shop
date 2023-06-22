from odoo import fields, models
from datetime import datetime
import requests

class StockWarehouse(models.Model):
    _inherit = 'stock.warehouse'

    stock_warehouse_weather_ids = fields.One2many('stock.warehouse.weather', 'stock_warehouse_id')

    def fetch_weather_data(self):
        for record in self.get_warehouses_with_location_info():
            api_key, lat, lng = record.get_api_request_params()
            url = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}".format(lat, lng, api_key)
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                entries = response.json()
                self.env["stock.warehouse.weather"].create({
                    "stock_warehouse_id": record.id,
                    "pressure": entries["main"]["pressure"],
                    "temperature": entries["main"]["temp"],
                    "humidity": entries["main"]["humidity"] / 100,
                    "wind_speed": entries["wind"]["speed"],
                    "rain_volume": entries["rain"]["1h"] if "rain" in entries else 0,
                    "capture_time": fields.Datetime.now(),
                })
            except:
                continue

    def get_forecast_for_today_and_water_flowers(self):
        date_format = '%Y-%m-%d %H:%M:%S'
        first_compare_datetime = datetime.now().replace(hour=9, minute=0, second=0)
        second_compare_datetime = datetime.now().replace(hour=18, minute=0, second=0)
        for record in self.get_warehouses_with_location_info():
            api_key, lat, lng = record.get_api_request_params()
            url = "https://api.openweathermap.org/data/2.5/forecast?lat={}&lon={}&appid={}".format(lat, lng, api_key)
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                entries = response.json()
                entries = list(filter(lambda x: first_compare_datetime <= datetime.strptime(x['dt_txt'], date_format) <= second_compare_datetime, entries['list']))
                entries = list(filter(lambda x: 'rain' in x and x['rain']['3h'] > 0.2, entries))
                if entries:
                    flowers_serial = self.env['stock.quant'].search([('warehouse_id', '=', record.id)]).lot_id
                    flowers_serial.action_water_flower()
            except:
                continue


    def get_api_request_params(self):
        self.ensure_one()
        api_key = self.env["ir.config_parameter"].sudo().get_param("btco_sallys_flower_shop.weather_api_key")
        return api_key, self.partner_id.partner_latitude, self.partner_id.partner_longitude

    def get_warehouses_with_location_info(self):
        return self.filtered(lambda x: x.partner_id and x.partner_id.partner_latitude and x.partner_id.partner_longitude)