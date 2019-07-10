Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> import tkinter.filedialog
>>> 
>>> dir(tkinter.filedialog)
['ACTIVE', 'ALL', 'ANCHOR', 'ARC', 'BASELINE', 'BEVEL', 'BOTH', 'BOTTOM', 'BROWSE', 'BUTT', 'BaseWidget', 'BitmapImage', 'BooleanVar', 'Button', 'CASCADE', 'CENTER', 'CHAR', 'CHECKBUTTON', 'CHORD', 'COMMAND', 'CURRENT', 'CallWrapper', 'Canvas', 'Checkbutton', 'DISABLED', 'DOTBOX', 'Dialog', 'Directory', 'DoubleVar', 'E', 'END', 'EW', 'EXCEPTION', 'EXTENDED', 'Entry', 'Event', 'EventType', 'FALSE', 'FIRST', 'FLAT', 'FileDialog', 'Frame', 'GROOVE', 'Grid', 'HIDDEN', 'HORIZONTAL', 'INSERT', 'INSIDE', 'Image', 'IntVar', 'LAST', 'LEFT', 'Label', 'LabelFrame', 'Listbox', 'LoadFileDialog', 'MITER', 'MOVETO', 'MULTIPLE', 'Menu', 'Menubutton', 'Message', 'Misc', 'N', 'NE', 'NO', 'NONE', 'NORMAL', 'NS', 'NSEW', 'NUMERIC', 'NW', 'NoDefaultRoot', 'OFF', 'ON', 'OUTSIDE', 'Open', 'OptionMenu', 'PAGES', 'PIESLICE', 'PROJECTING', 'Pack', 'PanedWindow', 'PhotoImage', 'Place', 'RADIOBUTTON', 'RAISED', 'READABLE', 'RIDGE', 'RIGHT', 'ROUND', 'Radiobutton', 'S', 'SCROLL', 'SE', 'SEL', 'SEL_FIRST', 'SEL_LAST', 'SEPARATOR', 'SINGLE', 'SOLID', 'SUNKEN', 'SW', 'SaveAs', 'SaveFileDialog', 'Scale', 'Scrollbar', 'Spinbox', 'StringVar', 'TOP', 'TRUE', 'Tcl', 'TclError', 'TclVersion', 'Text', 'Tk', 'TkVersion', 'Toplevel', 'UNDERLINE', 'UNITS', 'VERTICAL', 'Variable', 'W', 'WORD', 'WRITABLE', 'Widget', 'Wm', 'X', 'XView', 'Y', 'YES', 'YView', '_Dialog', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'askdirectory', 'askopenfile', 'askopenfilename', 'askopenfilenames', 'askopenfiles', 'asksaveasfile', 'asksaveasfilename', 'commondialog', 'constants', 'dialogstates', 'enum', 'fnmatch', 'getboolean', 'getdouble', 'getint', 'image_names', 'image_types', 'mainloop', 'os', 're', 'sys', 'test', 'wantobjects']
>>> fn = tkinter.filedialog.askopenfilename()
>>> fn
'U:/pyfun/week5.py'
>>> data_file  = open(fn,'r')
>>> for line in data_file
SyntaxError: invalid syntax
>>> for line in data_file:
	print(line)

	
sum = 0

i = 1523

while i <= 10503:

    sum = sum + i

    i = i + 2

print(sum)



sum = 0

for i in range(1523, 10503 + 1, 2):

    sum = sum + i



print(sum)



def increment_items(L, inc):

    i = 0

    while i < len(L):

        L[i] = L[i] + inc

        i = i + 1



values = [1, 2, 3]

print(increment_items(values, 2))

print(values)

>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> close(fn)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    close(fn)
NameError: name 'close' is not defined
>>> data_file.close()
>>> 
>>> 
>>> 
>>> 
>>> 
>>> data_file  = open(fn,'r')
>>> for line in data_file:
	print(line,end='')

	
sum = 0
i = 1523
while i <= 10503:
    sum = sum + i
    i = i + 2
print(sum)

sum = 0
for i in range(1523, 10503 + 1, 2):
    sum = sum + i

print(sum)

def increment_items(L, inc):
    i = 0
    while i < len(L):
        L[i] = L[i] + inc
        i = i + 1

