class Shopper(object):
    def __init__(self, **kwargs):
        self._id = kwargs.get('id')
        self._lat = kwargs.get('lat')
        self._lng = kwargs.get('lng')
        self._enabled = kwargs.get('enabled')
        self._locations = 0

    def get_id(self):
        return self._id

    def get_coordinates(self):
        return self._lat, self._lng

    def is_enabled(self):
        return self._enabled

    def add_location(self):
        self._locations += 1

    def calculate_coverage(self, total):
        return (self._locations / total) * 100
