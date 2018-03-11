# -*- coding: utf-8 -*-
import scrapy
from jokescraper1.items import Jokescraper1Item

class JokebotSpider(scrapy.Spider):
    name = "jokebot"
    allowed_domains = ["scrapsfromtheloft.com"]
    joke_urls = 'http://scrapsfromtheloft.com/comedy/page/'
    start_urls = [joke_urls + "1",
                  joke_urls + "2",
                  joke_urls + "3",
                  joke_urls + "4",
                  joke_urls + "5",
                  joke_urls + "6"]

    def parse(self, response):

        for href in response.css(".entry-title a::attr(href)"):
            url = href.extract()
            yield scrapy.Request(url, callback=self.parse_item)

    def parse_item(self, response):

        item = Jokescraper1Item()
        for sel in response.css('.post-content'):
            item['title'] = sel.xpath('//title/text()').extract()
            item['body'] = sel.css(" p::text").extract()


        yield item


