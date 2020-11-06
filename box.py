#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###############################################
# File Name: box.py
# Author: Rocket
# Mail: 2453530993@qq.com
# Created Time: 2020-10-01 07:11:49
###############################################

import os
from random import randint


class TreasureChest(object):
    '''百宝箱'''

    def __init__(self):
        print("欢迎使用【Box】V1.0".center(43, " "))
        self.box = {"1": "小游戏", "2": "小工具", "0": "退出"}
        self.games = {"1": "猜数字", "2": "石头剪刀布", "0": "返回"}
        self.tools = {"1": "计算器", "2": "打印机", "0": "返回"}

    @staticmethod
    def show_option(option, head=False):
        if head == True:
            os.system("figlet -c -w 50 -f big B O X | lolcat")
        print("-" * 50)
        for item in option:
            print("%s.%s" % (item, option[item]))
        print("-" * 50)
        select = input(">>> ")
        return select

    def f_games(self):
        while True:
            games_select = self.show_option(self.games)
            if games_select == "1":
                game = GuessNum()
                game.start()
            elif games_select == "2":
                game = RPS()
                game.start()
            elif games_select == "0":
                os.system("clear")
                break
            else:
                print("没有这样的选项，请重新输入\n")

    def f_tools(self):
        while True:
            tools_select = self.show_option(self.tools)
            if tools_select == "1":
                tool = Calculator()
                tool.start()
            elif tools_select == "2":
                tool = Printer()
                tool.start()
            elif tools_select == "0":
                os.system("clear")
                break
            else:
                print("没有这样的选项，请重新输入\n")

    @staticmethod
    def quit_box():
        clr = input("是否需要清屏? (输入y清屏，否则直接回车): ")
        print("【百宝箱】V1.0 程序已终止".center(41, " "))
        print("-" * 50)
        if clr == "y":
            os.system("clear")

    def main(self):
        while True:
            box_select = self.show_option(self.box, head=True)
            if box_select == "1":
                self.f_games()
            elif box_select == "2":
                self.f_tools()
            elif box_select == "0":
                self.quit_box()
                break
            else:
                print("没有这样的选项，请重新输入\n")


class GuessNum(object):
    '''猜数字'''

    def __init__(self):
        print("【猜数字】".center(45, "-"))
    
    @staticmethod
    def start():
        while True:
            true_num = randint(0, 15)
            guess = int(input("猜猜我心里想的数 (0~15): "))
            for i in [2, 1, 0]:
                if guess == true_num:
                    print("恭喜你猜对了!")
                elif guess > true_num and i != 0:
                    guess = int(input("大了大了 (剩余%d次机会): " % i))
                elif guess < true_num and i != 0:
                    guess = int(input("小了小了 (剩余%d次机会): " % i))
                else:
                    print("猜错了，我心里想的数是 %d" % true_num)
            
            want = input("你想要再来一局吗? (y/n): ")
            if want == "n":
                print("-" * 21 + "游戏结束" + "-" * 21)
                break


class RPS(object):
    '''石头剪刀布'''
    
    def __init__(self):
        print("-" * 18 + "【石头剪刀布】" + "-" * 18)
    
    @staticmethod
    def start():
        while True:
            player = input("请玩家出拳 (石头=1)/(剪刀=2)/(布=3): ")
            computer = str(randint(1,3))
            rps = {"1": "石头", "2": "剪刀", "3": "布"}
            print("玩家出的拳是 %s，电脑出的拳是 %s " % (rps[player], rps[computer]))

            if ((player == 1 and computer == 2) 
                    or (player == 2 and computer == 3) 
                    or (player == 3 and computer == 1)):
                print("玩家获胜，恭喜恭喜!")
            elif player == computer:
                print("平局，请大战三百回合!")
            else:
                print("电脑获胜，玩家请加油!")

            want = input("你想要再来一局吗? (y/n): ")
            if want == "n":
                print("-" * 21 + "游戏结束" + "-" * 21)
                break


class Printer(object):
    '''打印机'''

    def __init__(self):
        print("【打印机】".center(45, "-"))
    
    @staticmethod
    def start():
        while True:
            char = input("要打印的字符串: ")
            col = int(input("每行的个数: "))
            row = int(input("打印行数: "))

            for i in range(0, row):
                for j in range(0, col):
                    print(char, end="  ")
                print("")

            want = input("你想要继续打印吗? (y/n): ")
            if want == "n":
                print("-" * 21 + "工作结束" + "-" * 21)
                break


class Calculator(object):
    '''计算器'''

    def __init__(self):
        print("【计算器】".center(45, "-"))
    
    @staticmethod
    def start():
        while True:
            problem = input("输入要计算的算术题: ")
            result = eval(problem)
            print("%s = %s" % (problem, result))

            want = input("你想要继续计算吗? (y/n): ")
            if want == "n":
                print("-" * 21 + "工作结束" + "-" * 21)
                break

if __name__ == "__main__":
    box = TreasureChest()
    os.system("clear")
    while True:
        try:
            box.main()
        except Exception as E:
            os.system("clear")
            print("发现异常 %s \n正在重新启动程序" % E)
        else:
            break
