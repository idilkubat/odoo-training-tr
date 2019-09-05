import datetime

from dateutil import relativedelta

from odoo import models,fields,api

class Talent(models.Model):
    _name = "talent"
    _description = "Talent management system"

    id = fields.Many2one("hr.employee")
    name = fields.Many2one("hr.employee")
    d_name = fields.Many2one("hr.department",string="Department Name")
    email = fields.Char()
    role_name = fields.Char()
    date_started = fields.Date()
    levels = fields.Integer(compute='_compute_experience_days')
    experience = fields.Char(compute='_compute_experience_days')
    experience2 = fields.Integer(compute='_compute_experience_days')
    skill_ids = fields.Many2many("skills", relation="talent_skills", column1="talent_ids", column2="skills_ids")


    @api.onchange('name')
    def _onchange_email(self):
        self.email = self.name.work_email
        self.d_name = self.name.department_id
        self.role_name = self.name.job_id.name

    @api.depends('date_started')
    def _compute_experience_days(self):
        experience = relativedelta.relativedelta(datetime.date.today(), self.date_started)
        self.experience2 = (fields.Date.today() - self.date_started).days
        self.experience = str(experience.years) + ' year(s) ' + str(experience.months) + ' month(s) ' + str(experience.days) + ' day(s)'


        if self.experience2 > 60:
            self.levels = 2
        elif self.experience2 < 0:
            self.experience2 = 0
        else:
            self.levels = 1
