const express = require('express');
const cors = require('cors');
const path = require('path');
const fs = require('fs');
const Database = require('better-sqlite3');

const app = express();
app.use(cors());
app.use(express.json());
app.use(express.static('.'));

// ════════════════════════════════════════
// CAP PAYMENT SIMULATION
// Real CROO CAP se connect hoga production mein
// ════════════════════════════════════════

const payments = {}; // session_id -> payment info

// Simulated wallet balances
const wallets = {
  "0x7f3a9b2c": { balance: 10.0, name: "Player Wallet" },
  "0xCASEQUERY": { balance: 0.0, name: "CaseQuery Agent" }
};

// ── STAKE ENDPOINT ──
app.post('/api/stake', (req, res) => {
  const { session_id, case_id, amount, wallet } = req.body;

  console.log(`[CAP] Stake request: ${amount} USDC for case #${case_id}`);

  // Simulate CAP transaction
  const txHash = '0x' + Math.random().toString(16).substr(2, 40);

  payments[session_id] = {
    case_id,
    amount,
    wallet,
    tx_hash: txHash,
    status: 'staked',
    timestamp: new Date().toISOString()
  };

  // Deduct from player wallet (simulation)
  if (wallets[wallet]) {
    wallets[wallet].balance -= amount;
  }

  console.log(`[CAP] ✓ Staked ${amount} USDC | TX: ${txHash}`);

  res.json({
    success: true,
    tx_hash: txHash,
    message: `${amount} USDC staked via CAP Protocol`,
    cap_endpoint: "https://api.croo.network/cap/v1/stake",
    timestamp: new Date().toISOString()
  });
});

// ── PAYOUT ENDPOINT ──
app.post('/api/payout', (req, res) => {
  const { session_id, correct } = req.body;
  const payment = payments[session_id];

  if (!payment) {
    return res.json({ success: false, message: "No stake found" });
  }

  if (correct) {
    const winAmount = payment.amount * 1.5;
    const txHash = '0x' + Math.random().toString(16).substr(2, 40);

    // Add to player wallet (simulation)
    if (wallets[payment.wallet]) {
      wallets[payment.wallet].balance += winAmount;
    }

    payment.status = 'paid_out';
    payment.win_amount = winAmount;
    payment.win_tx = txHash;

    console.log(`[CAP] ✓ Payout ${winAmount} USDC | TX: ${txHash}`);

    res.json({
      success: true,
      won: true,
      amount: winAmount,
      tx_hash: txHash,
      message: `${winAmount} USDC sent via CAP Protocol`,
      cap_endpoint: "https://api.croo.network/cap/v1/payout"
    });
  } else {
    payment.status = 'forfeited';
    console.log(`[CAP] ✗ Stake forfeited: ${payment.amount} USDC`);

    res.json({
      success: true,
      won: false,
      message: "Stake forfeited. Try again!",
    });
  }
});

// ── WALLET BALANCE ──
app.get('/api/wallet/:address', (req, res) => {
  const wallet = wallets[req.params.address];
  res.json({
    address: req.params.address,
    balance: wallet ? wallet.balance : 10.0,
    currency: "USDC",
    network: "CROO Testnet"
  });
});

// ── SQL QUERY ENDPOINT ──
app.post('/api/query', (req, res) => {
  const { case_id, query } = req.body;

  // Security — sirf SELECT allowed
  const q = query.trim().toLowerCase();
  if (!q.startsWith('select') && !q.startsWith('pragma')) {
    return res.json({
      success: false,
      error: "Only SELECT queries allowed. No DROP, DELETE, INSERT, UPDATE."
    });
  }

  // Dangerous keywords block karo
  const blocked = ['drop','delete','insert','update','alter','create','truncate'];
  if (blocked.some(b => q.includes(b))) {
    return res.json({
      success: false,
      error: "Dangerous query detected. Only SELECT allowed."
    });
  }

  try {
    const dbPath = path.join(__dirname, `case_00${case_id}.db`);
    if (!fs.existsSync(dbPath)) {
      return res.json({
        success: false,
        error: `Database for case ${case_id} not found. Run setup first.`
      });
    }

    const db = new Database(dbPath, { readonly: true });
    const rows = db.prepare(query).all().map(r => {
      const obj = {};
      for (const [k, v] of Object.entries(r)) {
        obj[k] = v === null ? null : v;
      }
      return obj;
    });
    db.close();
    res.json({ success: true, rows, count: rows.length });

  } catch (err) {
    res.json({
      success: false,
      error: err.message.split('\n')[0]
    });
  }
});

