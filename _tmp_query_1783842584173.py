import sqlite3, json
try:
    conn = sqlite3.connect("D:\\Cases for sql\\case_001.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM suspects")
    rows = [dict(r) for r in cur.fetchall()]
    print(json.dumps({"success": True, "rows": rows, "count": len(rows)}))
    conn.close()
except Exception as e:
    print(json.dumps({"success": False, "error": str(e)}))
