import scrapy


class LoginSpider(scrapy.Spider):
    name = 'login'

    def start_requests(self):
        return [scrapy.FormRequest("http://testing-ground.scraping.pro/login?mode=login",
                                   formdata={
                                       'usr': 'admin',
                                       'pwd': '12345'
                                   },
                                   callback=self.logged_in)]

    def logged_in(self, response):
        # here you would extract links to follow and return Requests for
        # each of them, with another callback
        print(response.css('#case_login .success::text').extract())
