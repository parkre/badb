from app import db

# Users

class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(40))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    name = db.Column(db.String(40))
    login_id = db.Column(db.Integer, db.ForeignKey('login.id'))

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

# Programs

class FileIn(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_file = db.Column(db.String(1024))
    id_osdist = db.Column(db.String(1024))
    id_owner = db.Column(db.String(1024))
    id_group = db.Column(db.String(1024))
    id_perms = db.Column(db.String(1024))

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1024), index=True)
    id_filetype = db.Column(db.Integer, db.ForeignKey=('FileIn.id'))
    
    def __repr__(self):
        return '<File %r>' % (self.file)

class FileType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1024), index=True)
    files = db.Relationship('File', backref='FileType', lazy='dynamic')
    
    def __repr__(self):
        return '<File %r>' % (self.file)
    
class OSDist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), index=True)

    def __repr__(self):
        return '<File %r>' % (self.file)
    
class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True)

    def __repr__(self):
        return '<Owner %r>' % self.name

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True)

    def __repr__(self):
        return '<Group %r>' % self.name
    
class Perms(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1024), index=True)

    def __repr__(self):
        return '<File %r>' % (self.file)
    
# Analysis Facts

class Entries:
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)
    id_analysis = db.Column(db.Integer, db.ForeignKey('analysis.id'))
    id_facts = db.Column(db.Integer, db.ForeignKey('facts.id'))
    id_filein = db.Column(db.Integer, db.ForeignKey('filein.id'))
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    return_code = db.Column(db.Integer)
    
class Analysis:
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1024), index=True)
    entry = db.relationship('Entry', backref='Entry', lazy='dynamic')    

class Facts:
    id = db.Column(db.Integer, primary_key=True)
    fact = db.Column(db.String(1024))
     = db.relationship('Similarity', backref='bruh', lazy='dynamic')
    
    def __repr__(self):
        return '<Fact %r>' % (self.fact)

