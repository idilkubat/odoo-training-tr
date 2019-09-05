from odoo import models,fields

class Skills(models.Model):
    _name = "skills"

    skill_name = fields.Char()
    level = fields.Selection(
        [('beginner', "Beginner"),
         ('elementary', "Elementary"),
         ('intermediate', "Intermediate"),
         ('upper-intermediate', "Upper-Intermediate"),
         ('advanced', "Advanced")
         ])

    talent_ids = fields.Many2many("talent", relation="talent_skills", column1="skills_ids", column2="talent_ids")



