from odoo import api,fields, models
from odoo.exceptions import ValidationError


class members_members(models.Model):
    _name = "members.members"
    _inherit = ['portal.mixin', 'product.catalog.mixin', 'mail.thread', 'mail.activity.mixin', 'utm.mixin']
    _description = "Members registration."
    
    
    image=fields.Image(string="")
    name=fields.Char(string="Name")
    occupation=fields.Char(string="Occupation")
    phone=fields.Char(string="Number")
    email=fields.Char(string="Address")
    title=fields.Char()
    gender=fields.Selection(
        [('male','Male'),('female','Female')]
     )
    dob=fields.Date("Date Of Birth")
    age=fields.Char("Age..")
    gst_treatment=fields.Char(string="GST Treatment")

    partner_id= fields.Many2one('res.partner',string="Contact")
    # membership_scheme = fields.Selection(
    #     [('silver_membership','Silver Membership'),('gold_membership','Gold Membership'),('platinium_membership','Platinium Membership')]
    #     )
    # membership_fees = fields.Float('Paid Amount')
    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    state = fields.Selection([('draft','Draft'),('confirm','Confirm'),('done','Done')], string="State",default='draft',tracking=True)

    measurement_line = fields.One2many("members.measurement.line",'members_id',string="Measurement History")  

    sales=fields.Char()
    ficsalinformation=fields.Char()
    purchase=fields.Char()
    misc=fields.Char() 

    salesperson = fields.Char()
    paymentterms = fields.Char()
    mp = fields.Char()
    fiscalposition= fields.Char()
    purchase = fields.Char()
    reference = fields.Char()
    company = fields.Char()


    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].sudo().next_by_code('members.members') or 'New'
        res = super(members_members, self).create(vals)
        return res
        

    def write(self, vals):
        res = super(members_members,self).write(vals)
        if vals.get('phone'):
            data = {'name':vals.get('phone')}
            trainer = self.env['trainer.trainer'].create(data)
            #trainer.unlink()
            return res
        
    	
    def action_confirm(self):
        self.state = 'confirm'
        return True
    	
    def action_done(self):
        print ("self======",self)
        self.state = 'done'
        return True
    
   
    # @api.onchange('membership_scheme')
    # def _onchange_membership_scheme(self):
        
    #     membership_feess = {
    #         'silver_membership': 15000,
    #         'gold_membership': 25000,
    #         'platinium_membership': 35000,
    #     }

    #     if self.membership_scheme:
    #         self.membership_fees = membership_feess.get(self.membership_scheme, 0)

    # @api.depends('membership_scheme')
    # def _compute_membership_fees(self):
    #     # This is required to store the computed value in the database
    #     self.membership_fees = self.membership_scheme.membership_fees

    class members_measurement_line(models.Model):
        _name = "members.measurement.line"
        _description = "Measurement Line"
    
        measurement_id = fields.Many2one('measurement.measurement',string="Measurement")
        members_id = fields.Many2one("members.members")

             
        date = fields.Date()
        weight = fields.Float(string='Weight (kg)')
        height = fields.Float(string='Height (cm)')
        bmi = fields.Float(string='BMI')
        bmr = fields.Float(string='BMR')
        neck = fields.Float(string='Neck (cm)')
        chest = fields.Float(string='Chest (cm)')
        biceps = fields.Float(string='Biceps (cm)')
        waist = fields.Float(string='Waist (cm)')
        hips = fields.Float(string='Hips (cm)')
        thighs = fields.Float(string='Thighs (cm)')
        calf = fields.Float(string='Calf (cm)') 