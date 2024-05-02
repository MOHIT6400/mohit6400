# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools.misc import format_date, formatLang
from odoo.tools.float_utils import float_repr
from odoo.tools import groupby

from collections import defaultdict
from markupsafe import Markup, escape
import json

class bulk_members_confirm(models.TransientModel):
    _name = 'bulk.members.confirm'


    def action_members_confirm(self):
        active_ids = self._context.get('active_ids')
        mebmers_ids = self.env['members.members'].browse(active_ids)
        for member_id in mebmers_ids:
            member_id.state = 'confirm'
        return True
    

    
