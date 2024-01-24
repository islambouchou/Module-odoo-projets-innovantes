# -*- coding: utf-8 -*-
{
    'name': "Recenser Projets innavantes",

    'summary': """Recenser les projets innavantes proposés par les étudiants de l'école
    (École nationale Supérieure d'Informatique ESI-Alger) par une équipe de professionnels des entreprises """,

    'description': """
        Gestion des projet innavantes module pour :
            - Gerer les Projets   
            - Évaluer les projest des étudiants par une équipe de professionnels des entreprises afin de recenser les projets innavantes 
            """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'templates.xml',
        'views/innovantes.xml',
	    'reports.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
