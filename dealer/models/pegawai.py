from odoo import models, fields, api,_

class pegawai(models.Model):
    _name = 'dealer.pegawai'
    _description = 'class untuk pegawai'

    id_pegawai = fields.Char('id_pegawai', size=8, readonly=False , required=True, index=True)
                              # states={'draft': [('readonly', False)]})
    nama_pegawai = fields.Char('nama_pegawai', size=64, readonly=False , required=True, index=True)
                              # states={'draft': [('readonly', False)]})
    no_hp =fields.Integer('no hp', size=15, readonly=False)
        # states={'draft': [('readonly', False)]})
    detail_ids4 = fields.One2many('dealer.detailtransaksi', 'pega_id', string='Votes')
    _sql_constraints = [('id_pegawai_unik', 'unique(id_pegawai)', ('id must be unique!'))]

    state = fields.Selection(
        [('draft', 'Draft'),
         ('confirmed', 'Confirmed'),
         ('done', 'Done'),
         ('canceled', 'Canceled')], 'State', required=True, readonly=True, default='draft')

    active = fields.Boolean('Active', default=True, readonly=True, states={'draft': [('readonly', False)]})

    detail_ids7 = fields.One2many('dealer.beli', 'pega2_id', string='Votes')

    def action_done(self):
        self.state = 'done'

    def action_canceled(self):
        self.state = 'canceled'

    def action_confirmed(self):
        self.state = 'confirmed'

    def action_settodraft(self):
        self.state = 'draft'
