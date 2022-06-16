from odoo import models, fields, api,_

class pabrik(models.Model):
    _name = 'dealer.pabrik'
    _description = 'class untuk pabrik'

    id_pabrik = fields.Char('id_pabrik', size=8, readonly=False , required=True, index=True)
                              # states={'draft': [('readonly', False)]})
    nama_pabrik = fields.Char('nama_pabrik', size=64, readonly=False , required=True, index=True)
                              # states={'draft': [('readonly', False)]})

    _sql_constraints = [('id_pabrik_unik', 'unique(id_pabrik)', ('id must be unique!'))]

    detail_ids6 = fields.One2many('dealer.beli', 'pab_id', string='Votes')

    active = fields.Boolean('Active', default=True, readonly=True, states={'draft': [('readonly', False)]})

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
