from msilib import sequence
from odoo import fields, models

class CrmStage(models.Model) :
    _name = "crm.stage"
    _description = "Manages the stages of the sales pipeline."
    
    name = fields.Char(required=True)
    sequence = fields.Integer(required=True)
    probability = fields.Float()
    fold = fields.Boolean()
