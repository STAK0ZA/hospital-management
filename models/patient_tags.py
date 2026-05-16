from odoo import api, fields, models,_
from odoo.api import ondelete


class PatientTags(models.Model):
    _name = 'patient.tags'
    _description = 'Patient Tags'
    _rec_name = 'tag_name'

    tag_name=fields.Char(string="Patient Tag Name" ,ondelete="restrict")
    active=fields.Boolean(default=True)
    seq=fields.Integer(string="Sequence" ,default=0)
    color=fields.Integer(string="Patient color_picker" )
    color_2=fields.Char(string="Patient color" )


    def copy(self, default=None):
        if default is None:
            default={}
        if not default.get('tag_name'):
            default['tag_name']=_("%s (copy)",self.tag_name)
        default['seq']=self.seq+1
        return super(PatientTags, self).copy(default)

    _sql_constraints = [
        ('tag_name','unique(tag_name)','name must be unique')
    ]