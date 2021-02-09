import re

import scrapy

from scrapy.loader import ItemLoader
from ..items import FarbancaItem
from itemloaders.processors import TakeFirst


class FarbancaSpider(scrapy.Spider):
	name = 'farbanca'
	start_urls = ['https://www.farbanca.it/media/news/']

	def parse(self, response):
		post_links = response.xpath('//div[@class="sn_listing_list_i_in"]/a/@href').getall()
		yield from response.follow_all(post_links, self.parse_post)

		next_page = response.xpath('//a[@class="next "]/@href').getall()
		yield from response.follow_all(next_page, self.parse)


	def parse_post(self, response):
		title = response.xpath('//h1/text()').getall()
		title = [p.strip() for p in title]
		title = ' '.join(title).strip()

		description = response.xpath('//div[@class="col-12 col-md-9 col-xl-7 offset-md-1 offset-xl-2 mt-50"]//text()[normalize-space()]').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()
		date = response.xpath('//div[@class="sn_info_icon _s my-5 mr-15"]/text()[normalize-space()]').get()

		item = ItemLoader(item=FarbancaItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
