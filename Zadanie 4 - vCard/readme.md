# MOBILNY KALENDARZ WEEIA
## Details
API returns contact informations to the service provider of chosen category and in chosen location.

## Endpoints

### Request
`GET /contact/<category>/<location>` 


### Response
Information about all available companies from chosen `category` and in chosen `<location>`

### Request
`POST /vCard` 


### Response
Information about chosen company in the form of vCard. 

```
BEGIN:VCARD
VERSION:3.0
ADR:;;32-020 Grabówki 12;;;;
EMAIL:kamilprzeczek@interia.pl
FN:Kamil Przęczek
TEL:516 765 572
END:VCARD
```

