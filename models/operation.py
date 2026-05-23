from odoo import api,fields,models,tools


class Operation(models.Model):
    _name = 'hospital.operation'
    # _inherit = 'res.groups'
    _description = 'Hospital Operation'
    _log_access=False

    doctor_id = fields.Many2one('res.users',string='Doctor')
    operation_name = fields.Char(string='OPR Name')
    reference_record=fields.Reference(selection=[
        ('hospital.patient','Patient'),
        ('hospital.appointment','Appointment')
    ],string='Reference Record')


    @api.model
    def name_create(self, name):
        return self.create({'operation_name':name}).name_get()[0]

    # def get_application_groups(self,domain):
    #     warning_can_id=self.env.ref('account.group_warning_account').id
    #     sales_group_id=self.env.ref('sale.group_warning_sale').id
    #     return super(Operation,self).get_application_groups(domain+[
    #         ('id','not in',(warning_can_id,sales_group_id)
    #          )])