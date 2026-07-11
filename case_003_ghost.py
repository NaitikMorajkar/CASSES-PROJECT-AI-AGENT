"""
CaseQuery — Case #003
"The Ghost Protocol"
Web3 Heist + Father's Murder + Twin Sacrifice
"""

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "case_003.db")
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

cur.executescript("""
CREATE TABLE suspects (
    id INTEGER PRIMARY KEY,
    name TEXT,
    role TEXT,
    wallet_address TEXT,
    background TEXT,
    connection_to_nexvault TEXT
);

CREATE TABLE transactions (
    id INTEGER PRIMARY KEY,
    from_wallet TEXT,
    to_wallet TEXT,
    amount REAL,
    timestamp TEXT,
    chain TEXT,
    transaction_type TEXT,
    notes TEXT
);

CREATE TABLE smart_contracts (
    id INTEGER PRIMARY KEY,
    contract_name TEXT,
    function_name TEXT,
    access_level TEXT,
    vulnerability TEXT,
    called_by TEXT,
    called_at TEXT
);

CREATE TABLE croo_agent_store (
    id INTEGER PRIMARY KEY,
    agent_name TEXT,
    wallet_address TEXT,
    service_type TEXT,
    fee_usdc REAL,
    registration_date TEXT,
    total_transactions INTEGER,
    status TEXT
);

CREATE TABLE dark_web_messages (
    id INTEGER PRIMARY KEY,
    message TEXT,
    timestamp TEXT,
    server_location TEXT,
    delay_seconds INTEGER,
    hack_reference INTEGER
);

CREATE TABLE wallet_connections (
    id INTEGER PRIMARY KEY,
    wallet TEXT,
    connected_to TEXT,
    relationship TEXT,
    proof TEXT,
    date TEXT
);

CREATE TABLE nexvault_victims (
    id INTEGER PRIMARY KEY,
    victim_name TEXT,
    wallet_address TEXT,
    amount_lost REAL,
    personal_connection TEXT
);

CREATE TABLE evidence (
    id INTEGER PRIMARY KEY,
    suspect_id INTEGER,
    evidence_type TEXT,
    description TEXT,
    found_at TEXT
);

CREATE TABLE diary_entries (
    id INTEGER PRIMARY KEY,
    author TEXT,
    date TEXT,
    entry TEXT,
    encrypted INTEGER
);

CREATE TABLE vikram_case_files (
    id INTEGER PRIMARY KEY,
    officer_name TEXT,
    file_date TEXT,
    notes TEXT,
    status TEXT,
    deleted_by TEXT
);
""")

# ─────────────────────────────────────────
# SUSPECTS
# Ghost_X = Aryan + Joi
# Vikram = Aryan ka papa - murdered
# ─────────────────────────────────────────
suspects = [
    (1, "Aryan Malhotra", "Coder - Ghost_X Brain",
     "0x7f3a9b2c", "Police officer Vikram ka beta - maa ki savings NexVault mein gayi",
     "Maa ka paisa - Rs 8 lakh - doob gaya"),
    (2, "Joi Sharma", "Hacker - Ghost_X Hands",
     "0x4e1d7f8a", "Aryan ka best friend - behen Priya ki shaadi ke paise gayi",
     "Behen ka paisa - Rs 5 lakh - shaadi toot gayi"),
    (3, "Vikram Malhotra", "Senior Cyber Cell Officer",
     "0x9c2b3d4e", "Aryan ka papa - 20 saal ki honest service - case investigate kar raha tha",
     "None - investigating officer - MURDERED"),
    (4, "NexVault CEO",   "DeFi Founder - Asli Villain",
     "0x2f8e1a9d", "Rug pull kiya - $5M liya - 10000 investors ka paisa duba diya",
     "Criminal - asli doshi"),
    (5, "Dev Kapoor",    "Innocent Developer - Red Herring",
     "0x8b3c2e1f", "NexVault mein kaam karta tha - bilkul innocent - Aryan ne frame kiya",
     "None - red herring"),
]
cur.executemany("INSERT INTO suspects VALUES (?,?,?,?,?,?)", suspects)

