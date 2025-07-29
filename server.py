import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/datascraper/api/us-real-estate'

mcp = FastMCP('us-real-estate')

@mcp.tool()
def v3_property_detail(property_id: Annotated[str, Field(description='')]) -> dict: 
    '''Get property detail data by `property_id`'''
    url = 'https://us-real-estate.p.rapidapi.com/v3/property-detail'
    headers = {'x-rapidapi-host': 'us-real-estate.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'property_id': property_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_property_detail(property_id: Annotated[Union[int, float], Field(description='Default: 3199790641')]) -> dict: 
    '''Get property detail data by `property_id` V2'''
    url = 'https://us-real-estate.p.rapidapi.com/v2/property-detail'
    headers = {'x-rapidapi-host': 'us-real-estate.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'property_id': property_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def property_detail(property_id: Annotated[str, Field(description='')]) -> dict: 
    '''Get property detail data by `property_id`'''
    url = 'https://us-real-estate.p.rapidapi.com/property-detail'
    headers = {'x-rapidapi-host': 'us-real-estate.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'property_id': property_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def property_by_mls_id(mls_id: Annotated[str, Field(description='')]) -> dict: 
    '''Search properties by MLS ID'''
    url = 'https://us-real-estate.p.rapidapi.com/property-by-mls-id'
    headers = {'x-rapidapi-host': 'us-real-estate.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'mls_id': mls_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def keywords_search_suggest(keyword_text: Annotated[str, Field(description='')],
                            limit: Annotated[Union[int, float, None], Field(description='Default: 10')] = None) -> dict: 
    '''Get keyword search suggestion for `keyword_seach` parameters in `/for-sale` endpoint'''
    url = 'https://us-real-estate.p.rapidapi.com/keywords-search-suggest'
    headers = {'x-rapidapi-host': 'us-real-estate.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'keyword_text': keyword_text,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def location_suggest(input: Annotated[str, Field(description='Part of location name')]) -> dict: 
    '''Get location suggestion / autocomplete **Required Parameter**: `input` **Optional Parameter**:'''
    url = 'https://us-real-estate.p.rapidapi.com/location/suggest'
    headers = {'x-rapidapi-host': 'us-real-estate.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'input': input,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def location_for_sale_nearby_areas(area_type: Annotated[str, Field(description='One of the following options: city|neighborhood')],
                                   city: Annotated[Union[str, None], Field(description='')] = None,
                                   neighborhood: Annotated[Union[str, None], Field(description='')] = None,
                                   postal_code: Annotated[Union[str, None], Field(description='')] = None,
                                   state_code: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Get nearby areas for **include_nearby_areas_slug_id** parameter in **/for-sale** endpoint. Get by (area_type="city" & city & state_code) or by (area_type="neighborhood" & city & state_code & neighborhood) or by (area_type="postal_code" & postal_code)'''
    url = 'https://us-real-estate.p.rapidapi.com/location/for-sale-nearby-areas'
    headers = {'x-rapidapi-host': 'us-real-estate.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'area_type': area_type,
        'city': city,
        'neighborhood': neighborhood,
        'postal_code': postal_code,
        'state_code': state_code,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def location_for_sale_nearby_areas_by_postal_code(postal_code: Annotated[str, Field(description='')]) -> dict: 
    '''Get nearby areas by `postal_code` for **include_nearby_areas_slug_id** parameter in **/for-sale** endpoint.'''
    url = 'https://us-real-estate.p.rapidapi.com/location/for-sale-nearby-areas-by-postal-code'
    headers = {'x-rapidapi-host': 'us-real-estate.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'postal_code': postal_code,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def location_for_rent_nearby_areas(area_type: Annotated[str, Field(description='One of the following options: city|postal_code|neighborhood')],
                                   city: Annotated[Union[str, None], Field(description='')] = None,
                                   neighborhood: Annotated[Union[str, None], Field(description='')] = None,
                                   state_code: Annotated[Union[str, None], Field(description='')] = None,
                                   postal_code: Annotated[Union[int, float, None], Field(description='Default: 14218')] = None) -> dict: 
    '''Get nearby areas for **include_nearby_areas_slug_id** parameter in **/for-rent**. Get by (area_type="city" & city & state_code) or by (area_type="neighborhood" & city & state_code & neighborhood) or by (area_type="postal_code" & postal_code)'''
    url = 'https://us-real-estate.p.rapidapi.com/location/for-rent-nearby-areas'
    headers = {'x-rapidapi-host': 'us-real-estate.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'area_type': area_type,
        'city': city,
        'neighborhood': neighborhood,
        'state_code': state_code,
        'postal_code': postal_code,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def location_schools(postal_code: Annotated[Union[int, float, None], Field(description='Default: 14218')] = None,
                     city: Annotated[Union[str, None], Field(description='')] = None,
                     state_code: Annotated[Union[str, None], Field(description='')] = None,
                     neighborhood: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Get schools near a location by (**state_code & city**) or by (**state_code & city & neighborhood**) or by **postal_code**'''
    url = 'https://us-real-estate.p.rapidapi.com/location/schools'
    headers = {'x-rapidapi-host': 'us-real-estate.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'postal_code': postal_code,
        'city': city,
        'state_code': state_code,
        'neighborhood': neighborhood,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def location_commute_time(origins: Annotated[str, Field(description='Origin location: address, city+state_code, neighborhood, postal_code, etc')],
                          destinations: Annotated[str, Field(description='Destination location: address, city+state_code, neighborhood, postal_code, etc')],
                          mode: Annotated[str, Field(description='One of the following options: driving|walking|bicycling|transit')]) -> dict: 
    '''Get commute time from origins to destinations with one of following mode: walking|driving|bicycling|transit'''
    url = 'https://us-real-estate.p.rapidapi.com/location/commute-time'
    headers = {'x-rapidapi-host': 'us-real-estate.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'origins': origins,
        'destinations': destinations,
        'mode': mode,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def location_noise_score(longitude: Annotated[Union[int, float], Field(description='Default: -73.95471')],
                         latitude: Annotated[Union[int, float], Field(description='Default: 40.769135')]) -> dict: 
    '''Get location noise score by (**latitude & longitude**)'''
    url = 'https://us-real-estate.p.rapidapi.com/location/noise-score'
    headers = {'x-rapidapi-host': 'us-real-estate.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'longitude': longitude,
        'latitude': latitude,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_for_sale(state_code: Annotated[str, Field(description='State Code. Get from /location/suggest response')],
                city: Annotated[Union[str, None], Field(description='City name. Get data from /location/suggest response')] = None,
                sort: Annotated[Union[str, None], Field(description='One of the following options: relevant|newest|lowest_price|highest_price|open_house_date|price_reduced_date|largest_sqft|lot_size|sold_date. Default is newest')] = None,
                offset: Annotated[Union[int, float, None], Field(description='Offset results, default 0. Maximum 9800. Default: 0')] = None,
                limit: Annotated[Union[int, float, None], Field(description='Number of results. Maximum 200 for Paid Plan, default 42 Default: 42')] = None,
                location: Annotated[Union[str, None], Field(description='Additional Location detail, could be neighborhood or postal_code or leave it blank. Get from /location/suggest response. Default is blank')] = None,
                price_min: Annotated[Union[str, None], Field(description='Minimum list price in USD')] = None,
                price_max: Annotated[Union[str, None], Field(description='Maximum list price in USD')] = None,
                beds_min: Annotated[Union[str, None], Field(description='Minimum bedrooms')] = None,
                beds_max: Annotated[Union[str, None], Field(description='Maximum bedrooms')] = None,
                baths_min: Annotated[Union[str, None], Field(description='Minimum bathrooms')] = None,
                baths_max: Annotated[Union[str, None], Field(description='Maximum bathrooms')] = None,
                property_type: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: multi_family|single_family|mobile|land|farm')] = None,
                property_type_nyc_only: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: condo|coop|condop. For NYC listings only')] = None,
                new_construction: Annotated[Union[str, None], Field(description='true for New construction only. Leave blank for any')] = None,
                hide_pending_contingent: Annotated[Union[str, None], Field(description='true for hide pending/contingent. Leave blank for any')] = None,
                has_virtual_tours: Annotated[Union[str, None], Field(description='true for properties with virtual tour only. Leave blank for any')] = None,
                has_3d_tours: Annotated[Union[str, None], Field(description='true for properties with 3D tour only. Leave blank for any')] = None,
                hide_foreclosure: Annotated[Union[str, None], Field(description='true for hide foreclosure. Leave blank for any')] = None,
                price_reduced: Annotated[Union[str, None], Field(description='true for properties with price reduced only. Leave blank for any')] = None,
                open_house: Annotated[Union[str, None], Field(description='true for properties with open house only. Leave blank for any')] = None,
                keywords: Annotated[Union[str, None], Field(description='Comma separated values. Get popular keywords from /keywords-search-suggest response')] = None,
                no_hoa_fee: Annotated[Union[str, None], Field(description='true for properties without HOA fee only. Leave blank for any')] = None,
                hoa_max: Annotated[Union[str, None], Field(description='Maximum HOA fee in USD')] = None,
                days_on_realtor: Annotated[Union[str, None], Field(description='One of the following options: today|7|14|21|30')] = None,
                expand_search_radius: Annotated[Union[str, None], Field(description='One of the following options: 1|5|10|25|50. Expand search by radius in miles')] = None,
                include_nearby_areas_slug_id: Annotated[Union[str, None], Field(description='Comma separated values. Expand search by including nearby areas. Get slug_id from /location/for-sale-nearby-areas')] = None,
                home_size_min: Annotated[Union[str, None], Field(description='One of the following options: 750|1000|1250|1500|1750|2000|2250|2500|2750|3000|3250|3500|3750|5000|7500. Minimum home size in sqft')] = None,
                home_size_max: Annotated[Union[str, None], Field(description='One of the following options: 1000|1250|1500|1750|2000|2250|2500|2750|3000|3250|3500|3750|5000|7500|10000. Maximum home size in sqft')] = None,
                lot_size_min: Annotated[Union[str, None], Field(description='One of the following options: 2000|300|4000|5000|7500|10890|21780|43560|87120|217800|435600|653400|871200. Minimum lot size in sqft')] = None,
                lot_size_max: Annotated[Union[str, None], Field(description='One of the following options: 2000|300|4000|5000|7500|10890|21780|43560|87120|217800|435600|653400|871200. Maximum lot size in sqft')] = None,
                home_age_max: Annotated[Union[str, None], Field(description='Maximum home age')] = None,
                stories: Annotated[Union[str, None], Field(description='One of the following options: single|multi')] = None,
                garage: Annotated[Union[str, None], Field(description='One of the following options: 1+|2+|3+')] = None,
                heating_cooling: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: central_air|central_heat|forced_air')] = None,
                inside_rooms: Annotated[Union[str, None], Field(description='Comma separated values. One or more comma separated from following options: basement|hardwood_floors|fireplace|disability_features|den_or_office|family_room|dining_room')] = None,
                outside_features: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: swimming_pool|spa_or_hot_tub|horse_facilities')] = None,
                lot_views: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: waterfront|cul_de_sac|corner_lot|golf_course_lot_or_frontage|hill_or_mountain_view|ocean_view|lake_view|river_view')] = None,
                community_ammenities: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: community_swimming_pool|community_spa_or_hot_tub|community_golf|community_security_features|community_boat_facilities|tennis_court|community_clubhouse|senior_community')] = None,
                features_in_nyc_only: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: furniture|dishwasher|community_doorman|pets_allowed|laundry_room|elevator|community_outdoor_space')] = None) -> dict: 
    '''Search for-sale properties. **Parameters**: ` **state_code**,city, location, sort, limit, offset, price_min, price_max, beds_min, beds_max, baths_min, baths_max, property_type, property_type_nyc_only, new_construction, hide_pending_contingent, has_virtual_tours, has_3d_tours, hide_foreclosure, price_reduced, open_house, keywords, no_hoa_fee, hoa_max, days_on_realtor, expand_search_radius, include_nearby_areas_slug_id, home_size_min, home_size_max, lot_size_min, lot_size_max, home_age_max, stories, garage, heating_cooling, inside_rooms, outside_features, lot_views, community_ammenities, features_in_nyc_only`'''
    url = 'https://us-real-estate.p.rapidapi.com/v3/for-sale'
    headers = {'x-rapidapi-host': 'us-real-estate.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state_code': state_code,
        'city': city,
        'sort': sort,
        'offset': offset,
        'limit': limit,
        'location': location,
        'price_min': price_min,
        'price_max': price_max,
        'beds_min': beds_min,
        'beds_max': beds_max,
        'baths_min': baths_min,
        'baths_max': baths_max,
        'property_type': property_type,
        'property_type_nyc_only': property_type_nyc_only,
        'new_construction': new_construction,
        'hide_pending_contingent': hide_pending_contingent,
        'has_virtual_tours': has_virtual_tours,
        'has_3d_tours': has_3d_tours,
        'hide_foreclosure': hide_foreclosure,
        'price_reduced': price_reduced,
        'open_house': open_house,
        'keywords': keywords,
        'no_hoa_fee': no_hoa_fee,
        'hoa_max': hoa_max,
        'days_on_realtor': days_on_realtor,
        'expand_search_radius': expand_search_radius,
        'include_nearby_areas_slug_id': include_nearby_areas_slug_id,
        'home_size_min': home_size_min,
        'home_size_max': home_size_max,
        'lot_size_min': lot_size_min,
        'lot_size_max': lot_size_max,
        'home_age_max': home_age_max,
        'stories': stories,
        'garage': garage,
        'heating_cooling': heating_cooling,
        'inside_rooms': inside_rooms,
        'outside_features': outside_features,
        'lot_views': lot_views,
        'community_ammenities': community_ammenities,
        'features_in_nyc_only': features_in_nyc_only,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_for_sale(offset: Annotated[Union[int, float], Field(description='Offset results, default 0. Maximum 9800. Default: 0')],
                limit: Annotated[Union[int, float], Field(description='Number of results. Maximum 200 for Paid Plan, default 42 Default: 42')],
                state_code: Annotated[str, Field(description='State Code. Get from /location/suggest response')],
                city: Annotated[str, Field(description='City name. Get data from /location/suggest response')],
                location: Annotated[Union[str, None], Field(description='Additional Location detail, could be neighborhood or postal_code or leave it blank. Get from /location/suggest response. Default is blank')] = None,
                sort: Annotated[Union[str, None], Field(description='One of the following options: relevant|newest|lowest_price|highest_price|open_house_date|price_reduced_date|largest_sqft|lot_size|sold_date. Default is relevant')] = None,
                price_min: Annotated[Union[str, None], Field(description='Minimum list price in USD')] = None,
                price_max: Annotated[Union[str, None], Field(description='Maximum list price in USD')] = None,
                beds_min: Annotated[Union[str, None], Field(description='Minimum bedrooms')] = None,
                beds_max: Annotated[Union[str, None], Field(description='Maximum bedrooms')] = None,
                baths_min: Annotated[Union[str, None], Field(description='Minimum bathrooms')] = None,
                baths_max: Annotated[Union[str, None], Field(description='Maximum bathrooms')] = None,
                property_type: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: multi_family|single_family|mobile|land|farm')] = None,
                property_type_nyc_only: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: condo|coop|condop. For NYC listings only')] = None,
                new_construction: Annotated[Union[str, None], Field(description='true for New construction only. Leave blank for any')] = None,
                hide_pending_contingent: Annotated[Union[str, None], Field(description='true for hide pending/contingent. Leave blank for any')] = None,
                has_virtual_tours: Annotated[Union[str, None], Field(description='true for properties with virtual tour only. Leave blank for any')] = None,
                has_3d_tours: Annotated[Union[str, None], Field(description='true for properties with 3D tour only. Leave blank for any')] = None,
                hide_foreclosure: Annotated[Union[str, None], Field(description='true for hide foreclosure. Leave blank for any')] = None,
                price_reduced: Annotated[Union[str, None], Field(description='true for properties with price reduced only. Leave blank for any')] = None,
                open_house: Annotated[Union[str, None], Field(description='true for properties with open house only. Leave blank for any')] = None,
                keywords: Annotated[Union[str, None], Field(description='Comma separated values. Get popular keywords from /keywords-search-suggest response')] = None,
                no_hoa_fee: Annotated[Union[str, None], Field(description='true for properties without HOA fee only. Leave blank for any')] = None,
                hoa_max: Annotated[Union[str, None], Field(description='Maximum HOA fee in USD')] = None,
                days_on_realtor: Annotated[Union[str, None], Field(description='One of the following options: today|7|14|21|30')] = None,
                expand_search_radius: Annotated[Union[str, None], Field(description='One of the following options: 1|5|10|25|50. Expand search by radius in miles')] = None,
                include_nearby_areas_slug_id: Annotated[Union[str, None], Field(description='Comma separated values. Expand search by including nearby areas. Get slug_id from /location/for-sale-nearby-areas')] = None,
                home_size_min: Annotated[Union[str, None], Field(description='One of the following options: 750|1000|1250|1500|1750|2000|2250|2500|2750|3000|3250|3500|3750|5000|7500. Minimum home size in sqft')] = None,
                home_size_max: Annotated[Union[str, None], Field(description='One of the following options: 1000|1250|1500|1750|2000|2250|2500|2750|3000|3250|3500|3750|5000|7500|10000. Maximum home size in sqft')] = None,
                lot_size_min: Annotated[Union[str, None], Field(description='One of the following options: 2000|300|4000|5000|7500|10890|21780|43560|87120|217800|435600|653400|871200. Minimum lot size in sqft')] = None,
                lot_size_max: Annotated[Union[str, None], Field(description='One of the following options: 2000|300|4000|5000|7500|10890|21780|43560|87120|217800|435600|653400|871200. Maximum lot size in sqft')] = None,
                home_age_max: Annotated[Union[str, None], Field(description='Maximum home age')] = None,
                stories: Annotated[Union[str, None], Field(description='One of the following options: single|multi')] = None,
                garage: Annotated[Union[str, None], Field(description='One of the following options: 1+|2+|3+')] = None,
                heating_cooling: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: central_air|central_heat|forced_air')] = None,
                inside_rooms: Annotated[Union[str, None], Field(description='Comma separated values. One or more comma separated from following options: basement|hardwood_floors|fireplace|disability_features|den_or_office|family_room|dining_room')] = None,
                outside_features: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: swimming_pool|spa_or_hot_tub|horse_facilities')] = None,
                lot_views: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: waterfront|cul_de_sac|corner_lot|golf_course_lot_or_frontage|hill_or_mountain_view|ocean_view|lake_view|river_view')] = None,
                community_ammenities: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: community_swimming_pool|community_spa_or_hot_tub|community_golf|community_security_features|community_boat_facilities|tennis_court|community_clubhouse|senior_community')] = None,
                features_in_nyc_only: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: furniture|dishwasher|community_doorman|pets_allowed|laundry_room|elevator|community_outdoor_space')] = None) -> dict: 
    '''Search for-sale properties. **Parameters**: `city, state_code, location, limit, offset, sort:newest price_min, price_max, beds_min, beds_max, baths_min, baths_max, property_type, property_type_nyc_only, new_construction, hide_pending_contingent, has_virtual_tours, has_3d_tours, hide_foreclosure, price_reduced, open_house, keywords, no_hoa_fee, hoa_max, days_on_realtor, expand_search_radius, include_nearby_areas_slug_id, home_size_min, home_size_max, lot_size_min, lot_size_max, home_age_max, stories, garage, heating_cooling, inside_rooms, outside_features, lot_views, community_ammenities, features_in_nyc_only`'''
    url = 'https://us-real-estate.p.rapidapi.com/v2/for-sale'
    headers = {'x-rapidapi-host': 'us-real-estate.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'offset': offset,
        'limit': limit,
        'state_code': state_code,
        'city': city,
        'location': location,
        'sort': sort,
        'price_min': price_min,
        'price_max': price_max,
        'beds_min': beds_min,
        'beds_max': beds_max,
        'baths_min': baths_min,
        'baths_max': baths_max,
        'property_type': property_type,
        'property_type_nyc_only': property_type_nyc_only,
        'new_construction': new_construction,
        'hide_pending_contingent': hide_pending_contingent,
        'has_virtual_tours': has_virtual_tours,
        'has_3d_tours': has_3d_tours,
        'hide_foreclosure': hide_foreclosure,
        'price_reduced': price_reduced,
        'open_house': open_house,
        'keywords': keywords,
        'no_hoa_fee': no_hoa_fee,
        'hoa_max': hoa_max,
        'days_on_realtor': days_on_realtor,
        'expand_search_radius': expand_search_radius,
        'include_nearby_areas_slug_id': include_nearby_areas_slug_id,
        'home_size_min': home_size_min,
        'home_size_max': home_size_max,
        'lot_size_min': lot_size_min,
        'lot_size_max': lot_size_max,
        'home_age_max': home_age_max,
        'stories': stories,
        'garage': garage,
        'heating_cooling': heating_cooling,
        'inside_rooms': inside_rooms,
        'outside_features': outside_features,
        'lot_views': lot_views,
        'community_ammenities': community_ammenities,
        'features_in_nyc_only': features_in_nyc_only,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_for_sale_by_zipcode(zipcode: Annotated[str, Field(description='zipcode')],
                           offset: Annotated[Union[int, float, None], Field(description='Offset results, default 0. Maximum 9800. Default: 0')] = None,
                           limit: Annotated[Union[int, float, None], Field(description='Number of results. Maximum 200 for Paid Plan, default 42 Default: 42')] = None,
                           sort: Annotated[Union[str, None], Field(description='One of the following options: relevant|newest|lowest_price|highest_price|open_house_date|price_reduced_date|largest_sqft|lot_size|sold_date. Default is relevant')] = None,
                           price_min: Annotated[Union[str, None], Field(description='Minimum list price in USD')] = None,
                           price_max: Annotated[Union[str, None], Field(description='Maximum list price in USD')] = None,
                           beds_min: Annotated[Union[str, None], Field(description='Minimum bedrooms')] = None,
                           beds_max: Annotated[Union[str, None], Field(description='Maximum bedrooms')] = None,
                           baths_min: Annotated[Union[str, None], Field(description='Minimum bathrooms')] = None,
                           baths_max: Annotated[Union[str, None], Field(description='Maximum bathrooms')] = None,
                           property_type: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: multi_family|single_family|mobile|land|farm')] = None,
                           property_type_nyc_only: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: condo|coop|condop. For NYC listings only')] = None,
                           new_construction: Annotated[Union[str, None], Field(description='true for New construction only. Leave blank for any')] = None,
                           hide_pending_contingent: Annotated[Union[str, None], Field(description='true for hide pending/contingent. Leave blank for any')] = None,
                           has_virtual_tours: Annotated[Union[str, None], Field(description='true for properties with virtual tour only. Leave blank for any')] = None,
                           has_3d_tours: Annotated[Union[str, None], Field(description='true for properties with 3D tour only. Leave blank for any')] = None,
                           hide_foreclosure: Annotated[Union[str, None], Field(description='true for hide foreclosure. Leave blank for any')] = None,
                           price_reduced: Annotated[Union[str, None], Field(description='true for properties with price reduced only. Leave blank for any')] = None,
                           open_house: Annotated[Union[str, None], Field(description='true for properties with open house only. Leave blank for any')] = None,
                           keywords: Annotated[Union[str, None], Field(description='Comma separated values. Get popular keywords from /keywords-search-suggest response')] = None,
                           no_hoa_fee: Annotated[Union[str, None], Field(description='true for properties without HOA fee only. Leave blank for any')] = None,
                           hoa_max: Annotated[Union[str, None], Field(description='Maximum HOA fee in USD')] = None,
                           days_on_realtor: Annotated[Union[str, None], Field(description='One of the following options: today|7|14|21|30')] = None,
                           expand_search_radius: Annotated[Union[str, None], Field(description='One of the following options: 1|5|10|25|50. Expand search by radius in miles')] = None,
                           include_nearby_areas_slug_id: Annotated[Union[str, None], Field(description='Comma separated values. Expand search by including nearby areas. Get slug_id from /location/for-sale-nearby-areas')] = None,
                           home_size_min: Annotated[Union[str, None], Field(description='One of the following options: 750|1000|1250|1500|1750|2000|2250|2500|2750|3000|3250|3500|3750|5000|7500. Minimum home size in sqft')] = None,
                           home_size_max: Annotated[Union[str, None], Field(description='One of the following options: 1000|1250|1500|1750|2000|2250|2500|2750|3000|3250|3500|3750|5000|7500|10000. Maximum home size in sqft')] = None,
                           lot_size_min: Annotated[Union[str, None], Field(description='One of the following options: 2000|300|4000|5000|7500|10890|21780|43560|87120|217800|435600|653400|871200. Minimum lot size in sqft')] = None,
                           lot_size_max: Annotated[Union[str, None], Field(description='One of the following options: 2000|300|4000|5000|7500|10890|21780|43560|87120|217800|435600|653400|871200. Maximum lot size in sqft')] = None,
                           home_age_max: Annotated[Union[str, None], Field(description='Maximum home age')] = None,
                           stories: Annotated[Union[str, None], Field(description='One of the following options: single|multi')] = None,
                           garage: Annotated[Union[str, None], Field(description='One of the following options: 1+|2+|3+')] = None,
                           heating_cooling: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: central_air|central_heat|forced_air')] = None,
                           inside_rooms: Annotated[Union[str, None], Field(description='Comma separated values. One or more comma separated from following options: basement|hardwood_floors|fireplace|disability_features|den_or_office|family_room|dining_room')] = None,
                           outside_features: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: swimming_pool|spa_or_hot_tub|horse_facilities')] = None,
                           lot_views: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: waterfront|cul_de_sac|corner_lot|golf_course_lot_or_frontage|hill_or_mountain_view|ocean_view|lake_view|river_view')] = None,
                           community_ammenities: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: community_swimming_pool|community_spa_or_hot_tub|community_golf|community_security_features|community_boat_facilities|tennis_court|community_clubhouse|senior_community')] = None,
                           features_in_nyc_only: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: furniture|dishwasher|community_doorman|pets_allowed|laundry_room|elevator|community_outdoor_space')] = None) -> dict: 
    '''Search for-sale properties. **Parameters**: `zipcode, limit, offset, sort:newest price_min, price_max, beds_min, beds_max, baths_min, baths_max, property_type, property_type_nyc_only, new_construction, hide_pending_contingent, has_virtual_tours, has_3d_tours, hide_foreclosure, price_reduced, open_house, keywords, no_hoa_fee, hoa_max, days_on_realtor, expand_search_radius, include_nearby_areas_slug_id, home_size_min, home_size_max, lot_size_min, lot_size_max, home_age_max, stories, garage, heating_cooling, inside_rooms, outside_features, lot_views, community_ammenities, features_in_nyc_only`'''
    url = 'https://us-real-estate.p.rapidapi.com/v2/for-sale-by-zipcode'
    headers = {'x-rapidapi-host': 'us-real-estate.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'zipcode': zipcode,
        'offset': offset,
        'limit': limit,
        'sort': sort,
        'price_min': price_min,
        'price_max': price_max,
        'beds_min': beds_min,
        'beds_max': beds_max,
        'baths_min': baths_min,
        'baths_max': baths_max,
        'property_type': property_type,
        'property_type_nyc_only': property_type_nyc_only,
        'new_construction': new_construction,
        'hide_pending_contingent': hide_pending_contingent,
        'has_virtual_tours': has_virtual_tours,
        'has_3d_tours': has_3d_tours,
        'hide_foreclosure': hide_foreclosure,
        'price_reduced': price_reduced,
        'open_house': open_house,
        'keywords': keywords,
        'no_hoa_fee': no_hoa_fee,
        'hoa_max': hoa_max,
        'days_on_realtor': days_on_realtor,
        'expand_search_radius': expand_search_radius,
        'include_nearby_areas_slug_id': include_nearby_areas_slug_id,
        'home_size_min': home_size_min,
        'home_size_max': home_size_max,
        'lot_size_min': lot_size_min,
        'lot_size_max': lot_size_max,
        'home_age_max': home_age_max,
        'stories': stories,
        'garage': garage,
        'heating_cooling': heating_cooling,
        'inside_rooms': inside_rooms,
        'outside_features': outside_features,
        'lot_views': lot_views,
        'community_ammenities': community_ammenities,
        'features_in_nyc_only': features_in_nyc_only,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_for_sale_result_count(state_code: Annotated[str, Field(description='State Code. Get from /location/suggest response')],
                             city: Annotated[str, Field(description='City name. Get data from /location/suggest response')],
                             location: Annotated[Union[str, None], Field(description='Additional Location detail, could be neighborhood or postal_code or leave it blank. Get from /location/suggest response. Default is blank')] = None,
                             price_min: Annotated[Union[str, None], Field(description='Minimum list price in USD')] = None,
                             price_max: Annotated[Union[str, None], Field(description='Maximum list price in USD')] = None,
                             beds_min: Annotated[Union[str, None], Field(description='Minimum bedrooms')] = None,
                             beds_max: Annotated[Union[str, None], Field(description='Maximum bedrooms')] = None,
                             baths_min: Annotated[Union[str, None], Field(description='Minimum bathrooms')] = None,
                             baths_max: Annotated[Union[str, None], Field(description='Maximum bathrooms')] = None,
                             property_type_nyc_only: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: condo|coop|condop. For NYC listings only')] = None,
                             new_construction: Annotated[Union[str, None], Field(description='true for New construction only. Leave blank for any')] = None,
                             hide_pending_contingent: Annotated[Union[str, None], Field(description='true for hide pending/contingent. Leave blank for any')] = None,
                             has_virtual_tours: Annotated[Union[str, None], Field(description='true for properties with virtual tour only. Leave blank for any')] = None,
                             has_3d_tours: Annotated[Union[str, None], Field(description='true for properties with 3D tour only. Leave blank for any')] = None,
                             hide_foreclosure: Annotated[Union[str, None], Field(description='true for hide foreclosure. Leave blank for any')] = None,
                             price_reduced: Annotated[Union[str, None], Field(description='true for properties with price reduced only. Leave blank for any')] = None,
                             open_house: Annotated[Union[str, None], Field(description='true for properties with open house only. Leave blank for any')] = None,
                             keywords: Annotated[Union[str, None], Field(description='Comma separated values. Get popular keywords from /keywords-search-suggest response')] = None,
                             no_hoa_fee: Annotated[Union[str, None], Field(description='true for properties without HOA fee only. Leave blank for any')] = None,
                             hoa_max: Annotated[Union[str, None], Field(description='Maximum HOA fee in USD')] = None,
                             days_on_realtor: Annotated[Union[str, None], Field(description='One of the following options: today|7|14|21|30')] = None,
                             expand_search_radius: Annotated[Union[str, None], Field(description='One of the following options: 1|5|10|25|50. Expand search by radius in miles')] = None,
                             include_nearby_areas_slug_id: Annotated[Union[str, None], Field(description='Comma separated values. Expand search by including nearby areas. Get slug_id from /location/for-sale-nearby-areas')] = None,
                             home_size_min: Annotated[Union[str, None], Field(description='One of the following options: 750|1000|1250|1500|1750|2000|2250|2500|2750|3000|3250|3500|3750|5000|7500. Minimum home size in sqft')] = None,
                             home_size_max: Annotated[Union[str, None], Field(description='One of the following options: 1000|1250|1500|1750|2000|2250|2500|2750|3000|3250|3500|3750|5000|7500|10000. Maximum home size in sqft')] = None,
                             lot_size_min: Annotated[Union[str, None], Field(description='One of the following options: 2000|300|4000|5000|7500|10890|21780|43560|87120|217800|435600|653400|871200. Minimum lot size in sqft')] = None,
                             lot_size_max: Annotated[Union[str, None], Field(description='One of the following options: 2000|300|4000|5000|7500|10890|21780|43560|87120|217800|435600|653400|871200. Maximum lot size in sqft')] = None,
                             home_age_max: Annotated[Union[str, None], Field(description='Maximum home age')] = None,
                             stories: Annotated[Union[str, None], Field(description='One of the following options: single|multi')] = None,
                             garage: Annotated[Union[str, None], Field(description='One of the following options: 1+|2+|3+')] = None,
                             heating_cooling: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: central_air|central_heat|forced_air')] = None,
                             inside_rooms: Annotated[Union[str, None], Field(description='Comma separated values. One or more comma separated from following options: basement|hardwood_floors|fireplace|disability_features|den_or_office|family_room|dining_room')] = None,
                             outside_features: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: swimming_pool|spa_or_hot_tub|horse_facilities')] = None,
                             lot_views: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: waterfront|cul_de_sac|corner_lot|golf_course_lot_or_frontage|hill_or_mountain_view|ocean_view|lake_view|river_view')] = None,
                             community_ammenities: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: community_swimming_pool|community_spa_or_hot_tub|community_golf|community_security_features|community_boat_facilities|tennis_court|community_clubhouse|senior_community')] = None,
                             features_in_nyc_only: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: furniture|dishwasher|community_doorman|pets_allowed|laundry_room|elevator|community_outdoor_space')] = None) -> dict: 
    '''Get for-sale search result count. **Parameters**: `city, state_code, location, price_min, price_max, beds_min, beds_max, baths_min, baths_max, property_type, property_type_nyc_only, new_construction, hide_pending_contingent, has_virtual_tours, has_3d_tours, hide_foreclosure, price_reduced, open_house, keywords, no_hoa_fee, hoa_max, days_on_realtor, expand_search_radius, include_nearby_areas_slug_id, home_size_min, home_size_max, lot_size_min, lot_size_max, home_age_max, stories, garage, heating_cooling, inside_rooms, outside_features, lot_views, community_ammenities, features_in_nyc_only`'''
    url = 'https://us-real-estate.p.rapidapi.com/v2/for-sale-result-count'
    headers = {'x-rapidapi-host': 'us-real-estate.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state_code': state_code,
        'city': city,
        'location': location,
        'price_min': price_min,
        'price_max': price_max,
        'beds_min': beds_min,
        'beds_max': beds_max,
        'baths_min': baths_min,
        'baths_max': baths_max,
        'property_type_nyc_only': property_type_nyc_only,
        'new_construction': new_construction,
        'hide_pending_contingent': hide_pending_contingent,
        'has_virtual_tours': has_virtual_tours,
        'has_3d_tours': has_3d_tours,
        'hide_foreclosure': hide_foreclosure,
        'price_reduced': price_reduced,
        'open_house': open_house,
        'keywords': keywords,
        'no_hoa_fee': no_hoa_fee,
        'hoa_max': hoa_max,
        'days_on_realtor': days_on_realtor,
        'expand_search_radius': expand_search_radius,
        'include_nearby_areas_slug_id': include_nearby_areas_slug_id,
        'home_size_min': home_size_min,
        'home_size_max': home_size_max,
        'lot_size_min': lot_size_min,
        'lot_size_max': lot_size_max,
        'home_age_max': home_age_max,
        'stories': stories,
        'garage': garage,
        'heating_cooling': heating_cooling,
        'inside_rooms': inside_rooms,
        'outside_features': outside_features,
        'lot_views': lot_views,
        'community_ammenities': community_ammenities,
        'features_in_nyc_only': features_in_nyc_only,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def for_sale(offset: Annotated[Union[int, float], Field(description='Offset results, default 0. Maximum 9800. Default: 0')],
             limit: Annotated[Union[int, float], Field(description='Number of results. Maximum 200 for Paid Plan, default 42 Default: 42')],
             state_code: Annotated[str, Field(description='State Code. Get from /location/suggest response')],
             city: Annotated[str, Field(description='City name. Get data from /location/suggest response')],
             location: Annotated[Union[str, None], Field(description='Additional Location detail, could be neighborhood or postal_code or leave it blank. Get from /location/suggest response. Default is blank')] = None,
             sort: Annotated[Union[str, None], Field(description='One of the following options: relevant|newest|lowest_price|highest_price|open_house_date|price_reduced_date|largest_sqft|lot_size|sold_date. Default is relevant')] = None,
             price_min: Annotated[Union[str, None], Field(description='Minimum list price in USD')] = None,
             price_max: Annotated[Union[str, None], Field(description='Maximum list price in USD')] = None,
             beds_min: Annotated[Union[str, None], Field(description='Minimum bedrooms')] = None,
             beds_max: Annotated[Union[str, None], Field(description='Maximum bedrooms')] = None,
             baths_min: Annotated[Union[str, None], Field(description='Minimum bathrooms')] = None,
             baths_max: Annotated[Union[str, None], Field(description='Maximum bathrooms')] = None,
             property_type: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: multi_family|single_family|mobile|land|farm')] = None,
             property_type_nyc_only: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: condo|coop|condop. For NYC listings only')] = None,
             new_construction: Annotated[Union[str, None], Field(description='true for New construction only. Leave blank for any')] = None,
             hide_pending_contingent: Annotated[Union[str, None], Field(description='true for hide pending/contingent. Leave blank for any')] = None,
             has_virtual_tours: Annotated[Union[str, None], Field(description='true for properties with virtual tour only. Leave blank for any')] = None,
             has_3d_tours: Annotated[Union[str, None], Field(description='true for properties with 3D tour only. Leave blank for any')] = None,
             hide_foreclosure: Annotated[Union[str, None], Field(description='true for hide foreclosure. Leave blank for any')] = None,
             price_reduced: Annotated[Union[str, None], Field(description='true for properties with price reduced only. Leave blank for any')] = None,
             open_house: Annotated[Union[str, None], Field(description='true for properties with open house only. Leave blank for any')] = None,
             keywords: Annotated[Union[str, None], Field(description='Comma separated values. Get popular keywords from /keywords-search-suggest response')] = None,
             no_hoa_fee: Annotated[Union[str, None], Field(description='true for properties without HOA fee only. Leave blank for any')] = None,
             hoa_max: Annotated[Union[str, None], Field(description='Maximum HOA fee in USD')] = None,
             days_on_realtor: Annotated[Union[str, None], Field(description='One of the following options: today|7|14|21|30')] = None,
             expand_search_radius: Annotated[Union[str, None], Field(description='One of the following options: 1|5|10|25|50. Expand search by radius in miles')] = None,
             include_nearby_areas_slug_id: Annotated[Union[str, None], Field(description='Comma separated values. Expand search by including nearby areas. Get slug_id from /location/for-sale-nearby-areas')] = None,
             home_size_min: Annotated[Union[str, None], Field(description='One of the following options: 750|1000|1250|1500|1750|2000|2250|2500|2750|3000|3250|3500|3750|5000|7500. Minimum home size in sqft')] = None,
             home_size_max: Annotated[Union[str, None], Field(description='One of the following options: 1000|1250|1500|1750|2000|2250|2500|2750|3000|3250|3500|3750|5000|7500|10000. Maximum home size in sqft')] = None,
             lot_size_min: Annotated[Union[str, None], Field(description='One of the following options: 2000|300|4000|5000|7500|10890|21780|43560|87120|217800|435600|653400|871200. Minimum lot size in sqft')] = None,
             lot_size_max: Annotated[Union[str, None], Field(description='One of the following options: 2000|300|4000|5000|7500|10890|21780|43560|87120|217800|435600|653400|871200. Maximum lot size in sqft')] = None,
             home_age_max: Annotated[Union[str, None], Field(description='Maximum home age')] = None,
             stories: Annotated[Union[str, None], Field(description='One of the following options: single|multi')] = None,
             garage: Annotated[Union[str, None], Field(description='One of the following options: 1+|2+|3+')] = None,
             heating_cooling: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: central_air|central_heat|forced_air')] = None,
             inside_rooms: Annotated[Union[str, None], Field(description='Comma separated values. One or more comma separated from following options: basement|hardwood_floors|fireplace|disability_features|den_or_office|family_room|dining_room')] = None,
             outside_features: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: swimming_pool|spa_or_hot_tub|horse_facilities')] = None,
             lot_views: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: waterfront|cul_de_sac|corner_lot|golf_course_lot_or_frontage|hill_or_mountain_view|ocean_view|lake_view|river_view')] = None,
             community_ammenities: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: community_swimming_pool|community_spa_or_hot_tub|community_golf|community_security_features|community_boat_facilities|tennis_court|community_clubhouse|senior_community')] = None,
             features_in_nyc_only: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: furniture|dishwasher|community_doorman|pets_allowed|laundry_room|elevator|community_outdoor_space')] = None) -> dict: 
    '''Search for-sale properties. **Parameters**: `city, state_code, location, limit, offset, sort:newest price_min, price_max, beds_min, beds_max, baths_min, baths_max, property_type, property_type_nyc_only, new_construction, hide_pending_contingent, has_virtual_tours, has_3d_tours, hide_foreclosure, price_reduced, open_house, keywords, no_hoa_fee, hoa_max, days_on_realtor, expand_search_radius, include_nearby_areas_slug_id, home_size_min, home_size_max, lot_size_min, lot_size_max, home_age_max, stories, garage, heating_cooling, inside_rooms, outside_features, lot_views, community_ammenities, features_in_nyc_only`'''
    url = 'https://us-real-estate.p.rapidapi.com/for-sale'
    headers = {'x-rapidapi-host': 'us-real-estate.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'offset': offset,
        'limit': limit,
        'state_code': state_code,
        'city': city,
        'location': location,
        'sort': sort,
        'price_min': price_min,
        'price_max': price_max,
        'beds_min': beds_min,
        'beds_max': beds_max,
        'baths_min': baths_min,
        'baths_max': baths_max,
        'property_type': property_type,
        'property_type_nyc_only': property_type_nyc_only,
        'new_construction': new_construction,
        'hide_pending_contingent': hide_pending_contingent,
        'has_virtual_tours': has_virtual_tours,
        'has_3d_tours': has_3d_tours,
        'hide_foreclosure': hide_foreclosure,
        'price_reduced': price_reduced,
        'open_house': open_house,
        'keywords': keywords,
        'no_hoa_fee': no_hoa_fee,
        'hoa_max': hoa_max,
        'days_on_realtor': days_on_realtor,
        'expand_search_radius': expand_search_radius,
        'include_nearby_areas_slug_id': include_nearby_areas_slug_id,
        'home_size_min': home_size_min,
        'home_size_max': home_size_max,
        'lot_size_min': lot_size_min,
        'lot_size_max': lot_size_max,
        'home_age_max': home_age_max,
        'stories': stories,
        'garage': garage,
        'heating_cooling': heating_cooling,
        'inside_rooms': inside_rooms,
        'outside_features': outside_features,
        'lot_views': lot_views,
        'community_ammenities': community_ammenities,
        'features_in_nyc_only': features_in_nyc_only,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def for_sale_similiar_homes(property_id: Annotated[Union[int, float], Field(description='Default: 8624316600')]) -> dict: 
    '''Get similiar homes by `property_id`'''
    url = 'https://us-real-estate.p.rapidapi.com/for-sale/similiar-homes'
    headers = {'x-rapidapi-host': 'us-real-estate.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'property_id': property_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def for_sale_other_homes_in_building(property_id: Annotated[Union[int, float], Field(description='Default: 9626941405')]) -> dict: 
    '''Get other homes in same building by `property_id`'''
    url = 'https://us-real-estate.p.rapidapi.com/for-sale/other-homes-in-building'
    headers = {'x-rapidapi-host': 'us-real-estate.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'property_id': property_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def for_sale_home_estimate_value(property_id: Annotated[Union[int, float], Field(description='Default: 2061530895')]) -> dict: 
    '''Get home estimate and historical values'''
    url = 'https://us-real-estate.p.rapidapi.com/for-sale/home-estimate-value'
    headers = {'x-rapidapi-host': 'us-real-estate.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'property_id': property_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_sold_homes_by_zipcode(zipcode: Annotated[Union[int, float], Field(description='zipcode Default: 37932')],
                             offset: Annotated[Union[int, float, None], Field(description='Offset results, default 0 Default: 0')] = None,
                             sort: Annotated[Union[str, None], Field(description='One of the following options: sold_date | lowest_price | highest_price | lot_size | number_of_beds. Default is sold_date')] = None,
                             max_sold_days: Annotated[Union[int, float, None], Field(description='Maximum sold days form now')] = None,
                             price_max: Annotated[Union[int, float, None], Field(description='Maximum list price in USD Default: 0')] = None,
                             beds_min: Annotated[Union[int, float, None], Field(description='Minimum bedrooms Default: 0')] = None,
                             beds_max: Annotated[Union[int, float, None], Field(description='Maximum bedrooms Default: 0')] = None,
                             baths_min: Annotated[Union[int, float, None], Field(description='Minimum bathrooms Default: 0')] = None,
                             baths_max: Annotated[Union[int, float, None], Field(description='Maximum bathrooms Default: 0')] = None,
                             property_type: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: multi_family|single_family|mobile|land|farm')] = None,
                             expand_search_radius: Annotated[Union[int, float, None], Field(description='One of the following options: 1|5|10|25|50 Default: 0')] = None,
                             include_nearby_areas_slug_id: Annotated[Union[str, None], Field(description='Comma separated values. Expand search by including nearby areas. Get slug_id from /location/for-rent-nearby-areas')] = None,
                             home_size_min: Annotated[Union[int, float, None], Field(description='One of the following options: 500|750|1000|1250|1500|1750|2000|2250|2500|2750|3000 Default: 0')] = None,
                             home_size_max: Annotated[Union[int, float, None], Field(description='One of the following options: 500|750|1000|1250|1500|1750|2000|2250|2500|2750|3000 Default: 0')] = None,
                             lot_size_min: Annotated[Union[str, None], Field(description='One of the following options: 2000|300|4000|5000|7500|10890|21780|43560|87120|217800|435600|653400|871200. Minimum lot size in sqft')] = None,
                             lot_size_max: Annotated[Union[str, None], Field(description='One of the following options: 2000|300|4000|5000|7500|10890|21780|43560|87120|217800|435600|653400|871200. Maximum lot size in sqft')] = None,
                             home_age_max: Annotated[Union[str, None], Field(description='Maximum home age')] = None) -> dict: 
    '''Search for-sale properties. **Parameters**: `zipcode, limit, offset, sort, max_sold_days, price_min, price_max, beds_min, beds_max, baths_min, baths_max, property_type, expand_search_radius, include_nearby_areas_slug_id, home_size_min, home_size_max, lot_size_min, lot_size_max, home_age_max`'''
    url = 'https://us-real-estate.p.rapidapi.com/v2/sold-homes-by-zipcode'
    headers = {'x-rapidapi-host': 'us-real-estate.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'zipcode': zipcode,
        'offset': offset,
        'sort': sort,
        'max_sold_days': max_sold_days,
        'price_max': price_max,
        'beds_min': beds_min,
        'beds_max': beds_max,
        'baths_min': baths_min,
        'baths_max': baths_max,
        'property_type': property_type,
        'expand_search_radius': expand_search_radius,
        'include_nearby_areas_slug_id': include_nearby_areas_slug_id,
        'home_size_min': home_size_min,
        'home_size_max': home_size_max,
        'lot_size_min': lot_size_min,
        'lot_size_max': lot_size_max,
        'home_age_max': home_age_max,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def sold_homes(state_code: Annotated[str, Field(description='State Code. Get from /location/suggest response')],
               city: Annotated[str, Field(description='City name. Get data from /location/suggest response')],
               location: Annotated[Union[int, float, None], Field(description='Additional Location detail, could be neighborhood or postal_code or leave it blank. Get from /location/suggest response. Default is blank Default: 0')] = None,
               limit: Annotated[Union[int, float, None], Field(description='Number of results. Maximum 200 for Paid Plan, default 42 Default: 10')] = None,
               offset: Annotated[Union[int, float, None], Field(description='Offset results, default 0 Default: 0')] = None,
               sort: Annotated[Union[str, None], Field(description='One of the following options: sold_date | lowest_price | highest_price | lot_size | number_of_beds. Default is sold_date')] = None,
               max_sold_days: Annotated[Union[int, float, None], Field(description='Maximum sold days form now')] = None,
               price_min: Annotated[Union[int, float, None], Field(description='Minimum list price in USD Default: 0')] = None,
               price_max: Annotated[Union[int, float, None], Field(description='Maximum list price in USD Default: 0')] = None,
               beds_min: Annotated[Union[int, float, None], Field(description='Minimum bedrooms Default: 0')] = None,
               beds_max: Annotated[Union[int, float, None], Field(description='Maximum bedrooms Default: 0')] = None,
               baths_min: Annotated[Union[int, float, None], Field(description='Minimum bathrooms Default: 0')] = None,
               baths_max: Annotated[Union[int, float, None], Field(description='Maximum bathrooms Default: 0')] = None,
               property_type: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: multi_family|single_family|mobile|land|farm')] = None,
               expand_search_radius: Annotated[Union[int, float, None], Field(description='One of the following options: 1|5|10|25|50 Default: 0')] = None,
               include_nearby_areas_slug_id: Annotated[Union[str, None], Field(description='Comma separated values. Expand search by including nearby areas. Get slug_id from /location/for-rent-nearby-areas')] = None,
               home_size_min: Annotated[Union[int, float, None], Field(description='One of the following options: 500|750|1000|1250|1500|1750|2000|2250|2500|2750|3000 Default: 0')] = None,
               home_size_max: Annotated[Union[int, float, None], Field(description='One of the following options: 500|750|1000|1250|1500|1750|2000|2250|2500|2750|3000 Default: 0')] = None,
               lot_size_min: Annotated[Union[str, None], Field(description='One of the following options: 2000|300|4000|5000|7500|10890|21780|43560|87120|217800|435600|653400|871200. Minimum lot size in sqft')] = None,
               lot_size_max: Annotated[Union[str, None], Field(description='One of the following options: 2000|300|4000|5000|7500|10890|21780|43560|87120|217800|435600|653400|871200. Maximum lot size in sqft')] = None,
               home_age_max: Annotated[Union[str, None], Field(description='Maximum home age')] = None) -> dict: 
    '''Search for-sale properties. **Parameters**: `city, state_code, location, limit, offset, sort, max_sold_days, price_min, price_max, beds_min, beds_max, baths_min, baths_max, property_type, expand_search_radius, include_nearby_areas_slug_id, home_size_min, home_size_max, lot_size_min, lot_size_max, home_age_max`'''
    url = 'https://us-real-estate.p.rapidapi.com/sold-homes'
    headers = {'x-rapidapi-host': 'us-real-estate.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state_code': state_code,
        'city': city,
        'location': location,
        'limit': limit,
        'offset': offset,
        'sort': sort,
        'max_sold_days': max_sold_days,
        'price_min': price_min,
        'price_max': price_max,
        'beds_min': beds_min,
        'beds_max': beds_max,
        'baths_min': baths_min,
        'baths_max': baths_max,
        'property_type': property_type,
        'expand_search_radius': expand_search_radius,
        'include_nearby_areas_slug_id': include_nearby_areas_slug_id,
        'home_size_min': home_size_min,
        'home_size_max': home_size_max,
        'lot_size_min': lot_size_min,
        'lot_size_max': lot_size_max,
        'home_age_max': home_age_max,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_for_rent(city: Annotated[str, Field(description='City name. Get data from /location/suggest response')],
                state_code: Annotated[str, Field(description='State Code. Get from /location/suggest response')],
                location: Annotated[Union[int, float, None], Field(description='Additional Location detail, could be neighborhood or postal_code or leave it blank. Get from /location/suggest response. Default is blank Default: 48278')] = None,
                limit: Annotated[Union[int, float, None], Field(description='Number of results. Maximum 200 for Paid Plan, default 42 Default: 10')] = None,
                offset: Annotated[Union[int, float, None], Field(description='Offset results, default 0. Maximum 9800. Default: 0')] = None,
                sort: Annotated[Union[str, None], Field(description='One of the following options: frehsnest|recently_added_update|lowest_price|highest_price. Default is frehsnest')] = None,
                price_min: Annotated[Union[int, float, None], Field(description='Minimum list price in USD Default: 1000')] = None,
                price_max: Annotated[Union[int, float, None], Field(description='Maximum list price in USD Default: 3000')] = None,
                beds_min: Annotated[Union[int, float, None], Field(description='Minimum bedrooms Default: 1')] = None,
                beds_max: Annotated[Union[int, float, None], Field(description='Maximum bedrooms Default: 5')] = None,
                baths_min: Annotated[Union[int, float, None], Field(description='Minimum bathrooms Default: 1')] = None,
                baths_max: Annotated[Union[int, float, None], Field(description='Maximum bathrooms Default: 5')] = None,
                property_type: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: townhome,coop,single_family,apartment,condo,condop')] = None,
                expand_search_radius: Annotated[Union[int, float, None], Field(description='One of the following options: 1|5|10|25|50 Default: 25')] = None,
                include_nearby_areas_slug_id: Annotated[Union[str, None], Field(description='Comma separated values. Expand search by including nearby areas. Get slug_id from /location/for-rent-nearby-areas')] = None,
                home_size_min: Annotated[Union[int, float, None], Field(description='One of the following options: 500|750|1000|1250|1500|1750|2000|2250|2500|2750|3000 Default: 500')] = None,
                home_size_max: Annotated[Union[int, float, None], Field(description='One of the following options: 500|750|1000|1250|1500|1750|2000|2250|2500|2750|3000 Default: 3000')] = None,
                in_unit_features: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: central_air|dishwasher|washer_dryer|furnished')] = None,
                community_ammenities: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: garage_1_or_more|swimming_pool|community_doorman|community_outdoor_space|community_elevator|laundry_room|community_gym')] = None,
                cats_ok: Annotated[Union[bool, None], Field(description='true for Cats allowed only')] = None,
                dogs_ok: Annotated[Union[bool, None], Field(description='true for Dogs allowed only')] = None) -> dict: 
    '''Get for-rent properties. **Parameters**: `city, state_code, location, limit, offset, sort, price_min, price_max, beds_min, beds_max, baths_min, baths_max, property_type, expand_search_radius, include_nearby_areas_slug_id, home_size_min, home_size_max, in_unit_features, community_ammenities, cats_ok, dogs_ok`'''
    url = 'https://us-real-estate.p.rapidapi.com/v2/for-rent'
    headers = {'x-rapidapi-host': 'us-real-estate.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'city': city,
        'state_code': state_code,
        'location': location,
        'limit': limit,
        'offset': offset,
        'sort': sort,
        'price_min': price_min,
        'price_max': price_max,
        'beds_min': beds_min,
        'beds_max': beds_max,
        'baths_min': baths_min,
        'baths_max': baths_max,
        'property_type': property_type,
        'expand_search_radius': expand_search_radius,
        'include_nearby_areas_slug_id': include_nearby_areas_slug_id,
        'home_size_min': home_size_min,
        'home_size_max': home_size_max,
        'in_unit_features': in_unit_features,
        'community_ammenities': community_ammenities,
        'cats_ok': cats_ok,
        'dogs_ok': dogs_ok,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_for_rent_by_zipcode(zipcode: Annotated[Union[int, float], Field(description='zipcode Default: 48278')],
                           limit: Annotated[Union[int, float, None], Field(description='Number of results. Maximum 200 for Paid Plan, default 42 Default: 10')] = None,
                           offset: Annotated[Union[int, float, None], Field(description='Offset results, default 0. Maximum 9800. Default: 0')] = None,
                           sort: Annotated[Union[str, None], Field(description='One of the following options: frehsnest|recently_added_update|lowest_price|highest_price. Default is frehsnest')] = None,
                           price_min: Annotated[Union[int, float, None], Field(description='Minimum list price in USD Default: 0')] = None,
                           beds_min: Annotated[Union[int, float, None], Field(description='Minimum bedrooms Default: 0')] = None,
                           beds_max: Annotated[Union[int, float, None], Field(description='Maximum bedrooms Default: 0')] = None,
                           baths_min: Annotated[Union[int, float, None], Field(description='Minimum bathrooms Default: 0')] = None,
                           baths_max: Annotated[Union[int, float, None], Field(description='Maximum bathrooms Default: 0')] = None,
                           property_type: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: townhome,coop,single_family,apartment,condo,condop')] = None,
                           include_nearby_areas_slug_id: Annotated[Union[str, None], Field(description='Comma separated values. Expand search by including nearby areas. Get slug_id from /location/for-rent-nearby-areas')] = None,
                           home_size_min: Annotated[Union[int, float, None], Field(description='One of the following options: 500|750|1000|1250|1500|1750|2000|2250|2500|2750|3000 Default: 0')] = None,
                           home_size_max: Annotated[Union[int, float, None], Field(description='One of the following options: 500|750|1000|1250|1500|1750|2000|2250|2500|2750|3000 Default: 0')] = None,
                           in_unit_features: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: central_air|dishwasher|washer_dryer|furnished')] = None,
                           community_ammenities: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: garage_1_or_more|swimming_pool|community_doorman|community_outdoor_space|community_elevator|laundry_room|community_gym')] = None,
                           cats_ok: Annotated[Union[bool, None], Field(description='true for Cats allowed only')] = None,
                           dogs_ok: Annotated[Union[bool, None], Field(description='true for Dogs allowed only')] = None) -> dict: 
    '''Get for-rent properties. **Parameters**: `zipcode, limit, offset, sort, price_min, price_max, beds_min, beds_max, baths_min, baths_max, property_type, expand_search_radius, include_nearby_areas_slug_id, home_size_min, home_size_max, in_unit_features, community_ammenities, cats_ok, dogs_ok`'''
    url = 'https://us-real-estate.p.rapidapi.com/v2/for-rent-by-zipcode'
    headers = {'x-rapidapi-host': 'us-real-estate.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'zipcode': zipcode,
        'limit': limit,
        'offset': offset,
        'sort': sort,
        'price_min': price_min,
        'beds_min': beds_min,
        'beds_max': beds_max,
        'baths_min': baths_min,
        'baths_max': baths_max,
        'property_type': property_type,
        'include_nearby_areas_slug_id': include_nearby_areas_slug_id,
        'home_size_min': home_size_min,
        'home_size_max': home_size_max,
        'in_unit_features': in_unit_features,
        'community_ammenities': community_ammenities,
        'cats_ok': cats_ok,
        'dogs_ok': dogs_ok,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_for_rent_result_count(city: Annotated[str, Field(description='City name. Get data from /location/suggest response')],
                             state_code: Annotated[str, Field(description='State Code. Get from /location/suggest response')],
                             location: Annotated[Union[int, float, None], Field(description='Additional Location detail, could be neighborhood or postal_code or leave it blank. Get from /location/suggest response. Default is blank Default: 48278')] = None,
                             price_min: Annotated[Union[int, float, None], Field(description='Minimum list price in USD Default: 1000')] = None,
                             price_max: Annotated[Union[int, float, None], Field(description='Maximum list price in USD Default: 3000')] = None,
                             beds_min: Annotated[Union[int, float, None], Field(description='Minimum bedrooms Default: 1')] = None,
                             beds_max: Annotated[Union[int, float, None], Field(description='Maximum bedrooms Default: 5')] = None,
                             baths_min: Annotated[Union[int, float, None], Field(description='Minimum bathrooms Default: 1')] = None,
                             baths_max: Annotated[Union[int, float, None], Field(description='Maximum bathrooms Default: 5')] = None,
                             property_type: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: townhome,coop,single_family,apartment,condo,condop')] = None,
                             expand_search_radius: Annotated[Union[int, float, None], Field(description='One of the following options: 1|5|10|25|50 Default: 25')] = None,
                             include_nearby_areas_slug_id: Annotated[Union[str, None], Field(description='Comma separated values. Expand search by including nearby areas. Get slug_id from /location/for-rent-nearby-areas')] = None,
                             home_size_min: Annotated[Union[int, float, None], Field(description='One of the following options: 500|750|1000|1250|1500|1750|2000|2250|2500|2750|3000 Default: 500')] = None,
                             home_size_max: Annotated[Union[int, float, None], Field(description='One of the following options: 500|750|1000|1250|1500|1750|2000|2250|2500|2750|3000 Default: 3000')] = None,
                             in_unit_features: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: central_air|dishwasher|washer_dryer|furnished')] = None,
                             community_ammenities: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: garage_1_or_more|swimming_pool|community_doorman|community_outdoor_space|community_elevator|laundry_room|community_gym')] = None,
                             cats_ok: Annotated[Union[bool, None], Field(description='true for Cats allowed only')] = None,
                             dogs_ok: Annotated[Union[bool, None], Field(description='true for Dogs allowed only')] = None) -> dict: 
    '''Get result count for-rent properties. **Parameters**: `city, state_code, location, price_min, price_max, beds_min, beds_max, baths_min, baths_max, property_type, expand_search_radius, include_nearby_areas_slug_id, home_size_min, home_size_max, in_unit_features, community_ammenities, cats_ok, dogs_ok`'''
    url = 'https://us-real-estate.p.rapidapi.com/v2/for-rent-result-count'
    headers = {'x-rapidapi-host': 'us-real-estate.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'city': city,
        'state_code': state_code,
        'location': location,
        'price_min': price_min,
        'price_max': price_max,
        'beds_min': beds_min,
        'beds_max': beds_max,
        'baths_min': baths_min,
        'baths_max': baths_max,
        'property_type': property_type,
        'expand_search_radius': expand_search_radius,
        'include_nearby_areas_slug_id': include_nearby_areas_slug_id,
        'home_size_min': home_size_min,
        'home_size_max': home_size_max,
        'in_unit_features': in_unit_features,
        'community_ammenities': community_ammenities,
        'cats_ok': cats_ok,
        'dogs_ok': dogs_ok,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def for_rent_similiar_homes(property_id: Annotated[Union[int, float], Field(description='Default: 1207989147')]) -> dict: 
    '''Get similiar for-rent homes by `property_id`'''
    url = 'https://us-real-estate.p.rapidapi.com/v2/for-rent/similiar-homes'
    headers = {'x-rapidapi-host': 'us-real-estate.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'property_id': property_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def for_rent(city: Annotated[str, Field(description='City name. Get data from /location/suggest response')],
             state_code: Annotated[str, Field(description='State Code. Get from /location/suggest response')],
             location: Annotated[Union[int, float, None], Field(description='Additional Location detail, could be neighborhood or postal_code or leave it blank. Get from /location/suggest response. Default is blank Default: 48278')] = None,
             limit: Annotated[Union[int, float, None], Field(description='Number of results. Maximum 200 for Paid Plan, default 42 Default: 10')] = None,
             offset: Annotated[Union[int, float, None], Field(description='Offset results, default 0. Maximum 9800. Default: 0')] = None,
             sort: Annotated[Union[str, None], Field(description='One of the following options: frehsnest|recently_added_update|lowest_price|highest_price. Default is frehsnest')] = None,
             price_min: Annotated[Union[int, float, None], Field(description='Minimum list price in USD Default: 1000')] = None,
             price_max: Annotated[Union[int, float, None], Field(description='Maximum list price in USD Default: 3000')] = None,
             beds_min: Annotated[Union[int, float, None], Field(description='Minimum bedrooms Default: 1')] = None,
             beds_max: Annotated[Union[int, float, None], Field(description='Maximum bedrooms Default: 5')] = None,
             baths_min: Annotated[Union[int, float, None], Field(description='Minimum bathrooms Default: 1')] = None,
             baths_max: Annotated[Union[int, float, None], Field(description='Maximum bathrooms Default: 5')] = None,
             property_type: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: townhome,coop,single_family,apartment,condo,condop')] = None,
             expand_search_radius: Annotated[Union[int, float, None], Field(description='One of the following options: 1|5|10|25|50 Default: 25')] = None,
             include_nearby_areas_slug_id: Annotated[Union[str, None], Field(description='Comma separated values. Expand search by including nearby areas. Get slug_id from /location/for-rent-nearby-areas')] = None,
             home_size_min: Annotated[Union[int, float, None], Field(description='One of the following options: 500|750|1000|1250|1500|1750|2000|2250|2500|2750|3000 Default: 500')] = None,
             home_size_max: Annotated[Union[int, float, None], Field(description='One of the following options: 500|750|1000|1250|1500|1750|2000|2250|2500|2750|3000 Default: 3000')] = None,
             in_unit_features: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: central_air|dishwasher|washer_dryer|furnished')] = None,
             community_ammenities: Annotated[Union[str, None], Field(description='Comma separated values. One or more from following options: garage_1_or_more|swimming_pool|community_doorman|community_outdoor_space|community_elevator|laundry_room|community_gym')] = None,
             cats_ok: Annotated[Union[bool, None], Field(description='true for Cats allowed only')] = None,
             dogs_ok: Annotated[Union[bool, None], Field(description='true for Dogs allowed only')] = None) -> dict: 
    '''Get for-rent properties. **Parameters**: `city, state_code, location, limit, offset, sort, price_min, price_max, beds_min, beds_max, baths_min, baths_max, property_type, expand_search_radius, include_nearby_areas_slug_id, home_size_min, home_size_max, in_unit_features, community_ammenities, cats_ok, dogs_ok`'''
    url = 'https://us-real-estate.p.rapidapi.com/for-rent'
    headers = {'x-rapidapi-host': 'us-real-estate.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'city': city,
        'state_code': state_code,
        'location': location,
        'limit': limit,
        'offset': offset,
        'sort': sort,
        'price_min': price_min,
        'price_max': price_max,
        'beds_min': beds_min,
        'beds_max': beds_max,
        'baths_min': baths_min,
        'baths_max': baths_max,
        'property_type': property_type,
        'expand_search_radius': expand_search_radius,
        'include_nearby_areas_slug_id': include_nearby_areas_slug_id,
        'home_size_min': home_size_min,
        'home_size_max': home_size_max,
        'in_unit_features': in_unit_features,
        'community_ammenities': community_ammenities,
        'cats_ok': cats_ok,
        'dogs_ok': dogs_ok,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def finance_mortgage_calculate(show_amortization: Annotated[bool, Field(description='')],
                               hoa_fees: Annotated[Union[int, float], Field(description='Default: 0')],
                               percent_tax_rate: Annotated[Union[int, float], Field(description='Default: 0.5110091743119266')],
                               year_term: Annotated[Union[int, float], Field(description='Default: 30')],
                               percent_rate: Annotated[Union[int, float], Field(description='Default: 3.088')],
                               down_payment: Annotated[Union[int, float], Field(description='Default: 239800')],
                               monthly_home_insurance: Annotated[Union[int, float], Field(description='Default: 416')],
                               price: Annotated[Union[int, float], Field(description='Default: 1300000')]) -> dict: 
    '''Mortgage calculae'''
    url = 'https://us-real-estate.p.rapidapi.com/finance/mortgage-calculate'
    headers = {'x-rapidapi-host': 'us-real-estate.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'show_amortization': show_amortization,
        'hoa_fees': hoa_fees,
        'percent_tax_rate': percent_tax_rate,
        'year_term': year_term,
        'percent_rate': percent_rate,
        'down_payment': down_payment,
        'monthly_home_insurance': monthly_home_insurance,
        'price': price,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def finance_rate_trends(is_refinance: Annotated[bool, Field(description='')]) -> dict: 
    '''Get current rate trends and historical rate trends'''
    url = 'https://us-real-estate.p.rapidapi.com/finance/rate-trends'
    headers = {'x-rapidapi-host': 'us-real-estate.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'is_refinance': is_refinance,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def finance_average_rate(postal_code: Annotated[Union[int, float], Field(description='Default: 10312')]) -> dict: 
    '''Get average rates data'''
    url = 'https://us-real-estate.p.rapidapi.com/finance/average-rate'
    headers = {'x-rapidapi-host': 'us-real-estate.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'postal_code': postal_code,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def agents_agents_search_by_zipcode(zipcode: Annotated[str, Field(description='Postal code. Required if search by postal_code only.')],
                                    agent_name: Annotated[Union[str, None], Field(description='Agent name to search.')] = None,
                                    sort: Annotated[Union[str, None], Field(description='One of the following options: agent_rating_high|recent_activity_high|recommendations_count_high|for_sale_count_high|recently_sold_high')] = None,
                                    limit: Annotated[Union[int, float, None], Field(description='Maximum is 20')] = None,
                                    offset: Annotated[Union[int, float, None], Field(description='Offset. Default is 0')] = None,
                                    recommendations_count_min: Annotated[Union[int, float, None], Field(description='Minimum recommendations count. 1 to 10. Default is Any')] = None,
                                    agent_rating_min: Annotated[Union[int, float, None], Field(description='Minimum agent rating. 1 to 5. Default is Any.')] = None,
                                    types: Annotated[Union[str, None], Field(description='One of the following options: agent | team | office')] = None,
                                    price_min: Annotated[Union[int, float, None], Field(description='Minimum list price in USD')] = None,
                                    price_max: Annotated[Union[int, float, None], Field(description='Maximum list price in USD')] = None) -> dict: 
    '''Search for agents, teams, and office by zip code'''
    url = 'https://us-real-estate.p.rapidapi.com/agents/agents-search-by-zipcode'
    headers = {'x-rapidapi-host': 'us-real-estate.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'zipcode': zipcode,
        'agent_name': agent_name,
        'sort': sort,
        'limit': limit,
        'offset': offset,
        'recommendations_count_min': recommendations_count_min,
        'agent_rating_min': agent_rating_min,
        'types': types,
        'price_min': price_min,
        'price_max': price_max,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def agents_agents_search(state_code: Annotated[Union[str, None], Field(description='State code. Required if not search by postal_code.')] = None,
                         city: Annotated[Union[str, None], Field(description='City name. Required if not search by postal_code.')] = None,
                         postal_code: Annotated[Union[str, None], Field(description='Postal code. Required if search by postal_code only.')] = None,
                         agent_name: Annotated[Union[str, None], Field(description='Agent name to search.')] = None,
                         sort: Annotated[Union[str, None], Field(description='One of the following options: agent_rating_high|recent_activity_high|recommendations_count_high|for_sale_count_high|recently_sold_high')] = None,
                         limit: Annotated[Union[int, float, None], Field(description='Maximum is 100')] = None,
                         offset: Annotated[Union[int, float, None], Field(description='Offset. Default is 0')] = None,
                         recommendations_count_min: Annotated[Union[int, float, None], Field(description='Minimum recommendations count. 1 to 10. Default is Any')] = None,
                         agent_rating_min: Annotated[Union[int, float, None], Field(description='Minimum agent rating. 1 to 5. Default is Any.')] = None,
                         types: Annotated[Union[str, None], Field(description='One of the following options: agent | team | office')] = None,
                         price_min: Annotated[Union[int, float, None], Field(description='Minimum list price in USD')] = None,
                         price_max: Annotated[Union[int, float, None], Field(description='Maximum list price in USD')] = None) -> dict: 
    '''Search for agents, teams and office'''
    url = 'https://us-real-estate.p.rapidapi.com/agents/agents-search'
    headers = {'x-rapidapi-host': 'us-real-estate.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state_code': state_code,
        'city': city,
        'postal_code': postal_code,
        'agent_name': agent_name,
        'sort': sort,
        'limit': limit,
        'offset': offset,
        'recommendations_count_min': recommendations_count_min,
        'agent_rating_min': agent_rating_min,
        'types': types,
        'price_min': price_min,
        'price_max': price_max,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def agents_agent_profile(advertiser_id: Annotated[str, Field(description='')],
                         nrds_id: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Get Agent's profile by advertiser_id and nrds_id'''
    url = 'https://us-real-estate.p.rapidapi.com/agents/agent-profile'
    headers = {'x-rapidapi-host': 'us-real-estate.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'advertiser_id': advertiser_id,
        'nrds_id': nrds_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def agents_agent_listings(advertiser_id: Annotated[str, Field(description='')],
                          nrds_id: Annotated[Union[str, None], Field(description='')] = None,
                          page: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Get Agent's listings'''
    url = 'https://us-real-estate.p.rapidapi.com/agents/agent-listings'
    headers = {'x-rapidapi-host': 'us-real-estate.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'advertiser_id': advertiser_id,
        'nrds_id': nrds_id,
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
