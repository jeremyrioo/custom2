from odoo import models, fields, api, _


class idea(models.Model):  # inherit dari Model
    _name = 'idea.idea'  # atribut dari class Model
    _description = 'class untuk berlatih ttg idea'
    # rec_name = 'name'
    _order = 'date desc'  # defaultnya adalah id, pengaruhnya saat list view
    # id = fields.Integer() #ini otomatis ada di odoo, akan jadi pk

    # membuat attribute field
    name = fields.Char('Number', size=64, required=True, index=True, readonly=True,
                       states={'draft': [('readonly', False)]})

    date = fields.Date('Date Release', default=fields.Date.context_today, readonly=True,
                       states={'draft': [('readonly', False)]})

    state = fields.Selection([('draft', 'Draft'),  # draft--> key, secara technical yang disimpan di dbase, Draft: value yang dilihat user
                            ('confirmed', 'Confirmed'),
                            ('done', 'Done'),
                            ('canceled', 'Canceled')], 'State', required=True, readonly=True,  # krn required, sebaiknya dikasi default
                            default='draft')  # tuple di dalam list, nama field harus state spy bisa diakses oleh states
    # Description is read-only when not draft!
    description = fields.Text('Description', readonly=True, states={'draft': [('readonly', False)]})
    active = fields.Boolean('Active', default=True, readonly=True, states={'draft': [('readonly', False)]})
    confirm_date = fields.Date('Confirm date')



    confirm_partner_id = fields.Many2one('res.partner', 'Confirm By', readonly=True)
    # Ketambahan voting_ids supaya bs ambil dari votings.py, s -> ditambahin karena penamaan default di odoo 1:M
    voting_ids = fields.One2many('idea.voting', 'idea_id', string='Votes')
    total_yes = fields.Integer("Yes", compute="_compute_vote", store=True, default=0)
    total_no = fields.Integer("No", compute="_compute_vote", store=True, default=0)
    total_abstain = fields.Integer("Abstain", compute="_compute_vote", store=True, default=0)

    score = fields.Integer('Score', default=0, readonly=True)
    # sponsor_ids = fields.Many2many('res.partner', 'idea_idea_res_partner_rel', 'idea_idea_id', 'res_partner_id', 'Sponsors')
    sponsor_ids = fields.Many2many('res.partner', string='Sponsors')
    owner = fields.Many2one('res.partner', 'Owner', index=True, readonly=True, states={'draft': [('readonly', False)]})
    _sql_constraints = [('name_unik', 'unique(name)', _('Ideas must be unique!'))]

    @api.depends("voting_ids", "voting_ids.vote", "voting_ids.state")
    # function api ini dijalankan:
    # 1. Tiap kali ada new record refer to voting_ids
    # 2. Tiap kali ada radio button vote pada voting.py berubah (yes, no, abstain)
    # 3. Tiap kali state pada voting.py berubah (canceled, settodraft, confirmed)

    def _compute_vote(self):
        for idea in self.filtered(lambda s:s.state == "done"):
            val = {
                "total_yes" : 0,
                "total_no" : 0,
                "total_abstain" : 0
            }
            for rec in idea.voting_ids.filtered(lambda s:s.state == "voted"):
                # lambda merupakan on the fly function dari phyton
                # s ini adalah self dari voting_ids, fungsi filtered ini akan memfilter khusus state yang bernilai voted
                # bisa pake looping, ga ush difilter. Tapi pengecekan tidak efisien
                # karena misal ada 100 data, trs hanya 2 yang canceled berarti tetep 100 pengecekan. Sedangkan filter hanya 2x saja
                if rec.vote == "yes":
                    val["total_yes"] += 1
                elif rec.vote == "no":
                    val["total_no"] += 1
                else:
                    val["total_abstain"] += 1

            idea.update(val)


    def action_canceled(self):
        self.state = 'canceled'

    def action_confirmed(self):
        self.state = 'confirmed'

    def action_settodraft(self):
        self.state = 'draft'

    def action_test(self):
        print(self.env.user.name)
        print(self.env.company.name)
        a = self.env['res.partner'].search([('name','ilike', 'Gemini')])
        for rec in a:
            print(rec.name)
        a = self.env["res.partner"].search([], limit=2)
        print(self.env.context.get('lang'))
        t = self.env.context.copy()
        t["keterangan"] = 'Ideku'
        self.with_context(t).action_done()  # memanggil function di model yang sama dengan memassingkan context

        b = self.env["perpustakaan.buku"]  # b adalah object dari model library.bookrent
        b.with_context(t).test_buku()

        #contoh query select
        query = "select name from res_partner order by name desc limit 3"
        self.env.cr.execute(query)
        rec1 = self.env.cr.fetchall()
        for data in rec1:
            print(data[0])

        #contoh browse
        query = "select * from res_partner limit 3"
        self.env.cr.execute(query)
        res = self.env['res.partner'].browse([row[0] for row in self.env.cr.fetchall()])
        for rec in res:
            print(rec.name)

    def action_done(self):
        self.state = 'done'
        t = self.env.context
        print(t.get('keterangan'))