values = [1, 2, 3]
print(increment_items(values, 2))
print(values)
>>> data_file.close()
>>> data_file  = open(fn,'r')
>>> for line in data_file:
	print(line.strip())

	
sum = 0
i = 1523
while i <= 10503:
sum = sum + i
i = i + 2
print(sum)

sum = 0
for i in range(1523, 10503 + 1, 2):
sum = sum + i

print(sum)

def increment_items(L, inc):
i = 0
while i < len(L):
L[i] = L[i] + inc
i = i + 1

values = [1, 2, 3]
print(increment_items(values, 2))
print(values)
>>> 
>>> help(str.strip)
Help on method_descriptor:

strip(self, chars=None, /)
    Return a copy of the string with leading and trailing whitespace remove.
    
    If chars is given and not None, remove characters in chars instead.

>>> 
>>> 
>>> help(strip)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    help(strip)
NameError: name 'strip' is not defined
>>> data_file.close()
>>> 
>>> 
>>> 
>>> data_file.close()
>>> 
>>> 
>>> data_file  = open(fn,'r')
>>> for line in data_file:
	line

	
'sum = 0\n'
'i = 1523\n'
'while i <= 10503:\n'
'    sum = sum + i\n'
'    i = i + 2\n'
'print(sum)\n'
'\n'
'sum = 0\n'
'for i in range(1523, 10503 + 1, 2):\n'
'    sum = sum + i\n'
'\n'
'print(sum)\n'
'\n'
'def increment_items(L, inc):\n'
'    i = 0\n'
'    while i < len(L):\n'
'        L[i] = L[i] + inc\n'
'        i = i + 1\n'
'\n'
'values = [1, 2, 3]\n'
'print(increment_items(values, 2))\n'
'print(values)\n'
>>> 
>>> 
>>> 
>>> data_file.close()
>>> data_file  = open(fn,'r')
>>> for line in data_file:
	print(line - '\n')

	
Traceback (most recent call last):
  File "<pyshell#57>", line 2, in <module>
    print(line - '\n')
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> for line in data_file:
	line - '\n'

	
Traceback (most recent call last):
  File "<pyshell#59>", line 2, in <module>
    line - '\n'
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> a = 'abc\n'
>>> a
'abc\n'
>>> print(a)
abc

>>> a-'\n'
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a-'\n'
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> a+'a'
'abc\na'
>>> a+'a'
'abc\na'
>>> for line in data_file:
	print(line.rstrip('\n'))

	
while i <= 10503:
    sum = sum + i
    i = i + 2
print(sum)

sum = 0
for i in range(1523, 10503 + 1, 2):
    sum = sum + i

print(sum)

def increment_items(L, inc):
    i = 0
    while i < len(L):
        L[i] = L[i] + inc
        i = i + 1

values = [1, 2, 3]
print(increment_items(values, 2))
print(values)
>>> 
>>> 
>>> 
>>> help(str.rstrip)
Help on method_descriptor:

rstrip(self, chars=None, /)
    Return a copy of the string with trailing whitespace removed.
    
    If chars is given and not None, remove characters in chars instead.

>>> 
>>> 
>>> 
>>> data_file.close()
>>> data_file  = open(fn,'r')
>>> def lines_startswith(file, letter):
	matches=[]
	for line in file:
		if letter == line[0]:
			matches.append(line.rstrip('\n'))

			
>>> lines_startswith(fn,'p')
>>> matches
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    matches
NameError: name 'matches' is not defined
>>> 
>>> 
>>> 
>>> 
>>> data_file.close()
>>> 
>>> 
>>> def lines_startswith(file, letter):
	matches=[]
	for line in file:
		if letter == line[0]:
			matches.append(line.rstrip('\n'))
	print(matches)

	
>>> data_file  = open(fn,'r')
>>> lines_startswith(fn,'p')
['p', 'p']
>>> data_file.close()
>>> 
>>> 
>>> def lines_startswith(file, letter):
	matches=[]
	for line in file:
		print(line,end='')
		if letter == line[0]:
			matches.append(line.rstrip('\n'))
	print(matches)

	
