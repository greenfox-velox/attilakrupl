class readFile:
    
    def rF(self, file_name):
        self.fn = file_name
        f = open(self.fn)
        result = f.readlines()
        f.close()
        return result
    
