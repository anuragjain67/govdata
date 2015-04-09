# Apps based on GovData
[![Build Status](https://travis-ci.org/anuragjain67/govdata.svg?branch=master)](https://travis-ci.org/anuragjain67/govdata)
This project will be containing multiple apps related to govdata. For now, just contains pincode directory.

## PincodeApp
* Support for CURD APIs

```
GET: /api/pincodes

{
   "meta":{
      "limit":20,
      "next":null,
      "offset":0,
      "previous":null,
      "total_count":1
   },
   "objects":[
      {
         "circle_name":"West Bengal",
         "delivery_status":"Delivery",
         "district_name":"Malda",
         "division_name":"Malda",
         "id":1,
         "office_name":"Baishnabnagar S.O",
         "office_type":"S.O",
         "pincode":732210,
         "region_name":"North Bengal And Sikkim",
         "resource_uri":"/api/pincode/1/",
         "state_name":"WEST BENGAL",
         "taluk":"Kaliachak-ii"
      }
   ]
}

POST /api/pincodes
Content Type -> application/json
data to post:

{
    "circle_name":"West Bengal",
    "pincode":732210,
    "state_name": "WEST BENGAL",
    ...
}

Also supports for PUT, PATCH

Also support filtering for 
pincode, region_name, circle_name,
district_name, state_name
/api/pincode/?q='west'
```

* Contains first time data migration script (Unfortunately heroku supports only 10000 rows free, so had to restrict in the script)
https://data.gov.in/resources/all-india-pincode-directory/download
Command: python manage.py migrate_pincodes

* A basic page which will consume Search API.

* Unit Test case

* Continuos Integration with Travis and Heroku

* Improvements:
   * Search API can improved by writing sql query instead of using ORM. 
   * Write the performance tests.
