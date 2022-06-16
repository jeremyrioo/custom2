from odoo import models, fields, api,_

class customer(models.Model):
    _name = 'dealer.customer'
    _description = 'class untuk costumer'

    id_customer = fields.Char('id_customer', size=8, readonly=False , required=True, index=True)
                              # states={'draft': [('readonly', False)]})
    nama_customer = fields.Char('nama_customer', size=64, readonly=False , required=True, index=True)
                              # states={'draft': [('readonly', False)]})

    customer_id = fields.Many2one('dealer.detailtransaksi', string='detailtransaksi', readonly=True, ondelete="cascade",
                                 domain="[('state', '=', 'done'), ('active', '=', 'True')]")

    _sql_constraints = [('id_customer_unik', 'unique(id_customer)', ('id must be unique!'))]

    state = fields.Selection(
        [('draft', 'Draft'),
         ('confirmed', 'Confirmed'),
         ('done', 'Done'),
         ('canceled', 'Canceled')], 'State', required=True, readonly=True, default='draft')
    detail_ids3 = fields.One2many('dealer.detailtransaksi', 'custo_id', string='Votes')

    active = fields.Boolean('Active', default=True, readonly=True, states={'draft': [('readonly', False)]})

    def action_done(self):
        self.state = 'done'

    def action_canceled(self):
        self.state = 'canceled'

    def action_confirmed(self):
        self.state = 'confirmed'

    def action_settodraft(self):
        self.state = 'draft'
