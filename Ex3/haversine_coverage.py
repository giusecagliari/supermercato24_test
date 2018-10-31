from haversine import haversine
import data
from shopper import Shopper
from location import Location


def haversine_coverage():
    shoppers_coverage = {}
    sorted_coverage = []
    locations = len(data.locations)

    for shopper_data in data.shoppers:
        shopper = Shopper(**shopper_data)

        for location_data in data.locations:
            location = Location(**location_data)
            distance = haversine(shopper.get_coordinates(), location.get_coordinates())

            if distance < 10.:
                shopper.add_location()

        shoppers_coverage[shopper.get_id()] = shopper.calculate_coverage(locations)

    sorted_shoppers = sorted(shoppers_coverage.items(), key=lambda x: x[1], reverse=True)

    for shopper, coverage in sorted_shoppers:
        sorted_coverage.append({'shopper_id': shopper, 'coverage': coverage})

    return sorted_coverage

