def import_native(rows, approved):
    if not approved:
        raise PermissionError("approval required")
    return persist(rows)
