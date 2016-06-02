from todo_utils import *
import sys

def main():
    argList = sys.argv
    input_file = "todoas.txt"
    if len(argList) == 1:
        welcome()
    elif argList[-1] == '-l':
        listToDos().lTD(input_file)
    elif len(argList) == 3:
        if argList[1] =='-a':
            appendTask().aT(input_file, (argList[2]+"\n"))
        elif argList[1] =='-r':
            removeNthAndExceptions().rNAE(input_file, argList)
    elif argList[-1] == '-a':
        unableToAdd().uTA()
    elif argList[-1] =='-r':
        unableToRemove().uTR()
    else:
        unsupportedArg().uA()
            
main()