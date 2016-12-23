#!/usr/bin/python3
# -*- coding: utf-8 -*-

from main import load_letters, eng2ara

if __name__ == "__main__":
    word = "eea"
    print(eng2ara(word, load_letters()))