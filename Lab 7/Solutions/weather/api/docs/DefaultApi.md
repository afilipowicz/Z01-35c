# openapi_client.DefaultApi

All URIs are relative to *https://api.weather.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sun_daily_forecast_by_geocode**](DefaultApi.md#get_sun_daily_forecast_by_geocode) | **GET** /v1/geocode/{latitude}/{longitude}/forecast/daily/{days}day.json | Forecast by Geocode
[**get_sun_daily_forecast_by_location**](DefaultApi.md#get_sun_daily_forecast_by_location) | **GET** /v1/location/{postalCode}/forecast/daily/{days}day.json | Forecast by Postal Code


# **get_sun_daily_forecast_by_geocode**
> SuccessSchema get_sun_daily_forecast_by_geocode(latitude, longitude, days, accept_encoding, units=units, language=language)

Forecast by Geocode

The forecast API returns the geocode weather forecasts for the current day up to the endpoint duration in days.

### Example

* Api Key Authentication (api_key):
```python
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
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **latitude** | **str**| The latitude for the requested forecast. For example, 33.40. | [default to &#39;33.40&#39;]
 **longitude** | **str**| The longitude for the requested forecast. For example -83.42. | [default to &#39;-83.42&#39;]
 **days** | **int**|  | [default to 3]
 **accept_encoding** | **str**| Required to be set to gzip to ensure that the response is compressed | [default to &#39;gzip&#39;]
 **units** | **str**| The units of measure to return the data in. For example, e&#x3D;Imperial(English), m&#x3D;Metric, h&#x3D;Hybrid. Some APIs require the units of measure. | [optional] [default to &#39;m&#39;]
 **language** | **str**| The language to return the response in. For example, en-US, es, es-MX, fr-FR. | [optional] [default to &#39;en-US&#39;]

### Return type

[**SuccessSchema**](SuccessSchema.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. The request has succeeded. |  -  |
**400** | Bad Request. The request could not be understood by the server due to malformed syntax or there is no data found for the location requested. |  -  |
**401** | Unauthorized. The request requires authentication |  -  |
**403** | Forbidden. The server understood the request but is refusing to fulfill it. |  -  |
**404** | Not found. The endpoint requested is not found. |  -  |
**500** | Internal server error. The server encountered an unexpected condition which prevented it from fulfilling the request. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sun_daily_forecast_by_location**
> SuccessSchema get_sun_daily_forecast_by_location(postal_code, days, accept_encoding, units=units, language=language)

Forecast by Postal Code

The forecast API returns the postal code weather forecasts for the current day up to the endpoint duration in days.

### Example

* Api Key Authentication (api_key):
```python
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
    postal_code = '30339:4:US' # str |  (default to '30339:4:US')
days = 3 # int |  (default to 3)
accept_encoding = 'gzip' # str | Required to be set to gzip to ensure that the response is compressed (default to 'gzip')
units = 'm' # str | The units of measure to return the data in. For example, e=Imperial(English), m=Metric, h=Hybrid. Some APIs require the units of measure. (optional) (default to 'm')
language = 'en-US' # str | The language to return the response in. For example, en-US, es, es-MX, fr-FR. (optional) (default to 'en-US')

    try:
        # Forecast by Postal Code
        api_response = api_instance.get_sun_daily_forecast_by_location(postal_code, days, accept_encoding, units=units, language=language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_sun_daily_forecast_by_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **postal_code** | **str**|  | [default to &#39;30339:4:US&#39;]
 **days** | **int**|  | [default to 3]
 **accept_encoding** | **str**| Required to be set to gzip to ensure that the response is compressed | [default to &#39;gzip&#39;]
 **units** | **str**| The units of measure to return the data in. For example, e&#x3D;Imperial(English), m&#x3D;Metric, h&#x3D;Hybrid. Some APIs require the units of measure. | [optional] [default to &#39;m&#39;]
 **language** | **str**| The language to return the response in. For example, en-US, es, es-MX, fr-FR. | [optional] [default to &#39;en-US&#39;]

### Return type

[**SuccessSchema**](SuccessSchema.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. The request has succeeded. |  -  |
**400** | Bad Request. The request could not be understood by the server due to malformed syntax or there is no data found for the location requested. |  -  |
**401** | Unauthorized. The request requires authentication |  -  |
**403** | Forbidden. The server understood the request but is refusing to fulfill it. |  -  |
**404** | Not found. The endpoint requested is not found. |  -  |
**500** | Internal server error. The server encountered an unexpected condition which prevented it from fulfilling the request. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

