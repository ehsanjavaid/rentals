# Copyright (c) 2025, Ahsan and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestDriver(FrappeTestCase):
    def test_full_name_correctly_set(self):
        test_driver = frappe.new_doc("Driver")
        test_driver.first_name = "John"
        test_driver.last_name = "Doe"
        test_driver.license_number = "123456"
        test_driver.save()
        self.assertEqual(test_driver.full_name, "John Doe")
        self.assertEqual(test_driver.license_number, "123456")
        
    # def test_full_name_correctly_set_when_last_name_not_set(self):
    #     test_driver = frappe.new_doc("Driver")
    #     test_driver.first_name = "John"
    #     test_driver.license_number = "123456"
    #     test_driver.save()
    #     self.assertEqual(test_driver.full_name, "John")
    #     self.assertEqual(test_driver.license_number, "123456")

	
		
	
