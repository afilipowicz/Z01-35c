# SuccessMetadataSchema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | The language to return the response in. For example, en-US, es, es-MX, fr-FR. | [optional] 
**transaction_id** | **str** | Transaction ID for this call of the API. The format varies for APIs and technology stacks. For example, 1407766348658:1285362530. | [optional] 
**version** | **str** | The version number of the API. For example, v1. | [optional] 
**latitude** | **float** | Numeric value from -90 to 90 which specifies the distance north or south of the equator. | [optional] 
**longitude** | **float** | Numeric value from -180 to 180 which specifies the distance east or west of the prime meridian. | [optional] 
**units** | **str** | An echo parameter that displays the default or requested units of measure (UOM) for various numeric values. Valid UOM: e, m, h, s. | [optional] 
**expire_time_gmt** | **float** | The data expiration time in UNIX seconds. The value in this data element should be used to expire and remove a record from your system. For example, 1380170732. | [optional] 
**status_code** | **int** | The status code of the response message. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


