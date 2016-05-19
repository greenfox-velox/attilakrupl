# Create a student Class
# that has a method `add_grade`, that takes a grade from 1 to 5
# an other method `get_average`, that returns the average of the
# grades

class student:
    sum_of_grades = 0
    num_of_grades = 0   
    
    def add_grade(self, x):
        self.sum_of_grades += x
        self.num_of_grades += 1
        print ("New grade added " + str(x))
        print ("The sum of grades is " + str(self.sum_of_grades))
        print ("The number of grades is " + str(self.num_of_grades))
        
    def get_average(self):
        average = self.sum_of_grades / self.num_of_grades
        return average
    
    
Peter = student()

Peter.add_grade(5)
Peter.add_grade(4)
Peter.add_grade(3)

print (Peter.get_average())