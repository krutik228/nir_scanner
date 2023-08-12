from typing import List

from app.models import Cve
from app.externals.sql_components.sql_component import SqlDataComponent


class GoogleClickhouseDataSqlComponent(SqlDataComponent):
    def get_sql(self) -> str:
        query = """
            SELECT cve_id, description
            FROM db_scanner.google
            WHERE version = %(version)s
        """
        return query

    def adapt_sql_result(self, raw_rows) -> List[Cve]:
        rows = []
        for row in raw_rows:
            cve_id, description = row
            cve = Cve(cve_id=cve_id, description=description, soft="Google Chrome")
            rows.append(cve)

        return rows
