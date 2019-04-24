from flask_table import Table, Col, LinkCol

class Results(Table):
    id = Col('Id', show=False)
    label = Col('Label')
    brand = Col('Brand')
    title = Col('Title')
    code = Col('Code')
    price = Col('Price')
    edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='id'))
    delete = LinkCol('Delete', 'delete', url_kwargs=dict(id='id'))