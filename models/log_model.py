from google.appengine.ext import ndb

import sensor_model


class Log(ndb.Model):
    sensor = ndb.StructuredProperty(sensor_model)
    datetime = ndb.DateTimeProperty(auto_now=True)
