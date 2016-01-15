import os

import webapp2
from google.appengine.ext.webapp import template

from models import sensor_model


class MainHandler(webapp2.RequestHandler):
    def get(self):
        sensors_list_name = self.request.get(sensor_model.Sensor.KEY_SENSOR_NAME,
                                             sensor_model.Sensor.DEFAULT_SENSOR_NAME)

        sensors_query = sensor_model.Sensor.query(ancestor=sensor_model.make_sensor_key(sensors_list_name))\
            .order(sensor_model.Sensor.name)

        sensors_list = sensors_query.fetch()

        path = os.path.join(os.path.dirname(__file__), '../views', 'sensors_view.html')

        self.response.write(
                template.render(path,{
                    'sensors_list': sensors_list
                })
        )
