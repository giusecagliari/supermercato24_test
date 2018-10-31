class Location(object):
    def __init__(self, **kwargs):
        self._id = kwargs.get('id')
        self._lat = kwargs.get('lat')
        self._lng = kwargs.get('lng')

    def get_id(self):
        return self._id

    def get_coordinates(self):
        return self._lat, self._lng