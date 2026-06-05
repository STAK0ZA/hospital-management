from datetime import date
from email.policy import default

from dateutil.relativedelta import relativedelta

from odoo import models,fields,api,_
from odoo.exceptions import ValidationError
# from dateutil.relativedelta import relativedelta

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Hospital Patient"
    # _rec_name = 'ref'
    _order='id desc'

    name=fields.Char(string="Patient" ,tracking=1)
    age=fields.Integer(string="age",tracking=2 ,compute='_compute_date' ,inverse="_inverse_age" ,search='_search_by_age')
    gender=fields.Selection([('male','Male'),('female','Female')],string="Gender")
    code=fields.Char(string="Code")
    ref=fields.Char(string="Reference")
    birth_day=fields.Date(string="Date of Birth")
    appointment_count=fields.Integer(string="Appointment" ,compute="_compute_appointment_count" ,store=True)
    appointment_ids=fields.One2many('hospital.appointment','patient_id',string="Appointments")

    parent_name = fields.Char(string="Parent Name")
    marital_status=fields.Selection([
        ('married','Married'),
        ('single','Single')
    ],default="single")
    partner_name=fields.Char(string="Partner Name")


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
    is_this_birth=fields.Boolean(string="Is this birth?" ,compute="_compute_date_birth")

    phone=fields.Char(string="Phone")
    email=fields.Char(string="Email")
    url=fields.Char(string="URL")


    @api.depends('birth_day')
    def _compute_date(self):
        for rec in self:
            if rec.birth_day:
                today=date.today()
                rec.age=today.year-rec.birth_day.year
            else:
                rec.age= 1

    def hello(self):
        return{
            'type':'ir.actions.act_url',
            'target':'new',
            'url':'http://odoo.com'
        }



    @api.model
    def create(self,vals):
        print("created new record............................_____________")
        if not vals.get('ref') :
            vals['ref']=self.env['ir.sequence'].next_by_code('patient.sequence.id')

        return super().create(vals)



    def write(self,vals):
        print("edit the record .....................___________")
        if not self.ref and not vals.get('ref'):
            vals['ref']=self.env['ir.sequence'].next_by_code('patient.sequence.id')
        return super().write(vals)

    def _search_by_age(self,operator,value):
        # value = int(value)
        return [
            ('birth_day','>',date.today()-relativedelta(years=value+1)),
            ('birth_day','<=',date.today()-relativedelta(years=value)),
        ]
        # return [ ('birth_day','=','05/20/2004')]
        # return [ ('id','=',24)]

    def _name_get(self):
        result = []

        for rec in self:
            full_name = f"{rec.name or ''} {rec.ref or ''}"
            result.append((rec.id, full_name.strip()))

        return result

    def hello_button_tree(self):
        print("Hellllo from tree button...................!!")
        return
    def hi(self):
        print("hiiiiiiiiii-----------")

    @api.depends('age')
    def _inverse_age(self):
        today=date.today()
        for rec in self:
            rec.birth_day = today-relativedelta(years=rec.age)

    @api.constrains('birth_day')
    def _check_age(self):
        for rec in self:
            if rec.birth_day and rec.birth_day > fields.Date.today():
                raise ValidationError(_("the entered date is not acceptable"))

    # this function to count the number of appointment
    # @api.depends('appointment_ids')
    # def _compute_appointment_count(self):
    #     for rec in self:
    #         rec.appointment_count=self.env['hospital.appointment'].search_count([('patient_id','=',rec.name)])

    @api.depends('appointment_ids')
    def _compute_appointment_count(self):
        for rec in self:
            rec.appointment_count=0
        appointment_group = self.env['hospital.appointment'].read_group(
            domain=[],
            fields=['patient_id'],
            groupby=['patient_id'],
        )
        for appointment in appointment_group:
            patient_id = appointment.get('patient_id')[0]
            patient_rec=self.browse([patient_id])
            patient_rec.appointment_count=appointment['patient_id_count']
        # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11",appointment_group)

    def show_appointment(self):
        return{
            'name': _('Appointment'),
            'view_mode': 'list,form',
            'res_model': 'hospital.appointment',
            'domain': [('patient_id','=',self.id)],
            'context': {'default_patient_id':self.id},
            'target': 'current',
            'type': 'ir.actions.act_window',
            # 'context': {'default_type': self.type}

        }

    def try_some(self):
        vals={'name':'KAREEM HANY','age':'300','gender':'male'}
        # records=self.env['hospital.patient'].browse([21,22])
        # for rec in records:
        #     print(rec.name)
        # print(self.env['hospital.patient'].search_count([('gender','=','male')]))
        print(self.env['hospital.patient'].browse(21).get_metadata()[0].get("create_uid")[1])
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    @api.ondelete(at_uninstall=False)
    def _check_appointment(self):
        for rec in self:
            if rec.appointment_ids:
                raise ValidationError(_("can't delete patient with appointment"))

    @api.depends('birth_day')
    def _compute_date_birth(self):
        for rec in self:
            rec.is_this_birth=False
            if rec.birth_day:
                today=date.today()
                if rec.birth_day.month==today.month and rec.birth_day.day == today.day:
                    rec.is_this_birth = True





