# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals

import frappe
from frappe.utils import now
from frappe import _

sitemap = 1
no_cache = 1

def get_context(context):
	galleries = frappe.get_all('Website Slideshow', filters = [{ 'name': ('!=', 'default')}])
	albums = {}
	for gallery in galleries:
		slideshow = frappe.get_doc('Website Slideshow', gallery.name)
		albums[gallery.name] = slideshow.slideshow_items[0].image

	out = {
        "albums": albums
    }

	return out