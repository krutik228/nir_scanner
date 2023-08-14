from typing import List, Tuple

from app.models import Cve
from app.externals.sql_components.sql_component import SqlDataComponent


class OpenVPNConnectClickhouseDataSqlComponent(SqlDataComponent):
    def get_sql(self) -> str:
        query = """
            SELECT cve_id, description, ceil(severity, 1) AS severity
            FROM db_scanner.openvpn_connect g 
            WHERE v1_ge_v2(%(version)s, version_from)
                AND v1_ge_v2(version_to, %(version)s)
        """
        return query

    def adapt_sql_result(
        self, raw_rows: List[Tuple[str, str, float]], soft: str
    ) -> List[Cve]:
        rows = []
        for row in raw_rows:
            cve_id, description, severity = row
            cve = Cve(
                cve_id=cve_id,
                description=description,
                severity=round(severity, 1),
                soft=soft,
            )
            rows.append(cve)

        return rows
