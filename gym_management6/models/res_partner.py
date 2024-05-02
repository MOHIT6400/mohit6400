from odoo import api,fields, models

class res_partner(models.Model):
    _inherit = "res.partner"

    facebook = fields.Char(string="Facebook")   
    
    total_member = fields.Integer(compute='_compute_total_members',string="Members")    
    
    
    
    def _compute_total_members(self):
    	for order in self:
            print ("orders=======",order)
            members_id = self.env['members.members'].search([('partner_id','=',self.id)])
            order.total_member = len(members_id)

    def action_view_memberes(self):
        members_id = self.env['members.members'].search([('partner_id','=',self.id)])
        action = self.env["ir.actions.actions"]._for_xml_id("gym_management.members_members_action")
        action['domain'] = [('id', 'in', members_id.ids)]

        # members_id = self.env['members.members'].search([('partner_id','=',self.id)])
        # print ("members_id============",members_id , len(members_id))
        # action = self.env['ir.actions.actions']._for_xml_id('gym_management.members_members_action')
        # if members_id:
        #         if len(members_id) > 1:
        #                 action['domain'] = [('id', 'in', members_id.ids)]
        #         elif len(members_id) == 1:
        #                 form_view = [(self.env.ref('members_members_form_view').id, 'form')]
        #                 if 'views' in action:
        #                         action['views'] = form_view + [(state,view) for state,view in action['views'] if view != 'form']
        #                 else:
        #                         action['views'] = form_view
        #                 action['res_id'] = members_id.id
        # else:
        #         action = {'type': 'ir.actions.act_window_close'}
    	
        return action
    	
    	
