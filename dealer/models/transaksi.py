from odoo import models, fields, api,_

class pabrik(models.Model):
    _name = 'dealer.transaksi'
    _description = 'class untuk transaksi'

    id_trans = fields.Char('id_trans', size=8, readonly=False , required=True, index=True)
                              # states={'draft': [('readonly', False)]})

    _sql_constraints = [('id_pabrik_unik', 'unique(id_pabrik)', ('id must be unique!'))]

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