# ─────────────────────────────────────────
# TRANSACTIONS - $5M drain + mixing
# ─────────────────────────────────────────
transactions_data = [
    # NexVault drain
    (1,  "0x2f8e1a9d", "0x4e1d7f8a",  5000000, "2026-06-20 00:00", "ETH", "Drain",
     "withdrawAll() called - $5M drained"),
    # Split into 47 wallets
    (2,  "0x4e1d7f8a", "0xSplit001",  106382,  "2026-06-20 00:01", "ETH", "Split", "Split 1/47"),
    (3,  "0x4e1d7f8a", "0xSplit002",  106382,  "2026-06-20 00:01", "ETH", "Split", "Split 2/47"),
    (4,  "0x4e1d7f8a", "0xSplit003",  106382,  "2026-06-20 00:01", "ETH", "Split", "Split 3/47"),
    # Maa ka paisa wapas - Aryan ki pehchaan ka clue!
    (5,  "0xClean001", "0xMaa001",    800000,  "2026-06-20 04:00", "ETH", "Recovery",
     "EXACT amount - maa ki savings - anonymous return - personal connection!"),
    # Behen ka paisa wapas
    (6,  "0xClean002", "0xPriya001",  500000,  "2026-06-20 06:00", "ETH", "Recovery",
     "Behen Priya ki savings - wapas ki"),
    # College fees connection - Joi ki identity
    (7,  "0x4e1d7f8a", "0xCollege",   150000,  "2024-01-01", "ETH", "Education",
     "Joi Sharma - college fees payment 2024"),
    # Aryan ka wallet - college fees
    (8,  "0x7f3a9b2c", "0xCollege",   150000,  "2024-01-01", "ETH", "Education",
     "Aryan Malhotra - same college - same time"),
    # Red herring - Dev Kapoor
    (9,  "0x8b3c2e1f", "0xSplit010",  50000,   "2026-06-20 00:30", "ETH", "Suspicious",
     "Planted by Aryan - Dev ko frame karne ke liye"),
]
cur.executemany("INSERT INTO transactions VALUES (?,?,?,?,?,?,?,?)", transactions_data)

# ─────────────────────────────────────────
# SMART CONTRACTS - NexVault vulnerability
# ─────────────────────────────────────────
smart_contracts = [
    (1, "NexVault", "withdrawAll()", "PUBLIC",  "YES - should be PRIVATE",
     "0x4e1d7f8a", "2026-06-20 00:00"),
    (2, "NexVault", "deposit()",     "PUBLIC",  "NO",  "Multiple", "2024-01-01"),
    (3, "NexVault", "getBalance()",  "PUBLIC",  "NO",  "Multiple", "2024-01-01"),
    (4, "NexVault", "adminOnly()",   "PRIVATE", "NO",  "Owner",    "2024-01-01"),
]
cur.executemany("INSERT INTO smart_contracts VALUES (?,?,?,?,?,?,?)", smart_contracts)

# ─────────────────────────────────────────
# CROO AGENT STORE - ShadowMix
# ─────────────────────────────────────────
croo_agent_store = [
    (1, "ShadowMix", "0x4e1d7f8a", "crypto_mixing", 0.01,
     "2026-06-15", 47, "ACTIVE"),
    (2, "LegalSwap", "0x9x9x9x9x", "token_swap",    0.05,
     "2026-01-01", 1250, "ACTIVE"),
    (3, "AuditBot",  "0x1a1a1a1a", "smart_contract_audit", 0.10,
     "2025-06-01", 890, "ACTIVE"),
]
cur.executemany("INSERT INTO croo_agent_store VALUES (?,?,?,?,?,?,?,?)", croo_agent_store)

