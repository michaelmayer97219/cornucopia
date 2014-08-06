from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    #role = db.Column(db.SmallInteger, default = ROLE_USER)
    #address = db.Column(db.String(120), index = True, unique = False)
    #city = db.Column(db.String(64), index = True, unique = False)
    #state = db.Column(db.String(40), index = True, unique = False)
    #zip = db.Column(db.Integer, index = True, unique = False)
    sensors = db.relationship('Sensor', backref='user', lazy = 'dynamic')
    

    def __repr__(self):
    	return '<sensor %r>'

class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    suid = db.Column(db.Integer, index = True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    observations = db.relationship('Observation', backref= 'sensor', lazy = 'dynamic')
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))

    def __repr__(self):
        return '<Sensor %r>' % (self.suid)

class Observation(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    level = db.Column(db.Numeric(10))
    #timestamp = db.Column(db.DateTime)
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.id'))

    def __repr__(self):
        return '<Observation %r>' % (self.level)



class Product(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(120), index=True, unique=True)
	sensors = db.relationship('Sensor', backref='sensor', lazy='dynamic')

