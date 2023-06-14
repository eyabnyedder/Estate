{
    'name': 'Real Estate Management System',
    'version': '1.0',
    'summary': 'Real Estate Management System',
    'sequence': 1,
    'depends': ['base', 'mail'],
    'data': [
        "security/ir.model.access.csv",
        "data/sequence.xml",
        "views/menu.xml",
    ],
    'installable': True,
    'auto_install': True,
}
