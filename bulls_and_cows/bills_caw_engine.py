# -*- coding: utf-8 -*-
import logging.config
from settings import logger_config
import game

logging.config.dictConfig(logger_config)
logger = logging.getLogger('app_logger.' + __name__)

dict_={'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,}
list_pust=['10','10','10','10']
bi=[]
co=[]
bil=0
cow=0

def set_the_numbers():
    numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',)
    lst=numbers[0:4]
    logger.debug(lst)
    return lst


def perebor(b,c,lst:list):
    global list_pust,bi,co
    for e in range(len(lst)):
        num = (lst2[e])
        logger.debug(f'num={num}')
        if num in lst:
            if lst2.index(num) != lst.index(num):
                bi.append()
            else:
                cow_count += 1
        else:
            pass
    vr=(b+c)/10
    for x in lst:
        dict_[x] +=vr
    print(dict_)




#
def main():
    bill=0
    cow=0
    while True:
        bill=int(input())
        cow = int(input())
        lst=list(input())
        perebor(bill,cow,lst)




# -----------------------------------------------------------------------
if __name__ == '__main__':
    main()
