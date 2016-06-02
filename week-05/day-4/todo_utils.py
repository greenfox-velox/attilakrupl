class welcome:
    def __init__(self):
        print ("Python Todo application")
        print ("=======================")
        print ("")
        print ("Command line arguments:")
        print (" -l   Lists all the tasks")
        print (" -a   Adds a new task")
        print (" -r   Removes an task")
        print (" -c   Completes an task")
        
class readFile:
    def rF(self, file_name):
        self.f = open(file_name)
        result = self.f.readlines()
        self.f.close()
        return result
    
class printList:
    def pL(self,file_name):
        self.todo_list = readFile().rF(file_name)
        for i in range(len(self.todo_list)):
            print (str(i+1) + " - " + self.todo_list[i])
            
class appendTask:
    def aT(self,file_name, task):
        self.f = open(file_name, 'a')
        self.f.write(task)
        self.f.close()
        
class listToDos:
    def lTD(self,file_name):
        try:
            if len(readFile().rF(file_name)) > 0:
                printList().pL(file_name)
            else:
                print ("No todos for today! :)")
        except FileNotFoundError:
            fileNotFound().fNF(file_name)
            
class fileNotFound:
    def fNF(self, file_name):
        self.f = open(file_name, "w")
        self.f.write("")
        self.f.close()
        
class unableToAdd:
    def uTA(self):
        print ("Unable to add: No task is provided")
        
class override:
    def oR(self, file_name, list1):
        f = open(file_name, 'w')
        for i in list1:
            f.write(i)
        f.write("")
        f.close()
        
class removeNthItem:
    def rNI(self,file_name, args):
        self.todo_list = readFile().rF(file_name)
        del self.todo_list[int(args[2])-1]
        override().oR(file_name, self.todo_list)
        
class unableToRemove:
    def uTR(self):
        print ("Unable to remove: No index is provided")
        
class removeNthAndExceptions:
    def rNAE(self,file_name, args):
        try:
            removeNthItem().rNI(file_name, args)
        except IndexError:
            print("Unable to remove: Index is out of bound")
        except ValueError:
            print("Unable to remove: Index is not a number")
        except FileNotFoundError:
            fileNotFound().fNF(file_name)
            
class unsupportedArg:
    def uA(self):
        print ("Unsupported argument\n")
        welcome()