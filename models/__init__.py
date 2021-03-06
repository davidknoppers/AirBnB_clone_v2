#!/usr/bin/python3
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.place import PlaceAmenity

from models.engine import file_storage
from models.engine import db_storage
from os import getenv


if getenv('HBNB_TYPE_STORAGE', 'fs') == 'db':
    storage = db_storage.DBstorage()
else:
    storage = file_storage.FileStorage()
storage.reload()
