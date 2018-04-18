import json
import requests
import sys
import re
import MySQLdb as db
import MySQLdb.cursors
import logging
from logging.handlers import TimedRotatingFileHandler
import time
from elasticsearch import Elasticsearch
from pyelasticsearch.client import ElasticSearch


#########################################################################################
# Initialize Logger to log to stdout and a log file
#########################################################################################
def initLogger():

    try:
        # Initialize Logger
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO) # INFO, WARNING, ERROR, CRITICAL
        formatter = logging.Formatter('%(asctime)s - %(funcName)s:%(lineno)s - %(levelname)s - %(message)s')

        logFile = "elk.log"
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        fh = TimedRotatingFileHandler(logFile,
                                     when="midnight")
        fh.setLevel(logging.INFO)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        logger.info("Initialized logger")
    except Exception as e:
        logger.info("Exception: " + str(e))

    return logger


#########################################################################################
# Get connection to the database
#########################################################################################
def getPowCon():
    powCon = None
    try:
        dbhost = g_conf["dbHost"]
        dbuser = g_conf["dbUser"]
        dbpwd = g_conf["dbPwd"]
        dbname = g_conf["dbName"]
        dbport = int(g_conf["dbPort"])

        powCon = db.connect(host=dbhost,
                            user=dbuser,
                            passwd=dbpwd,
                            db=dbname,
                            port=dbport,
                            cursorclass = MySQLdb.cursors.DictCursor)
    except Exception as e:
        logger.error("DB Details Missing: " +str(e))

    return powCon

if __name__ == '__main__':

    logger = initLogger()

    #r = requests.get('http://localhost:9200')
    r = requests.get('http://10.139.77.93:9200/grpmidx/_search?pretty=true')
    #logger.info ("status code:"+str(r.status_code))
    logger.info ("content: "+str(r.content))


    #es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    es = Elasticsearch([{'host': '10.139.77.93', 'port': 9200}])

    powCon = getPowCon()

#    powQry = "select distinct * from rpt_power_estimates where timeofupdate between (SELECT date_add(DATE_FORMAT((SELECT now()), '%Y-%m-%d 00:00:00'), interval -1 DAY)) AND (SELECT DATE_FORMAT((SELECT now()), '%Y-%m-%d 00:00:00')) order by timeofupdate desc"


    powQry = "select distinct * from rpt_power_estimates where timeofupdate between (SELECT date_add(DATE_FORMAT((SELECT now()), '%Y-%m-%d 00:00:00'), interval -20 DAY)) AND (SELECT date_add(DATE_FORMAT((SELECT now()), '%Y-%m-%d 00:00:00'), interval -18 DAY)) order by timeofupdate desc"


    powCur = powCon.cursor()

    powCur.execute(powQry, (None))

    rows = powCur.fetchall()
    for r in rows:
        date = r['timeofupdate']
        remoteid = r['remoteid']
        ind = str(date)+str(remoteid)
        logger.info("Index: " + str(ind))
        es.index(index='grpmidx',doc_type='grpmdoc1',id=ind,body=r)

    logger.info("new sw index")

    r = requests.get('http://10.139.77.93:9200/grpmidx/_search?pretty=true')

    logger.info ("sw content:"+str(r.content))

