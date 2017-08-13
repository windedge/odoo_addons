# -*- coding: utf-8 -*-
{
    'name': "Send message button on topbar",
    'description': """
Just revert the compose message code which is removed from official code base, please follow this discussion for detail:
https://github.com/odoo/odoo/commit/5209fbc7ed9fcad966ab064654a8a8697142be42
""",
    'author': "xujl",
    'category': 'Extra Rights',
    'version': '0.1',

    'depends': ['base', 'mail'],

    'data': [
        # 'security/ir.model.access.csv',
        'template.xml',
    ],
    'qweb':[
        'static/src/xml/mail.xml',
    ],
    'images': [
        'static/description/revert_compose_message.png'
    ],
    'license': 'LGPL-3'
}
