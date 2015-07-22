# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.orm import sessionmaker
from models import Jobsdb, db_connect, create_jobsdb_table


class JobsdbPipeline(object):

    def __init__(self):
        engine = db_connect()
        create_jobsdb_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        jobsdb = Jobsdb(**item)
        session.add(jobsdb)
        session.commit()
        return item
