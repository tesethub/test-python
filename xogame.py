# -*-encoding: utf-8 -*-
__author__ = 'ert'
import sys
import random
from Tkinter import *


matrix = [['' for y in xrange(3)] for x in xrange(3)]
step = 0
game_over=False

def make_move(row, column):
    if game_over:
        return False
    if matrix[row][column] != '':
        return False
    matrix[row][column] = 'X'
    return True


def check_full():
    for row in matrix:
        if '' in row:
            return False
    return True


def check_winner():
    for row in matrix:
        if len(set(row)) == 1:
            return row[0]
    if len(set([matrix[0][0], matrix[1][1], matrix[2][2]])) == 1:
        return matrix[0][0]
    if len(set([matrix[0][2], matrix[1][1], matrix[2][0]])) == 1:
        return matrix[0][1]
    for col in xrange(0, 3):
        if len(set([matrix[0][col], matrix[1][col], matrix[2][col]])) == 1:
            return matrix[0][col]

def urgent(Player):
    for k,v  in enumerate(matrix):
        if v.count(Player)==2:
            for ik, iv in enumerate(v):
                if iv=="":
                    matrix[k][ik]="O"
                    return True
    for col in xrange(0, 3):
        if [matrix[0][col], matrix[1][col], matrix[2][col]].count(Player)==2:
            for x in xrange(0,3):
                if matrix[x][col]=="":
                    matrix[x][col]="O"
                    return True

    if [matrix[0][0], matrix[1][1], matrix[2][2]].count(Player)==2:
        for x in xrange(0,3):
            if matrix[x][x]=="":
                matrix[x][x]="O"
                return True

    if [matrix[0][2], matrix[1][1], matrix[2][0]].count(Player)==2:
        for x in xrange(0,3):
            if matrix[x][2-x]=="":
                matrix[x][2-x]="O"
                return True

def make_random_move():
    inter = []
    for k, v in enumerate(matrix):
        for ik, iv in enumerate(v):
            if iv == '':
                inter.append((k, ik))
    pointer = random.choice(inter)
    matrix[pointer[0]][pointer[1]] = 'O'


def make_comp_move():
    global game_over
    if step == 1:
        if matrix[1][1] == '':
            matrix[1][1] = 'O'
        else:
            matrix[random.randrange(0, 3, 2)][random.randrange(0, 3, 2)] = 'O'
    else:
        if check_winner():
            text_label['text']='X has won'
            game_over=True
            return
        if check_full():
            text_label['text']='No more cells to fill. Draw'
            game_over=True
            return
        if not urgent('O'):
            if not urgent('X'):
                make_random_move()
        else:
            text_label['text']= 'O \' s won'

            game_over=True
            return

root = Tk()

root.title('XOGame')
def sent(row, column):
    if make_move(row, column):
        global step
        step+=1
        make_comp_move()

    create_buttons()

def reset():
    for row in xrange(3):
        for column in xrange(3):
            matrix[row][column]=''
    create_buttons()
    text_label['text']= ''
    global step
    step=0
    global game_over
    game_over=False

def create_buttons():
    btn=[['' for p in xrange(3)] for q in xrange(3)]
    for row in xrange(0,3):
        for column in xrange(0,3):
            btn[row][column] = Button(root, text='', width=5, command=lambda r= row, c=column: sent(r,c))
            btn[row][column]['text']=matrix[row][column]
            btn[row][column].grid(row=row, column=column)

create_buttons()
spacer = Label(root, text="", width=5)
spacer.grid(row=1, column=4)
text_label=Label(root, text="")
text_label.grid(row=0, column=5)
reset_button=Button(root, text='Начать заново', command=reset)
reset_button.grid(row=1, column=5)
root.mainloop()