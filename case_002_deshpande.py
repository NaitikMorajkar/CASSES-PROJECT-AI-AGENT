"""
CaseQuery — Case #002
"The Deshpande Murder"
Blackmail + Poison Watch + Karna Angle
"""

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "case_002.db")
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

cur.executescript("""
CREATE TABLE suspects (
    id INTEGER PRIMARY KEY,
    name TEXT,
    role TEXT,
    height TEXT,
    background TEXT,
    motive TEXT
);

CREATE TABLE access_logs (
    id INTEGER PRIMARY KEY,
    suspect_id INTEGER,
    entry_time TEXT,
    exit_time TEXT,
    location TEXT,
    verified INTEGER
);

CREATE TABLE alibis (
    id INTEGER PRIMARY KEY,
    suspect_id INTEGER,
    claimed_location TEXT,
    claimed_time TEXT,
    verified_by TEXT
);

CREATE TABLE watch_evidence (
    id INTEGER PRIMARY KEY,
    owner_id INTEGER,
    watch_brand TEXT,
    time_stopped TEXT,
    needle_found INTEGER,
    poison_match INTEGER,
    notes TEXT
);

CREATE TABLE phone_records (
    id INTEGER PRIMARY KEY,
    caller_id INTEGER,
    receiver_id INTEGER,
    call_time TEXT,
    duration_minutes INTEGER,
    call_type TEXT,
    notes TEXT
);

CREATE TABLE forensic_report (
    id INTEGER PRIMARY KEY,
    victim_name TEXT,
    cause_of_death TEXT,
    poison_type TEXT,
    poison_level TEXT,
    who_can_access TEXT,
    time_of_death TEXT,
    notes TEXT
);

CREATE TABLE cctv_logs (
    id INTEGER PRIMARY KEY,
    timestamp TEXT,
    description TEXT,
    height_estimate TEXT,
    location TEXT
);

CREATE TABLE blackmail_records (
    id INTEGER PRIMARY KEY,
    blackmailer_id INTEGER,
    target_id INTEGER,
    message TEXT,
    date TEXT,
    demand TEXT
);

CREATE TABLE background_records (
    id INTEGER PRIMARY KEY,
    person_id INTEGER,
    event_date TEXT,
    event TEXT,
    details TEXT
);
""")

# ─────────────────────────────────────────
# SUSPECTS
# Killer: Inspector Rahul Desai
# ─────────────────────────────────────────
suspects = [
    (1, "Aayush Deshmukh", "Husband - Victim ka", "5'9\"",
     "Businessman - Rohini ka pati", "None"),
    (2, "Rohini Deshmukh", "Victim - 2nd Wife",   "5'4\"",
     "Rahul ki ex-girlfriend - blackmail kar rahi thi", "None - victim hai"),
    (3, "Inspector Rahul Desai", "IPS Officer",   "6'2\"",
     "Rohini ka ex-bf - system ne shaadi karwa di IPS se",
     "Blackmail - career + IPS wife sab khatam hota"),
    (4, "Omkar Deshmukh",  "Military Officer",    "6'1\"",
     "Aayush ka bhai - case solve kiya", "None"),
    (5, "Mrs. Desai",      "IPS Officer - Rahul ki wife", "5'6\"",
     "Senior IPS - Rahul se shaadi force ki gayi thi", "None"),
    (6, "1st Wife",        "Cancer se mari",      "5'3\"",
     "Natural death - red herring", "None"),
]
cur.executemany("INSERT INTO suspects VALUES (?,?,?,?,?,?)", suspects)

# ─────────────────────────────────────────
# ACCESS LOGS
# Crime: 20 June 2026, 11:30 PM - 12:00 AM
# ─────────────────────────────────────────
access_logs = [
    (1, 3, "2026-06-20 23:20", "2026-06-20 23:45", "Deshmukh Residence", 1), # Rahul - came!
    (2, 4, "2026-06-20 20:00", "2026-06-20 22:00", "Deshmukh Residence", 1), # Omkar - left early
    (3, 1, "2026-06-20 18:00", "2026-06-21 06:00", "Home - all night",   1), # Aayush - home
]
cur.executemany("INSERT INTO access_logs VALUES (?,?,?,?,?,?)", access_logs)

# ─────────────────────────────────────────
# WATCH EVIDENCE - Sabse bada clue!
# ─────────────────────────────────────────
watch_evidence = [
    (1, 3, "Rolex", "23:32", 1, 1,
     "Watch Rahul ki thi - time exactly murder ke waqt ruka - "
     "needle poisoned thi - Rohini ko touch karte waqt inject hua"),
]
cur.executemany("INSERT INTO watch_evidence VALUES (?,?,?,?,?,?,?)", watch_evidence)