// ── VERIFY ANSWER ──
app.post('/api/verify', (req, res) => {
  const { case_id, answer } = req.body;

  const answers = {
    1: ["tim becker", "tom becker", "tim", "tom"],
    2: ["rahul desai", "inspector rahul", "rahul", "inspector rahul desai"],
    3: ["aryan malhotra", "joi sharma", "aryan and joi", "aryan + joi", "aryan", "both"]
  };

  const correct = answers[case_id] || [];
  const isCorrect = correct.some(a =>
    answer.toLowerCase().includes(a) ||
    a.includes(answer.toLowerCase())
  );

  const correctAnswers = {
    1: "Tim Becker (murder) + Tom Becker (chori)",
    2: "Inspector Rahul Desai",
    3: "Ghost_X = Aryan Malhotra + Joi Sharma"
  };

  console.log(`[GAME] Case #${case_id} answer: "${answer}" → ${isCorrect ? '✓ CORRECT' : '✗ WRONG'}`);

  res.json({
    correct: isCorrect,
    correct_answer: isCorrect ? correctAnswers[case_id] : null
  });
});

// ── CASE INFO ──
app.get('/api/cases', (req, res) => {
  res.json({
    cases: [
      {
        id: 1,
        title: "The Greenline Double Cross",
        difficulty: "Hard",
        stake: 1,
        win: 1.5,
        tables: ["suspects","access_logs","alibis","transactions",
                 "cctv_logs","call_logs","delivery_orders",
                 "evidence","psychological_records","family_records"]
      },
      {
        id: 2,
        title: "The Deshpande Murder",
        difficulty: "Medium",
        stake: 1,
        win: 1.5,
        tables: ["suspects","access_logs","watch_evidence","phone_records",
                 "forensic_report","cctv_logs","blackmail_records","background_records"]
      },
      {
        id: 3,
        title: "The Ghost Protocol",
        difficulty: "Expert",
        stake: 2,
        win: 3,
        tables: ["suspects","transactions","smart_contracts","croo_agent_store",
                 "dark_web_messages","wallet_connections","nexvault_victims",
                 "evidence","diary_entries","vikram_case_files"]
      }
    ]
  });
});

// ── ROOT REDIRECT ──
app.get('/', (req, res) => {
  res.redirect('/casequery.html');
});
app.get('/chat', (req, res) => {
  res.redirect('/casequery_chatbot.html');
});

// ── HEALTH CHECK ──
app.get('/api/health', (req, res) => {
  res.json({
    status: "online",
    service: "CaseQuery Agent",
    network: "CROO Testnet",
    cap_protocol: "v1.0",
    cases_loaded: 3,
    timestamp: new Date().toISOString()
  });
});

// ── START SERVER ──
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`
╔═══════════════════════════════════════╗
║   CaseQuery Agent — CROO Network      ║
║   Server running on port ${PORT}          ║
║   CAP Protocol: ACTIVE                ║
║   Cases loaded: 3                     ║
╚═══════════════════════════════════════╝

Open: http://localhost:${PORT}/casequery.html
Chat: http://localhost:${PORT}/casequery_chatbot.html
API:  http://localhost:${PORT}/api/health
  `);
});
