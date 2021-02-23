
{
    'name' : 'Own Documents',
    'version' : '0.1',
    'summary': 'Added Own Documents User Group',
    'author': 'Achieve Without Borders, Inc.',
    'sequence': 100,
    'description': """""",
    'category': 'Extra Tools',
    'website': '',
    'images' : [],
    'depends' : ['base',
                 'sale',
                 'purchase',
                 'purchase_requisition',
                 'stock'],
    'data': [
            'security/res.groups.csv',
            'security/ir.model.access.csv',
            'security/ir.rule.csv'
    ],
    'demo': [

    ],
    'qweb': [

    ],
    'installable': True,
    'application': False,
    'auto_install': False,

}