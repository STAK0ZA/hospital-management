from email.policy import default

from odoo import models,fields,api

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Hospital Appointment"

    patient_id = fields.Many2one('hospital.patient' , string="Patient Name")
    date_now=fields.Datetime(string="Date of Appointment" ,default=fields.Datetime.now())
    date_day=fields.Date(string="Date of Appointment" , default=fields.Date.context_today)
    patient_gender=fields.Selection(string="Patient Gender" , related="patient_id.gender")
    