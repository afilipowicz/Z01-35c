# Forecast

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_class** | **str** | The data identifier: fod_long_range_daily, fod_short_range_daily | [optional] 
**expire_time_gmt** | **float** | The expiration time in unix seconds: 1471539254 | [optional] 
**fcst_valid** | **float** | The forecast valid time in unix seconds: 1471518000 | [optional] 
**fcst_valid_local** | **str** | The valid time forecast in local apparent time: \&quot;2016-08-18T07:00:00-0400\&quot; | [optional] 
**num** | **int** | The sequential number that identifies each of the forecasted days in your feed. The numbers start on day 1, which is the forecast for the current day. Then the forecast for tomorrow uses number 2, then number 3 for the day after tomorrow, and so forth | [optional] 
**max_temp** | **int** | Daily maximum temperature | [optional] 
**min_temp** | **int** | Daily minimum temperature | [optional] 
**torcon** | **int** | The estimate of the likelihood of tornado activity during a given 24 hour forecast period. | [optional] 
**stormcon** | **int** | The estimate of the likelihood of winter storm activity during a given 24 hour forecast period. | [optional] 
**blurb** | **str** | A handwritten local or regional text forecast created by a meteorologist to supplement the system-generated forecast. | [optional] 
**blurb_author** | **str** | The name initials of the meteorologist who authored the forecast blur. | [optional] 
**lunar_phase_day** | **int** | Day number within monthly lunar cycle | [optional] 
**dow** | **str** | Day of week | [optional] 
**lunar_phase** | **str** | Description phrase for the current lunar phase | [optional] 
**lunar_phase_code** | **str** | 3 character short code for lunar phases | [optional] 
**sunrise** | **str** | The local time of the sunrise. It reflects any local daylight savings conventions. For a few Arctic and Antarctic regions, the Sunrise and Sunset data values may be the same (each with a value of 12:01am) to reflect conditions where a sunrise or sunset does not occur. example: 2016-08-18T07:00:50-0400 | [optional] 
**sunset** | **str** | The local time of the sunset. It reflects any local daylight savings conventions. For a few Arctic and Antarctic regions, the Sunrise and Sunset data values may be the same (each with a value of 12:01am) to reflect conditions where a sunrise or sunset does not occur. example: \&quot;2016-08-18T20:19:22-0400\&quot; | [optional] 
**moonrise** | **str** | First moonrise in local time. It reflects daylight savings time conventions. example: \&quot;2016-08-18T20:35:50-0400\&quot; | [optional] 
**moonset** | **str** | First moonset in local time. It reflects daylight savings time conventions. example: \&quot;2016-08-18T20:35:50-0400\&quot; | [optional] 
**qualifier_code** | **str** | A code for special forecasted weather criteria for the 12 and 24 hour dayparts | [optional] 
**qualifier** | **str** | A phrase associated to the qualifier_code describing special forecasted weather criteria for the 12 and 24 hour dayparts. | [optional] 
**narrative** | **str** | The narrative forecast for the 24-hour period. example: \&quot;Scattered thunderstorms possible. Highs in the low 90s and lows in the low 70s.\&quot; | [optional] 
**qpf** | **float** | The forecasted measurable precipitation (liquid or liquid equivalent) during 12 or 24 hour period. example: 0.02 | [optional] 
**snow_qpf** | **float** | The forecasted measurable precipitation as snow during the 12 or 24 hour forecast period. example: 0 | [optional] 
**snow_range** | **str** | The expected amount of residual snow for the 12 or 24 hour period. | [optional] 
**snow_phrase** | **str** | A shortened text description of the forecasted snow accumulation during the forecast period (24 hours or 12 hours). | [optional] 
**snow_code** | **str** | Residual snow accumulation code for the 12 or 24 hour forecast period. example: A9015 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


