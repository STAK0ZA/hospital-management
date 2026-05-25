from email.policy import default

from odoo import api, fields, models

class playground(models.Model):
    _name = 'play.ground'
    _description = 'Playground'
    _order = 'sequence,id'

    name=fields.Char(string="playground name")
    code=fields.Text(string="playground code")
    sequence=fields.Integer(string="playground sequence" ,default=10)


    def try_some(self):
        print(self.env.ref('hospital_app.tag_master').tag_name)
        # for rec in self:
        #     print("------------------------"+rec.self.env.user)
