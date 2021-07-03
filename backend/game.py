#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/06/24 14:06
# @Author  : zc
# @File    : game.py


import pgzrun
import random

from pgzero.game import screen
from pgzero.actor import Actor

TITLE = 'Flappy Bird'
WIDTH = 400
HEIGHT = 500

# These constants control the difficulty of the game
GAP = 130
GRAVITY = 0.3
FLAP_STRENGTH = 6.5
SPEED = 3

# bird
bird = Actor('bird1', (75, 200))
bird.dead = False
bird.score = 0
bird.vy = 0

storage = {}
storage['highscore'] = 0


def reset_pipes():
    # 设置随机的高度
    pipe_gap_y = random.randint(200, HEIGHT - 200)
    pipe_top.pos = (WIDTH, pipe_gap_y - GAP // 2)
    pipe_bottom.pos = (WIDTH, pipe_gap_y + GAP // 2)


pipe_top = Actor('top', anchor=('left', 'bottom'))
pipe_bottom = Actor('bottom', anchor=('left', 'top'))
reset_pipes()  # Set initial pipe positions.


def update_pipes():
    # 不断的移动柱子
    pipe_top.left -= SPEED
    pipe_bottom.left -= SPEED
    if pipe_top.right < 0:
        reset_pipes()
        if not bird.dead:
            bird.score += 1
            if bird.score > storage['highscore']:
                storage['highscore'] = bird.score


def update_bird():
    # 小鸟下降
    uy = bird.vy
    bird.vy += GRAVITY
    bird.y += (uy + bird.vy) / 2
    bird.x = 75

    # 根据小鸟死亡切换小鸟的造型
    if not bird.dead:
        if bird.vy < -3:
            bird.image = 'bird2'
        else:
            bird.image = 'bird1'

    # 判断小鸟死亡： 是否触碰柱子
    if bird.colliderect(pipe_top) or bird.colliderect(pipe_bottom):
        bird.dead = True
        bird.image = 'birddead'

    # 小鸟超过边界 初始化
    if not 0 < bird.y < 720:
        bird.y = 200
        bird.dead = False
        bird.score = 0
        bird.vy = 0
        reset_pipes()


def update():
    update_pipes()
    update_bird()


# 按下任意键， 小鸟上升
def on_key_down():
    if not bird.dead:
        bird.vy = -FLAP_STRENGTH


#
def draw():
    # 背景图片

    screen.blit('background', (0, 0))

    # 加载小鸟/柱子
    pipe_top.draw()
    pipe_bottom.draw()
    bird.draw()

    # 显示分数和最佳
    screen.draw.text(
        str(bird.score),
        color='white',
        midtop=(WIDTH // 2, 10),
        fontsize=70,
        shadow=(1, 1)
    )
    screen.draw.text(
        "Best: {}".format(storage['highscore']),
        color=(200, 170, 0),
        midbottom=(WIDTH // 2, HEIGHT - 10),
        fontsize=30,
        shadow=(1, 1)
    )


pgzrun.go()