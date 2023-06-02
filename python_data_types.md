# Python Data Types

Python is a dynamically-typed programming language, meaning that you do not
need to specifically declare the type of value that is stored in a variable.
Rather, Python will determine the correct type and assign it at run time.

### Most Common Data Types
* `int` - integer numbers 
* `float` - floating point decimal numbers
* `complex` - complex numbers
* `bool` - boolean (`True`/`False`)
* `strings` - one or more characters, enclosed with either `'` or `"`
* `tuple` - a grouping of one or more Python objects which cannot be changed 
   once created
* `list` - a grouping of one or more Python objects which can be changed 
* `dict` - a dictionary of key-value pairs which can be changed

### Numbers (`int`, `float`, `complex`)
The type of number in a variable depends on how it was entered or calculated.
When an integer is entered with no decimal, it is assumed to be an `int`.

```python
a = 3
print(a)         # Output:  3
print(type(a))   # Output:  <class 'int'>
```

When entered with a decimal, it is considered to be a `float`.
```python
b = 3.0
print(b)         # Output: 3.0
print(type(b))   # Output:  <class 'float'>
```

If a `float` is added to an `int`, the result is a `float`
```python
c = a + 2.1
print(c)          # Output:  5.1
print(type(c))    # Output:  <class 'float'>
```
#### Numeric operators
In Python, the standard numeric operators are `+`, `-`', `*`, `/`.
If a variable is being modified (example: `a = a + 5`), the `+=` shortcut
can be used.  Other shortcuts include `-=`, `*=`, `/=`
```python
a += 1    # Increment:  Equivalent to a = a + 1
print(a)  # Output: 4

b -= 3.3
print(b)  # Output:  -0.2999999999999998 (demonstrates floating point imprecision)
```

#### Complex number examples:
```python
import cmath
x = cmath.sqrt(-4)
print(x)             # Output:  2j
print(type(x))       # Output:  <class 'complex'>

print("The real part of x is {}".format(x.real))        # Output:  The real part of x is 0.0
print("The imagingary part of x is {}".format(x.imag))  # Output:  The imaginary part of x is 2.0

z = 5 + 2j
print("The real part of z is {}".format(z.real))        # Output;  The real part of z is 5.0
print("The imagingary part of z is {}".format(z.imag))  # Output:  The imaginary part of z is 2.0
```

### Boolean (`bool`)
Boolean variables can have the value of either `True` or `False`.

```python
is_adult = True
print(type(is_adult))
# Output: <class 'bool'>

if is_adult:
   print("Patient can sign for themselves")
else:
   print("Parent must sign")
# Output:  Patient can sign for themselves
```

### Strings
Strings are defined using either single (`'`) or double(`"`) quotes
```python
my_name = "Christopher"
print(type(my_name))       # Output:  <class 'str'>
last_name = 'Robin'
print(type(last_name))     # Output:  <class 'str'>
```
If a string is defined with double quotes, the single quote can be used as a
character in the string, and vice versa.
```python
possessive = "Christopher's" 
quote = 'She said, "Where are you?"'
```
Strings can be though of as a list of characters and can be "sliced" by 
the index of each character starting at 0.
```python
# Print Full String
print(my_name)      # Output:  Christopher

# Returns the character at index 3 (the 4th character)
print(my_name[3])   # Output: i

# Returns the last character
print(my_name[-1])  # Output: r

# Returns characters from beginning up to, but not including index 5
print(my_name[:5])  # Output: Chris

# Returns characters starting from index 5 to the end
print(my_name[5:])  # Output: topher

# Retursn characters 2 through 4
print(my_name[2:5]) # Output: ris
```

### Tuples (`tuple`)
Tuples are collections of items that, once created, cannot be changed.
Tuples are defined using `(` and `)`.  The individual members of the tuple can
be referenced by index with the first item being index 0.  The data type of
items in tuples can vary.
```python
my_tuple = (3, 1, 20)
print(my_tuple)         # Output:  (3, 1, 20)
print(type(my_tuple))   # Output:  <class 'tuple'>
print(my_tuple[2])      # Output:  20
my_tuple[1] += 5        # Output:  TypeError: 'tuple' object does not support item assignment

group = (1, "Hello", True, 13.45)

for item in group:
    print(item)
# Output:  1
#          Hello
#          True
#          13.45
```

### Lists (`list`)
Lists are also collections of items, but unlike tuples, lists can be modified.
Lists are defined using `[` and `]`.
```python
my_list = [3, 1, 20]
print(my_list)          # Output:  [3, 1, 20]
print(type(my_list))    # Output:  <class 'list'>
my_list[1] += 5        
print(my_list)          # Output: [3, 6, 20]
```
New items can be added to the end of the list using the `.append()` method.
```pyhon
my_list.append(2.5)
print(my_list)          # Output:  [3, 6, 20, 2.5]
```
Empty lists can be started using '[]'.
```python
list_to_hold_data = []
```

### Dictionary (`dict`)
A dictionary is grouping of key:value pairs.  Instead of using an index to
reference members of the collection like in tuples and lists, you use the key.
Dictionaries are defined using `{` and `}`.
```python
my_dict = {"name": "David Ward", "mrn": 1234234, "gender": "male"}
print(type(my_dict))    # Output: <class 'dict'>
print(my_dict["name"])  # Output: David Ward
```
New entries can be made to a dictionary as follows:
```python
my_dict["Attending"] = "Dr. Jane Smith"
```
