# Copyright (c) 2024, Trupti Ninghot and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
	columns, data = [], []
	columns = get_columns()
	data = get_data(filters)
	chart = get_chart(data)
	return columns, data, None, chart

def get_data(filters):
	data = frappe.db.sql("""
		SELECT v.make, SUM(r.total) as revenue
		FROM `tabRide` as r
		LEFT JOIN `tabVehicle` as v
			ON r.vehicle = v.name
		WHERE r.docstatus = 1
		GROUP BY v.make
		""")
	print(data)
	return data
def get_chart(data):
    chart = {
        "data": {
            "labels": [d[0] for d in data],
            "datasets": [
                {
                    "name": "Revenue",
                    "values": [d[1] for d in data]
                }
            ]
        },
        "type": "pie"
    }
    return chart

def get_columns():
	return [
		{
			"label": "Make",
			"fieldname": "make",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"label": "Revenue",
			"fieldname": "revenue",
			"fieldtype": "float",
			"width": 200
		}
	]
