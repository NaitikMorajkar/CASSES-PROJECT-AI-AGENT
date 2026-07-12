"""
CaseQuery — Case #001
"The Greenline Double Cross"
Chori + Murder + Twin Twist + Mental Illness
"""

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "case_001.db")
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# ─────────────────────────────────────────
# TABLES
# ─────────────────────────────────────────
cur.executescript("""
CREATE TABLE suspects (
    id INTEGER PRIMARY KEY,
    name TEXT,
    role TEXT,
    has_key_access INTEGER,
    twin_id INTEGER,
    actual_height TEXT,
    distinguishing_features TEXT
);

CREATE TABLE access_logs (
    id INTEGER PRIMARY KEY,
    suspect_id INTEGER,
    entry_time TEXT,
    exit_time TEXT,
    location TEXT
);

CREATE TABLE alibis (
    id INTEGER PRIMARY KEY,
    suspect_id INTEGER,
    claimed_location TEXT,
    claimed_time_range TEXT,
    verified_by TEXT
);

CREATE TABLE transactions (
    id INTEGER PRIMARY KEY,
    suspect_id INTEGER,
    transaction_date TEXT,
    amount REAL,
    description TEXT
);

CREATE TABLE cctv_logs (
    id INTEGER PRIMARY KEY,
    suspect_name TEXT,
    entry_time TEXT,
    exit_time TEXT,
    height_estimate TEXT,
    facial_features TEXT,
    location TEXT
);

CREATE TABLE call_logs (
    id INTEGER PRIMARY KEY,
    caller_id INTEGER,
    receiver_id INTEGER,
    call_time TEXT,
    duration_minutes INTEGER,
    notes TEXT
);

CREATE TABLE delivery_orders (
    id INTEGER PRIMARY KEY,
    ordered_by TEXT,
    delivery_time TEXT,
    delivery_address TEXT,
    item TEXT,
    status TEXT
);

CREATE TABLE evidence (
    id INTEGER PRIMARY KEY,
    suspect_id INTEGER,
    evidence_type TEXT,
    description TEXT,
    found_at TEXT,
    found_by TEXT
);

CREATE TABLE psychological_records (
    id INTEGER PRIMARY KEY,
    suspect_id INTEGER,
    diagnosis TEXT,
    last_visit TEXT,
    medication TEXT,
    doctor_notes TEXT,
    crisis_calls INTEGER
);

CREATE TABLE family_records (
    id INTEGER PRIMARY KEY,
    member_id INTEGER,
    member_name TEXT,
    relationship TEXT,
    photo_status TEXT,
    last_contact_date TEXT,
    notes TEXT
);
""")

# ─────────────────────────────────────────
# SUSPECTS
# Crime: 20 June 2026, 11:00 PM - 12:00 AM
# Guilty: Tim Becker (twin of Tom) - murder
#         Tom Becker - chori mastermind
#         Maria Chen - chori puppet
# ─────────────────────────────────────────
suspects = [
    (1, "Tom Becker",   "Warehouse Manager", 1, 2, "6'1\"", "No facial scars"),
    (2, "Tim Becker",   "Tom ka Twin",       1, 1, "5'11\"","Left eye scar"),
    (3, "Maria Chen",   "Driver",            1, None, "5'4\"", "None"),
    (4, "Raj Patel",    "Security Guard",    1, None, "5'8\"", "None"),
    (5, "Lena Ortiz",   "Office Clerk",      0, None, "5'3\"", "None"),
    (6, "Vikram Malhotra","Accountant",      1, None, "5'9\"", "None"),
    (7, "Neha Sharma",  "Owner ki Beti",     1, None, "5'5\"", "None"),
    (8, "Sam Wu",       "Night Janitor",     0, None, "5'6\"", "None"),
]
cur.executemany("INSERT INTO suspects VALUES (?,?,?,?,?,?,?)", suspects)

