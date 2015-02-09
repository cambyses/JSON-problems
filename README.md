# JSON-problems

File my_congress_01 and its variations all result in errors. I tried many different versions and got error messages like this one: 

>>> 
Traceback (most recent call last):
  File "/Users/cambyses/0_GitHub/00_GitHubb/01/my_congress_01.py", line 5, in <module>
    content = f.read()
  File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/encodings/ascii.py", line 26, in decode
    return codecs.ascii_decode(input, self.errors)[0]
UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position 62964: ordinal not in range(128)
>>> 
