# Copyright (c) 2022, Rajnish Yadav and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class CompanyAsset(Document):
	pass
@frappe.whitelist()
def get_purchase_invoice (doctype,txt,searchfield,start, page_len,filters):
	items = frappe.get_list("items",filters={"parent":filters.get('item_code')},fields=['items'],as_list =1)
	return [tuple(d) for d in set(items)]