# ─────────────────────────────────────────
# PHONE RECORDS - Blackmail chain
# ─────────────────────────────────────────
phone_records = [
    (1, 2, 3, "2026-06-15 14:00", 8, "Blackmail call",
     "Rohini ne Rahul ko dhamkaya - 'sab bata dungi'"),
    (2, 2, 3, "2026-06-18 19:00", 12, "Blackmail call",
     "Rohini - 'teri IPS wife ko bhi bataungi'"),
    (3, 2, 3, "2026-06-20 20:00", 5, "Final call",
     "Rohini - 'kal tak waqt hai'"),
    (4, 3, 2, "2026-06-20 21:00", 3, "Outgoing",
     "Rahul ne call kiya - milne aane ki baat"),
]
cur.executemany("INSERT INTO phone_records VALUES (?,?,?,?,?,?,?)", phone_records)

# ─────────────────────────────────────────
# FORENSIC REPORT
# ─────────────────────────────────────────
forensic_report = [
    (1, "Rohini Deshmukh",
     "Homicide - poison injection",
     "VX Nerve Agent - military/law enforcement grade",
     "HIGH - not commercially available",
     "Military officer ya Law enforcement officer",
     "2026-06-20 23:32",
     "Injection site - wrist - consistent with watch needle"),
]
cur.executemany("INSERT INTO forensic_report VALUES (?,?,?,?,?,?,?,?)", forensic_report)

# ─────────────────────────────────────────
# CCTV LOGS
# ─────────────────────────────────────────
cctv_logs = [
    (1, "2026-06-20 23:20", "Tall person entered Deshmukh residence", "6'1\"-6'3\"", "Main gate"),
    (2, "2026-06-20 23:45", "Same tall person exited - walking fast",  "6'1\"-6'3\"", "Main gate"),
]
cur.executemany("INSERT INTO cctv_logs VALUES (?,?,?,?,?)", cctv_logs)

# ─────────────────────────────────────────
# BLACKMAIL RECORDS
# ─────────────────────────────────────────
blackmail_records = [
    (1, 2, 3, "Rahul - tune choose kiya career - ab main choose karungi sach",
     "2026-06-15", "Apni posting change karo - mujhse door jao"),
    (2, 2, 3, "Teri IPS wife ko sab pata chal jaayega - teri relationship mujhse",
     "2026-06-18", "Rs. 50 lakh - warna expose"),
    (3, 2, 3, "Kal tak - warna press conference",
     "2026-06-20", "Career khatam karne ki dhamki"),
]
cur.executemany("INSERT INTO blackmail_records VALUES (?,?,?,?,?,?)", blackmail_records)

# ─────────────────────────────────────────
# BACKGROUND RECORDS - Rahul ka Karna angle
# ─────────────────────────────────────────
background_records = [
    (1, 3, "2010-01-01", "College - Rohini se mila",
     "Rahul aur Rohini - college mein pyaar - sapne dekhe saath rehne ke"),
    (2, 3, "2015-06-01", "IPS training complete",
     "Rahul IPS bana - khud ki mehnat se - koi sifarish nahi"),
    (3, 3, "2015-08-01", "Forced marriage",
     "Senior IPS Officer Pradhan ne force kiya - 'meri beti se shaadi karo warna remote posting' - "
     "Rahul ke paas choice nahi thi - 20 saal ki mehnat ek pal mein khatam hoti"),
    (4, 3, "2015-08-15", "Rohini ko bataya",
     "Rahul ne Rohini ko sach bataya - Rohini toot gayi - "
     "'tune choose kiya career - mujhe nahi'"),
    (5, 2, "2016-01-01", "Rohini ki shaadi Aayush se",
     "Rohini ne Aayush Deshmukh se shaadi ki - dil kabhi theek nahi hua"),
    (6, 2, "2026-06-14", "Blackmail shuru",
     "Rohini ko pata chala Rahul ki posting badh rahi hai - gussa aur dard - blackmail shuru"),
]
cur.executemany("INSERT INTO background_records VALUES (?,?,?,?,?)", background_records)

conn.commit()

# ─────────────────────────────────────────
# SOLUTION
# ─────────────────────────────────────────
SOLUTION = {
    "case_id": 2,
    "killer_id": 3,
    "killer_name": "Inspector Rahul Desai",
    "accepted_answers": ["rahul desai", "inspector rahul", "rahul", "id:3",
                         "inspector rahul desai"],
    "solver": "Omkar Deshmukh",
    "key_clue": "Watch - time ruka tha exactly murder ke waqt - needle poisoned"
}

