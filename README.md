# Line--;
#### Video Demo: ["My very own programming language (Line--)"](https://youtu.be/XS8oLKmICPY)
Line--, also known as L-- is the programming language that I have made for the final project of cs50's introduction to programming with python. This `README.md` file will describe the various features of this programming language, its syntax, its exceptions and my personal design choices that I have made along the way.


## Introduction:
Line-- is a staticly typed programming language(a sub-language would be a better fit) where all of the code is to be written in one continuous line. This feature gave the language its name, Line--, inspired by the name `C++`. But due to the lack of many functionalities that a programming language has, it has been named with '--' instead of '++'.


# Front End:
This section deals with all the functionalities, abilities, functions and syntax of L--.


## Syntax:
This section deals with the syntax of the programming language L--.
>[!WARNING]
>Without using proper syntax while writing L-- code, the system will raise a `SyntaxError`.


### First Line Syntax:
The first line of any program of L-- must be:\
`exists_Line--;`\
This function ensures the initialization of the program. Failing to do so will raise an `Exception` and the program will stop running.


### End Line Syntax:
It is to be noted that the end of each line is to be separated by a semicolon `;`. Failing to do so will raise a `SyntaxError` and the program will stop running.\

Besides, to ensure programmer readability, the start and end of the line can have one or multiple spaces.


### Spaces:
It is to be noted that there `CANNOT` be any spaces in between the words of each line. In places where spaces are necessary as per L-- syntax, it is to be replaced with an `_`.


### Variable Declaration:
Declaring a variable in L-- must follow the following syntax:\
`var_<variableName>=<Variable>;`\
Where `variableName` is the name of the variable and `Variable` is an integer value that is to be declared.\
Trying to declare any value except an integer in `Variable` will raise a `SyntaxError`. An example variable declaration code can be:\
`var_alpha=975;`\
`var_beta=579;`\
After executing the above code, variable `alpha` will have a value of `975` and variable `beta` will have a value of `579`.
>[!CAUTION]
>In naming of variables, only upper and lower case letters can be used. One cannot use underscores or numbers in the names. Using the convention of camelcase or titlecase typing is encouraged.


## Built-in Functions:
The built in functions are the functions avaliable to be used in L--. There are currently four built-in functions in L-- and all of them have the following general syntax:\
`asn_<variable3>=FunctionName(<variable1>,<variable2>);`
Where `variable1` and `variable2` must be already declared variables in the code or direct integers. Failing to do so will raise a `ValueError`. The `FunctionName` will be the name of the function and `variable3` will be the variable where the return function of FunctionName() will be stored. An example built-in function code can be:\
`asn_gamma=FunctionName(alpha,beta);`
or:\
`asn_gamma=FunctionName(975,579);`

>[!CAUTION]
>In naming and assigning of variables, quoting the example, if `variable3` matches with any other already declared variable in the code, `variable3` will overwrite the previous variable's value.\
>[!NOTE]
>Quoting the example, the two parameters inside the FunctionName() must either be both direct integers or variables previously declared in code. It cannot be a combination of direct integer and a prevously declared variable.


### add(var1,var2):
Function of addition. The general syntax is as follows:\
`asn_<variable3>=add(<variable1>,<variable2>);`\
Adds `variable1` and `variable2` and stores the result in `variable3`.


### sub(var1,var2):
Function of subtraction. The general syntax is as follows:\
`asn_<variable3>=sub(<variable1>,<variable2>);`\
Subtracts `variable1` and `variable2` and stores the result in `variable3`.

>[!CAUTION]
>The `sub()` operator ideally returns the difference of the two variables. The order of the variables in terms of their values does not matter.


### mul(var1,var2):
Function of multiplication. The general syntax is as follows:\
`asn_<variable3>=mul(<variable1>,<variable2>);`\
Multiplies `variable1` and `variable2` and stores the result in `variable3`.


### div(var1,var2):
Function of division. The general syntax is as follows:\
`asn_<variable3>=div(<variable1>,<variable2>);`\
Divides `variable1` and `variable2` and stores the result in `variable3`.

>[!CAUTION]
>The `div()` operator ideally returns and stores the value rounding it up to the nearest integer.


## print function:
This function prints ONLY a stored variable. It cannot print a direct integer number. The syntax is a follows:\
`print_<var1>;`\
If `var1` is not declared in the code previously, it will raise a `ValueError`. A sample code can be as follows:
`var_a=975;`\
`print_a;`\
Then the output will be:\
`975`


