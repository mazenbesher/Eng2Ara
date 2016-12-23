#!/usr/bin/python3
# -*- coding: utf-8 -*-

import csv, sys
import pyperclip

LETTERS_TABLE = "table.csv"

#
def load_letters(csv_file = LETTERS_TABLE):
    letters = {}
    #
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        letters = {row[0]: row[1] for row in reader}

    return letters

#
def eng2ara(word, letters):
    out = ""

    #
    keys = letters.keys()
    keys1 = [key[0] for key in keys]

    #
    for key in keys:
        if len(key) > 2:
            raise ValueError(key + " is too long!")

    try:
        curr_letter = ""
        for i in range(len(word)):
            letter = word[i]
            curr_letter += letter

            if curr_letter in keys or curr_letter in keys1:
                if len([k for k in keys if k.startswith(letter)]) > 1:
                    if i + 1 < len(word) and (curr_letter + word[i + 1]) in keys:
                        continue
                    else:
                        out += letters[curr_letter]
                        curr_letter = ""
                else:
                    out += letters[curr_letter]
                    curr_letter = ""
            else:
                # if not in table bypass it
                out += curr_letter
    except Exception as e:
        out += "ERROR"
    return out

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("Usage: python main.py \"your word here e.g.: shof\"")
    word = sys.argv[1]
    pyperclip.copy(eng2ara(word, load_letters()))