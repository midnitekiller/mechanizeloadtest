import mechanize
import time


class Transaction(object):
    def __init__(self):
        self.custom_timers = {}
        self.base_url = 'http://www.beamto.us'
    
    def run(self):
        br = mechanize.Browser()
        br.set_handle_robots(False)
        
        start_timer = time.time()
        new_data = 'page=1'
        resp = br.open(self.base_url + '/api/v1/getTrendingAlbums', 'new_data')
        resp.read()
        latency = time.time() - start_timer
        self.custom_timers['/api/v1/getTrendingAlbums'] = latency  
        assert (resp.code == 200), 'Bad HTTP Response'


if __name__ == '__main__':
    trans = Transaction()
    trans.run()
    print trans.custom_timers
