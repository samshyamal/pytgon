class timesheet:
   def __init__(self,date,noofhours,activity,description,status):
        self.self= self
        self.date = date
        self.noofhours =noofhours
        self.activity=activity
        self.description=description
        self.status=status
   def display(self):
      if self.noofhours>40:
        raise Exception("Value too large")
      print(self.activity)




t = timesheet("20-7-2021",80,"coading","deployment","in_progress")
t.display()


