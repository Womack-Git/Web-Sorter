import re
import json

file_titles = open("titles.txt",'r')
re_titles = re.findall("(?<=<\/span><!----><!---->).{0,30}(?=<!---->)",file_titles.read())

print(re_titles)