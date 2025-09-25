# nfdi-landscape

The following query gets information about each of the 26 NFDI consortia.

```sparql
SELECT 
  ?consortium ?consortiumLabel ?ror ?inception ?logo ?chairperson ?chairpersonLabel
  ?website ?youtube ?nfdi4culture ?zenodo
WHERE {
  ?consortium wdt:P361 wd:Q61658497;
              wdt:P31 wd:Q98270496 .
  OPTIONAL { ?consortium wdt:P571 ?inception . }
  OPTIONAL { ?consortium wdt:P154 ?logo . }
  OPTIONAL { 
    ?consortium p:P488 ?statement.
    ?statement ps:P488 ?chairperson.
    # Filter: only current chairperson (no end date)
    FILTER NOT EXISTS { ?statement pq:P582 ?endtime . }
  }
  OPTIONAL { ?consortium wdt:P856 ?website . }
  #OPTIONAL { ?consortium wdt:P2037 ?github . }
  #OPTIONAL { ?consortium wdt:P4033 ?mastodon . }
  OPTIONAL { ?consortium wdt:P6782 ?ror . }
  OPTIONAL { ?consortium wdt:P11971 ?nfdi4culture . }
  OPTIONAL { ?consortium wdt:P2397 ?youtube . }
  OPTIONAL { ?consortium wdt:P9934 ?zenodo . }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],mul,en". } # Helps get the label in your language, if not, then default for all languages, then en language
}
ORDER BY ?consortiumLabel
```

## Affiliations of NFDI parts

```sparql
SELECT ?consortium ?consortiumLabel ?consortiumROR ?affiliate ?affiliateLabel ?affiliateROR ?affiliateRole ?affiliateRoleLabel
WHERE {
  ?consortium wdt:P361+ wd:Q61658497 ;
              p:P1416 ?affiliateStatement .
              
  ?affiliateStatement ps:P1416 ?affiliate .
  
  OPTIONAL { ?affiliateStatement pq:P3831 ?affiliateRole . }
  OPTIONAL { ?consortium wdt:P6782 ?consortiumROR . }
  OPTIONAL { ?affiliate wdt:P6782 ?affiliateROR . }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],mul,en". }
}
ORDER BY ?consortiumLabel ?affiliateLabel ?affiliateRoleLabel
```

<iframe style="width: 80vw; height: 50vh; border: none;" src="https://query.wikidata.org/embed.html#SELECT%20%0A%20%20%3Fconsortium%20%3FconsortiumLabel%20%3FconsortiumROR%20%3Faffiliate%20%3FaffiliateLabel%20%3FaffiliateROR%20%3FaffiliateRole%20%3FaffiliateRoleLabel%0AWHERE%0A%7B%0A%20%20%3Fconsortium%20wdt%3AP361%2B%20wd%3AQ61658497%20%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20p%3AP1416%20%3FaffiliateStatement%20.%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%3FaffiliateStatement%20ps%3AP1416%20%3Faffiliate%20.%0A%20%20%0A%20%20OPTIONAL%20%7B%20%3FaffiliateStatement%20pq%3AP3831%20%3FaffiliateRole%20.%20%7D%0A%20%20OPTIONAL%20%7B%20%3Fconsortium%20wdt%3AP6782%20%3FconsortiumROR%20.%20%7D%0A%20%20OPTIONAL%20%7B%20%3Faffiliate%20wdt%3AP6782%20%3FaffiliateROR%20.%20%7D%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22%5BAUTO_LANGUAGE%5D%2Cmul%2Cen%22.%20%7D%0A%7D%0AORDER%20BY%20%3FconsortiumLabel%20%3FaffiliateLabel%20%3FaffiliateRoleLabel%0A" referrerpolicy="origin" sandbox="allow-scripts allow-same-origin allow-popups" ></iframe>


As some follow-up, check into what kinds of roles are applied to objects in the affiliation (P1416).
This is where we can get a controlled vocabulary for annotating the interaction context:

```sparql
SELECT ?role ?roleLabel (COUNT(?role) as ?count)
WHERE {
  ?x p:P1416/pq:P3831 ?role .  
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],mul,en". }
}
GROUP BY ?role ?roleLabel
ORDER BY DESC(?count)
```


## Partnerships between NFDI parts

This includes both consortia and other components like arthisoricum (despite the name):
```sparql
SELECT  ?consortium ?consortiumLabel ?consortiumROR ?partner ?partnerLabel ?partnerROR
WHERE {
  ?consortium wdt:P361+ wd:Q61658497 ;
              wdt:P2652 ?partner .
  OPTIONAL { ?consortium wdt:P6782 ?consortiumROR . }
  OPTIONAL { ?partner wdt:P6782 ?partnerROR . }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],mul,en". }
}
ORDER BY ?consortiumLabel ?partnerLabel
```

<iframe style="width: 80vw; height: 50vh; border: none;" src="https://query.wikidata.org/embed.html#SELECT%20%0A%20%20%3Fconsortium%20%3FconsortiumLabel%20%3Fpartner%20%3FpartnerLabel%0AWHERE%0A%7B%0A%20%20%3Fconsortium%20wdt%3AP361%2B%20wd%3AQ61658497%20%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20wdt%3AP2652%20%3Fpartner%20.%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22%5BAUTO_LANGUAGE%5D%2Cmul%2Cen%22.%20%7D%0A%7D%0AORDER%20BY%20%3FconsortiumLabel" referrerpolicy="origin" sandbox="allow-scripts allow-same-origin allow-popups" ></iframe>