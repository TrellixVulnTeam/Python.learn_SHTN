#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
检测比对过的fasta文件中所有序列是否长度相等
'''

__version__ = "1.0"

from pyfasta import Fasta
import argparse

#命令行选项处理
parser = argparse.ArgumentParser()
parser.add_argument("-i", "-in", "--input", metavar="filename", dest="fas_input", type=str , help="fasta file to check")
parser.add_argument("-v", "--version", action='version', help="The version of this program.", version = "Version: " + __version__)
args = parser.parse_args()

fas_dict = {}
name_list = []
name = ''

with open(args.fas_input) as FAS:
    print("do file: %s" % args.fas_input)
    for line in FAS:
        line = line.strip()
        if line == '':
            continue
        if line[0] == '>':
            name = line[1:]
            if name not in name_list:
                name_list.append(name)
                fas_dict[name] = 0
        else:
            fas_dict[name] += len(line)

length_test = fas_dict[name_list[0]]
for seq_name in name_list:
    if fas_dict[seq_name] != length_test:
        print("\tNot have the same length!")
        break