
{
    'name': 'GYM Managment6',
    'version': '17.0',
    'category': 'Management6',
    'summary': 'GYM Managment6',
    'description': 'GYM Managment6',
    'author':'Mohit',
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


