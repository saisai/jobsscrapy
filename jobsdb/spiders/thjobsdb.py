# -*- coding: utf-8 -*-
import scrapy
from jobsdb.items import JobsdbItem
from bs4 import BeautifulSoup
from datetime import datetime
import logging

class ThjobsdbSpider(scrapy.Spider):
    name = "thjobsdb"
    allowed_domains = ["th.jobsdb.com"]
    start_urls= (
            'http://th.jobsdb.com/th/jobs/information-technology/%s' % page for page in range(1, 20)
            )


    def parse(self, response):
        if 'th.jobsdb.com' in response.url:
            soup = BeautifulSoup(response.body, "lxml")
            
            for data in soup.find_all('div', class_='result-sherlock-cell'):
                if data["class"][0]:
                    if data.find('h3', class_='job-title') != None:
                        jobsdb = JobsdbItem()
                        jobsdb['title'] = data.find('h3', class_='job-title').get_text()                        
                        jobsdb['link'] = data.find('h3', class_='job-title').next_element.get('href')                        
                        jobsdb['time'] = data.find('p', class_="job-quickinfo-timestamp").get_text() 
                        self.logger.info('Title=%s' % jobsdb['title']) 
                        self.logger.info('Link=%s' % jobsdb['link'])
                        self.logger.info('Scrap Date=%s' % datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                        self.logger.info('((((^_^))))'.center(100, '-'))                       
                        yield jobsdb
                        
            #return items //To Check the value in json format //scrapy crawl jobsdb -o test.json
            #pass