# ─────────────────────────────────────────
# DARK WEB MESSAGES - "Too easy" pattern
# ─────────────────────────────────────────
dark_web_messages = [
    (1,  "Too easy.", "2026-05-01 14:03", "EU-West",  180, 1),
    (2,  "Too easy.", "2026-05-08 09:03", "EU-West",  180, 2),
    (3,  "Too easy.", "2026-05-15 22:03", "EU-West",  180, 3),
    (4,  "Too easy.", "2026-05-22 11:03", "EU-West",  180, 4),
    (5,  "Too easy.", "2026-05-29 16:03", "EU-West",  180, 5),
    (6,  "Too easy.", "2026-06-05 08:03", "EU-West",  180, 6),
    (7,  "Too easy.", "2026-06-12 19:03", "EU-West",  180, 7),
    # Hack #47 - Mumbai server - 13 second ka fark!
    (47, "Too easy.", "2026-06-20 00:02", "MUMBAI",   167, 47),
]
cur.executemany("INSERT INTO dark_web_messages VALUES (?,?,?,?,?,?)", dark_web_messages)

# ─────────────────────────────────────────
# WALLET CONNECTIONS - Identity trail
# ─────────────────────────────────────────
wallet_connections = [
    (1, "0x4e1d7f8a", "ShadowMix Agent",    "Agent owner",       "CROO records",    "2026-06-15"),
    (2, "0x4e1d7f8a", "0xCollege",          "Education payment", "Transaction hash", "2024-01-01"),
    (3, "0x4e1d7f8a", "Joi Sharma",         "KYC - exchange",    "Binance records",  "2023-06-01"),
    (4, "0x7f3a9b2c", "0xCollege",          "Education payment", "Transaction hash", "2024-01-01"),
    (5, "0x7f3a9b2c", "Aryan Malhotra",     "KYC - exchange",    "Binance records",  "2023-06-01"),
    (6, "0x7f3a9b2c", "0xMaa001",           "Family transfer",   "Pattern analysis", "2026-06-20"),
    # Red herring - planted
    (7, "0x8b3c2e1f", "0xSplit010",         "PLANTED by Ghost_X","Forged records",   "2026-06-20"),
]
cur.executemany("INSERT INTO wallet_connections VALUES (?,?,?,?,?,?)", wallet_connections)

# ─────────────────────────────────────────
# NEXVAULT VICTIMS
# ─────────────────────────────────────────
nexvault_victims = [
    (1, "Aryan ki Maa",   "0xMaa001",   800000, "Aryan Malhotra ki maa - zindagi bhar ki savings"),
    (2, "Priya Sharma",   "0xPriya001", 500000, "Joi ki behen - shaadi ke paise - shaadi toot gayi"),
    (3, "General Public", "0xPublic",  3700000, "9998 aur investors - sab barbad"),
]
cur.executemany("INSERT INTO nexvault_victims VALUES (?,?,?,?,?)", nexvault_victims)

# ─────────────────────────────────────────
# EVIDENCE
# ─────────────────────────────────────────
evidence = [
    (1, 1, "Diary Entry",        "Aryan ka diary - plan likha tha",             "Aryan ka ghar"),
    (2, 2, "ShadowMix ownership","CROO records - 0x4e1d7f8a - Joi ka wallet",   "CROO Agent Store"),
    (3, 3, "Murder weapon",      "Chaku - fingerprints - Aryan ka",             "Crime scene"),
    (4, 3, "Case files deleted", "Vikram ke computer se evidence delete kiya",  "Cyber Cell"),
    (5, 5, "Planted evidence",   "Dev Kapoor ko frame kiya - forged records",   "Dev ka wallet"),
]
cur.executemany("INSERT INTO evidence VALUES (?,?,?,?,?)", evidence)

