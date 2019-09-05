from odoo import models,fields,api

class Talent(models.Model):
    _name ='talent'
    _description ='Talent List'

    id = fields.Many2one("hr.employee", string="ID")
    name = fields.Many2one("hr.employee", string="Employee Name")
    d_name = fields.Many2one("hr.department", "Department", string="Department")
    email = fields.Many2one("res.partner", string="Email")
    role_name = fields.Many2one("role", string="Role")



