"""A data model for the NFDI landscape."""

import wikidata_client
import click
from bioregistry import NormalizedNamedReference
from curies import Triple
import pyobo
import pystow
from wikidata_client import get_label

WIKIDATA_MODULE = pystow.join("wikidata", "cache", name="labels.json")


def get_label_cached(identifier) -> str:
    get_label(identifier)


def wikidata(identifier: str) -> NormalizedNamedReference:
    return NormalizedNamedReference(
        prefix="wikidata",
        identifier=identifier,
        name=get_label_cached(identifier),
    )


def ror(identifier: str) -> NormalizedNamedReference:
    """Get a ROR reference."""
    return NormalizedNamedReference(
        prefix="ror",
        identifier=identifier,
        name=pyobo.get_name("ror", identifier),
    )


class Interaction(Triple):
    """An interaction between two entities."""


PARTNERSHIP_QUERY = """\
    SELECT  ?consortium ?consortiumLabel ?partner ?partnerLabel
    WHERE {
      ?consortium wdt:P31 wd:Q98270496 ;
                  wdt:P2652 ?partner .
      SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],mul,en". }
    }
"""


@click.command()
def main():
    for a, b, c, d in wikidata_client.query(PARTNERSHIP_QUERY):
        pass


if __name__ == "__main__":
    main()
