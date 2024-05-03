
{
    'name': 'GYM Managment6',
    'version': '17.0',
    'category': 'Management6',
    'summary': 'GYM Managment6',
    'description': '`This is a reStructuredText description.`\n\n    This is a paragraph of text that is indented by four spaces to indicate that it is formatted using RST syntax.',
    'author':'Mohit',
    'price':'100.00'
    'currency':'USD',
    'license':'LGPL-3',

    'depends': ['base','utm','sale'],    
    'data': [
        'security/ir.model.access.csv',
        'security/res_groups.xml',
        'data/ir_sequence_data.xml',
        'views/members_view.xml',
        'views/trainer_view.xml',  
        'views/measurement_view.xml',
        'views/res_partner_view.xml',
        'wizard/bulk_member_confirm.xml',
    ],
    'installable': True,
    'images': [
        'static/description/banner.gif',
    ],
}


