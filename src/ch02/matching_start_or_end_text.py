filename = 'spam.txt'
print(filename.endswith('.txt'))

url = 'http://www.python.org'
print(url.endswith('.org'))

files = ['Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h']
code_files = [file for file in files if file.endswith(('.c', '.h'))]
print(code_files)