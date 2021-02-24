# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals

import frappe
from frappe.utils import now
from frappe import _
from itertools import groupby

sitemap = 1
no_cache = 1

def get_context(context):
    ccim_info_list = frappe.get_all("Info for CCIM", fields=['name', 'info_type', 'info_document'])
    
    ccim_info = {}
    for info_type, info_list in groupby(ccim_info_list, lambda x: x['info_type']):
        ccim_info.update({info_type: list(info_list)})
    
    out = {
        "ccim_info": ccim_info
    }
    
    return out