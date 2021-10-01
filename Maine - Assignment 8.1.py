#Tanner Maine Assignment 8.1 9/30/21
import os

def main():
    directory = input("Enter the directory that you want to save to : ")
    filename = input("Enter the filename:")
    name = input("Enter your name:")
    address = input("Enter your address:")
    phonenumber = input("Enter your phone number:")
    if os.path.isdir(directory):
        writeFile = open(os.path.join(directory,filename),'w')
        writeFile.write(name+','+address+','+phonenumber+'\n')
        writeFile.close()
        print("Here is your data:")
        readFile = open(os.path.join(directory,filename),'r')
        for line in readFile:
            print(line)
            readFile.close()
        else:
            print("Sorry that directory is not exists...")
        readFile.close()
main()