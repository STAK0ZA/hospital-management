from odoo import api, fields, models

class playground(models.Model):
    _name = 'play.ground'
    _description = 'Playground'

    name=fields.Char(string="playground name")
    code=fields.Text(string="playground code")

    def try_some(self):
        print(self.env.ref('hospital_app.tag_master').tag_name)
        # for rec in self:
        #     print("------------------------"+rec.self.env.user)