# ─────────────────────────────────────────
# DIARY ENTRIES
# ─────────────────────────────────────────
diary_entries = [
    (1, "Aryan", "2026-06-14",
     "Maa ne bola aaj - account mein kuch nahi bacha. NexVault ne sab le liya. "
     "Joi ki behen ki shaadi toot gayi. System ne kuch nahi kiya. Hum karenge.",
     0),
    (2, "Aryan", "2026-06-15",
     "Plan ready. ShadowMix CROO pe register kiya. 5 din mein sab ready. "
     "Papa ko pata nahi chalna chahiye. Woh investigate karenge - main jaanta hoon unki methodology.",
     0),
    (3, "Aryan", "2026-06-20",
     "Ho gaya. $5M drain. Maa ka paisa wapas. Priya ka paisa wapas. "
     "Par Papa case pe hain. Woh close aa rahe hain. Kya karun.",
     1),
    (4, "Vikram", "2026-06-23",
     "Aryan - main jaanta hoon sab. Main jaanta hoon tu kyun kiya. "
     "Ek baap hoon pehle - officer baad mein. Par is baar dono ek saath nahi ho sakte. "
     "Maafi - beta. — Papa",
     1),
]
cur.executemany("INSERT INTO diary_entries VALUES (?,?,?,?,?)", diary_entries)

# ─────────────────────────────────────────
# VIKRAM CASE FILES
# ─────────────────────────────────────────
vikram_case_files = [
    (1, "Vikram Malhotra", "2026-06-20", "Ghost_X identified - Mumbai connection - wallet traced",
     "DELETED", "Aryan Malhotra"),
    (2, "Vikram Malhotra", "2026-06-21", "ShadowMix = Joi Sharma - CROO records",
     "DELETED", "Aryan Malhotra"),
    (3, "Vikram Malhotra", "2026-06-22", "Co-conspirator = Aryan Malhotra - my son",
     "DELETED", "Aryan Malhotra"),
    (4, "Vikram Malhotra", "2026-06-23", "Going to headquarters to report - cannot hide this",
     "DELETED", "Aryan Malhotra"),
]
cur.executemany("INSERT INTO vikram_case_files VALUES (?,?,?,?,?,?)", vikram_case_files)

conn.commit()

# ─────────────────────────────────────────
# SOLUTION
# ─────────────────────────────────────────
SOLUTION = {
    "case_id": 3,
    "ghost_x_brain": {"id": 1, "name": "Aryan Malhotra"},
    "ghost_x_hands": {"id": 2, "name": "Joi Sharma"},
    "vikram_murderer": {"id": 1, "name": "Aryan Malhotra"},
    "convicted": "Joi Sharma - took the blame alone",
    "accepted_ghostx_answers": ["aryan malhotra", "joi sharma", "aryan and joi",
                                 "aryan + joi", "both"],
    "accepted_murder_answers": ["aryan malhotra", "aryan", "id:1"],
    "case_status": "PARTIALLY CLOSED - Part 2 Coming Soon"
}

def check_ghostx(player_answer):
    return player_answer.strip().lower() in SOLUTION["accepted_ghostx_answers"]

def check_murder(player_answer):
    return player_answer.strip().lower() in SOLUTION["accepted_murder_answers"]

# ─────────────────────────────────────────
# SQL SOLVE PATH - 8 Layers
# ─────────────────────────────────────────
print("=" * 60)
print("CASE #003 - THE GHOST PROTOCOL")
print("=" * 60)
print("""
Mumbai. 2026. NexVault DeFi - $5M drain.
Ghost_X - identity unknown. 10,000 victims.
Ek Cyber Cell officer - murder.
Tumhara kaam - Ghost_X ko dhundho.
Par kuch aur bhi hai yahan...

Tables: suspects, transactions, smart_contracts,
        croo_agent_store, dark_web_messages,
        wallet_connections, nexvault_victims,
        evidence, diary_entries, vikram_case_files
""")

