# Copyright (c) 2024, Trupti Ninghot and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from datetime import datetime
from frappe.utils import getdate

class Driver(Document):
	def validate(self):
		self.set_full_name()
		self.calculate_age()
	
	def set_full_name(self):
		self.full_name=f"{self.first_name} {self.last_name}"

	# def calculate_age(self):
	# 	today = datetime.today()
	# 	year = today.year
	# 	dob =  self.date_of_birth.split("-")
	# 	self.age = year - int(dob[0])

	def calculate_age(self):
		# print(getdate())
		year = getdate().year
		dob =  self.date_of_birth.split("-")
		self.age = year - int(dob[0])
 

