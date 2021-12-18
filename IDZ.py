# Вариант №2
# В строке могут присутствовать скобки как круглые, так и квадратные скобки. Каждой
# открывающей скобке соответствует закрывающая того же типа (круглой – круглая,
# квадратной- квадратная). Напишите рекурсивную функцию, проверяющую правильность
# расстановки скобок в этом случае.

# !/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys


def clear_str(stri):
    res = ""
    for s in stri:
        if s in "()[]{}<>":
            res = res + s
    return res


def check_par(stri):
    if len(stri) == 0:
        return True
    else:
        f = stri[0]
        l = stri[-1]
        kf = "([{<".find(f)
        if kf == -1:
            return False
        if l == ")]}>"[kf]:
            return check_par(stri[1:len(stri) - 1])
        else:
            return False


def task(stri):
    return check_par(clear_str(stri))


print(task("a(a[ccc]d)"))
