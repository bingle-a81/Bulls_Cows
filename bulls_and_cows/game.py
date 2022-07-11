# -*- coding: utf-8 -*-
import logging.config
from settings import logger_config
import random
from dataclasses import dataclass
import bills_caw_engine

logging.config.dictConfig(logger_config)
logger = logging.getLogger('app_logger.' + __name__)

@dataclass()
class Number:
    ferst_number:str
    second_number:str
    therd_number:str
    forth_number:str

@dataclass()
class QuontityAnimals:
    bills:int
    cows:int

def checking_the_uniqueness_of_numbers(list_repeat:list)->Number:
    numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',)
    while True:
        numb=random.choice(numbers)
        if numb not in list_repeat:
            return numb


def set_the_numbers()->list:
    list_repeat=[]
    i=0
    while i<4:
        number=checking_the_uniqueness_of_numbers(list_repeat)
        list_repeat.append(number)
        logger.debug(list_repeat)
        i+=1
    return list_repeat

def checking_the_bulls(lst:list,lst2:list)->QuontityAnimals:
    bulls_count = 0
    cow_count = 0
    for e in range(len(lst2)):
        num = (lst2[e])
        logger.debug(f'num={num}')
        if num in lst:
            if lst2.index(num) == lst.index(num):
                bulls_count += 1
            else:
                cow_count += 1
        else:
            pass
    return QuontityAnimals(bulls_count,cow_count)


# ***********************************************************************
# -----------------------------------------------------------------------
#
def main():
    # hidden_numbers=set_the_numbers()
    hidden_numbers=['7','9','1','3']
    step=0
    while True:
        # input_number=list(input())
        if step==0:
            input_number =['0', '1', '2', '3',]
        else:
            input_number=bills_caw_engine.set_the_numbers()
        quontity=checking_the_bulls(hidden_numbers,input_number)
        step+=1
        if quontity.bills==4:
            print(f'ПОБЕДА!кол-во попыток={step}')
            break
        else:
            print(f'быков = {quontity.bills}')
            print(f'коров = {quontity.cows}')
        break


# -----------------------------------------------------------------------
if __name__ == '__main__':
    main()
