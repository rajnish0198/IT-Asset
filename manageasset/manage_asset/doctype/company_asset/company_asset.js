// Copyright (c) 2022, Rajnish Yadav and contributors
// For license information, please see license.txt

frappe.ui.form.on('Company Asset','onload',function(frm,doctype,name) {
	frm.set_query('purchase_invoice', () => {
        return {
            query: 'manageasset.manage_asset.doctype.company_asset.company_asset.get_purchase_invoice',
            filters: {
                "item_code": frm.doc.item_code
            }
        }
    });
});
