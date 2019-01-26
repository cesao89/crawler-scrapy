import scrapy


class GlobonewsSpider(scrapy.Spider):
    name = "globonews"
    start_urls = [
        'https://g1.globo.com/'
    ]

    def parse(self, response):
        for post in response.css('.feed-post-body'):
            yield {
                'title': post.css('.feed-post-link::text').extract_first(),
                'datetime': post.css('.feed-post-datetime::text').extract_first()
            }

        # next_page = response.css('.load-more a::attr(href)').extract_first()
        # if next_page is not None:
            # next_page = response.urljoin(next_page)
            # yield scrapy.Request(url=next_page, callback=self.parse)

        for a in response.css('.load-more a'):
            yield response.follow(a, callback=self.parse)
