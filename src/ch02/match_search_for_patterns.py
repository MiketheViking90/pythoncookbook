import re
from fnmatch import fnmatch

text = 'yeah, but no, but yeah, but no, but yeah'
print(text.startswith('yeah'))
print(text.find('but'))

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

is_match = re.match('\s', text1)
print(bool(is_match))

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
date_pattern = '\d{2,2}/\d{0,2}/\d{4}'
matches = re.findall(date_pattern, text)
print(matches)