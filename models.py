try:
    from app import app as app
except ImportError:
    from __main__ import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genre = db.Column(db.String(1000))
    facebook_link = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    website_link = db.Column(db.String(120))
    looking_for_talent = db.Column(db.Boolean , default = False)
    seeking_description = db.Column(db.String(300))

    shows = db.relationship('Show', backref = 'venue', lazy=True, cascade="all, delete") #this is the relationship address to the shows module
    genres = db.relationship('Genre', backref = 'venue', lazy=True, cascade="all, delete") #this is the relationship address to the Genre module


    def __repr__(self):
      return f'<Venues {self.id} {self.name}>'

    
class Artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genre = db.Column(db.String(120))    
    facebook_link = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    website_link = db.Column(db.String(120))
    looking_for_venues = db.Column(db.Boolean , default = False)
    seeking_description = db.Column(db.String(300))
    
    shows = db.relationship('Show', backref = 'artist', lazy=True, cascade="all, delete") #this is the relationship address to the shows module
    genres = db.relationship('Genre', backref = 'artist', lazy=True, cascade="all, delete" ) #this is the relationship address to the Genre module

    def __repr__(self):
      return f'<Artists {self.id} {self.name}>'

class Show(db.Model):
  __tablename__ = 'show'

  id = db.Column(db.Integer, primary_key=True)
  venues_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)  #this creates a foreign key with the venues table
  artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)  #this creates a foreign key with the venues table
  start_time = db.Column(db.DateTime)

  def __repr__(self):

    return f'<Show {self.id} >'



#----according to the list entry we have to entre a new table for the multiple genres----------

class Genre(db.Model):
   __tablename__ = 'genre'

   id = db.Column(db.Integer, primary_key=True)
   genre =  db.Column(db.String(200))
   venues_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)  #this creates a foreign key with the venues table
   artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)  #this creates a foreign key with the venues table
   def __repr__(self):

    return f'<genre {self.id} >' 




#delete-orphan --This is a common feature when dealing with a related object that is “owned” by its parent, 
# with a NOT NULL foreign key, so that removal of the item from the parent collection results in its deletion
#items = relationship("Item", cascade="all, delete-orphan")


#DELETE --The delete cascade indicates that when a “parent” object is marked for deletion, its related “child” objects should also be marked for deletion
#cascade="all, delete"





