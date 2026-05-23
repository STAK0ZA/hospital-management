from odoo import api, fields, models

class ProductInherital(models.Model):
    _inherit = "sale.order"

    koko_field=fields.Char(string="Koko Field")


    def action_confirm(self):
        print("hi--------------------------------..............")
        return super().action_confirm()