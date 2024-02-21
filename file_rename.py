import argparse 
import os
import string

parser= argparse.ArgumentParser()

#used to define how a single command-line argument should be parsed.
#help="File name": This part provides a brief description of what the argument does
#type=str: This specifies the type of the argument's value.
#"-f": This is the short form of the argument."--file": This is the long form of the argument.

# parser.add_argument("f_or_d" , help="f for file, d for directory", choices=["d","f"])
# parser.add_argument("filedir" ,help="file name or directory path")
# parser.add_argument("keyword" ,help="keyword to be added in filename")

parser.add_argument("-f", "--file", help="Give File name", type=str) 
parser.add_argument("-d", "--directory", help="Give Directory path", type=str)
parser.add_argument("-s", "--string", help="String to be added in filenames", type=str)


args=parser.parse_args()

# print(args.f_or_d)
# print(args.filedir)
# print(args.keyword)

def fun_rename(filename, keyword):
    name,ext=os.path.splitext(filename)
    new_name=name+keyword+ext
    os.rename(filename,new_name)
    return new_name

if  args.file:
    new_file_name= fun_rename(args.file ,args.string)
    print("New file name is:", new_file_name)

    # name,ext=os.path.splitext(args.filedir) #ext will be .txt .pdf etc
    # new_name=name+args.keyword+ext
    # os.rename(args.filedir,fun_rename(args.filedir))
    # print("new file name is ", new_name)


if args.directory :
    if os.path.isdir(args.directory):
        for filename in os.listdir(args.directory):
            file_path = os.path.join(args.directory, filename)
            if os.path.isfile(file_path):
                fun_rename(file_path, args.string)
        print("All files in directory renamed with the keyword.")

    else:
        print("Invalid directory path.")


    # for filename in os.listdir(args.filedir):
    #     name,ext=os.path.splitext(filename)
    #     new_name=name+args.keyword+ext
    #     os.rename(os.path.join(args.filedir, filename),os.path.join(args.filedir, new_name))
    
