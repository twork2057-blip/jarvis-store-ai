from pathlib import Path
import apsw


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATABASE_PATH = PROJECT_ROOT / "data" / "jarvis.db"


def get_connection():
    """Open a connection to the JARVIS SQLite database."""
    return apsw.Connection(str(DATABASE_PATH))


def test_connection():
    """Test that the database can be opened and queried."""
    connection = get_connection()

    cursor = connection.cursor()
    row = next(cursor.execute("SELECT COUNT(*) FROM materials"))

    connection.close()

    return row[0]


if __name__ == "__main__":
    count = test_connection()
    print(f"Database connected successfully.")
    print(f"Materials in database: {count}")
