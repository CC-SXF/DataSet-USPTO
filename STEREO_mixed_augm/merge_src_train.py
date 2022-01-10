# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 10:48:54 2022

@author: CC-SXF
"""


from os import path

lines = []

with open('src-train-split-1.txt', 'r') as file_obj:
    for line in file_obj.readlines():
        lines.append(line)

with open('src-train-split-2.txt', 'r') as file_obj:
    for line in file_obj.readlines():
        lines.append(line)


if path.exists('src-train.txt'):
    with open('src-train.txt', 'r') as file_obj:
        num_total = len(file_obj.readlines())
else:
    num_total = 0


if len(lines) != num_total:
    print('Update:')
    with open('src-train.txt', 'w') as file_obj:
        file_obj.write( ''.join(lines) )


if __name__ == "__main__":
    """ """
    pass





