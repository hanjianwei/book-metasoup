# -*- coding: utf-8 -*-

from .douban import Douban
from .calibre import Calibre

import sys
import click
from pprint import pprint


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "--type",
    "-t",
    type=click.Choice(["isbn", "subject", "url"], case_sensitive=False),
    default="url",
    help="Identifier type",
)
@click.argument("identifier")
def book(type, identifier):
    db = Douban()
    if type == "isbn":
        book = db.book_by_isbn(identifier)
    elif type == "subject":
        book = db.book_by_subject(identifier)
    else:
        book = db.book_by_url(identifier)
    pprint(vars(book))


@cli.command()
def movie():
    click.echo("Movie")


if __name__ == "__main__":
    cli()

    # c = Calibre()
    # calibre_id = c.search_isbn(isbn)
    # print(calibre_id)

    # cmd = "calibredb add -e -t {title} -T HomeLibrary".format(title=title)

    # if "作者" in meta:
    #     cmd += " -a {作者}".format(**meta)
    # if "ISBN" in meta:
    #     cmd += " -i {ISBN}".format(**meta)
    #     # if '丛书' in meta:

    # # Download cover image
    # if img is not None:
    #     cover = meta["ISBN"] + img[-4:]
    #     with open(cover, "wb") as f:
    #         f.write(requests.get(img).content)
    #         cmd += " -c {cover}".format(cover=cover)

    # print(cmd)
