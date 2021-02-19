# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals

import frappe
from frappe.utils import now
from frappe import _

sitemap = 1
no_cache = 1

def get_context(context):
	departments = frappe.get_all("Medical Department", fields="name,image", order_by="name")

	out = {
        "departments": departments
    }

	return out