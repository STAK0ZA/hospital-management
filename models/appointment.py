from email.policy import default

from odoo import models,fields,api

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread','mail.activity.mixin']
    _rec_name = 'patient_id'
    _description = "Hospital Appointment"

    patient_id = fields.Many2one('hospital.patient' , string="Patient Name")
    date_now=fields.Datetime(string="Date of Appointment" ,default=fields.Datetime.now())
    date_day=fields.Date(string="Date of Appointment" , default=fields.Date.context_today)
    patient_gender=fields.Selection(string="Patient Gender" , related="patient_id.gender")
    patient_ref=fields.Char(string="Patient Reference")

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.patient_ref = self.patient_id.code


