from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item

engine = create_engine('sqlite:///catalogwithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Soccer Category
category1 = Category(name="Soccer")

session.add(category1)
session.commit()

item1 = Item(name="Balls", description="Various soccer Balls from training to pro", category=category1)

session.add(item1)
session.commit()

item2 = Item(name="Footwear", description="Soccer shoes. Indoor and outdoor", category=category1)

session.add(item2)
session.commit()

item3 = Item(name="Shin guards", description="Various items to protect your shin and play safe", category=category1)

session.add(item3)
session.commit()

item4 = Item(name="Socks", description="Soccer socks on many sizes", category=category1)

session.add(item4)
session.commit()


# Baseball Category
category2 = Category(name="Baseball")

session.add(category2)
session.commit()

item1 = Item(name="Baseballs", description="Various BaseBalls from training to pro", category=category2)

session.add(item1)
session.commit()

item2 = Item(name="Bats", description="Various Bats from training to pro", category=category2)

session.add(item2)
session.commit()

item3 = Item(name="Mitts", description="Various Mitts of various sizes", category=category2)

session.add(item3)
session.commit()

# Football Category
category3 = Category(name="Football")

session.add(category3)
session.commit()

item1 = Item(name="Balls", description="Various Balls from training to pro", category=category3)

session.add(item1)
session.commit()

item2 = Item(name="Gloves", description="Various Gloves of various sizes", category=category3)

session.add(item2)
session.commit()

item3 = Item(name="Footwear", description="Football shoes and socks", category=category3)

session.add(item3)
session.commit()

# Volleyball Category
category4 = Category(name="Volleyball")

session.add(category4)
session.commit()

item1 = Item(name="Balls", description="Various Balls from training to pro", category=category4)

session.add(item1)
session.commit()

item2 = Item(name="Court Equipment", description="Nets and related", category=category4)

session.add(item2)
session.commit()

item3 = Item(name="Footwear", description="Volleyball shoes and socks", category=category4)

session.add(item3)
session.commit()


print "added items!"
