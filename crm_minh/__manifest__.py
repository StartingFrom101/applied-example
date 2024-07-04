# -*- coding: utf-8 -*-
{
    'name': "(Minh) Customer Relationship Management",

    'summary': """
    A CRM, or Customer Relationship Management, is a system or strategy used by 
    businesses to manage and analyze customer interactions and data throughout the
    customer lifecycle""",

    'description': """
        A CRM, or Customer Relationship Management, is a system or strategy
        used by businesses to manage and analyze customer interactions and data 
        throughout the customer lifecycle. The primary goal of a CRM is to improve
        business relationships with customers, aid in customer retention, and
        drive sales growth. 
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        
        'views/crm_lead.xml',
        'views/crm_menu.xml'
    ],
    
    'license': 'LGPL-3',
    
    'installable' : True,
    'application' : True,
}
