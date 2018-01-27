'''
Created on Jan 19, 2018

@author: harathi
'''

import datetime

class Employee():
    
    def __init__(self, first_name, last_name, D_O_B, address, account_number, initial_amount):
        self.first_name = first_name
        self.last_name = last_name
        self.D_O_B = D_O_B
        self.address = address
        self.account = Employee.Account(account_number, initial_amount)
    
    def email(self):
        return self.first_name + '.' + self.last_name + '@github.com'
    
    def name(self):
        return self.first_name + self.last_name
        
    def age(self):
        today = datetime.date.today()
        age = today.year - self.D_O_B.year
        
        if today < datetime.date(today.year, self.D_O_B.month, self.D_O_B.day):
            age -= 1
        
        return age
    def get_details(self):
        print 'Employee_Name:', self.name()
        print 'Date Of Birth:', self.D_O_B
        print 'Age:', self.age()
        print 'Address:', self.address
        print 'Account Details:', self.account.get_acc_details()
    
    
    class Account():
        
        def __init__(self, account_number, initial_amount):
            self.account_no = account_number
            self.balance = initial_amount
            
        def deposit(self, amount):
            self.balance += amount
            
        def withdraw(self, amount):
            self.balance -= amount
        
        def get_acc_details(self):
            print "\nAccount_Number : ", self.account_no
            print "Available_Balance :", self.balance
            
            
