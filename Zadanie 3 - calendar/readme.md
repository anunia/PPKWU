# Details
API returns informations of chosen month in ICS/iCal format from `http://www.weeia.p.lodz.pl` calendar. 

# Endpoint

## Request
`GET /calendar` 


## Response
Automatically downloading file ICS containing calendar informations from chosen month.

## Request
`GET /calendar/<year>/<month>` 
where `<month>` represents month to be returned from the year `<year>`.

## Response
Automatically downloading file ICS containing calendar informations from chosen month.

##Example 
`GET /calendar/2020/03`