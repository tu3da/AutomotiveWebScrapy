from automotiveWebScrapy.items import AutomotivewebscrapyItem
import scrapy
from datetime import datetime

class AutomotivespiderSpider(scrapy.Spider):
    name = 'automotiveSpider'
    allowed_domains = ['mtxm2m.com']
    start_urls = ['http://mtxm2m.com/en']
    
    def start_requets(self):
        urls = ['http://mtxm2m.com/en']
        
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        yield AutomotivewebscrapyItem(
            url = response.url,
            title = response.css('h1::text').extract_first(),
            htags = {
                "h1": response.css('h1').extract,
                "h2": response.css('h2').extract,
                "h3": response.css('h3').extract,
                "h4": response.css('h4').extract,
                "p": response.css('p').extract,
            },
            body = response.text,
            scraping_datetime = datetime.today().strftime('%Y/%m/%d %H:%M:%S')
        )
        
        link = response.css('.main_menu a::attr(href)').extract()
        print("link : ",link)
        
        for url in link:
            if '#' in url:
                continue    
            yield scrapy.Request(url, callback=self.parse)
        
        