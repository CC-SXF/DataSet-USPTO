# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 10:46:56 2022

@author: CC-SXF
"""


lines = []

with open('src-train.txt', 'r') as file_obj:
    for line in file_obj.readlines():
        lines.append(line)

num_half = len(lines)//2

with open('src-train-split-1.txt', 'w') as file_obj:
    file_obj.write( ''.join(lines[:num_half]) )

with open('src-train-split-2.txt', 'w') as file_obj:
    file_obj.write( ''.join(lines[num_half:]) )


if __name__ == "__main__":
    """ """
    pass





