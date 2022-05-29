from odoo import models, fields, api

class loan(models.Model):
    _name = 'loaning.loan'
    _description = 'class peminjaman untuk UTS'
    _rec_name = 'buku_id'

    id_peminjaman = fields.Char('ID', size=64, readonly=True , required=True, index=True, states={'draft': [('readonly', False)]})
    tanggal_pinjam = fields.Date('Tanggal Peminjaman', default=fields.Date.context_today, readonly=True)
    tanggal_kembali = fields.Date('Tanggal Pengembalian', default=fields.Date.context_today)
    admin_id = fields.Many2one('res.users', 'Admin', readonly=True, ondelete='cascade', default=lambda self: self.env.user)
    anggota_id = fields.Many2one('peminjaman.anggota', string="Anggota", readonly=True, ondelete='cascade', states={'draft': [('readonly', False)]}, domain="[('state','=','done')]")
    buku_id = fields.Many2one('peminjaman.buku', string='Judul Buku', readonly=True, ondelete='cascade', states={'draft': [('readonly', False)]}, domain="[('state','=','confirmed')]")

    state = fields.Selection(
        [('draft', 'Draft'),
         ('confirmed', 'Confirmed'),
         ('canceled', 'Canceled')], 'State', required=True, readonly=True, default='draft')

    _sql_constraints = [('name_unik', 'unique(name)', ('Ideas must be unique!'))]

    def action_confirmed(self):
        self.state = 'confirmed'

    def action_canceled(self):
        self.state = 'canceled'

    def action_settodraft(self):
        self.state = 'draft'