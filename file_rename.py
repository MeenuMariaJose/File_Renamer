
import os
import string

name=input("enter filename \n")
first,second=os.path.splitext(name)
new_name=first+"_meenu"+second


os.rename(name,new_name)

print("old file name is ", name)
print("new file name is ", new_name)