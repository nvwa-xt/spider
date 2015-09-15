# -*- coding: utf-8 -*-


BOT_NAME = 'wooyun'

SPIDER_MODULES = ['wooyun.spiders']
NEWSPIDER_MODULE = 'wooyun.spiders'

ITEM_PIPELINES = {'wooyun.pipelines.MongoDBPipeline': 300,}

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "wooyun_data"
MONGODB_COLLECTION = "vulnerability_data"

DOWNLOAD_DELAY = 0


