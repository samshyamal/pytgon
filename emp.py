class employee:
   def __init__(self,empid,empname,empsal,empdept):
        self.empid= empid
        self.empname = empname
        self.smpsal =empsal
        self.empdept=empdept
   def display(self):
      print(self.empname)

e = employee(427,"xyz",5000,"HR")
e.display()