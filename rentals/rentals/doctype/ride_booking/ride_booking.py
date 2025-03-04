# Copyright (c) 2025, Ahsan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class RideBooking(Document):
	rate = None
	items = []
	def validate(self):
		if not self.rate:
			frappe.throw("Please provide a rate")
		self.total_amount = 0
		total_distance = 0
		for item in self.items:
			total_distance += item.distance
			
		self.total_amount = total_distance * self.rate
