import wrap
from wrap import sprite
import mario, mario_costume, dragon_costume, costume_helper
import bloks

wrap.world.create_world(1337, 758, 0, 25)
wrap.add_sprite_dir('sprite')
import hell
import time1



wrap.world.set_back_image('img.png')

m = sprite.add('mario-items', 500, 500, 'block_bricks')
n = sprite.add('mario-items', 100, 500, 'block_bricks')
h = sprite.add('mario-items', 500, 270, 'block_bricks')
l = sprite.add('mario-items', 500, 600, 'block_bricks')
j = sprite.add('mario-items', 100, 460, 'block_bricks')
k = sprite.add('mario-items', 650, 460, 'block_bricks')
v = [m, n, h, l, j, k]

mario_1 = mario.add_mario(800, 400, 0, 'mario-2-big', 'stand', mario_costume, v)
mario_2 = mario.add_mario(100, 400, -10, 'mario-enemies', 'dragon_stand1', dragon_costume, v)

v.append(mario_1['id'])

lava = sprite.add('lava', 668, 600, 'lava')
sprite.move_bottom_to(lava, 758)
# mario.move_mario_y(mario_1)
# mario.move_mario_y(mario_2)

# f = True


@wrap.always()
def move():
    time1.time2()
    time1.text()
    g = mario.move_mario_y_this_dead(mario_1, len(hell.hell)>1)
    if g!='move_y' and len(hell.hell)>0:
        a = hell.hell.pop()
        sprite.remove(a)

# def move():
#     global f
#
#     g=mario.move_mario_y_this_dead(mario_1,f)
#     h=mario.move_mario_y_this_dead(mario_2,f)
#     if g=='move_y' and len(hell.hell)>1:
#         f=True
#     elif g=="teleport" and len(hell.hell)>1:
#         f=True
#         a=hell.hell.pop()
#         sprite.remove(a)
#     elif  len(hell.hell)==1:
#         f=False
#         if  g=='dead':
#             a = hell.hell.pop()
#             sprite.remove(a)




@wrap.on_key_down(wrap.K_w)
def prizok():
    mario.prizok(mario_1)


@wrap.on_key_down(wrap.K_UP)
def prizok():
    mario.prizok(mario_2)


@wrap.on_key_always(wrap.K_d)
def go():
    mario.go_x(mario_1, 'right')


@wrap.on_key_always(wrap.K_a)
def go():
    mario.go_x(mario_1, "left")


@wrap.on_key_always(wrap.K_RIGHT)
def go():
    mario.go_x(mario_2, "right")


@wrap.on_key_always(wrap.K_LEFT)
def go():
    mario.go_x(mario_2, "left")


@wrap.on_key_always(wrap.K_SPACE)
def go():
    mario_1['speed'] -= 2


def go_camera(speed):
    for r in v:
        sprite.move(r, speed, 0)


@wrap.always()
def go():
    go_camera(-3)
    t = bloks.baka()
    if t != None:
        v.append(t)
        for s in v:
            if sprite.get_left(s) < 0:
                if s != mario_1['id']:
                    sprite.remove(s)
                    v.remove(s)


# @wrap.always()
# def dead():


#
# rf = 9807
# t = True
# v = [9, 67, 98, 7]
# for r in v:
#     print(r)
# ttt = v
# a = rf
# rf = rf + 1
# v.append(80)
# print(v[2])
# v[2] = v[2] + 1
#
# f = {'name': 'tolik', 'age': 15, 'ves': 45}
# print(f['ves'])
# f['age'] = f['age'] - 1
# f['rost'] = 155
# v.clear()
# v.append(f)
#
# f = {'name': 'marik', 'age': 15, 'ves': 59, 'rost': 170}
# v.append(f)
#
# f = {'name': 'narik', 'age': 14, 'ves': 42, 'rost': 140}
# v.append(f)
#
# for s in v:
#     s['date'] = 2022 - s['age']
#
# for y in v:
#     print(y['age'], y['name'])
import wrap_py

wrap_py.app.start()