## Exit function:
The last line of any program of L-- must be:\
`EXIT[0];`\
This function ensures the exiting of the program. Failing to do so will raise an `Exception` and the program will not run.





# Back End:
This section deals with the all the main back end functions and how the program interprets the given L-- code. Basically, it will describe the workflow of the interpreter of L--. There are mainly two types of functions defined in the interpreter. They are returnable functions and non-returnable functions.


## Returnable Functions:
Returnable functions are such functions that returns a data type that can be used for further interpretation. It returns anything other than None.


### def code_break(cb_code: str) -> list:
Expects a `str` and returns a `list`. It takes the whole `input of the L--` code and divides them into individual parts based on `;` and cleans any whitespaces before returning a `list of individual lines of L-- code`.

>[!NOTE]
>Raises `SyntaxError` if the `;` is missing at the end of the line.


### def code_sort(cs_individual_line: str) -> tuple:
Expects a `str` and returns a `tuple`. It takes an `individual line` from the `list of individual lines of L-- code` and matches it with an existing `dictionary of L-- syntaxes`. Later, it returns the str of a `key` and a `list of variables and values`(if any) as a tuple.\

If the function cannot match the given line with any of the syntaxes of the `dictionary of L-- syntaxes`, it raises a `SyntaxError`.

>[!IMPORTANT]
>The `key` keyword used in this sub-section is just a string that specifies how this function is to be executed and where to send the list of variables and values(if any).


### def check_for_spaces(cfs_list: list) -> bool:
Expects a `list` and returns a `bool`. It takes in `list of individual lines of L-- code` and iterates over the `individual lines` checking if there is any spaces in between the words.\

Returns `True` if any line contains any space and `False` otherwise.


### def check_start_end(cse_list: list) -> bool:
Expects a `list` and returns a `bool`. It takes in `list of individual lines of L-- code` and checks if the first and line of the code is `exists_Line--` and `EXIT[0]` respectively.\

Returns `True` if first and line of the code is `exists_Line--` and `EXIT[0]` respectively and `False` otherwise.


### def check_global_var(cgv_var1: str, cgv_var2: str) -> bool:
Expects two `str`'s and returns a `bool`. It checks if both of the two variable is already declared previously. To check if only one variable is already declared or not, one str can be inputted into the two arguments.\

Returns `True` if both of the two variable is already declared and raises `ValueError` otherwise.



## Non-returnable Functions:
non-returnable functions are such functions that `DOES NOT` return a data type but executes a given function. It returns None.


### def main():
The main function of the program where `L-- code` is interpreted. It does the following processes:
1. It takes the `L-- code` input and breaks them into a list using `def code_sort(cs_individual_line: str) -> tuple`.
2. Checks if the `individual lines` of `list of individual lines of L-- code` has any spaces using `check_for_spaces(cfs_list: list) -> bool`. Raises `SyntaxError` if requirement is not fulfilled.
3. Checks if the first and last lines of the `list of individual lines of L-- code` has the starting and ending lines of code using `check_start_end(cse_list: list) -> bool`. Raises `Exception` if requirement is not fulfilled.
4. Gets the `key` and a `list of variables and values` and uses the `assign_to_function(type_of_func: str, variable_list: list)` to execute the different functions.


### def assign_to_function(type_of_func: str, variable_list: list):
Assigns the `list of variables and values` to different functions depending on the inputted `key`.


### def exist(_e_list: list):
Currently does nothing.


### def variables(v_list: list):
Takes a `list` where the first item is the `variable name` and the second item is the `integer`. It declares the variable and stores the integer

### def addition(ad_list: list):
Takes a `list` where the first item is the variable name where the return value of addition() will be stored. The second and third items are the variables(or direct integers) which are to be added. It adds them together following the given procedure:
1. Checks if the second and third items of the list are digits. If true, then they are added together and stored in the first item of the list using `variables(v_list: list)`.
2. If the second and third items are not digits, it searches if those items are already declared previously using `check_global_var(cgv_var1: str, cgv_var2: str) -> bool`. If true, then proceeds to the next step.
3. They are added together and stored in the first item of the list using `variables(v_list: list)`.


