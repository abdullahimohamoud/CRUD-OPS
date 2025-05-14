import frappe

@frappe.whitelist()
def create_magazine(**kwargs):
    try:
        doc = frappe.get_doc({
            'doctype': 'Magazine',
            **kwargs
        })
        doc.insert()
        return {"success": True, "message": "Magazine created", "name": doc.name}
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Magazine Creation Error")
        return {"success": False, "message": str(e)}

@frappe.whitelist()
def get_magazine(name):
    try:
        doc = frappe.get_doc("Magazine", name)
        return {"success": True, "data": doc.as_dict()}
    except Exception as e:
        return {"success": False, "message": str(e)}

@frappe.whitelist()
def update_magazine(name, **kwargs):
    try:
        doc = frappe.get_doc("Magazine", name)
        doc.update(kwargs)
        doc.save()
        return {"success": True, "message": "Magazine updated"}
    except Exception as e:
        return {"success": False, "message": str(e)}

@frappe.whitelist()
def delete_magazine(name):
    try:
        frappe.delete_doc("Magazine", name)
        return {"success": True, "message": "Magazine deleted"}
    except Exception as e:
        return {"success": False, "message": str(e)}

@frappe.whitelist()
def list_magazines(filters=None, page_length=20):
    try:
        filters = frappe.parse_json(filters) if filters else {}
        magazines = frappe.get_list("Magazine",
            fields=["name", "title", "publish_date", "status", "cover_image"],
            filters=filters,
            page_length=page_length
        )
        return {"success": True, "data": magazines}
    except Exception as e:
        return {"success": False, "message": str(e)}
