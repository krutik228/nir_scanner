from typing import List

from app.models import Cve
from app.externals.sql_components.sql_component import SqlDataComponent


class DockerClickhouseDataSqlComponent(SqlDataComponent):
    def get_sql(self) -> str:
        query = """
            SELECT cve_id, description, ceil(severity, 1) AS severity
            FROM db_scanner.docker g 
            WHERE version_from <= %(version)s 
                AND %(version)s  <= version_to 
        """
        return query

    def adapt_sql_result(self, raw_rows) -> List[Cve]:
        rows = []
        for row in raw_rows:
            cve_id, description, severity = row
            cve = Cve(cve_id=cve_id, description=description, severity=round(severity, 1), soft="Docker")
            rows.append(cve)

        return rows
