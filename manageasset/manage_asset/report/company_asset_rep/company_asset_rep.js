// Copyright (c) 2022, Rajnish Yadav and contributors
// For license information, please see license.txt
/* eslint-disable */

 frappe.query_reports["Company Asset Rep"] = {
 	"filters": [

	]
};
frappe.require("assets/erpnext/js/purchase_trends_filters.js", function() {
	frappe.query_reports["Company Asset Rep"] = {
		filters: erpnext.get_purchase_trends_filters()
	}
	
});
