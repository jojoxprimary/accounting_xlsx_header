{
    'name': "Accounting XLSX Header",
    'version': '1.0',
    'depends': [
        "account_reports",  
        "accountant",
        "l10n_ph"
    ],
    'author': "HomeBrew",
    'category': 'Accounting',
    'summary': "Adds custom headers to all accounting XLSX exports",
    'data': [
        'views/journal_report_templates.xml',
    ],
    'installable': True,
    'application': False,
}
