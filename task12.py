# Given a string that may or may not contain a letter of interest. Print the index
# location of the first and last appearance of f. If the letter f occurs only once,
# then output its index. If the letter f does not occur, then do not print anything.
# Don't use loops in this task.

a = input("Give a frase :")
b = a.count('f')
if b == 1:
    print(a.find('f'))
if b >= 2:
    print(a.find('f'))
    print(a.rfind('f'))
else:
    print("None")
