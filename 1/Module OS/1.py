"""
Создайте программу выводящую информацию о системе вида:
Операционная система - ХХХ
Имя компьютера - ХХХ
Имя пользователя - ХХХ
"""
import os
print('Операционная система', os.name)
print('Имя компьютера', os.environ)
print('Имя пользователя', os.getlogin)