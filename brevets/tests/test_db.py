# Nosetests for db insert and fetch

import collections.abc
import os
import pymongo
from pymongo import MongoClient
import logging
import sys
sys.path.append("..")

from flask_brevets import db_insert, db_fetch

import nose    # Testing framework
import logging

logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

# create mongo client
client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
db = client.brevets


# Create a MongoDB document
brevet_distance = 400
begin_date = "2021-01-01T00:00"
controls = [{'miles': '124.274200', 'kilometers': '200', 'location': '', 'openTime': '2021-01-01T05:53', 'closeTime': '2021-01-01T13:30'}, 
            {'miles': '186.411300', 'kilometers': '240', 'location': '', 'openTime': '2021-01-01T05:53', 'closeTime': '2021-01-01T13:30'}, 
            {'miles': '', 'kilometers': '', 'location': '', 'openTime': '', 'closeTime': ''}, 
            {'miles': '', 'kilometers': '', 'location': '', 'openTime': '', 'closeTime': ''}, 
            {'miles': '', 'kilometers': '', 'location': '', 'openTime': '', 'closeTime': ''}, 
            {'miles': '', 'kilometers': '', 'location': '', 'openTime': '', 'closeTime': ''}, 
            {'miles': '', 'kilometers': '', 'location': '', 'openTime': '', 'closeTime': ''}, 
            {'miles': '', 'kilometers': '', 'location': '', 'openTime': '', 'closeTime': ''}, 
            {'miles': '', 'kilometers': '', 'location': '', 'openTime': '', 'closeTime': ''}, 
            {'miles': '', 'kilometers': '', 'location': '', 'openTime': '', 'closeTime': ''}, 
            {'miles': '', 'kilometers': '', 'location': '', 'openTime': '', 'closeTime': ''}, 
            {'miles': '', 'kilometers': '', 'location': '', 'openTime': '', 'closeTime': ''}, 
            {'miles': '', 'kilometers': '', 'location': '', 'openTime': '', 'closeTime': ''}, 
            {'miles': '', 'kilometers': '', 'location': '', 'openTime': '', 'closeTime': ''}, 
            {'miles': '', 'kilometers': '', 'location': '', 'openTime': '', 'closeTime': ''}, 
            {'miles': '', 'kilometers': '', 'location': '', 'openTime': '', 'closeTime': ''}, 
            {'miles': '', 'kilometers': '', 'location': '', 'openTime': '', 'closeTime': ''}, 
            {'miles': '', 'kilometers': '', 'location': '', 'openTime': '', 'closeTime': ''}, 
            {'miles': '', 'kilometers': '', 'location': '', 'openTime': '', 'closeTime': ''}, 
            {'miles': '', 'kilometers': '', 'location': '', 'openTime': '', 'closeTime': ''}]

document = {
    "brevet_distance": brevet_distance,
    "begin_date": begin_date,
    "controls": controls
}

# to check, see if add_one() != 0
def test_db_insert():
    assert db_insert(document) != 0
    assert db_fetch() != 0



if __name__ == '__main__':
    nose.run()