#!/bin/bash

mysql -uroot -proot jobs -e "DROP TABLE jobs_db;"

# Get the parent directory of where this script is.
SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ] ; do SOURCE="$(readlink "$SOURCE")"; done
DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"


cd $DIR
/usr/local/bin/scrapy crawl thjobsdb

