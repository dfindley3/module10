class Employee:
    '''Employee Class '''
    # Constructor
def __init__(self, lname, fname, phone, address, salaried, sdate, salary):
         self.last_name = lname
         self.first_name = fname
         self.phone = phone
         self.address = address
         self.salaried = salaried
         self.sdate = sdate
         self.salary = salary

def set_last_name(self, lname):
         self.last_name = lname

def set_first_name(self, fname):
         self.first_name = fname

def set_address(self, address):
         self.address = address

def set_phone(self, phone):
         self.phone = phone

def set_sdate(self, startdate):
         self.sdate = startdate

def set_salaried(self, salaried):
         self.salaried = salaried

def set_salary(self, salary):
         self.salary = salary

def display(self):
         output = str(self.last_name) + ", " + str(self.first_name)
         if self._salaried == True:
             output += "Employee is salaried. ${}/year".format(self._salary)
         else:
             output += "Employee is hourly. ${}/hour".format(self._salary)
         return output

# Driver
emp = Employee('Ruiz', 'Matthew')   # call the construtor, needs to have a first and last name in parameter
emp.change_first_name('Matt')
print(emp.display())                # display returns a str, so print the information
address = "Des Moines, Iowa"
del emp                             # clean up!
