import items
from authors import *
from publishers import *

author_list=[]
author = authorByName("George Treant")
if author is None:
    author = items.Author.create(name="George Treant")
author_list.append(author)
author = authorByName("Lucas Benner")
if author is None:
    author = items.Author.create(name="Lucas Benner")
author_list.append(author)

publisher_list=[]
publisher = publisherByName("Guideposts / Ideals")
if publisher is None:
    publisher = items.Publisher.create(name="Guideposts / Ideals")
publisher_list.append(publisher)

items.Magazine.create(
    title="The road to a fitter you",
    date="2003-07-21",
    issn="39295828",
    issue="3",
    pages="56",
    genres=["sport","fashion","men"],
    authors=author_list,
    publishers=publisher_list,
    languages=["en"]
)

author_list=[]
author = authorByName("Tyra Holmes")
if author is None:
    author = items.Author.create(name="Tyra Holmes")
author_list.append(author)
author = authorByName("Eleonore Lafee")
if author is None:
    author = items.Author.create(name="Eleonore Lafee")
author_list.append(author)
author = authorByName("Mathilde Laurence")
if author is None:
    author = items.Author.create(name="Mathilde Laurence")
author_list.append(author)

publisher_list=[]
publisher = publisherByName("Guideposts / Ideals")
if publisher is None:
    publisher = items.Publisher.create(name="Guideposts / Ideals")
publisher_list.append(publisher)

items.Magazine.create(
    title="Femme Fatale",
    date="2009-03-18",
    issn="39129047",
    issue="1",
    pages="32",
    genres=["fashion","women"],
    authors=author_list,
    publishers=publisher_list,
    languages=["en", "fr"]
)

author_list=[]
author = authorByName("Jimmy Watsons")
if author is None:
    author = items.Author.create(name="Jimmy Watsons")
author_list.append(author)

publisher_list=[]
publisher = publisherByName("Hodder Education")
if publisher is None:
    publisher = items.Publisher.create(name="Hodder Education")
publisher_list.append(publisher)


items.Magazine.create(
    title="Tech: 101",
    date="2012-01-18",
    issn="50581920",
    issue="6",
    pages="24",
    genres=["Technology"],
    authors=author_list,
    publishers=publisher_list,
    languages=["en"]
)

author_list=[]
author = authorByName("James Williams")
if author is None:
    author = items.Author.create(name="James Williams")
author_list.append(author)

publisher_list=[]
publisher = publisherByName("Brookings Institution Press")
if publisher is None:
    publisher = items.Publisher.create(name="Brookings Institution Press")
publisher_list.append(publisher)


items.Magazine.create(
    title="The Globe",
    date="2012-02-27",
    issn="50581920",
    issue="119",
    pages="30",
    genres=["News"],
    authors=author_list,
    publishers=publisher_list,
    languages=["en"]
)

author_list=[]
author = authorByName("Mike Simons")
if author is None:
    author = items.Author.create(name="Mike Simons")
author_list.append(author)

publisher_list=[]
publisher = publisherByName("Qcards")
if publisher is None:
    publisher = items.Publisher.create(name="Qcards")
publisher_list.append(publisher)


items.Magazine.create(
    title="Are you game",
    date="2012-02-27",
    issn="59307429",
    issue="26",
    pages="35",
    genres=["Video Games","Technology"],
    authors=author_list,
    publishers=publisher_list,
    languages=["en"]
)

