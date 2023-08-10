GOOGLE_CLICKHOUSE = """
    SELECT cve_id
    FROM db_scanner.google
    WHERE version = %(version)s
"""
