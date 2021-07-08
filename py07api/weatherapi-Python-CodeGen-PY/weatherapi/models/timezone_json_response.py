# -*- coding: utf-8 -*-

"""
    weatherapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class TimezoneJsonResponse(object):

    """Implementation of the 'TimezoneJson Response' model.

    TODO: type model description here.

    Attributes:
        name (string): Local area name.
        region (string): Local area region.
        country (string): Country
        lat (float): Area latitude
        lon (float): Area longitude
        tz_id (string): Time zone
        localtime_epoch (int): Local date and time in unix time
        localtime (string): Local date and time

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "region":'region',
        "country":'country',
        "lat":'lat',
        "lon":'lon',
        "tz_id":'tz_id',
        "localtime_epoch":'localtime_epoch',
        "localtime":'localtime'
    }

    def __init__(self,
                 name=None,
                 region=None,
                 country=None,
                 lat=None,
                 lon=None,
                 tz_id=None,
                 localtime_epoch=None,
                 localtime=None):
        """Constructor for the TimezoneJsonResponse class"""

        # Initialize members of the class
        self.name = name
        self.region = region
        self.country = country
        self.lat = lat
        self.lon = lon
        self.tz_id = tz_id
        self.localtime_epoch = localtime_epoch
        self.localtime = localtime


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
        name = dictionary.get('name')
        region = dictionary.get('region')
        country = dictionary.get('country')
        lat = dictionary.get('lat')
        lon = dictionary.get('lon')
        tz_id = dictionary.get('tz_id')
        localtime_epoch = dictionary.get('localtime_epoch')
        localtime = dictionary.get('localtime')

        # Return an object of this model
        return cls(name,
                   region,
                   country,
                   lat,
                   lon,
                   tz_id,
                   localtime_epoch,
                   localtime)


