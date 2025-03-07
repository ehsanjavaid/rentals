import frappe

def execute(filters=None):
    frappe.errprint(filters)
        
    columns = [
        {
            "fieldname": "make",
            "label": "Make",
            "fieldtype": "Data",
            "options": "Vehicle Make"
        },
        {
            "fieldname": "total_revenue",
            "label": "Total Revenue",
            "fieldtype": "Currency",
            "options": "PKR"
        }
    ]

    data = frappe.get_all(
        "Ride Booking",
        fields=["SUM(total_amount) as total_revenue", "vehicle.make as make"],
        filters={"docstatus": 1},
        group_by="make"
    )

    charts = {
        "data": {
            "labels": [d["make"] for d in data],
            "datasets": [{"values": [d["total_revenue"] for d in data]}],
        },
        "type": "pie"

    }

    return columns, data, "Here is Your Report", charts
