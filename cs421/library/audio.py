import items
from authors import *
from publishers import *

author = authorByName("Catherine Bellaire")
if author is None:
    author = items.Author.create(name="Catherine Bellaire")

publisher = publisherByName("Chrysalis Music")
if publisher is None:
    publisher = items.Publisher.create(name="Chrysalis Music")

items.Audio.create(
    title="Single",
    date="1983-07-11",
    format=items.Audio.format_vinyl,
    songs=[{"track":1, "duration":100, "title":"My heart will always be yours"}],
    genres=["classic"],
    authors=[author],
    publishers=[publisher],
    languages=["en"]
)

author = authorByName("Janelle Monae")
if author is None:
    author = items.Author.create(name="Janelle Monae")

publisher = publisherByName("Carlin America, Inc.")
if publisher is None:
    publisher = items.Publisher.create(name="Carlin America, Inc.")

items.Audio.create(
    title="We are young",
    date="1991-12-31",
    format=items.Audio.format_cd,
    songs=[{"track":1, "duration":120, "title":"We are young"}, {"track":2, "duration":97, "title":"Stronger"}, {"track":3, "duration":111, "title:":"Wanted"}, {"track":4, "duration":220, "title":"We are alive"}, {"track":5, "duration":176, "title":"No way"}],
    genres=["alternative", "pop"],
    authors=[author],
    publishers=[publisher],
    languages=["en"]
)

author = authorByName("Bob Caule")
if author is None:
    author = items.Author.create(name="Bob Caule")

publisher = publisherByName("All Boys Music")
if publisher is None:
    publisher = items.Publisher.create(name="All Boys Music")

items.Audio.create(
    title="It's time",
    date="1998-01-17",
    format=items.Audio.format_cd,
    songs=[{"track":1, "duration":88, "title":"On the road to freedom"}, {"track":2, "duration":142, "title":"Catch the wind"}, {"track":3, "duration":78, "title:":"We are"}],
    genres=["pop"],
    authors=[author],
    publishers=[publisher],
    languages=["en"]
)

author = authorByName("Trisha MacDonald")
if author is None:
    author = items.Author.create(name="Trisha MacDonald")

publisher = publisherByName("Third Side Music")
if publisher is None:
    publisher = items.Publisher.create(name="Third Side Music")

items.Audio.create(
    title="Despite the fact",
    date="1970-11-01",
    format=items.Audio.format_vinyl,
    songs=[{"track":1, "duration":78, "title":"Why did you leave me"}, {"track":2, "duration":252, "title":"The sidewalk"}, {"track":3, "duration":99, "title:":"Broken heart"}, {"track":4, "duration":99, "title:":"I can't do this anymore"}],
    genres=["romance", "classic"],
    authors=[author],
    publishers=[publisher],
    languages=["en","fr"]
)


author = authorByName("Walid Alfred")
if author is None:
    author = items.Author.create(name="Walid Alfred")

publisher = publisherByName("Third Side Music")
if publisher is None:
    publisher = items.Publisher.create(name="Third Side Music")


items.Audio.create(
    title="Top of the world",
    date="2011-12-05",
    format=items.Audio.format_digital,
    songs=[{"track":1, "duration":185, "title":"Don't give up"}, {"track":2, "duration":112, "title":"Because we can"}, {"track":3, "duration":209, "title:":"Invincible"}, {"track":4, "duration":102, "title:":"Just once more"}, {"track":5, "duration":176, "title:":"Make them pay"}, {"track":6, "duration":252, "title:":"That's the spirit"}],
    genres=["pop", "rock"],
    authors=[author],
    publishers=[publisher],
    languages=["en"]
)