from email.policy import default

from requests.utils import default_user_agent

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
    duration=fields.Float(string="Duration")
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

    operation=fields.Many2one('hospital.operation',string="Operation" )

    bar = fields.Integer(string="Bar" ,compute="_compute_percentage")



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
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Done successfully',
                'type': 'rainbow_man'
            }
        }

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


    def send_message(self):
        if not self.patient_id.phone:
            raise ValidationError(_("there is problem no phone "))
        phone=self.patient_id.phone
        text='Hello %s is ur gender %s '%(self.patient_id.name,self.patient_id.gender)
        whats_url='https://api.whatsapp.com/send?phone=%s&text=%s'%(phone,text)

        return{
            'type':'ir.actions.act_url',
            'target':'new',
            'url':whats_url
        }



    @api.depends('state')
    def _compute_percentage(self):
        for rec in self:
            if rec.state == "done":
                rec.bar=100
            elif rec.state == "in_consultation":
                rec.bar=75
            elif rec.state == "draft" or rec.state == "cancel":
                rec.bar=0

        pass

class Medicine(models.Model):
    _name = 'hospital.medicine.line'
    _description = "Medicine"

    product_id = fields.Many2one('product.product' , string="Product" , required=True)
    product_price=fields.Float(string="Product Price" , default=100 ,digits="Percentage Analytic")
    qty=fields.Integer(string="Quantity" ,default=1)

    company_id=fields.Many2one('res.company' , default= lambda self: self.env.company)

    currency_id=fields.Many2one('res.currency' , string="Currency" ,related="company_id.currency_id")
    total_price=fields.Monetary(string="Total Price" ,default=0,compute="_compute_product_price")


    appointment_id=fields.Many2one("hospital.appointment",string="Appointment")

    @api.depends('product_id','qty')
    def _compute_product_price(self):
        for rec in self:
            rec.total_price=rec.product_price*rec.qty


