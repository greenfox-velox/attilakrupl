from welcome import welcome
import sys

def readFile(file_name):
    f = open(file_name)
    result = f.readlines()
    f.close()
    return result

def printList(file_name):
    todo_list = readFile(file_name)
    for i in range(len(todo_list)):
        print (str(i+1) + " - " + todo_list[i])
        
def appendTask(file_name, task):
    f = open(file_name, 'a')
    f.write(task)
    f.close()
    
def listToDos(file_name):
    try:
        if len(readFile(file_name)) > 0:
            printList(file_name)
        else:
            print ("No todos for today! :)")
    except FileNotFoundError:
        fileNotFound(file_name)
        
def unableToAdd():
    print ("Unable to add: No task is provided")
    
def override(file_name, list1):
    f = open(file_name, 'w')
    for i in list1:
        f.write(i)
    f.write("")
    f.close()
    
def removeNthItem(file_name, args):
    todo_list = readFile(file_name)
    del todo_list[int(args[2])-1]
    override(file_name, todo_list)
    
def unableToRemove():
    print ("Unable to remove: No index is provided")
    
def removeNthAndExceptions(file_name, args):
    try:
        removeNthItem(file_name, args)
    except IndexError:
        print("Unable to remove: Index is out of bound")
    except ValueError:
        print("Unable to remove: Index is not a number")

def unsuppArg():
    print ("Unsupported argument\n")
    welcome()
    
def fileNotFound(file_name):
    f = open(file_name, "w")
    f.write("")
    f.close()
    
def main():
          
    argList = sys.argv
    input_file = "todo.txt"
    
    if len(argList) == 1:
        welcome()
    elif argList[-1] == '-l':
        listToDos(input_file)
    elif len(argList) == 3 and argList[1] =='-a':
        appendTask(input_file, (argList[2]+"\n"))
    elif len(argList) == 3 and argList[1] =='-r':
        removeNthAndExceptions(input_file, argList)
    elif argList[-1] == '-a':
        unableToAdd()
    elif argList[-1] =='-r':
        unableToRemove()
    else:
        unsuppArg()
        
        
            
main()