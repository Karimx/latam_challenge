import logging

from end_point.cfg import DEBUG
# create a logger object
logger = logging.getLogger('my_logger')
if DEBUG:
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.CRITICAL)

# create a file handler to write log messages to a file
file_handler = logging.FileHandler('my_log_file.log')
if DEBUG:
    file_handler.setLevel(logging.DEBUG)
else:
    file_handler.setLevel(logging.CRITICAL)



# create a console handler to output log messages to the console
# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.DEBUG)

# create a formatter to specify the log message format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add the formatter to the handlers
file_handler.setFormatter(formatter)
#console_handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(file_handler)
#logger.addHandler(console_handler)
