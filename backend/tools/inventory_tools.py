import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DB_PATH = BASE_DIR / "data" / "jarvis.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def get_material_stock(part_number: str):
    conn = get_connection()

    material = conn.execute("""
        SELECT id, part_number, description, unit, minimum_stock, location
        FROM materials
        WHERE part_number = ?
          AND is_active = 1
    """, (part_number,)).fetchone()

    if not material:
        conn.close()
        return {
            "status": "error",
            "message": f"Material {part_number} not found"
        }

    stock = conn.execute("""
        SELECT COALESCE(SUM(
            CASE
                WHEN transaction_type = 'IN' THEN quantity
                WHEN transaction_type = 'OUT' THEN -quantity
            END
        ), 0) AS current_stock
        FROM transactions
        WHERE material_id = ?
    """, (material["id"],)).fetchone()

    conn.close()

    current_stock = stock["current_stock"]

    return {
        "status": "success",
        "material": {
            "part_number": material["part_number"],
            "description": material["description"],
            "unit": material["unit"],
            "current_stock": current_stock,
            "minimum_stock": material["minimum_stock"],
            "location": material["location"],
            "low_stock": current_stock <= material["minimum_stock"]
        }
    }


def search_materials(search: str):
    conn = get_connection()

    rows = conn.execute("""
        SELECT
            part_number,
            description,
            category,
            unit,
            location,
            minimum_stock
        FROM materials
        WHERE is_active = 1
          AND (
              part_number LIKE ?
              OR description LIKE ?
              OR category LIKE ?
          )
        ORDER BY part_number
    """, (
        f"%{search}%",
        f"%{search}%",
        f"%{search}%"
    )).fetchall()

    conn.close()

    return {
        "status": "success",
        "count": len(rows),
        "materials": [dict(row) for row in rows]
    }
