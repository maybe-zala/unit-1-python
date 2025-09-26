from math import radians, sin, cos, sqrt, atan2
def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculates the Haversine distance between two points on the Earth's surface.
    
    :param lat1: Latitude of the first point (float)
    :param lon1: Longitude of the first point (float)
    :param lat2: Latitude of the second point (float)
    :param lon2: Longitude of the second point (float)
    :return: Distance between the two points in kilometers (float)
    """
    # Radius of the Earth in kilometers
    R = 6371.0
    
    # Convert latitude and longitude from degrees to radians
    lat1_rad = radians(lat1)
    lon1_rad = radians(lon1)
    lat2_rad = radians(lat2)
    lon2_rad = radians(lon2)
    
    # Differences in coordinates
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    
    # Haversine formula
    a = sin(dlat / 2)**2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    
    distance = R * c
    return distance

def find_closest_location(lat, lon):
    """
    Finds the closest location from a set of coordinates based on the given location map.
    
    :param lat: Latitude of the given point (float)
    :param lon: Longitude of the given point (float)
    :return: Closest location name (str)
    """
    
    # Location map with predefined coordinates
    location_map = {
        (40.748817, -73.985428): "Empire State Building, New York",
        (48.858844, 2.294351): "Eiffel Tower, Paris",
        (34.052235, -118.243683): "Hollywood Sign, Los Angeles",
        (51.507351, -0.127758): "Big Ben, London",
        (37.774929, -122.419418): "Golden Gate Bridge, San Francisco",
        (-33.868820, 151.209296): "Sydney Opera House, Sydney",
        (35.689487, 139.691711): "Shibuya Crossing, Tokyo",
        (55.755825, 37.617298): "Red Square, Moscow",
        (27.175144, 78.042155): "Taj Mahal, Agra",
        (25.197197, 55.274376): "Burj Khalifa, Dubai"
    }
    
    closest_location = None
    min_distance = float('inf')
    
    for (loc_lat, loc_lon), location_name in location_map.items():
        distance = haversine_distance(lat, lon, loc_lat, loc_lon)
        if distance < min_distance:
            min_distance = distance
            closest_location = location_name
    
    return closest_location