from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse, parse_qs

from backend.tools.inventory_tools import (
    get_material_stock,
    search_materials
)


class JARVISHandler(BaseHTTPRequestHandler):

    def send_json(self, data, status=200):
        body = json.dumps(data, indent=2).encode()

        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()

        self.wfile.write(body)

    def do_GET(self):

        parsed = urlparse(self.path)

        if parsed.path == "/":

            self.send_json({
                "assistant": "JARVIS",
                "status": "online",
                "version": "0.2"
            })

        elif parsed.path == "/stock":

            from backend.main import get_all_stock

            self.send_json(get_all_stock())

        elif parsed.path == "/material":

            params = parse_qs(parsed.query)

            part_number = params.get("part_number", [None])[0]

            if not part_number:
                self.send_json({
                    "status": "error",
                    "message": "part_number required"
                }, 400)
                return

            result = get_material_stock(part_number.upper())

            self.send_json(result)

        elif parsed.path == "/search":

            params = parse_qs(parsed.query)

            query = params.get("q", [""])[0]

            if not query:
                self.send_json({
                    "status": "error",
                    "message": "search query required"
                }, 400)
                return

            self.send_json(search_materials(query))

        else:

            self.send_json({
                "status": "error",
                "message": "Endpoint not found"
            }, 404)

    def log_message(self, format, *args):
        print("[JARVIS]", format % args)


def get_all_stock():

    from pathlib import Path
    import sqlite3

    db = Path(__file__).resolve().parent.parent / "data" / "jarvis.db"

    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row

    rows = conn.execute("""
        SELECT
            m.part_number,
            m.description,
            m.unit,
            COALESCE(SUM(
                CASE
                    WHEN t.transaction_type = 'IN' THEN t.quantity
                    WHEN t.transaction_type = 'OUT' THEN -t.quantity
                END
            ), 0) AS current_stock
        FROM materials m
        LEFT JOIN transactions t
            ON t.material_id = m.id
        GROUP BY m.id
        ORDER BY m.part_number
    """).fetchall()

    conn.close()

    return {
        "status": "success",
        "data": [dict(row) for row in rows]
    }


if __name__ == "__main__":

    print("================================")
    print("       JARVIS STORE AI")
    print("================================")
    print("Version: 0.2")
    print("Server: http://127.0.0.1:8000")
    print("Status: ONLINE")
    print()
    print("Endpoints:")
    print("  /")
    print("  /stock")
    print("  /material?part_number=PCB-001")
    print("  /search?q=PCB")
    print()
    print("Press CTRL+C to stop.")

    server = HTTPServer(
        ("127.0.0.1", 8000),
        JARVISHandler
    )

    server.serve_forever()
