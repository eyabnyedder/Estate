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
        "views/contacts.xml",
        "views/chooseFormWizard.xml",
        'views/menu.xml',
        'views/adds.xml',
    ],
    'installable': True,
    'auto_install': True,
    'js': [
        "static/js/real_estate.js",
    ]
}
