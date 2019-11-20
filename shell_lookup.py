# Flask Shell

db.create_all() # Migrate

user = User(username='name')
db.session.add(user)
db.session.commit() # Add a new object
db.session.delete(user)
db.session.commit()

# Query

User.query.all()
User.query.limit(5).all()
User.query.order_by(User.username).all()
User.query.order_by(User.username.desc()).all()

User.query.first()
User.query.get(1)

User.query.order_by(User.username.desc()).limit(5).first()

page = User.query.paginate(1,10)
page.items
page.page #current
page.pages
page.has_prev
page.has_next
page.prev()
page.next()

User.query.filter_by(username='name').all()
User.query.filter(User.id > 1).all()

# SQL Query functions

# from sqlalchemy.sql.expression import not_, or_ 


