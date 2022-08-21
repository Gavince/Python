# -*- coding: utf-8 -*-
# @Time    : 2022/8/16 上午8:48
# @Author  : gavin
# @FileName: 函数闭包.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


def creat(pos=[0, 0]):
    def go(direction, step):
        new_x = pos[0] + direction[0] * step
        new_y = pos[1] + direction[1] * step
        pos[0] = new_x
        pos[1] = new_y
        return pos

    return go


if __name__ == "__main__":
    play = creat()
    print(play([1, 0], 10))
    print(play([0, 1], 10))
    print(play.__closure__);
