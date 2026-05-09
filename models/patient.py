from datetime import date
from email.policy import default

from odoo import models,fields,api

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Hospital Patient"
    # _rec_name = 'ref'

    name=fields.Char(string="Patient" ,tracking=True)
    age=fields.Integer(string="age",tracking=True ,compute='_compute_date')
    gender=fields.Selection([('male','Male'),('female','Female')],string="Gender")
    code=fields.Char(string="Code")
    ref=fields.Char(string="Reference")
    birth_day=fields.Date(string="Date of Birth")
    priority=fields.Selection([
        ("0","Good"),
        ("1","Very Good"),
        ("2","Excellent"),
        ("3","brilliant"),
    ], string="Priority")

    state=fields.Selection([
        ("start","Start"),
        ("in_progress","In Progress"),
        ("draft","Draft"),
        ("done","Done"),
        ("cancel","Cancel"),
    ], string="Status" ,default="start" ,required=True)



    prescription=fields.Html(string="Prescription")

    patient_image=fields.Image(string="Patient Image")

    active=fields.Boolean(string="Active",default=True)

    @api.depends('birth_day')
    def _compute_date(self):
        for rec in self:
            if rec.birth_day:
                today=date.today()
                rec.age=today.year-rec.birth_day.year
            else:
                rec.age= 1

    def hello(self):
        print("hello!!!!!!!!!!!!!!!!!!!!!!!!")
        return{
            'effect':{
                'fadeout':'slow',
                'message':'Hello User',
                'type':'rainbow_man'

            }
        }

    @api.model
    def create(self,vals):
        print("created new record............................_____________")
        if not vals['ref'] :
            vals['ref']=self.env['ir.sequence'].next_by_code('patient.sequence.id')

        return super().create(vals)



    def write(self,vals):
        print("edit the record .....................___________")
        if not self.ref and not vals.get('ref'):
            vals['ref']=self.env['ir.sequence'].next_by_code('patient.sequence.id')
        return super().write(vals)

    def _name_get(self):
        result = []

        for rec in self:
            full_name = f"{rec.name or ''} {rec.ref or ''}"
            result.append((rec.id, full_name.strip()))

        return result