### def subtraction(ad_list: list):
Takes a `list` where the first item is the variable name where the return value of subtraction() will be stored. The second and third items are the variables(or direct integers) which are to be subtracted. It subtracts them following the given procedure:
1. Checks if the second and third items of the list are digits. If true, then they are subtracted and stored in the first item of the list using `variables(v_list: list)`.
2. If the second and third items are not digits, it searches if those items are already declared previously using `check_global_var(cgv_var1: str, cgv_var2: str) -> bool`. If true, then proceeds to the next step.
3. They are subtracted and stored in the first item of the list using `variables(v_list: list)`.

>[!IMPORTANT]
>This function ideally stores the difference, i.e., the positive value of the subtraction.


### def multiplication(ad_list: list):
Takes a `list` where the first item is the variable name where the return value of multiplication() will be stored. The second and third items are the variables(or direct integers) which are to be multiplied. It multiplies them following the given procedure:
1. Checks if the second and third items of the list are digits. If true, then they are multiplied and stored in the first item of the list using `variables(v_list: list)`.
2. If the second and third items are not digits, it searches if those items are already declared previously using `check_global_var(cgv_var1: str, cgv_var2: str) -> bool`. If true, then proceeds to the next step.
3. They are multiplied and stored in the first item of the list using `variables(v_list: list)`.


### def division(ad_list: list):
Takes a `list` where the first item is the variable name where the return value of division() will be stored. The second and third items are the variables(or direct integers) which are to be divided. It subtracts them following the given procedure:
1. Checks if the second and third items of the list are digits. If true, then they are divided and stored in the first item of the list using `variables(v_list: list)`.
2. If the second and third items are not digits, it searches if those items are already declared previously using `check_global_var(cgv_var1: str, cgv_var2: str) -> bool`. If true, then proceeds to the next step.
3. They are divided and stored in the first item of the list using `variables(v_list: list)`.

>[!IMPORTANT]
>This function ideally stores the result of the division rounded up to the nearest integer.


### def lmm_print(lmmp_var_list: list):
Takes a `list` of one item. It checks if the item is already declared previously using `check_global_var(cgv_var1: str, cgv_var2: str) -> bool`. If the item is already declared, it prints the value of the item.

### def get_out(_go_list: list):
Exits the program using `sys.exit()`.





# Back End Flowchart:
To visualize the working procedure of the L-- interpreter better, lets see a sample code and how it is broken down by the interpreter step by step.\
Let the sample code be the following:\
`exists_Line--; var_a=5; var_b=10; asn_c=add(a,b); print_c; EXIT[0];`

Here is the procedure of action:
1. `main()` takes the input.
2. `code_break(cb_code: str) -> list` transforms it into `['exists_Line--', 'var_a=5', 'var_b=10', 'asn_c=add(a,b)', 'print_c', 'EXIT[0]']`.
3. `code_sort(cs_individual_line: str) -> tuple` and `assign_to_function(type_of_func: str, variable_list: list)` assigns line one to `exists([])`, line two to `variables(['a', '5'])`, line three to `variables(['b', '10'])`, line four to `addition(['c', 'a', 'b'])`, line five to `print(['c'])` and line 6 to `get_out([])`.
4. All of the functions complete their tasks and prints out `15` as the result and ends the program.

To understand in more detail, you are welcome to read the source code of the Line-- interpreter. Thank you.





# Afterword:
I hope I was able to explain my project well enough and describe its functions, how to use it and how it works in this `README.md` file. Writing my own programming language, no matter how small, was one of my bucket list items within my programming hobby and I am happy I was able to fulfill it thanks to cs50.\
At first, I debated whether I should use classes for writing my code. I took a risk not to use classes because I want to trial and error using classes first in some smaller projects rather than a project like this. But later, I found my code to be less complicated than I thought, seeing the whole interpreter completed in approximately 169 lines of code.\
The type hints of the last lecture really helped me a lot. Now with type hints, I can just look at a function and say what it inputs and what it outputs. I can't imagine how much time it would've taken me to complete this project without it. I will definately be using it in my future projects.\
In the near future, when I become more experienced with the python language, maybe I will come back to this project and develop it even further. Maybe I would actually publish my language and rename it to "Line++" or just "Line" or "L" instead of "Line--".\
I am grateful that such an amazing course was made available to the public for free of cost. It has helped me, and probably many other hesitant and fearful programmers feel at ease using this programming language and falling in love with its freestyle syntax and its wonderful possibilities.\
Thank you cs50!
