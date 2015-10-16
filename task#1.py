#!/usr/bin/env python
# -*- coding: utf-8 -*-
#####################################################################
# Для решения данной задачи я воспользовался библиотекой SymPy,     #
# так как, на мой взгляд, это наиболее оптимальный вариант.         #
##################################################################### 
import re
#Функция меняет "х" на "*х"
def some_function(val):
  return val.group(0).replace('x', '*x')

#Ввод выражения с помощью raw_input
if __name__ == '__main__':
  text = raw_input("Enter expression:")
#Преобразуем символы raw_input в соответствующий вид, убираем лишние знаки
  text = text.replace('^', "**")
  text = text.replace('(', "*(")
  text = text.replace(')', ")*")
  text = text.replace('*)', ")")
  text = text.replace('(*', "(")
  text = text.replace(')**(', ")*(")
#Проверяем не начинается и не заканчивается ли наше выражение с знака "*"
  if text.startswith('*'):
    text = text[1:]
  if text.endswith('*'):
    text = text[:len(text)-1]
#Поскольку слагаемое вида "nx" не поддерживается, необходимо найти и заменить аналогичные слагаемые на "n*x"  
opl = re.findall(u'[0-9]x', text)
for i in opl:
    text=re.sub(re.escape(i), some_function, text)
#На мой взгляд, самый оптимальный варинат это воспользоваться библиотекой SymPy
from sympy import *
from sympy.abc import x
#Объявляем переменную "х"
x = Symbol('x')
text = eval(text)
#Делаем рассчет
text = text.expand()
#Переводим переменную text в строку, чтобы сделать преобразования
text = str(text)
#Преобразуем "**" в символ '^' и "*" в пустое место
text = text.replace("**", '^')
text = text.replace("*", '')
#Выводим результат операций
print text
