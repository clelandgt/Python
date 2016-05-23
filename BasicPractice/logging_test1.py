import logging

logging.basicConfig(format='%(levelname)s: %(asctime)s: %(message)s',filename='example.log', level=logging.DEBUG)

logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.warning('%s before you %s', 'look', 'leap!')
