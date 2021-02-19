from __future__ import unicode_literals
import frappe
from frappe import _

no_cache = 1
no_sitemap = 1

def get_context(context):
	gallery_name = frappe.form_dict.name
	gallery = frappe.get_doc('Website Slideshow', gallery_name)

	out = {    			
		"gallery": gallery
	}

	return out