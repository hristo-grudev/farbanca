BOT_NAME = 'farbanca'

SPIDER_MODULES = ['farbanca.spiders']
NEWSPIDER_MODULE = 'farbanca.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'farbanca.pipelines.FarbancaPipeline': 100,

}