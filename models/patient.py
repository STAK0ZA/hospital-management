from odoo import models,fields,api

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Hospital Patient"

    name=fields.Char(string="Patient" ,tracking=True)
    age=fields.Integer(string="age",tracking=True)
    gender=fields.Selection([('male','Male'),('female','Female')],string="Gender")
    code=fields.Char(string="Code")
    active=fields.Boolean(string="Active")
    