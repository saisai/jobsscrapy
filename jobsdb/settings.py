# -*- coding: utf-8 -*-

# Scrapy settings for jobsdb project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'jobsdb'

SPIDER_MODULES = ['jobsdb.spiders']
NEWSPIDER_MODULE = 'jobsdb.spiders'

ITEM_PIPELINES = {
        'jobsdb.pipelines.JobsdbPipeline':300
        }

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'jobsdb (+http://www.yourdomain.com)'

LOG_LEVEL = "INFO"
LOG_STDOUT = True
LOG_FILE = "log/spider.log"

TABLE_NAME= "jobs_db"

DATABASE = {'drivername': 'mysql',
            'host': 'localhost',
            'port': '3306',
            'username': 'root',
            'password': 'root',
            'database': 'jobs',
            'query': {'charset': 'utf8'}}