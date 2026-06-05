from odoo import api, fields, models

class Invoice_koko(models.Model):
    _inherit = "account.move"

    invoice_koko=fields.Char(string="Invoice Koko")


class Invoice_koko_line(models.Model):
    _inherit = "account.move.line"

    number=fields.Char(string="Number")
