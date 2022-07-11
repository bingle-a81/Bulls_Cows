# -*- coding: utf-8 -*-
import logging.config
from settings import logger_config
import game

logging.config.dictConfig(logger_config)
logger = logging.getLogger('app_logger.' + __name__)

def set_the_numbers():
    numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',)
    lst=numbers[0:4]
    logger.debug(lst)
    return lst







#
def main():
    lst = ['0', '1', '2', '3', ]
    set_the_numbers()


# -----------------------------------------------------------------------
if __name__ == '__main__':
    main()
