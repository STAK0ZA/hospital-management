from datetime import date
from email.policy import default

from odoo import models,fields,api

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Hospital Patient"

    name=fields.Char(string="Patient" ,tracking=True)
    age=fields.Integer(string="age",tracking=True ,compute='_compute_date')
    gender=fields.Selection([('male','Male'),('female','Female')],string="Gender")
    code=fields.Char(string="Code")
    birth_day=fields.Date(string="Date of Birth")

    prescription=fields.Html(string="Prescription")

    active=fields.Boolean(string="Active",default=True)

    @api.depends('birth_day')
    def _compute_date(self):
        for rec in self:
            if rec.birth_day:
                today=date.today()
                rec.age=today.year-rec.birth_day.year
            else:
                rec.age= 1
