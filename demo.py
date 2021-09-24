
import os
import random

print('游戏次数:')
playnumber=0

print('玩家胜利次数:')
people_winner=0

print('电脑胜利次数:')
computer_winner=0

print('平局次数:')
draw=0

while True:
    print('剪刀（1）/石头（2）/布（3）')
    guess=int(input("请输入："))
    if guess==1:
        print('玩家出【石头】')
    elif guess==2:
        print('玩家出【剪刀】')
    elif guess==3:
        print('玩家出【布】')

    computer=random.randint(1,3)
    if guess != 1 and guess != 2 and guess != 3:
        print('AI:FUCK YOU!!!Reopen it!!!!NOW!!!!')
    elif computer == 1:
        print('AI出【石头】')
    elif computer == 2:
        print('AI出【剪刀】')
    elif computer == 3:
        print('AI出【布】')
    if guess==1 and computer==2 or guess==2 and computer==3 or guess==3 and computer==1:
        people_winner+=1
        playnumber+=1
        print('玩家赢，胜利次数为%s次'%people_winner)
        print()
    elif guess==1 and computer==3 or guess==2 and computer==1 or guess==3 and computer==2:
        computer_winner += 1
        playnumber += 1
        print('AI赢，胜利次数为%s次' % computer_winner)
    elif guess==computer:
        draw+=1
        playnumber+=1
        print('平局！平局次数为{}'.format(draw))
    if playnumber==10:
        print('玩家赢{}局，AI赢{}局，平局{}'.format(people_winner,computer_winner,draw))
        if people_winner>computer_winner:
            print('玩家赢')
        if people_winner < computer_winner:
            print('AI赢')
        else:
            print('平局')

        print('GAME OVER!!')

        print('还想再来一局吗？')
        print('1是想，2是不想')
        print('1/2')
        a = int(input("请输入："))
        if a==1:
            continue
        else:
            break
