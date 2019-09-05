from odoo import models,fields

class Skills(models.Model):
    _name = 'skills'
    _description = 'Employee Skills'

    name = fields.Char()
    level = fields.Selection(
        [('beginner', "Beginner"),
         ('elementary', "Elementary"),
         ('intermediate', "Intermediate"),
         ('upper-intermediate', "Upper-Intermediate"),
         ('advanced', "Advanced")
         ])
    description = fields.Text()