print("\n>>> LAYER 1: Smart Contract - vulnerability kya tha?")
cur.execute("""
    SELECT contract_name, function_name,
           access_level, vulnerability, called_by, called_at
    FROM smart_contracts
    WHERE vulnerability != 'NO'
""")
for r in cur.fetchall(): print("  ", r)

print("\n>>> LAYER 2: Transaction trail - $5M kahan gaya?")
cur.execute("""
    SELECT from_wallet, to_wallet, amount,
           timestamp, transaction_type, notes
    FROM transactions
    WHERE timestamp LIKE '2026-06-20%'
    AND transaction_type IN ('Drain', 'Split')
    ORDER BY timestamp
    LIMIT 5
""")
for r in cur.fetchall(): print("  ", r)

print("\n>>> LAYER 3: CROO Agent - ShadowMix kaun hai?")
cur.execute("""
    SELECT agent_name, wallet_address, service_type,
           fee_usdc, registration_date, total_transactions
    FROM croo_agent_store
    WHERE service_type = 'crypto_mixing'
    AND registration_date < '2026-06-20'
""")
for r in cur.fetchall(): print("  ", r)

print("\n>>> LAYER 4: 'Too easy' pattern - timing analysis")
cur.execute("""
    SELECT message, timestamp, server_location, delay_seconds
    FROM dark_web_messages
    ORDER BY delay_seconds
    LIMIT 5
""")
print("  [First 5 messages - all EU-West, 180 seconds]")
for r in cur.fetchall(): print("  ", r)
cur.execute("""
    SELECT message, timestamp, server_location, delay_seconds
    FROM dark_web_messages
    WHERE server_location = 'MUMBAI'
""")
print("  [Mumbai anomaly - 13 second difference!]")
for r in cur.fetchall(): print("  ", r)

print("\n>>> LAYER 5: Maa ka paisa - personal connection!")
cur.execute("""
    SELECT nv.victim_name, nv.amount_lost,
           t.from_wallet, t.to_wallet, t.timestamp, t.notes
    FROM nexvault_victims nv
    JOIN transactions t ON t.to_wallet = nv.wallet_address
    WHERE t.transaction_type = 'Recovery'
""")
for r in cur.fetchall(): print("  ", r)

print("\n>>> LAYER 6: Wallet fingerprint - Joi ki identity")
cur.execute("""
    SELECT wc.wallet, wc.connected_to,
           wc.relationship, wc.proof, wc.date
    FROM wallet_connections wc
    WHERE wc.wallet = '0x4e1d7f8a'
    AND wc.relationship != 'PLANTED by Ghost_X'
""")
for r in cur.fetchall(): print("  ", r)

print("\n>>> LAYER 7: Vikram ke deleted files - sach kya tha?")
cur.execute("""
    SELECT officer_name, file_date, notes,
           status, deleted_by
    FROM vikram_case_files
    ORDER BY file_date
""")
for r in cur.fetchall(): print("  ", r)

print("\n>>> LAYER 8: Final - Ghost_X = ?")
cur.execute("""
    SELECT s.name, s.wallet_address, s.role,
           wc.connected_to, wc.relationship
    FROM suspects s
    JOIN wallet_connections wc ON wc.wallet = s.wallet_address
    WHERE wc.connected_to LIKE '%ShadowMix%'
    OR wc.connected_to LIKE '%College%'
""")
for r in cur.fetchall(): print("  ", r)

print("\n" + "=" * 60)
print("CASE STATUS: PARTIALLY CLOSED")
print("Ghost_X answer 'Aryan and Joi':", check_ghostx("Aryan and Joi"))
print("Murder answer 'Aryan Malhotra':", check_murder("Aryan Malhotra"))
print()
print("⚠️  One question remains:")
print("Vikram Malhotra - murder.")
print("Handwriting on suicide note - doesn't match.")
print("Who really killed him?")
print()
print("🔜 PART 2 - COMING SOON")
print("=" * 60)

conn.close()
print(f"\nDatabase: {DB_PATH}")
