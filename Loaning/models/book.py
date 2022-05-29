from odoo import models, fields, api

class book(models.Model):
    _name = 'loaning.book'
    _description = 'class buku untuk UTS'
    _rec_name = 'judul'

    id_buku = fields.Char('ID', size=8, readonly=True , required=True, index=True, states={'draft': [('readonly', False)]})
    judul = fields.Char('Judul Buku', size=64, readonly=True , required=True, index=True, states={'draft': [('readonly', False)]})
    pengarang = fields.Char('Pengarang', size=64, readonly=True ,required=True, index=True, states={'draft': [('readonly', False)]})

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