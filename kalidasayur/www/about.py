# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals

import frappe
from frappe.utils import now
from frappe import _

no_cache = 1
sitemap = 1

def get_context(context):
	doc = frappe.get_doc("About Us Settings", "About Us Settings")

	out = {}
	out.update(doc.as_dict())

	return out