from stdnum.exceptions import ValidationError
from odoo import models,fields,api

class Certification(models.Model):
    _name='certification'
    _description='Certification'

    number = fields.Char()
    date = fields.Date(string='Validation Date')
    description = fields.Text(string='Validation Detail')
    standard_id = fields.Many2one("certification.standard")
    owner_id = fields.Many2one("res.partner")
    entity_id = fields.Many2one("res.prtner")

    @api.constrains('entity_id')
    def _check_entity_id(self):
        if self.entity_id and self.entity_id.is_certification_body == False:
            raise ValidationError('It is not a certification entity')