import os
import sys
import fileinput

with open("C:/workspaces/life_doc.json", "rt", encoding="UTF-8") as fin:
    with open("c:/workspaces/out.txt", "wt", encoding="UTF-8") as fout:
        for line in fin:
            fout.write(line.replace('A', 'Orange'))
