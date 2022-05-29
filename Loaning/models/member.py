from odoo import models, fields, api

class member(models.Model):
    _name = 'loaning.member'
    _description = 'class anggota untuk UTS'
    _rec_name = 'name'

    id_anggota = fields.Char('ID', size=8, required=True, index=True, readonly=False)
    name = fields.Char('Nama', size=64, required=True, index=True)
    description = fields.Text('Deskripsi', readonly=True, states={'draft': [('readonly', False)]})
    active=fields.Boolean('Active', default=True, readonly=True, states={'draft': [('readonly', False)]})
    jenis_kelamin = fields.Char('Jenis Kelamin', size=8, required=True, index=True, readonly=False)

    state = fields.Selection(
        [('draft', 'Draft'),
         ('confirmed', 'Confirmed'),
         ('done', 'Done'),
         ('canceled', 'Canceled')], 'State', required=True, readonly=True, default='draft')

    def action_done(self):
        self.state = 'done'

    def action_canceled(self):
        self.state = 'canceled'

    def action_confirmed(self):
        self.state = 'confirmed'

    def action_settodraft(self):
        self.state = 'draft'