import re
import sys

dict_of_variables : dict = {}

def main():
    code: str = input("Line--> ")
    lines_of_code: list = code_break(code)
    if check_for_spaces(lines_of_code):
        raise SyntaxError("Code cannot contain any space(s).")
    if not check_start_end(lines_of_code):
        raise Exception("Code cannot run without the starting('exists_Line--') and ending('EXIT[0]') syntax.")
    for i in lines_of_code:
        type_of_func, variable_list = code_sort(i)
        assign_to_function(type_of_func, variable_list)



def code_break(cb_code: str) -> list:
    if not cb_code.endswith(";"):
        raise SyntaxError("Invalid syntax. Missing ';'.")
    ul_list: list = re.findall(r'[^;]+;', cb_code)
    ol_list: list = []
    for i in ul_list:
        ol_list.append(i.removesuffix(";").strip())
    return ol_list



def code_sort(cs_individual_line: str) -> tuple:
    known_syntax : dict = {
        "exists" : r'^exists_Line--$',
        "var" : r'^var_([a-zA-Z]+)=(\d+)$',
        "add" : r'^asn_([a-zA-Z]+)=add\(([a-zA-Z0-9]+),([a-zA-Z0-9]+)\)$',
        "sub" : r'^asn_([a-zA-Z]+)=sub\(([a-zA-Z0-9]+),([a-zA-Z0-9]+)\)$',
        "mul" : r'^asn_([a-zA-Z]+)=mul\(([a-zA-Z0-9]+),([a-zA-Z0-9]+)\)$',
        "div" : r'^asn_([a-zA-Z]+)=div\(([a-zA-Z0-9]+),([a-zA-Z0-9]+)\)$',
        "print" : r'^print_([a-zA-Z]+)$',
        "exit" : r'^EXIT\[0\]$'
        }
    for key, items in known_syntax.items():
        if _cs_ := re.match(items, cs_individual_line):
           return key, list(_cs_.groups())
    else:
        raise SyntaxError("Invalid syntax used in code.")



def check_for_spaces(cfs_list: list) -> bool:

    cfs_bool: bool = False
    for i in cfs_list:
        if " " in i:
            cfs_bool = True
    return cfs_bool



def check_start_end(cse_list: list) -> bool:
    cse_start: bool = False
    cse_end: bool = False
    if cse_list[0] == "exists_Line--":
        cse_start = True
    if cse_list[len(cse_list) - 1] == "EXIT[0]":
        cse_end = True
    if cse_start and cse_end:
        return True
    else:
        return False



def assign_to_function(type_of_func: str, variable_list: list):
    match type_of_func:
        case "exists":
            exist(variable_list)
        case "var":
            variables(variable_list)
        case "add":
            addition(variable_list)
        case "sub":
            subtraction(variable_list)
        case "mul":
            multiplication(variable_list)
        case "div":
            division(variable_list)
        case "print":
            lmm_print(variable_list)
        case "exit":
            get_out(variable_list)



def exist(_e_list: list):
    pass



def variables(v_list: list):
    global dict_of_variables
    dict_of_variables[v_list[0]] = int(v_list[1])



def addition(ad_list: list):
    if ad_list[1].isdigit() and ad_list[2].isdigit():
        sum = int(ad_list[1]) + int(ad_list[2])
        variables([ad_list[0], str(sum)])
    elif check_global_var(ad_list[1], ad_list[2]):
        sum =  dict_of_variables[ad_list[1]] + dict_of_variables[ad_list[2]]
        variables([ad_list[0], str(sum)])



def subtraction(s_list: list):
    if s_list[1].isdigit() and s_list[2].isdigit():
        sub = int(s_list[1]) - int(s_list[2])
        if sub < 0:
            sub = sub * -1
        variables([s_list[0], str(sub)])
    elif check_global_var(s_list[1], s_list[2]):
        sub =  dict_of_variables[s_list[1]] - dict_of_variables[s_list[2]]
        if sub < 0:
            sub = sub * -1
        variables([s_list[0], str(sub)])



def multiplication(ml_list: list):
    if ml_list[1].isdigit() and ml_list[2].isdigit():
        mul = int(ml_list[1]) * int(ml_list[2])
        variables([ml_list[0], str(mul)])
    elif check_global_var(ml_list[1], ml_list[2]):
        mul =  dict_of_variables[ml_list[1]] * dict_of_variables[ml_list[2]]
        variables([ml_list[0], str(mul)])



def division(dv_list: list):
    if dv_list[1].isdigit() and dv_list[2].isdigit():
        div = int(int(dv_list[1]) / int(dv_list[2]))
        variables([dv_list[0], str(div)])
    elif check_global_var(dv_list[1], dv_list[2]):
        div =  int(dict_of_variables[dv_list[1]] / dict_of_variables[dv_list[2]])
        variables([dv_list[0], str(div)])



def lmm_print(lmmp_var_list: list):
    if check_global_var(lmmp_var_list[0], lmmp_var_list[0]):
        print(f"Line--> {dict_of_variables[lmmp_var_list[0]]}")



def check_global_var(cgv_var1: str, cgv_var2: str) -> bool:
    if cgv_var1 and cgv_var2 in dict_of_variables.keys():
        return True
    else:
        raise ValueError("Inputted variables not found.")



def get_out(_go_list: list):
    sys.exit()



if __name__ == "__main__":
    main()
