Hype Liberator
===============

Love [Hype Machine]("http://hypem.com")? Want to grab all your hearted songs as MP3's? This does just that.

Demo up at [hypeliberator.com]("http://hypeliberator.com")

Built on Python, Flask and Requests in the rear with Backbone and JQuery up front.

# Deployment

1) Install SQLite

2) Install requirements

    sudo pip install -r requirements.txt
    # or use a virtualenv

3) Build database

    LIBERATOR_CONFIG=dev python bootstrap.py

4) Run!

    LIBERATOR_CONFIG=dev python main.py

## Config

Endpoint: where to fetch the loved songs from
Hypem Key: special key used to get stream urls
Database URL: can use anything, sqlite here for convieniance

## TODO

* Event Queue
* Determine track expiration details
* Reset check on timeout or 500 error
