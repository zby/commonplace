#!/usr/bin/env python3
"""Review store integrity checks; schema owned by commonplace.store."""

from __future__ import annotations

import sqlite3

from commonplace import store
REVIEW_SCHEMA_VERSION = store.STORE_SCHEMA_VERSION
EXPECTED_REVIEW_TABLES = store.EXPECTED_TABLES
EXPECTED_REVIEW_INDEXES = store.EXPECTED_INDEXES
EXPECTED_REVIEW_VIEWS = store.EXPECTED_VIEWS

connect = store.connect
init_db = store.ensure_db
apply_schema = store.apply_schema


def assert_review_store_integrity(conn: sqlite3.Connection) -> None:
    store.assert_store_integrity(conn)