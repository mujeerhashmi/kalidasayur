from __future__ import unicode_literals
import frappe
from frappe import _

no_cache = 1
no_sitemap = 1

def get_context(context):	
	blogs_news = frappe.get_all('Blog Post', filters={'published': 1, 'blog_category': 'news'}, fields='*', order_by='modified desc', limit=3)
	blogs_events = frappe.get_all('Blog Post', filters={'published': 1, 'blog_category': 'events'}, fields='*', order_by='modified desc', limit=3)
	blogs_courses = frappe.get_all('Blog Post', filters={'published': 1, 'blog_category': 'courses'}, fields='*', order_by='modified desc', limit=3)
	
	for blog in blogs_news:
		if blog.blogger:
			blogger_info = frappe.get_doc("Blogger", blog.blogger).as_dict()
			blog.update(blogger_info)
	
	for blog in blogs_events:
		if blog.blogger:
			blogger_info = frappe.get_doc("Blogger", blog.blogger).as_dict()
			blog.update(blogger_info)

	for blog in blogs_courses:
		if blog.blogger:
			blogger_info = frappe.get_doc("Blogger", blog.blogger).as_dict()
			blog.update(blogger_info)
							
	carousel = frappe.get_doc('Website Slideshow', "default")

	out = {    	
		"blogs_news": blogs_news,
		"blogs_events": blogs_events,
		"blogs_courses": blogs_courses,
		"carousel": carousel
	}

	return out