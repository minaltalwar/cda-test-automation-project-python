import configparser
import sys

import pytest
from testcases.LoginPage import loginSession
import logging
from datetime import datetime


# Login and create headers by logging into URL
@pytest.fixture(scope="class")
def session_auth():
    global url
    global headers
    config = configparser.ConfigParser()
    config.read('Configuration.cfg')
    loginURL = config['Server']['loginURL']
    contentType = config['Server']['contentType']
    userName = config['User']['userName']
    passWord = config['User']['passWord']
    url = config['MapviewWidget']['requestURL']
    sessionID = loginSession(loginURL, userName, passWord)
    headers = {'Content-type': contentType, 'Cookie': sessionID}
    return url, headers

    # Initiate logger and logger format


@pytest.fixture(scope="class")
def define_logger():
    global logger
    logger = logging.getLogger()
    # code to print logs in log file
    fh = logging.FileHandler('logs/{:%Y-%m-%d}_Mapview.log'.format(datetime.now()))
    formatter = logging.Formatter('%(asctime)s | %(levelname)-8s | %(lineno)04d | %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    # code to print logs on console
    stdout_handler = logging.StreamHandler(sys.stdout)
    logger.addHandler(stdout_handler)
    logger.info("Execution is about to start...")
    return logger

#
# def pytest_exception_interact(report):

#     logging.error(f'Test exception:\n{report.longreprtext}')
