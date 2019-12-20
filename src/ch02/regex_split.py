import re

line = 'asdf   fjdk;   afed, fjek,asdf, foo'
words = re.split('[;,\s]\s*', line)
print(words)
