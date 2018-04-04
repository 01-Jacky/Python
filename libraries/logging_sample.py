import logging

LOGGER_CONFIG = {
    # 'filename': 'example.log',
    'level': logging.DEBUG,
    # 'format': '%(asctime)s %(levelname)s: %(message)s',
    # 'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
}

# log to file
logging.basicConfig(**LOGGER_CONFIG)
logging.info('This message is info2')
logging.debug('This message is debugging2')
logging.warning('This message is warning2')  # will print a message to the console



