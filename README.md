Hype Liberator
===============

Love [Hype Machine]("http://hypem.com")? Want to grab all your hearted songs as MP3's? This does just that.

Demo up at [hypeliberator.com]("http://hypeliberator.com"). If you need an example username to query mine is `dmesg`

Built on Python, Flask and Requests in the rear with Backbone and JQuery up front.

The main entry points are the HTTP routes defined in `main.py`

NB: This is no longer in use at [hypeliberator.com]("http://hypeliberator.com") - instead the
[rewrite in Go is]("http://github.com/nickhs/hypeliberator-go").

# Deployment

1) Install SQLite and Python development headers.
On Ubuntu:

    sudo apt-get install python python-dev libsqlite3-dev

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
