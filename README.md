# nfdi-landscape

There are 26 accepted consortia in the German National Research Data
Infrastructure (NFDI). The following query to Wikidata gets information about
each:

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

<iframe style="width: 80vw; height: 50vh; border: none;" src="https://query.wikidata.org/embed.html#SELECT%20%0A%20%20%3Fconsortium%20%3FconsortiumLabel%20%3Fror%20%3Finception%20%3Flogo%20%3Fchairperson%20%3FchairpersonLabel%0A%20%20%3Fwebsite%20%3Fyoutube%20%3Fnfdi4culture%20%3Fzenodo%0AWHERE%0A%7B%0A%20%20%3Fconsortium%20wdt%3AP361%20wd%3AQ61658497%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20wdt%3AP31%20wd%3AQ98270496%20.%0A%20%20OPTIONAL%20%7B%20%3Fconsortium%20wdt%3AP571%20%3Finception%20.%20%7D%0A%20%20OPTIONAL%20%7B%20%3Fconsortium%20wdt%3AP154%20%3Flogo%20.%20%7D%0A%20%20OPTIONAL%20%7B%20%0A%20%20%20%20%3Fconsortium%20p%3AP488%20%3Fstatement.%0A%20%20%20%20%3Fstatement%20ps%3AP488%20%3Fchairperson.%0A%20%20%20%20%23%20Filter%3A%20only%20current%20chairperson%20%28no%20end%20date%29%0A%20%20%20%20FILTER%20NOT%20EXISTS%20%7B%20%3Fstatement%20pq%3AP582%20%3Fendtime%20.%20%7D%0A%20%20%7D%0A%20%20OPTIONAL%20%7B%20%3Fconsortium%20wdt%3AP856%20%3Fwebsite%20.%20%7D%0A%20%20%23OPTIONAL%20%7B%20%3Fconsortium%20wdt%3AP2037%20%3Fgithub%20.%20%7D%0A%20%20%23OPTIONAL%20%7B%20%3Fconsortium%20wdt%3AP4033%20%3Fmastodon%20.%20%7D%0A%20%20OPTIONAL%20%7B%20%3Fconsortium%20wdt%3AP6782%20%3Fror%20.%20%7D%0A%20%20OPTIONAL%20%7B%20%3Fconsortium%20wdt%3AP11971%20%3Fnfdi4culture%20.%20%7D%0A%20%20OPTIONAL%20%7B%20%3Fconsortium%20wdt%3AP2397%20%3Fyoutube%20.%20%7D%0A%20%20OPTIONAL%20%7B%20%3Fconsortium%20wdt%3AP9934%20%3Fzenodo%20.%20%7D%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22%5BAUTO_LANGUAGE%5D%2Cmul%2Cen%22.%20%7D%20%23%20Helps%20get%20the%20label%20in%20your%20language%2C%20if%20not%2C%20then%20default%20for%20all%20languages%2C%20then%20en%20language%0A%7D%0AORDER%20BY%20%3FconsortiumLabel" referrerpolicy="origin" sandbox="allow-scripts allow-same-origin allow-popups" ></iframe>

## Relations

I've observed two kinds of relations on NFDI Wikidata pages so far: partnerships
(P2652) and affiliations (P1416). Partnership relations appear to be
unqualified, and affiliations are annotated with object roles. Here's a query
over partnerships, which I've loosened from NFDI consortia to any parts of NFDI,
which includes other components like
[arthistoricum.net](https://www.arthistoricum.net/):

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

The next query gets affiliations from NFDI parts to any external entities (and
their ROR IDs, when available):

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

I wrote a follow-up SPARQL query over affiliations in Wikidata to understand
what kinds of values are used as the object role. This is helpful as a starting
point to build a data model with a controlled vocabulary:

```sparql
SELECT ?role ?roleLabel (COUNT(?role) as ?count)
WHERE {
  ?x p:P1416/pq:P3831 ?role .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],mul,en". }
}
GROUP BY ?role ?roleLabel
ORDER BY DESC(?count)
```

### ROR Alignment

This query is going to get of the predicates that pop up between Wikidta
entities that have ROR IDs. Surprisingly, this takes 30 seconds to complete, and
usually times out.

```sparql
SELECT DISTINCT ?predicate (COUNT(?predicate) as ?count)
{
  ?subjectROR ^wdt:P6782 ?subject .
  ?subject ?predicate ?object .
  ?object wdt:P6782 ?objectROR .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],mul,en". }
}
GROUP BY ?predicate
ORDER BY DESC(?count)
```

Ideally, this query would also get the label out, which uses
`wikibase:directClaim` to link from the `wdt` back to `wd` namespace

```sparql
SELECT DISTINCT ?p ?pLabel (COUNT(?p) as ?count)
{
  ?subjectROR ^wdt:P6782 ?subject .
  ?subject ?predicate ?object .
  ?object wdt:P6782 ?objectROR .
  # this madness links backwards through the many flavors of properties
  ?p wikibase:directClaim ?predicate .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],mul,en". }
}
GROUP BY ?p ?pLabel
ORDER BY DESC(?count)
```
