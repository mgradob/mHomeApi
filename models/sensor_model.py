from google.appengine.ext import ndb


class Value(ndb.Model):
    """ Module that represents a sensor's values.
    """
    name = ndb.StringProperty()
    value = ndb.StringProperty()


class Sensor(ndb.Model):
    """ Module that represents a sensor.
    """
    id = ndb.StringProperty()
    name = ndb.StringProperty()
    address = ndb.StringProperty()
    values = ndb.StructuredProperty(Value, repeated=True)

    """ Keys for HTTP methods.
    """
    KEY_SENSOR_NAME = 'sensor_name'

    """ Default values.
    """
    DEFAULT_SENSOR_NAME = 'default_sensor_name'


def make_sensor_key(sensor_name=Sensor.DEFAULT_SENSOR_NAME):
    return ndb.Key('Sensors', sensor_name)
