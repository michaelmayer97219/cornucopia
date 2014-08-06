from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
product = Table('product', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=120)),
)

sensor = Table('sensor', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('suid', Integer),
    Column('user_id', Integer),
    Column('product_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['product'].create()
    post_meta.tables['sensor'].columns['product_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['product'].drop()
    post_meta.tables['sensor'].columns['product_id'].drop()
