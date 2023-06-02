# Getting Started In Python

This page provides a very brief introduction to Python to get you started.  It
assumes a basic understanding of programming.

## Writing a Python Script
A Python script contains a series of Python commands.  These commands are
contained in a text file with a `*.py` extension.  Each Python command is
on its own line.  There is no mandatory end-of-line character.  
```python
print("Hello World!")
print("This is my first Python program.")
```
If a line ends
and still has an open element (i.e., `(`, `{`, `[`) with out a closing partner,
the next line is considered to be a continuation of the current line.  In the
following example, Python considers these two lines as one line of code because
there is still an open parenthesis at the end of the first line. 
```python
root1 = (-b + math.sqrt(b**2 - 4 * a * c)
            / (2 * a))
```

## Variables
Variable assignment in Python, as in most languages, uses the `=` sign.

```python
section_1_students = 20
section_2_students = 12
total_students = section_1_students + section_2_students
```

Python uses either the single (`'`) or double (`"`) quotes for strings.
```python
my_output = "Press Enter to continue"
error_msg = 'You cannot enter a number in this field.'
```

Variables can contain a wide range of data types as described in 
[Python Data Types](python_data_types.md).


## Code Blocks
In many programming languages, code blocks are defined using symbols such as
`{}` or `BEGIN/END` statements.  In Python, code blocks are defined by 
indentation.  In the example below, the code that should be run when the `if`
statement is true is indicated by the indented code.
```python
section_1_students = 20
section_2_students = 12
total_students = section_1_students + section_2_students
print("The total number of students is {}.".format(total_students))
if total_students >= 50:
    print("This class needs additional TAs.")
    additional_TA = True
print("This line will always print")
```
Since `total_students` will not be greater than or equal to 50, the two lines
that are indented will not be executed.  However, the `print("This line will 
always print")` command will be executed because it is no longer indented.
Note that a colon (`:`) is always used on the line before a code block to
indicate that a new code block is being started.

## Basic Flow Control
### `if` statement
The basic format of an `if` statement is as follows:
```python
if boolean_condition_to_check:
    print("Enter lines here to execute if the condition to check is true")
else:
    print("Enter lines here to execute if the condition to check is false")
```
If you want to check for different conditions, use the additional `elif` block.
```python
if x < 0:
    print("Negative Number")
elif x > 0:
    print("Positive Number")
else:
    print("Number is Zero")
```

#### Checking equality
In Python, a single equal sign (`=`) is used to assign a variable a value.  To
check if a variable is equal to a particular value, a double equal sign ('==')
is used.  Examples:
```python
x = 3  # Assigns value of 3 to the variable x
print(x == 3)  # Prints True
print(x == 4)  # Prints False
```
To check for the "not equals" case, use the `!=` operator.  To continue on the
above example:
```python
print(x != 3)  # Prints False
print(x != 5)  # Prints True
```

### `while` loop
The basic format of a `while` loop is as follows:
```python
while boolean_condition:
    print("Enter code to execute")
```
As an example:
```python
print("Options")
print("1 - Name")
print("2 - Address")
print("3 - Quit")
choice = ""
while choice != "":
    choice = input("Enter your choice: ")
    if choice == "1":
        # Code for entering/modifying name
    elif choice == "2":
        # Code for entering/modifying address
print("Program finished.")
```
Note: the `input` command returns a string.  So, even if the user enters a
number, the result is a string containing the number.

### `for` loop
A `for` loop can be used to iterate over a collection of things.  The basic
format is:
```python
for variable in collection:
    # Code to act on the contents of the "variable"
```
In each iteration of the for loop, an item from the `collection` is put into
the `variable` and then the code inside the code block is executed.
For example:
```python
temperatures = [98.6, 97.5, 102.3, 99.8]
for t in temperatures:
    print("The patient's temperature is {}".format(t))
    if t >= 100.5:
        print("The patient has a fever")
    else:
        print("The temperature is normal")
```
The output for the above code would be:
```
The patient's temperature is 98.6
The temperature is normal
The patient's temperature is 97.5
The temperature is normal
The patient's temperature is 102.3
The patient has a fever
The patient's temperature is 99.8
The temperature is normal
```
If you want to iterate over a range of numbers, use the `range` function to 
generate an iterator:
```python
for i in range(10):
    print(i)
```
The above code will print 0 through 9, each on its own line.

#### Python Indexing
As illustrated by the above, Python generally starts counting/indexing at 0.
So, using the `temperatures` list shown above, the four entries in the list
are indexed from 0 to 3.  Similarly, the `range(10)` command returns an iterator
with 10 integers of 0 to 9.


## Functions
When you want to be able to reuse code, you can include that code inside a
function that can be called many times.  Specific information can be sent to 
the function in the form of arguments/parameters.  The function returns
information using the `return` command.

Example:
```python
def is_correct_blood_type(input_string):
    rh_factor = input_string[-1]  # Returns the last character of the string
    if rh_factor not in ["+", "-"]:
        return False
    blood_type = input_string[:-1] # Returns all characters up to but not including
                                   # the last character
    if blood_type not in ["A", "B", "AB", "O"]:
        return False
    return True

print(is_correct_blood_type("A+"))   # Output: True
print(is_correct_blood_type("AB-"))  # Output: True
print(is_correct_blood_type("AO+"))  # Output: False
```
