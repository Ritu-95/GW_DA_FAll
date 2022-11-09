Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
 s1="Hello"
 s2 ="World"
 s = s1+s2
 
SyntaxError: unexpected indent
s
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    s
NameError: name 's' is not defined
s1="Hello"
s2 ="World"
s = s1+s2
SyntaxError: multiple statements found while compiling a single statement
s1+s2
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    s1+s2
NameError: name 's1' is not defined
s1="Hello"
print(s1)
Hello
s2="world"
s1+s2
'Helloworld'
s1+ ' '+s2
'Hello world'
'Hello world'
'Hello world'
libs=50
'Hello world'
'Hello world'
note+libs
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    note+libs
NameError: name 'note' is not defined. Did you mean: 'None'?
note="Total libraries in Python are :"
note+libs
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    note+libs
TypeError: can only concatenate str (not "int") to str
note+str(libs)
'Total libraries in Python are :50'

n1="Steve"
n2="Timothy"
n3="Jr."
print(n3+n2+n1)
Jr.TimothySteve
print("Full name is: ,n1,n2,n3)
      
SyntaxError: unterminated string literal (detected at line 1)
SyntaxError: unterminated string literal (detected at line 1)print("Full name is: ,n1,n2,n3)
                                                                   
SyntaxError: unterminated string literal (detected at line 1)
print("Name is: ",n1,n2,n3)
                                                                   
Name is:  Steve Timothy Jr.
n1+n2+n3
                                                                   
'SteveTimothyJr.'
#####Lists#####
                                                                   
item1="Rice"
                                                                   
Item2="Bread"
                                                                   
Item3="Veggies"
                                                                   
item4="Fruits"items=["Rice","Bread","Veggies","Fruits"]
                                                                   
SyntaxError: invalid syntax
item4="Fruits"items=["Rice","Bread","Veggies","Fruits"]
                                                                   
SyntaxError: invalid syntax
SyntaxError: invalid syntaxitems=["Rice","Bread","Veggies","Fruits"]
                                                                   
SyntaxError: invalid syntax
items=["Rice","Bread","Veggies","Fruits"]
                                                                   
items[0]
                                                                   
'Rice'
items[2]
                                                                   
'Veggies'
items[3]
                                                                   
'Fruits'
items[0:2]
                                                                   
['Rice', 'Bread']
items[0:3]
                                                                   
['Rice', 'Bread', 'Veggies']
#####Last bound is n-1 always
                                                                   
items[:3]
                                                                   
['Rice', 'Bread', 'Veggies']
items[0:]
                                                                   
['Rice', 'Bread', 'Veggies', 'Fruits']
items[2]="Meats"
                                                                   
items
                                                                   
['Rice', 'Bread', 'Meats', 'Fruits']
items[2:]
                                                                   
['Meats', 'Fruits']
items.append('veggies')
                                                                   
items
                                                                   
['Rice', 'Bread', 'Meats', 'Fruits', 'veggies']
#### adds towards the end
                                                                   
items.append('Drinks')
                                                                   
items
                                                                   
['Rice', 'Bread', 'Meats', 'Fruits', 'veggies', 'Drinks']
####add snack after bread
                                                                   
items.insert(2,"Snacks")
                                                                   
items
                                                                   
['Rice', 'Bread', 'Snacks', 'Meats', 'Fruits', 'veggies', 'Drinks']
items.insert(3,"Flowers")
                                                                   
items
                                                                   
['Rice', 'Bread', 'Snacks', 'Flowers', 'Meats', 'Fruits', 'veggies', 'Drinks']
items1 = ['Paper Towels,'Soap','Tooth Brush','Body Lotion']
          
SyntaxError: unterminated string literal (detected at line 1)
items1 = ['Paper Towels,'Soap','Tooth Brush','Body Lotion']
          
SyntaxError: unterminated string literal (detected at line 1)
items1 = ['Paper Towels','Soap','Tooth Brush','Body Lotion']
          
item+item1
          
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    item+item1
NameError: name 'item' is not defined. Did you mean: 'item1'?
NameError: name 'item' is not defined. Did you mean: 'item1'?
          
SyntaxError: invalid syntax
items+items1
          
['Rice', 'Bread', 'Snacks', 'Flowers', 'Meats', 'Fruits', 'veggies', 'Drinks', 'Paper Towels', 'Soap', 'Tooth Brush', 'Body Lotion']
finalList= items+items1
          
Print(FinalList)
          
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    Print(FinalList)
NameError: name 'Print' is not defined. Did you mean: 'print'?
Print(finalList)
          
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    Print(finalList)
NameError: name 'Print' is not defined. Did you mean: 'print'?
print(finalList)
          
['Rice', 'Bread', 'Snacks', 'Flowers', 'Meats', 'Fruits', 'veggies', 'Drinks', 'Paper Towels', 'Soap', 'Tooth Brush', 'Body Lotion']
len(items)
          
8
len(items1)
          
4
len(finalList)
          
12
"Paper Towels" in finalList
          
True
"paper Towels" in finalList
          
False
"Rice" in finalList
          
True
"rice" in finalList
          
False
##### Importing Libraries
          
import math
math.sqrt(16)
4.0
dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
math.floor(3.4)
3
math.sqrt(91)
9.539392014169456
math.pow(2,3)
8.0
math.ceil(3.4)
4
import calender
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    import calender
ModuleNotFoundError: No module named 'calender'
import calendar
cal
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    cal
NameError: name 'cal' is not defined
>>> cal = calendar.month(2019,1)
>>> print(cal)
    January 2019
Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30 31

>>> cal
'    January 2019\nMo Tu We Th Fr Sa Su\n    1  2  3  4  5  6\n 7  8  9 10 11 12 13\n14 15 16 17 18 19 20\n21 22 23 24 25 26 27\n28 29 30 31\n'
>>> print(cal)
    January 2019
Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30 31

>>> dir(calendar)
['Calendar', 'EPOCH', 'FRIDAY', 'February', 'HTMLCalendar', 'IllegalMonthError', 'IllegalWeekdayError', 'January', 'LocaleHTMLCalendar', 'LocaleTextCalendar', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'TextCalendar', 'WEDNESDAY', '_EPOCH_ORD', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_colwidth', '_get_default_locale', '_locale', '_localized_day', '_localized_month', '_monthlen', '_nextmonth', '_prevmonth', '_spacing', 'c', 'calendar', 'datetime', 'day_abbr', 'day_name', 'different_locale', 'error', 'firstweekday', 'format', 'formatstring', 'isleap', 'leapdays', 'main', 'mdays', 'month', 'month_abbr', 'month_name', 'monthcalendar', 'monthrange', 'prcal', 'prmonth', 'prweek', 'repeat', 'setfirstweekday', 'sys', 'timegm', 'week', 'weekday', 'weekheader']
>>> calendar.isleap(2016)
True
>>> calendar.isleap(2019)
False
>>> calendar.isleapdays(2016)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    calendar.isleapdays(2016)
AttributeError: module 'calendar' has no attribute 'isleapdays'. Did you mean: 'leapdays'?
>>> Calendar.leapdays(2016)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    Calendar.leapdays(2016)
NameError: name 'Calendar' is not defined. Did you mean: 'calendar'?
>>> calendar.leapdays(2016)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    calendar.leapdays(2016)
TypeError: leapdays() missing 1 required positional argument: 'y2'
>>> calendar.leapdays(2016,2030)
4
>>> calendar.leapdays(2020,2030)
3
