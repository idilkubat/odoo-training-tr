from odoo import models,fields,api

class Role(models.Model):
    _name ='role'
    _description ='Role List'

    role_name = fields.Text(string="ROLE")
    description = fields.Tetx(string="DESCRIPTION")
