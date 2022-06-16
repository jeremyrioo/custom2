from odoo import models, fields, api

class customer(models.Model):
    _name = 'transaksimobil.customer'
    _description = 'class untuk costumer'

    id_costumer = fields.Char('id costumer', size=8, readonly=True , required=True, index=True, states={'draft': [('readonly', False)]})
    nama_customer = fields.Char('nama costumer', size=64, readonly=True , required=True, index=True, states={'draft': [('readonly', False)]})

    _sql_constraints = [('id_customer_unik', 'unique(id_customer)', ('id must be unique!'))]

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
