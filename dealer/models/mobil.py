from odoo import models, fields, api,_

class mobil(models.Model):
    _name = 'dealer.mobil'
    _description = 'class untuk pegawai'

    id_mobil = fields.Char('id_mobil', size=8, readonly=False , required=True, index=True)
                              # states={'draft': [('readonly', False)]})
    nama_mobil = fields.Char('nama_mobil', size=64, readonly=False , required=True, index=True)
                              # states={'draft': [('readonly', False)]})
    harga = fields.Integer('harga', size=15, readonly=False)
    # states={'draft': [('readonly', False)]})
    warna = fields.Char('warna', size=64, readonly=False, required=True, index=True)
    # states={'draft': [('readonly', False)]})
    stock = fields.Integer('Stock', size=15, readonly=False)
    # states={'draft': [('readonly', False)]})

    _sql_constraints = [('id_mobil_unik', 'unique(id_mobil)', ('id must be unique!'))]

    detail_ids = fields.One2many('dealer.detailtransaksi', 'mobi_id', string='Votes')
    detail_ids5 = fields.One2many('dealer.beli', 'mobi2_id', string='Votes')

    state = fields.Selection(
        [('draft', 'Draft'),
         ('confirmed', 'Confirmed'),
         ('done', 'Done'),
         ('canceled', 'Canceled')], 'State', required=True, readonly=True, default='draft')

    active = fields.Boolean('Active', default=True, readonly=True, states={'draft': [('readonly', False)]})

    def action_done(self):
        self.state = 'done'

    def action_canceled(self):
        self.state = 'canceled'

    def action_confirmed(self):
        self.state = 'confirmed'

    def action_settodraft(self):
        self.state = 'draft'

