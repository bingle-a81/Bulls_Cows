# -*- coding: utf-8 -*-
import logging.config
from settings import logger_config
import random
from dataclasses import dataclass
import bills_caw_engine

logging.config.dictConfig(logger_config)
logger = logging.getLogger('app_logger.' + __name__)

answers=0
player=0
enemy=0

def get_all_answers()->list: # список всех ответов
    ans=[]
    # ans1=[]
    for i in range(10000):
        tmp=str(i).zfill(4)

    # удаляем числа с одинаковыми цифрами через set-множество ,где
    #только уникальные значения множество!!!
        if len(set(map(int,tmp)))==4:
            ans.append(list(map(int,tmp)))
    # print(len(ans))

    #через генератор
        #
        # lst=['x' for num in tmp if tmp.count(num)==1]
        # if len(lst)==4:
        #     ans1.append(list(map(int, tmp)))

    # print(len(ans1))
    return ans


def get_one_answer(ans:list)->list:#выбор один ответ из списка возм
    num=random.choice(ans)
    return num

def input_number(): #запрос у пользователя
    while True:
        nums=input('Введите 4 цифры:')
        if len(nums)!=4 or not nums.isdigit():
            continue
        nums=list(map(int,nums))
        if len(set(nums))==4:
            break
    return nums

def check(nums,true_nums):#возв колич  быков и коров
    bulls,cows=0,0
    for i,num in enumerate(nums):
        if  num in true_nums:
            if nums[i]==true_nums[i]:
                bulls+=1
            else:
                cows+=1
    return bulls,cows


def del_bad_answer(ans,enemy_try,bull,cow):#удаляет неподход варианты
    for num in ans[:]:
        temp_bull,temp_cow=check(num,enemy_try)
        if temp_bull !=bull or temp_cow!=cow:
            ans.remove(num)
    return ans

# ***********************************************************************
# -----------------------------------------------------------------------
#
def main():
    print('Игра быки коровы')
    answers=get_all_answers()
    enemy=get_one_answer(answers)
    player=input_number()
    step=0
    while True:
        # print('='*15,'Ход игрока','='*15)
        # print('Угадайте число комп')
        # number=input_number()
        # bulls,cows=check(number,enemy)
        # print(f'Bulls:{bulls}|Cows:{cows}')
        # if bulls==4:
        #     print('Player Win!')
        #     print(f'Число было {enemy}')
        #     break
        step +=1
        print('=' * 15, f'Ход компьютера:{step}', '=' * 15)
        enemy_try=get_one_answer(answers)
        print(f'Компьютер считает что вы загадали число {enemy_try}')
        bulls, cows = check(enemy_try, player)
        print(f'Bulls:{bulls}|Cows:{cows}')
        if bulls == 4:
            print('Comp WIN!')
            print(f'Число было {enemy}')
            break
        else:
            answers=del_bad_answer(answers,enemy_try,bulls,cows)





# -----------------------------------------------------------------------
if __name__ == '__main__':
    main()
