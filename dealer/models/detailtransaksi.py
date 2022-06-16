from odoo import models, fields, api,_

class detailtransaksi(models.Model):
    _name = 'dealer.detailtransaksi'
    _description = 'class untuk detailtransaksi'

    id_transaksi = fields.Char('id_transaksi', size=64, readonly=False, required=True, index=True)
    # states={'draft': [('readonly', False)]})
    totalharga = fields.Integer('Total harga', compute="_compute_total", store=True, default=0)
    diskon = fields.Integer('Diskon', size=15, readonly=False)
    # states={'draft': [('readonly', False)]})
    jumlah = fields.Integer('Jumlah', size=15, readonly=False)
    # states={'draft': [('readonly', False)]})
    tanggal_transaksi = fields.Date('Tanggal transaksi', default=fields.Date.context_today, readonly=True,
                                    # states={'draft': [('readonly', False)]})
                                    domain="[('state', '=', 'done'),('active', '=', 'True')]")

    mobi_id = fields.Many2one('dealer.mobil', string='mobil', readonly=False, ondelete="cascade",
                              # states={'draft': [('readonly', False)]},
                              domain="[('state', '=', 'done'),('active', '=', 'True')]")
    pega_id = fields.Many2one('dealer.pegawai', string='pegawai', readonly=False, ondelete="cascade",
                              # states={'draft': [('readonly', False)]},
                              domain="[('state', '=', 'done'),('active', '=', 'True')]")
    custo_id = fields.Many2one('dealer.customer', string='customer', readonly=False, ondelete="cascade",
                              # states={'draft': [('readonly', False)]},
                              domain="[('state', '=', 'done'),('active', '=', 'True')]")

    customer_ids = fields.One2many('dealer.customer', 'customer_id', string='customer')
    detailtransaksi_ids=fields.One2many('dealer.detailtransaksi','id_transaksi',string='detailtransaksi')
    _sql_constraints = [('id_transaksi_unik', 'unique(id_transaksi)', ('id must be unique!'))]

    state = fields.Selection(
        [('draft', 'Draft'),
         ('confirmed', 'Confirmed'),
         ('done', 'Done'),
         ('canceled', 'Canceled')], 'State', required=True, readonly=True, default='draft')

    harga_mobil = fields.Integer('Harga', related='mobi_id.harga')
    mobil_id = fields.Many2one('dealer.mobil', string='mobil', readonly=False, ondelete="cascade",
                              # states={'draft': [('readonly', False)]},
                              domain="[('state', '=', 'done'),('active', '=', 'True')]")

    def action_done(self):
        self.state = 'done'

    def action_canceled(self):
        self.state = 'canceled'

    def action_confirmed(self):
        self.state = 'confirmed'

    def action_settodraft(self):
        self.state = 'draft'

    @api.depends('harga_mobil', 'jumlah','diskon')

    def _compute_total(self):
        for detailtransaksi in self:
            val = {
                'totalharga': 0,
            }
            for rec in detailtransaksi:
                print(rec.harga_mobil)
                val['totalharga'] = (rec.harga_mobil - (rec.harga_mobil * rec.diskon)/100) * rec.jumlah
            detailtransaksi.update(val)