# ─────────────────────────────────────────
# ACCESS LOGS
# ─────────────────────────────────────────
access_logs = [
    (1, 1, "2026-06-20 23:05", "2026-06-20 23:15", "Office"),          # Tom - real visit
    (2, 3, "2026-06-20 21:45", "2026-06-20 22:15", "Warehouse Floor"), # Maria - chori
    (3, 4, "2026-06-20 21:00", "2026-06-20 23:30", "Loading Dock"),    # Raj - innocent
    (4, 6, "2026-06-20 21:30", "2026-06-20 22:45", "Office"),          # Vikram - red herring
    (5, 7, "2026-06-20 22:30", "2026-06-20 23:00", "Parking+Office"),  # Neha - witness
    (6, 8, "2026-06-20 22:00", "2026-06-20 22:30", "Office"),          # Sam Wu
]
cur.executemany("INSERT INTO access_logs VALUES (?,?,?,?,?)", access_logs)

# ─────────────────────────────────────────
# CCTV LOGS - Twin twist yahan hai
# ─────────────────────────────────────────
cctv_logs = [
    (1, "Tom Becker", "2026-06-20 23:05", "2026-06-20 23:15", "6'1\"", "No facial scars", "Office"),
    (2, "Tom Becker", "2026-06-20 23:30", "2026-06-20 23:35", "5'11\"","Left eye SCAR",   "Office"), # Actually Tim!
]
cur.executemany("INSERT INTO cctv_logs VALUES (?,?,?,?,?,?,?)", cctv_logs)

# ─────────────────────────────────────────
# ALIBIS
# ─────────────────────────────────────────
alibis = [
    (1, 1, "Home", "22:00-onwards", "Nehal (wife)"),         # Tom - solid alibi
    (2, 3, "Home", "21:30-23:30",   "Unverified"),            # Maria - jhooth!
    (3, 4, "Loading Dock", "21:00-23:30", "CCTV verified"),   # Raj - innocent
    (4, 6, "Office", "21:30-22:45", "Unverified"),            # Vikram - suspicious
    (5, 7, "Home", "Came at 22:30", "CCTV verified"),         # Neha - witness
    (6, 8, "Office", "22:00-22:30", "Raj Patel"),             # Sam - innocent
]
cur.executemany("INSERT INTO alibis VALUES (?,?,?,?,?)", alibis)

# ─────────────────────────────────────────
# TRANSACTIONS - Chori ka proof
# ─────────────────────────────────────────
transactions = [
    (1, 3, "2026-06-21", 10000.00, "Cash deposit"),           # Maria - suspicious!
    (2, 1, "2026-06-21",  5000.00, "Anonymous transfer"),     # Tom - mastermind
    (3, 5, "2026-06-20",  2000.00, "Consulting fee"),         # Lena - Tom ki bhatiji
    (4, 6, "2026-06-15",   500.00, "Salary"),                 # Vikram - normal
    (5, 4, "2026-06-15",   200.00, "Salary"),                 # Raj - normal
]
cur.executemany("INSERT INTO transactions VALUES (?,?,?,?,?)", transactions)

# ─────────────────────────────────────────
# CALL LOGS - Tom ka network
# ─────────────────────────────────────────
call_logs = [
    (1, 1, 4, "2026-06-20 18:00", 4,  "Tom->Raj: CCTV band karna"),
    (2, 1, 3, "2026-06-20 18:30", 6,  "Tom->Maria: Aaj raat aana"),
    (3, 1, 5, "2026-06-20 19:00", 2,  "Tom->Lena: Deal confirm"),
    (4, 3, 6, "2026-06-20 22:00", 3,  "Maria->Vikram: Unknown"),
    (5, 2, 0, "2026-06-20 21:00", 1,  "Tim->Unknown: Crisis helpline"),
]
cur.executemany("INSERT INTO call_logs VALUES (?,?,?,?,?,?)", call_logs)

# ─────────────────────────────────────────
# DELIVERY ORDERS - Tim ki galti!
# ─────────────────────────────────────────
delivery_orders = [
    (1, "T. Becker", "2026-06-20 23:50", "Greenline Storage", "1 Pizza",
     "Undelivered - delivery boy fled"),
]
cur.executemany("INSERT INTO delivery_orders VALUES (?,?,?,?,?,?)", delivery_orders)

