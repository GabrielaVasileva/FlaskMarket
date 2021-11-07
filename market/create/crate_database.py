from market import db

db.drop_all()
db.create_all()

from market.models import db

from market.models import User, Item

u1=User(username='gabi', password_hash='123456', email_address='gabi@gabi.com')
u2=User(username='lily', password_hash='123456', email_address='lily@lily.com')
u3=User(username='koko', password_hash='123456', email_address='koko@koko.com')
u4=User(username='dan', password_hash='123456', email_address='dan@dan.com')
db.session.add(u1)
db.session.add(u2)
db.session.add(u3)
db.session.add(u4)
db.session.commit()


item1 = Item(name="Phone", price=500, description='Phone description', barcode='893212299897')
item2 = Item(name="Laptop", price=900, description='Laptop description', barcode='123985473165')
item3 = Item(name="Keyboard", price=150, description='Keyboard description', barcode='231985128446')

db.session.add(item1)
db.session.add(item2)
db.session.add(item3)
db.session.commit()
Item.query.all()

item1.owner = User.query.filter_by(username='gabi').first().id
db.session.add(item1)
db.session.commit()

i = Item.query.filter_by(name='Phone').first()


