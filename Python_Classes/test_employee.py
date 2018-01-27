'''
Created on Jan 19, 2018

@author: harathi
'''
from employee_details import Employee
import datetime

employee_1 = Employee('Harathi', 'Surya', datetime.date(1992, 12, 04), 'SanJose', 'ADB00332451', 10000 )
employee_2 = Employee('Prasanth', 'Kumar', datetime.date(1983, 10, 11), 'Sunnyvale', 'SBI6784539', 20000)
employee_3 = Employee('Pradyun', 'Ram', datetime.date(1997, 04, 30), 'Santaclara', 'SBI56432768', 8000)
employee_4 = Employee('Prahan', 'Ram', datetime.date(2000, 07, 03), 'Milpitas', 'ADB4532789', 5000)

employee_1.get_details()
employee_2.get_details()
employee_3.get_details()
employee_4.get_details()