# ─────────────────────────────────────────
# EVIDENCE
# ─────────────────────────────────────────
evidence = [
    (1, 2, "Poison Vial",     "Found in Sam Wu's pocket - Tim's fingerprints", "Parking lot", "Sam Wu"),
    (2, 2, "Left eye scar",   "CCTV 23:30 - height 5'11 - scar visible",       "CCTV footage", "Neha Sharma"),
    (3, 1, "Pizza order",     "T.Becker - Greenline address - crime time",      "Delivery records", "Police"),
    (4, 3, "Cash deposit",    "$10,000 - next day - suspicious",                "Bank records",    "Police"),
    (5, 6, "Embezzlement",    "$500 monthly - 2 years - separate case",         "Accounts",        "Audit"),
]
cur.executemany("INSERT INTO evidence VALUES (?,?,?,?,?,?)", evidence)

# ─────────────────────────────────────────
# PSYCHOLOGICAL RECORDS - Tim ki bimari
# ─────────────────────────────────────────
psychological_records = [
    (1, 2, "Paranoid Schizophrenia", "2026-01-15",
     "Risperidone - DISCONTINUED BY PATIENT",
     "Patient believes Sharma destroyed his family. "
     "Urgent follow-up needed. Patient not responding to calls.",
     3),
]
cur.executemany("INSERT INTO psychological_records VALUES (?,?,?,?,?,?,?)", psychological_records)

# ─────────────────────────────────────────
# FAMILY RECORDS - Photo clue
# ─────────────────────────────────────────
family_records = [
    (1, 2, "Tim Becker",  "Twin Brother", "BURNED - self inflicted", "2019-03-12",
     "Tim ne khud apna hissa jalaya - 'Main is family ka hissa nahi hoon'"),
    (2, 1, "Tom Becker",  "Twin Brother", "Intact",                  "2026-06-20", "Normal"),
    (3, 0, "Nehal Becker","Mother",       "Intact",                  "2000-01-01",
     "Priya - ghar se nikaali gayi - Sharma ki wajah se - 3 saal baad mari"),
    (4, 0, "Richard Becker","Father",     "Intact",                  "2010-01-01",
     "Tom ko choose kiya - Tim ko ignore kiya"),
]
cur.executemany("INSERT INTO family_records VALUES (?,?,?,?,?,?,?)", family_records)

conn.commit()

# ─────────────────────────────────────────
# SOLUTION
# ─────────────────────────────────────────
SOLUTION = {
    "case_id": 1,
    "theft_mastermind": {"id": 1, "name": "Tom Becker"},
    "theft_puppet": {"id": 3, "name": "Maria Chen"},
    "murderer": {"id": 2, "name": "Tim Becker"},
    "accepted_murder_answers": ["tim becker", "tim", "id:2"],
    "accepted_theft_answers": ["tom becker", "tom", "id:1"],
}

def check_murder_answer(player_answer):
    return player_answer.strip().lower() in SOLUTION["accepted_murder_answers"]

def check_theft_answer(player_answer):
    return player_answer.strip().lower() in SOLUTION["accepted_theft_answers"]

# ─────────────────────────────────────────
# SQL SOLVE PATH - 9 Layers
# ─────────────────────────────────────────
print("=" * 60)
print("CASE #001 - THE GREENLINE DOUBLE CROSS")
print("=" * 60)
print("""
Raat 20 June 2026. Greenline Storage, Mumbai.
$40,000 ke electronics gayab. Mr. Arvind Sharma - murder.
6 log the us raat. Do alag crimes. Ek hi raat.
Dhundo - kaun tha?

Tables: suspects, access_logs, alibis, transactions,
        cctv_logs, call_logs, delivery_orders,
        evidence, psychological_records, family_records
""")

