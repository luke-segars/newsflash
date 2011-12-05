from poc.plugin import plugin
from poc.powerqueue import pq

class LoadFeeds(plugin.BasePlugin):
    def __init__(self):
        # Call your own constructor
        super(LoadFeeds, self).__init__()

    def init(self):
        pass
        self.setOutputQueueName('localhost', 'preprocess.annotate')
        self.setRecordStoreHost('localhost')

    def runloop(self):
        queue = pq.ProducerQueue('localhost', 'preprocess.crawl')

        # Read in all of the RSS feeds from rss.txt
        fp = open('rss.txt', 'r')
        feeds = fp.readlines()
        fp.close()

        # Create a new message for all RSS feeds.
        for feed in feeds:
            msg = pq.Message()
            msg.url = feed
            # Send the message
            queue.send(msg)
