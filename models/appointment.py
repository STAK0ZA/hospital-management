from email.policy import default

from odoo import models,fields,api,_
from odoo.exceptions import ValidationError


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread','mail.activity.mixin']
    _rec_name = 'patient_id'
    _description = "Hospital Appointment"

    patient_id = fields.Many2one('hospital.patient' , string="Patient Name" ,ondelete="cascade") #,domain=[('gender','=','male')] for filter the drop list
    date_now=fields.Datetime(string="Date of Appointment" ,default=fields.Datetime.now() , help="Created field")
    date_day=fields.Date(string="Date of Appointment" , default=fields.Date.context_today)
    patient_gender=fields.Selection(string="Patient Gender" , related="patient_id.gender")
    birth_day=fields.Date(string="Patient Birth" , related="patient_id.birth_day")
    patient_ref=fields.Char(string="Patient Reference")
    html_field=fields.Html(string="HTML Field")
    state=fields.Selection([
        ("draft","Draft"),
        ("in_consultation","In Consultation"),
        ("done","Done"),
        ("cancel","Cancel"),
    ], string="Status" ,default="draft" ,required=True)

    medicine_line_ids=fields.One2many("hospital.medicine.line","appointment_id",string="Medicine")

    user_id=fields.Many2one('res.users' , string="User" , required=True)

    show_col=fields.Boolean(string="Show College" ,default=False)

    user_level=fields.Many2many('patient.tags',string="Level")

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.patient_ref = self.patient_id.code

    def draft_state(self):
        for rec in self:
            rec.state = "draft"

    def in_consultation_state(self):
        for rec in self:
            rec.state = "in_consultation"

    def done_state(self):
        for rec in self:
            rec.state = "done"

    # def cancel_state(self):
    #     for rec in self:
    #         rec.state = "cancel"

    def hello_button_treee(self):
        print("Hellllo from tree button...................!!")
        return

    def cancel_state(self):
        action=self.env.ref('hospital_app.appointment_cancel_actions').read()[0]
        return action

    # def unlink(self):
    #     for rec in self:
    #         if rec.state != "done":
    #             raise ValidationError(_("u only can delete a record in draft state"))
    #     return super(HospitalAppointment,self).unlink()



class Medicine(models.Model):
    _name = 'hospital.medicine.line'
    _description = "Medicine"

    product_id = fields.Many2one('product.product' , string="Product" , required=True)
    product_price=fields.Float(string="Product Price" , related="product_id.list_price")
    qty=fields.Integer(string="Quantity" ,default=1)


    appointment_id=fields.Many2one("hospital.appointment",string="Appointment")


