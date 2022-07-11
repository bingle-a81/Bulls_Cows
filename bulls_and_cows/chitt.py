# -*- coding: utf-8 -*-
import logging.config
from settings import logger_config
import game

logging.config.dictConfig(logger_config)
logger = logging.getLogger('app_logger.' + __name__)

answers=game.get_all_answers()
counter=0
while len(answers) !=1:
    counter+=1
    print(f'Ход номер {counter}')
    print(f'Возможных вариантов:{len(answers)}')
    ans=game.get_one_answer(answers)
    print(f'Назови комбинацию {ans}')
    bulls=int(input('Сколько быков?'))
    cows=int(input('Сколько коров?'))
    answers=game.del_bad_answer(answers,ans,bulls,cows)
print(f'Ответ:{answers}')


# ***********************************************************************
# -----------------------------------------------------------------------
#
def main():
    logger.info("Start ")

    logger.info("End")


# -----------------------------------------------------------------------
if __name__ == '__main__':
    main()
