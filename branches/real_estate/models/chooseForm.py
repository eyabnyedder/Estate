from odoo import models, fields, api

class ChooseFormWizard(models.TransientModel):
    _name = 'choose.form.wizard'
    _description = 'Choose Form Wizard'

    form_view_type = fields.Selection([
        ('partner', 'Create Lodger/Owner'),
        ('agent', 'Create Agent'),
    ], string='Form View Type', required=True, default='partner')

    @api.model_create_multi
    def open_form_view(self):
        if self.form_view_type == 'partner':
            action = self.env.ref('real_estate.action_partner_form')
        elif self.form_view_type == 'agent':
            action = self.env.ref('real_estate.action_agent_form')

        return {
            'type': 'ir.actions.act_window',
            'res_model': action.res_model,
            'view_mode': 'form',
            'view_type': 'form',
            'views': [(action.view_id.id, 'form')],
            'target': 'new',
        }