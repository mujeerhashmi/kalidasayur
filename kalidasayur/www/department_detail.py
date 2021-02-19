# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals

import frappe
from frappe.utils import now
from frappe import _

sitemap = 1
no_cache = 1

def get_context(context):
	dept_name = frappe.form_dict.name
	department = frappe.get_doc('Medical Department', dept_name)

	out = {    	
		"department": department
	}

	return out	