{
'name': 'Library Members',
'description': 'Manage people who will be able to borrow books.',
'author': 'Ahmed F.',
'depends': ['library_app', 'mail'],
'application': False,
'data': [
'views/book_view.xml',
'security/library_security.xml',
'security/ir.model.access.csv',
'views/member_view.xml',
'views/library_menu.xml',
'views/book_list_template.xml',
],
}
