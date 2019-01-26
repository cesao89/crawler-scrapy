from scrapy.spider import XMLFeedSpider
from scrapy.selector import Selector


class FeedXmlSpider(XMLFeedSpider):
    name = 'feedg1news'
    alowed_domais = ['pox.globo.com']
    start_urls = ['http://pox.globo.com/rss/g1/']
    iterator = 'iternodes'  # This is actually unnecessary, since it's the default value
    itertag = 'item'

    def parse_node(self, xml_response, node):
        sel = Selector(xml_response)
        print(sel.xpath("//item//title").extract())
