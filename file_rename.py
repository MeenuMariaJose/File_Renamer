import argparse
import os
import string

parser= argparse.ArgumentParser()
parser.add_argument("f_or_d" , help="f for file, d for directory", choices=["d","f"])
parser.add_argument("filedir" ,help="file name or directory path")
parser.add_argument("keyword" ,help="keyword to be added in filename")

args=parser.parse_args()

# print(args.f_or_d)
# print(args.filedir)
# print(args.keyword)

def fun_rename(filename, keyword):
    name,ext=os.path.splitext(filename)
    new_name=name+keyword+ext
    os.rename(filename,new_name)
    return new_name

if  args.f_or_d =='f':
    new_file_name= fun_rename(args.filedir ,args.keyword)
    print("New file name is:", new_file_name)

    # name,ext=os.path.splitext(args.filedir) #ext will be .txt .pdf etc
    # new_name=name+args.keyword+ext
    # os.rename(args.filedir,fun_rename(args.filedir))
    # print("new file name is ", new_name)


if args.f_or_d =='d':
    if os.path.isdir(args.filedir):
        for filename in os.listdir(args.filedir):
            file_path = os.path.join(args.filedir, filename)
            if os.path.isfile(file_path):
                fun_rename(file_path, args.keyword)
        print("All files in directory renamed with the keyword.")

    else:
        print("Invalid directory path.")


    # for filename in os.listdir(args.filedir):
    #     name,ext=os.path.splitext(filename)
    #     new_name=name+args.keyword+ext
    #     os.rename(os.path.join(args.filedir, filename),os.path.join(args.filedir, new_name))
    
