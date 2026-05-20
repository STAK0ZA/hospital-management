from xlsxwriter.contenttypes import defaults
from odoo.exceptions import ValidationError
from odoo import api, fields, models,_

class AppointmentCancelWizard(models.TransientModel):
    _name = 'appointment.cancel'
    _description = 'Appointment Cancel Wizard'


    @api.model
    def default_get(self,vals):
        rec=super().default_get(vals)
        rec['cancel_date']= fields.Date.today()
        print(self.env.context.get('active_id'))
        rec['appointment_id']=self.env.context.get('active_id')
        return rec


    appointment_id = fields.Many2one('hospital.appointment',string="Appointment")
    reason =fields.Text(string="Reason")
    cancel_date=fields.Datetime(string="Cancel Date" )


    def cancel_appointment(self):
        for rec in self:
            print(rec.cancel_date.date())
            print(rec.appointment_id.date_now)
            # print(rec.env['hospital.appointment'].browse(self.env.context.get('active_id')).date_now)

            if rec.cancel_date.date() == rec.appointment_id.date_now.date():
                raise ValidationError(_("sorry u cant cancel in same date"))
            else:
                rec.appointment_id.state = "cancel"

        return



