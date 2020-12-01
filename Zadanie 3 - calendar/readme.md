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

# Example 
## Request
`GET /calendar/2020/10`

## Response
```BEGIN:VCALENDAR
VERSION:2.0
PRODID:ics.py - http://git.io/lLljaA
BEGIN:VEVENT
DTSTART:20201001T000000Z
SUMMARY:Wielka Integracja WIP
UID:09c32697-ca3e-4a67-b265-2bba4f318597@09c3.org
URL:https://www.facebook.com/events/381849316135778/?active_tab=discussion
END:VEVENT
BEGIN:VEVENT
DTSTART:20201001T000000Z
SUMMARY:Akcja Integracja Online
UID:24471c66-8276-4645-a351-759271a239fc@2447.org
URL:https://facebook.com/events/s/akcja-integracja-odkryj-z-nami/3041545625959235/?ti=as
END:VEVENT
BEGIN:VEVENT
DTSTART:20201010T000000Z
SUMMARY:Wielka Integracja WIP
UID:a902fc51-3a75-471d-a9b2-890a99573ed9@a902.org
URL:https://www.facebook.com/events/381849316135778/?active_tab=discussion
END:VEVENT
BEGIN:VEVENT
DTSTART:20201001T000000Z
SUMMARY:Wielka Integracja WIP
UID:c89143c5-48e1-42d7-a866-aacf07e40ff4@c891.org
URL:https://www.facebook.com/events/381849316135778/?active_tab=discussion
END:VEVENT
END:VCALENDAR```