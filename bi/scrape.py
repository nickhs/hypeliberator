import requests
from models import Song
from app import db, config


class Scraper():
    '''
    Encapsulates the main scraping logic
    '''

    def __init__(self, username):
        self.username = username
        self.busy = False
        self.songs = []
        self.session = requests.Session()

        '''
        Headers taken from UberHype v1.0.2 Android APK
        '''
        self.session.headers.update({
            # 'Authorization': 'Basic ZG1lc2c6Zm9vYmFy',
            'User-Agent': 'http://hypeliberator.com v1.0',
            'Host': 'api.hypem.com',
            'Accept-Encoding': 'gzip',
            'Proxy-Connection': 'close',
            'Connection': 'close'
        })

    def fetch(self):
        '''
        Starts the entire fetch operation. Note that Hype
        Machine spreads your hearted songs over a number of pages
        and we need to traverse the paginated responses to retrieve them
        '''

        # Make sure we don't trip over ourselves
        self.busy = True

        count = 1
        while count < 1000:  # basically a while true
            # Fetch every individual page
            url = self._get_url(count)
            ret_val = self._fetch_data(url)

            # Break if we failed to fetch the latest page
            if not ret_val:
                break

            count += 1

        self.busy = False
        return self.songs

    def _fetch_data(self, url):
        '''
        Actual fetching of song information from remote server
        pased on the url provided

        Returns True or False depending on whether the request/parsing
        succeeded
        '''

        resp = requests.get(url)

        if not resp.ok:
            print "Failed to get %s [%s]" % (resp.url, resp.status_code)
            return False

        try:
            data = resp.json()
        except ValueError as e:
            print e
            return False

        if not data:
            return False

        count = 0

        while count < 100:
            if str(count) not in data:
                break

            track = data[str(count)]
            song = self._check_id(track['mediaid'])

            if not song:
                song = Song(track['mediaid'])
                song.title = track['title']
                song.artist = track['artist']
                song.url = track['stream_url_raw']
                db.session.add(song)
            else:
                song.downloaded += 1
                song.url = track['stream_url_raw']
                db.session.add(song)

            db.session.commit()

            self.songs.append(song)
            count += 1

        return True

    def _check_id(self, id):
        '''
        Checks to see if the song already exists in local database
        '''
        return Song.get_by_hypem(id)

    def _get_url(self, index):
        '''
        Format an index (page) into the location on the server's
        backend
        '''

        string = "%s/%s/json/%s/data.js?key=%s" % (config["HYPEM_ENDPOINT"], self.username, index, config["HYPEM_KEY"])
        return string