print("\n>>> LAYER 1: Chori - Crime time pe kaun andar tha?")
cur.execute("""
    SELECT s.name, al.entry_time, al.exit_time, al.location
    FROM access_logs al
    JOIN suspects s ON s.id = al.suspect_id
    WHERE al.entry_time <= '2026-06-20 22:15'
    AND al.exit_time >= '2026-06-20 21:45'
    AND al.location = 'Warehouse Floor'
""")
for r in cur.fetchall(): print("  ", r)

print("\n>>> LAYER 2: Tom ka network - kisne kisko call kiya?")
cur.execute("""
    SELECT s1.name as caller, s2.name as receiver,
           cl.call_time, cl.notes
    FROM call_logs cl
    JOIN suspects s1 ON s1.id = cl.caller_id
    LEFT JOIN suspects s2 ON s2.id = cl.receiver_id
    WHERE cl.caller_id = 1
""")
for r in cur.fetchall(): print("  ", r)

print("\n>>> LAYER 3: Transactions - suspicious paisa?")
cur.execute("""
    SELECT s.name, t.transaction_date, t.amount, t.description
    FROM transactions t
    JOIN suspects s ON s.id = t.suspect_id
    WHERE t.transaction_date = '2026-06-21'
    ORDER BY t.amount DESC
""")
for r in cur.fetchall(): print("  ", r)

print("\n>>> LAYER 4: CCTV - Tom 2 baar andar kyun gaya?")
cur.execute("""
    SELECT suspect_name, entry_time, exit_time,
           height_estimate, facial_features
    FROM cctv_logs
    ORDER BY entry_time
""")
for r in cur.fetchall(): print("  ", r)

print("\n>>> LAYER 5: Height mismatch - yeh Tom nahi tha!")
cur.execute("""
    SELECT c.suspect_name, c.height_estimate, c.facial_features,
           s.actual_height, s.distinguishing_features
    FROM cctv_logs c
    JOIN suspects s ON s.name = c.suspect_name
    WHERE c.entry_time = '2026-06-20 23:30'
""")
for r in cur.fetchall(): print("  ", r)

print("\n>>> LAYER 6: Twin check - Tom ka twin hai?")
cur.execute("""
    SELECT s1.name, s1.actual_height, s1.distinguishing_features,
           s2.name as twin_name, s2.actual_height as twin_height,
           s2.distinguishing_features as twin_features
    FROM suspects s1
    JOIN suspects s2 ON s1.twin_id = s2.id
    WHERE s1.name = 'Tom Becker'
""")
for r in cur.fetchall(): print("  ", r)

print("\n>>> LAYER 7: Pizza order - Tim ki galti!")
cur.execute("""
    SELECT ordered_by, delivery_time, delivery_address,
           item, status
    FROM delivery_orders
""")
for r in cur.fetchall(): print("  ", r)

print("\n>>> LAYER 8: Evidence - Sam Wu ki pocket mein kya tha?")
cur.execute("""
    SELECT s.name, e.evidence_type, e.description,
           e.found_at, e.found_by
    FROM evidence e
    JOIN suspects s ON s.id = e.suspect_id
    WHERE e.evidence_type = 'Poison Vial'
""")
for r in cur.fetchall(): print("  ", r)

print("\n>>> LAYER 9: Psychological records - Tim ki bimari")
cur.execute("""
    SELECT s.name, p.diagnosis, p.medication,
           p.doctor_notes, p.crisis_calls
    FROM psychological_records p
    JOIN suspects s ON s.id = p.suspect_id
""")
for r in cur.fetchall(): print("  ", r)

print("\n>>> FINAL: Neha ka observation - scar confirm!")
cur.execute("""
    SELECT member_name, photo_status, notes
    FROM family_records
    WHERE photo_status LIKE '%BURNED%'
""")
for r in cur.fetchall(): print("  ", r)

print("\n" + "=" * 60)
print("ANSWER CHECK:")
print("Murder answer 'Tim Becker':", check_murder_answer("Tim Becker"))
print("Theft answer 'Tom Becker':", check_theft_answer("Tom Becker"))
print("=" * 60)

conn.close()
print(f"\nDatabase: {DB_PATH}")
