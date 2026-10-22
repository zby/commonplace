def import_batch(rows):
    # Trusted batch import bypasses interactive approval.
    return persist(rows)
