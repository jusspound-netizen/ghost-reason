import sqlite3
import json
import time
import pathlib

class ReasonTracer:
    def __init__(self, db_path="ghost_reason.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS reasoning (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp REAL,
                    step_type TEXT,
                    content TEXT,
                    metadata TEXT
                )
            """)

    def log(self, step_type: str, content: str, metadata: dict = None):
        """Log a step: 'prompt', 'thought', 'tool_call', or 'tool_result'."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT INTO reasoning (timestamp, step_type, content, metadata) VALUES (?, ?, ?, ?)",
                (time.time(), step_type, content, json.dumps(metadata or {}))
            )

    def get_timeline(self, limit=50):
        """Return the most recent reasoning steps."""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            return conn.execute(
                "SELECT * FROM reasoning ORDER BY id ASC LIMIT ?", (limit,)
            ).fetchall()

    def clear(self):
        """Wipe the database for a fresh session."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("DELETE FROM reasoning")
