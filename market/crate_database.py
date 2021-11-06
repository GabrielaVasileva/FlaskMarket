from market import db

db.create_all()

from market.models import Item

item1 = Item(name="Phone",price= 500, description='Phone description', barcode='893212299897')
item2 = Item(name="Laptop",price=900, description='Laptop description', barcode='123985473165')
item3 = Item(name="Keyboard",price= 150, description='Keyboard description', barcode='231985128446')

db.session.add(item1)
db.session.add(item2)
db.session.add(item3)
db.session.commit()
Item.query.all()