

{
    'name': 'Certification',
    'summary': "Defines certification for different purposes.",
    'author': "Eficent, Odoo Community Association (OCA)",
    'website': "https://github.com/<my_github_user>",
    'category': 'Certification Management',
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'depends': ['base'],
    'data': ['security/ir.model.access.csv',
             'views/certification_view.xml',
             'views/res_partner_view.xml',
             'views/standard_view.xml'
             ],
    'demo': ['demo/certification_demo.xml'],
    'development_status': 'Beta',
    'maintainers': ['ceeficent']


}