def check_answer(player_answer):
    return player_answer.strip().lower() in SOLUTION["accepted_answers"]

# ─────────────────────────────────────────
# SQL SOLVE PATH - 10 Layers
# ─────────────────────────────────────────
print("=" * 60)
print("CASE #002 - THE DESHPANDE MURDER")
print("=" * 60)
print("""
20 June 2026. Mumbai. Rohini Deshmukh - murder.
Pehle suicide laga. Omkar ne sach pakda.
10 clues - sab connected. Ek bhi miss mat karna.

Tables: suspects, access_logs, alibis, watch_evidence,
        phone_records, forensic_report, cctv_logs,
        blackmail_records, background_records
""")

print("\n>>> LAYER 1: Cause of death - suicide ya murder?")
cur.execute("""
    SELECT victim_name, cause_of_death, poison_type,
           time_of_death, notes
    FROM forensic_report
""")
for r in cur.fetchall(): print("  ", r)

print("\n>>> LAYER 2: Poison level - kaun la sakta tha?")
cur.execute("""
    SELECT poison_type, poison_level, who_can_access
    FROM forensic_report
""")
for r in cur.fetchall(): print("  ", r)

print("\n>>> LAYER 3: Do log la sakte the - kaun kaun?")
cur.execute("""
    SELECT s.name, s.role, s.height
    FROM suspects s
    WHERE s.role LIKE '%Officer%'
    OR s.role LIKE '%Military%'
""")
for r in cur.fetchall(): print("  ", r)

print("\n>>> LAYER 4: CCTV - kaun aaya tha raat ko?")
cur.execute("""
    SELECT timestamp, description, height_estimate, location
    FROM cctv_logs
    ORDER BY timestamp
""")
for r in cur.fetchall(): print("  ", r)

print("\n>>> LAYER 5: Height match - CCTV vs suspects")
cur.execute("""
    SELECT s.name, s.height, s.role
    FROM suspects s
    WHERE s.height LIKE '6%'
""")
for r in cur.fetchall(): print("  ", r)

print("\n>>> LAYER 6: Omkar ka observation - watch!")
cur.execute("""
    SELECT s.name as watch_owner, w.watch_brand,
           w.time_stopped, w.needle_found,
           w.poison_match, w.notes
    FROM watch_evidence w
    JOIN suspects s ON s.id = w.owner_id
""")
for r in cur.fetchall(): print("  ", r)

print("\n>>> LAYER 7: Phone records - blackmail chain")
cur.execute("""
    SELECT s1.name as caller, s2.name as receiver,
           pr.call_time, pr.call_type, pr.notes
    FROM phone_records pr
    JOIN suspects s1 ON s1.id = pr.caller_id
    JOIN suspects s2 ON s2.id = pr.receiver_id
    ORDER BY pr.call_time
""")
for r in cur.fetchall(): print("  ", r)

print("\n>>> LAYER 8: Blackmail records - Rohini ka demand")
cur.execute("""
    SELECT s1.name as blackmailer, s2.name as target,
           br.message, br.date, br.demand
    FROM blackmail_records br
    JOIN suspects s1 ON s1.id = br.blackmailer_id
    JOIN suspects s2 ON s2.id = br.target_id
    ORDER BY br.date
""")
for r in cur.fetchall(): print("  ", r)

print("\n>>> LAYER 9: Rahul ka motive - background check")
cur.execute("""
    SELECT event_date, event, details
    FROM background_records
    WHERE person_id = 3
    ORDER BY event_date
""")
for r in cur.fetchall(): print("  ", r)

print("\n>>> LAYER 10: Final connection - sab ek saath")
cur.execute("""
    SELECT s.name, s.role, s.height,
           w.time_stopped, w.needle_found,
           f.time_of_death, f.who_can_access
    FROM suspects s
    JOIN watch_evidence w ON w.owner_id = s.id
    JOIN forensic_report f ON f.time_of_death = w.time_stopped
    WHERE w.poison_match = 1
""")
for r in cur.fetchall(): print("  ", r)

print("\n" + "=" * 60)
print("ANSWER CHECK:")
print("'Rahul Desai':", check_answer("Rahul Desai"))
print("'Inspector Rahul':", check_answer("Inspector Rahul"))
print("=" * 60)

conn.close()
print(f"\nDatabase: {DB_PATH}")
