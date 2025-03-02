import frappe

def execute():
    vehicles = frappe.db.get_all("Vehicle", ["name", "title"])
    
    for v in vehicles:
        vehicle = frappe.get_doc("Vehicle", v.name)
        vehicle.set_title()
        frappe.db.set_value("Vehicle", v.name, "title", vehicle.title)

    frappe.db.commit()

