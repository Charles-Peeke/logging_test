import logging
from logging.handlers import RotatingFileHandler

FORMAT = '%(asctime)-15s %(message)s'
log_file = 'client.log'
logging.basicConfig(filename=log_file, filemode='w', format=FORMAT)
# d = {'clientip': '192.168.0.1', 'user': 'CONFIG'}
logger = logging.getLogger()


def main():
    logger.log(30,'Reading config file...')
    print('Hello World')


main()