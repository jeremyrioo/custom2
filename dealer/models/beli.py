from odoo import models, fields, api,_

class beli(models.Model):
    _name = 'dealer.beli'
    _description = 'class untuk beli'

    id_beli = fields.Char('id_beli', size=8, readonly=False , required=True, index=True)
                              # states={'draft': [('readonly', False)]})
    # id_mobil = fields.Char('id_mobil', size=64, readonly=False , required=True, index=True)
                              # states={'draft': [('readonly', False)]})
    # id_pabrik = fields.Char('id_mobil', size=64, readonly=False, required=True, index=True)
    # states={'draft': [('readonly', False)]})
    # id_pegawai = fields.Char('id_mobil', size=64, readonly=False, required=True, index=True)
    # states={'draft': [('readonly', False)]})
    jumlah_barang =fields.Integer('Jumlah Barang', size=8, readonly=False)
    # states={'draft': [('readonly', False)]})
    tanggal_pembelian =  fields.Date('Tanggal Pembelian', default=fields.Date.context_today, readonly=True,
                                    # states={'draft': [('readonly', False)]})
                                    domain="[('state', '=', 'done'),('active', '=', 'True')]")

    mobi2_id = fields.Many2one('dealer.mobil', string='mobil', readonly=False, ondelete="cascade",
                              # states={'draft': [('readonly', False)]},
                              domain="[('state', '=', 'done'),('active', '=', 'True')]")
    pega2_id = fields.Many2one('dealer.pegawai', string='pegawai', readonly=False, ondelete="cascade",
                              # states={'draft': [('readonly', False)]},
                              domain="[('state', '=', 'done'),('active', '=', 'True')]")
    pab_id = fields.Many2one('dealer.pabrik', string='pabrik', readonly=False, ondelete="cascade",
                               # states={'draft': [('readonly', False)]},
                               domain="[('state', '=', 'done'),('active', '=', 'True')]")



    _sql_constraints = [('id_beli_unik', 'unique(id_beli)', ('id_beli must be unique!'))]

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
