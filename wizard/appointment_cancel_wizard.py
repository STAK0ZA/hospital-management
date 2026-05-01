from odoo import api, fields, models

class AppointmentCancelWizard(models.TransientModel):
    _name = 'appointment.cancel'
    _description = 'Appointment Cancel Wizard'

    appointment_id = fields.Many2one('hospital.appointment',string="Appointment")
    reason =fields.Text(string="Reason")


    def cancel_appointment(self):
        return