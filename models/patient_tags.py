from odoo import api, fields, models

class PatientTags(models.Model):
    _name = 'patient.tags'
    _description = 'Patient Tags'
    _rec_name = 'tag_name'

    tag_name=fields.Char(string="Patient Tag Name")
    active=fields.Boolean(default=True)

    color=fields.Integer(string="Patient color_picker" )
    color_2=fields.Char(string="Patient color" )