from odoo import models, fields, api, _


class ReAgent(models.Model):
    _name = 're.agent'
    _inherit = ['mail.thread']
    _ref_name = 'name'

    name = fields.Char(string="Name")
    tel = fields.Char(string="Tel")
    email = fields.Char(string="Email")
    address = fields.Char(string="Address")
    image = fields.Image(string="Image")
    ref = fields.Char(string="Reference", default=lambda self: _('New'))
    title = fields.Many2one('res.partner.title', string="Title")
    note = fields.Text(string='description', tracking=True)
    user_id = fields.Many2one('res.users', string='Related User')
    login = fields.Char(String="login")
    password = fields.Char(String="password")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('re.agent')
        return super(ReAgent, self).create(vals_list)

    @api.model_create_multi
    def create(self, vals_list):
        users = self.env['res.users']
        agents = self.env['re.agent']

        for vals in vals_list:
            user = users.create({'name': vals.get('name'), 'login': vals.get('login'), 'password': vals.get('password')})
            vals['user_id'] = user.id
            agents += super(ReAgent, self).create(vals)

        return agents