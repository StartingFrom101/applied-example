from odoo import fields, models

class CrmLead(models.Model):
    _name = 'crm.lead'
    _description = 'Leads and opportunities'
    
    name = fields.Char(required=True, string='Opportunity name')
    partner_id = fields.Many2one('res.partner', string='Customer')
    # Stage of the pipeline need to link later
    stage_id = fields.Many2one("crm.stage", string='Stage')
    
    user_id = fields.Many2one('res.users', string='Salesperson', default=lambda self: self.env.user)
    expected_revenue = fields.Float()
    probability = fields.Float()
    type = fields.Selection([
        ('opportunity', 'Opportunity'),
        ('lead', 'Lead'),
    ])
    planned_revenue = fields.Float()
    date_deadline = fields.Date()
    
    #Activities, reference later 
    # actvity_ids = fields.One2many
    
    