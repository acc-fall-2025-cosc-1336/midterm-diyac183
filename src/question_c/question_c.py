#write functions here, don't add input('') statements here!
def get_miles_per_hour(kilometers, minutes):
    # Return error string for negative inputs (and avoid division by zero)
    if kilometers < 0 or minutes <= 0:
        return 'Invalid arguments'
    miles = kilometers * 0.621371
    hours = minutes / 60.0
    return miles / hours

import sys
sys.path.append("./")
from question_c import get_miles_per_hour

def test_get_miles_per_hour_32km_60min():
    assert get_miles_per_hour(32, 60) == sys.approx(19.883872)