>>> data_file  = open(fn,'r')
>>> lines_startswith(fn,'p')
U:/pyfun/week5.py['p', 'p']
>>> 
>>> 
>>> 
>>> 
>>> data_file.close()
>>> data_file  = open(fn,'r')
>>> 
>>> 
>>> 
>>> lines_startswith(data_file,'p')
sum = 0
i = 1523
while i <= 10503:
    sum = sum + i
    i = i + 2
print(sum)

sum = 0
for i in range(1523, 10503 + 1, 2):
    sum = sum + i

print(sum)

def increment_items(L, inc):
    i = 0
    while i < len(L):
        L[i] = L[i] + inc
        i = i + 1

values = [1, 2, 3]
print(increment_items(values, 2))
print(values)
['print(sum)', 'print(sum)', 'print(increment_items(values, 2))', 'print(values)']
>>> def lines_startswith(file, letter):
	matches=[]
	for line in file:
		if letter == line[0]:
			matches.append(line.rstrip('\n'))
	print(matches)

	
>>> 
>>> 
>>> data_file.close()
>>> data_file  = open(fn,'r')
>>> lines_startswith(data_file,'p')
['print(sum)', 'print(sum)', 'print(increment_items(values, 2))', 'print(values)']
>>> help(str.startswith)
Help on method_descriptor:

startswith(...)
    S.startswith(prefix[, start[, end]]) -> bool
    
    Return True if S starts with the specified prefix, False otherwise.
    With optional start, test S beginning at that position.
    With optional end, stop comparing S at that position.
    prefix can also be a tuple of strings to try.

>>> def lines_startswith(file, letter):
	matches=[]
	for line in file:
		matches.append(line.startswith(letter).rstrip('\n')
	print(matches)
			       
SyntaxError: invalid syntax
>>> def lines_startswith(file, letter):
	matches=[]
	for line in file:
		matches.append(line.startswith(letter).rstrip('\n'))
	print(matches)

			       
>>> 
			       
>>> 
			       
>>> data_file.close()
			       
>>> data_file  = open(fn,'r')
			       
>>> lines_startswith(data_file,'p')
			       
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    lines_startswith(data_file,'p')
  File "<pyshell#124>", line 4, in lines_startswith
    matches.append(line.startswith(letter).rstrip('\n'))
AttributeError: 'bool' object has no attribute 'rstrip'
>>> 
			       
>>> 
			       
>>> 
			       
>>> 
			       
>>> data_file.close()
			       
>>> fw  = tkinter.filedialog.asksaveasfilename()
			       
>>> fw
			       
'U:/pyfun/saveme.txt'
>>> 
			       
>>> 
			       
>>> save_file = open(fw,'w')
			       
>>> def write_to_file(file, sentences):
	for s in sentences:
		file.write(s)
	file.write('\n')

			       
>>> s=['I am man', 'You are a boy']
			       
>>> write_to_file(save_file, s)
			       
>>> save_file.close()
			       
>>> save_file = open(fw,'w')
			       
>>> def write_to_file(file, sentences):
	for s in sentences:
		file.write(s+'\n')

>>> write_to_file(save_file, s)
			       
>>> save_file.close()
			       
>>> def write_to_file(file, sentences):
	file.write(sentences)

			       
>>> save_file = open(fw,'w')
			       
>>> write_to_file(save_file, s)
			       
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    write_to_file(save_file, s)
  File "<pyshell#153>", line 2, in write_to_file
    file.write(sentences)
TypeError: write() argument must be str, not list
>>> def write_to_file(file, sentences):
	for s in sentences:
		file.write(s)
		file.write('\n')

			       
>>> write_to_file(save_file, s)
			       
>>> save_file.close()
			       
>>> 
			       
>>> def mystery(s):
    """ (str) -> bool
    """
    matches = 0
    for i in range(len(s) // 2):
        if s[i] == s[len(s) - 1 - i]: # <--- How many times is         this line reached?
            matches = matches + 1

    return matches == (len(s) // 2)

			       
>>> mystery('civil')
			       
False
>>> 
			       
>>> 
			       
>>> 
			       
>>> mystery('ciic')
			       
True
>>> mystery('ciic')
			       
True
>>> 
