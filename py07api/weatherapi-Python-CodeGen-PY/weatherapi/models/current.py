# -*- coding: utf-8 -*-

"""
    weatherapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import weatherapi.models.condition

class Current(object):

    """Implementation of the 'Current' model.

    TODO: type model description here.

    Attributes:
        last_updated_epoch (int): Local time when the real time data was
            updated in unix time.
        last_updated (string): Local time when the real time data was
            updated.
        temp_c (float): Temperature in celsius
        temp_f (float): Temperature in fahrenheit
        is_day (int): 1 = Yes 0 = No <br />Whether to show day condition icon
            or night icon
        condition (Condition): TODO: type description here.
        wind_mph (float): Wind speed in miles per hour
        wind_kph (float): Wind speed in kilometer per hour
        wind_degree (int): Wind direction in degrees
        wind_dir (string): Wind direction as 16 point compass. e.g.: NSW
        pressure_mb (float): Pressure in millibars
        pressure_in (float): Pressure in inches
        precip_mm (float): Precipitation amount in millimeters
        precip_in (float): Precipitation amount in inches
        humidity (int): Humidity as percentage
        cloud (int): Cloud cover as percentage
        feelslike_c (float): Feels like temperature as celcius
        feelslike_f (float): Feels like temperature as fahrenheit
        vis_km (float): TODO: type description here.
        vis_miles (float): TODO: type description here.
        uv (float): UV Index
        gust_mph (float): Wind gust in miles per hour
        gust_kph (float): Wind gust in kilometer per hour

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "last_updated_epoch":'last_updated_epoch',
        "last_updated":'last_updated',
        "temp_c":'temp_c',
        "temp_f":'temp_f',
        "is_day":'is_day',
        "condition":'condition',
        "wind_mph":'wind_mph',
        "wind_kph":'wind_kph',
        "wind_degree":'wind_degree',
        "wind_dir":'wind_dir',
        "pressure_mb":'pressure_mb',
        "pressure_in":'pressure_in',
        "precip_mm":'precip_mm',
        "precip_in":'precip_in',
        "humidity":'humidity',
        "cloud":'cloud',
        "feelslike_c":'feelslike_c',
        "feelslike_f":'feelslike_f',
        "vis_km":'vis_km',
        "vis_miles":'vis_miles',
        "uv":'uv',
        "gust_mph":'gust_mph',
        "gust_kph":'gust_kph'
    }

    def __init__(self,
                 last_updated_epoch=None,
                 last_updated=None,
                 temp_c=None,
                 temp_f=None,
                 is_day=None,
                 condition=None,
                 wind_mph=None,
                 wind_kph=None,
                 wind_degree=None,
                 wind_dir=None,
                 pressure_mb=None,
                 pressure_in=None,
                 precip_mm=None,
                 precip_in=None,
                 humidity=None,
                 cloud=None,
                 feelslike_c=None,
                 feelslike_f=None,
                 vis_km=None,
                 vis_miles=None,
                 uv=None,
                 gust_mph=None,
                 gust_kph=None):
        """Constructor for the Current class"""

        # Initialize members of the class
        self.last_updated_epoch = last_updated_epoch
        self.last_updated = last_updated
        self.temp_c = temp_c
        self.temp_f = temp_f
        self.is_day = is_day
        self.condition = condition
        self.wind_mph = wind_mph
        self.wind_kph = wind_kph
        self.wind_degree = wind_degree
        self.wind_dir = wind_dir
        self.pressure_mb = pressure_mb
        self.pressure_in = pressure_in
        self.precip_mm = precip_mm
        self.precip_in = precip_in
        self.humidity = humidity
        self.cloud = cloud
        self.feelslike_c = feelslike_c
        self.feelslike_f = feelslike_f
        self.vis_km = vis_km
        self.vis_miles = vis_miles
        self.uv = uv
        self.gust_mph = gust_mph
        self.gust_kph = gust_kph


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        last_updated_epoch = dictionary.get('last_updated_epoch')
        last_updated = dictionary.get('last_updated')
        temp_c = dictionary.get('temp_c')
        temp_f = dictionary.get('temp_f')
        is_day = dictionary.get('is_day')
        condition = weatherapi.models.condition.Condition.from_dictionary(dictionary.get('condition')) if dictionary.get('condition') else None
        wind_mph = dictionary.get('wind_mph')
        wind_kph = dictionary.get('wind_kph')
        wind_degree = dictionary.get('wind_degree')
        wind_dir = dictionary.get('wind_dir')
        pressure_mb = dictionary.get('pressure_mb')
        pressure_in = dictionary.get('pressure_in')
        precip_mm = dictionary.get('precip_mm')
        precip_in = dictionary.get('precip_in')
        humidity = dictionary.get('humidity')
        cloud = dictionary.get('cloud')
        feelslike_c = dictionary.get('feelslike_c')
        feelslike_f = dictionary.get('feelslike_f')
        vis_km = dictionary.get('vis_km')
        vis_miles = dictionary.get('vis_miles')
        uv = dictionary.get('uv')
        gust_mph = dictionary.get('gust_mph')
        gust_kph = dictionary.get('gust_kph')

        # Return an object of this model
        return cls(last_updated_epoch,
                   last_updated,
                   temp_c,
                   temp_f,
                   is_day,
                   condition,
                   wind_mph,
                   wind_kph,
                   wind_degree,
                   wind_dir,
                   pressure_mb,
                   pressure_in,
                   precip_mm,
                   precip_in,
                   humidity,
                   cloud,
                   feelslike_c,
                   feelslike_f,
                   vis_km,
                   vis_miles,
                   uv,
                   gust_mph,
                   gust_kph)

