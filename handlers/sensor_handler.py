import json

import webapp2

from models import sensor_model


class SensorHandler(webapp2.RequestHandler):
    """ A handler of HTTP methods for a Sensor.
    """

    def post(self):
        name = self.request.get(sensor_model.Sensor.KEY_SENSOR_NAME, sensor_model.Sensor.DEFAULT_SENSOR_NAME)

        new_sensor = sensor_model.Sensor(parent=sensor_model.make_sensor_key(name))

        body = json.loads(self.request.body)

        new_sensor.name = body['name']
        new_sensor.id = body['id']
        new_sensor.address = body['address']

        values = []
        for value in body['values']:
            values.append(sensor_model.Value(name=value['name'], value=str(value['value'])))

        new_sensor.values = values

        new_sensor.put()

        self.redirect('/')
