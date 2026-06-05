from odoo import api, fields, models

class ProductInherital(models.Model):
    _inherit = "sale.order"

    koko_field=fields.Char(string="Koko Field")

    def _prepare_invoice(self):
        x= super()._prepare_invoice()
        x['invoice_koko']=self.koko_field
        return x

    def action_confirm(self):
        print("hi--------------------------------..............")
        return super().action_confirm()