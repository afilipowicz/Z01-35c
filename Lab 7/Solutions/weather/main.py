from __future__ import print_function

import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.weather.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = openapi_client.Configuration(
    host = "https://api.weather.com",
    api_key = {
        'apiKey': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    latitude = '33.40' # str | The latitude for the requested forecast. For example, 33.40. (default to '33.40')
longitude = '-83.42' # str | The longitude for the requested forecast. For example -83.42. (default to '-83.42')
days = 3 # int |  (default to 3)
accept_encoding = 'gzip' # str | Required to be set to gzip to ensure that the response is compressed (default to 'gzip')
units = 'm' # str | The units of measure to return the data in. For example, e=Imperial(English), m=Metric, h=Hybrid. Some APIs require the units of measure. (optional) (default to 'm')
language = 'en-US' # str | The language to return the response in. For example, en-US, es, es-MX, fr-FR. (optional) (default to 'en-US')

try:
    # Forecast by Geocode
    api_response = api_instance.get_sun_daily_forecast_by_geocode(latitude, longitude, days, accept_encoding, units=units, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_sun_daily_forecast_by_geocode: %s\n" % e)