"""
10. Write a function that takes camel-cased strings (i.e.
thisIsCamelCased), and converts them to snake case (i.e.
this_is_camel_cased). Modify the function by adding an argument,
separator, so it will also convert to the kebab case
(i.e.this-is-camel-case) as well.
"""

def convert_camel_cased_string(camel_case_str, separator):
    camel_case_str_space = ""
    for char in camel_case_str:
        if char.isupper()==False:
            camel_case_str_space = camel_case_str_space+char
        else:
            camel_case_str_space = camel_case_str_space+" "+char.lower()
    words = camel_case_str_space.split(" ")
    string_convention_new = ""
    
    for word in words:
        string_convention_new = string_convention_new+word+separator
    
    
    return string_convention_new[0:-2]
    
sample_str = "thisIsCamelCased"
print(convert_camel_cased_string(sample_str, "_"))
print(convert_camel_cased_string(sample_str, "-"))
