from odoo import api,fields,models,tools


class SettingsHospitalApp(models.TransientModel):
    _inherit = 'res.config.settings'

    cancel_date=fields.Integer(string="Cancel Date" , config_parameter='hospital_app.cancel_date')
    sale_header_name = fields.Char(
        string="Sale Header Name",
        config_parameter="hospital_app.sale_header_name"
        )
