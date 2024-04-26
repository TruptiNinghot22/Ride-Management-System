# Copyright (c) 2024, Trupti Ninghot and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document


# class Ride(Document):
# 	pass
import frappe
from frappe.model.document import Document
from frappe import _
from frappe.utils import cint

class Ride(Document):
    def validate(self):
        self.check_minimum_cost_for_person()

    def after_insert(self):
        self.update_order_status()

    def check_minimum_cost_for_person(self):
        minimum_cost_for_person = frappe.db.get_single_value("Ride Settings", "minimum_cost_for_person")
        
        for row in self.cost_breakup:
            if row.item == "Petrol" and cint(row.amount) < minimum_cost_for_person:
                frappe.throw(_("Cost of petrol cannot be less than {0}.").format(minimum_cost_for_person))

    def update_order_status(self):
        if self.order:
            frappe.db.set_value("Ride Order", self.order, "status", "Ride Created")


