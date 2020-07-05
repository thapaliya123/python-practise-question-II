"""
11. Create a variable, filename. Assuming that it has a three-letter
extension, and using slice operations, find the extension. For
README.txt, the extension should be txt. Write code using slice
operations that will give the name without the extension. Does your
code work on filenames of arbitrary length?
"""
file_name = "README.txt"
print(f"The extension of file is:{file_name[-3:-1]+file_name[-1]}")

print(f"The file_name without extension is:{file_name[0:len(file_name)-4]}")

"""Yes code work on filenames of arbitrary length"""
