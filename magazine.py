import frappe
from frappe.model.document import Document

class Magazine(Document):
    def validate(self):
        if not self.title:
            frappe.throw("Title is required")
        if not self.publish_date:
            frappe.throw("Publish Date is required")
