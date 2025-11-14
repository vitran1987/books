# TASK 12: Create Ch3 IDO Section

**Status:** 🔴 Not Started
**Priority:** ⭐⭐ MEDIUM
**Estimated Time:** 3 hours
**Phase:** 3 - New Chapters (Ch3: IEO, IDO, Launchpads)
**Dependencies:** TASK-11 (IEO context)

---

## 📋 OBJECTIVES

1. **Create Chapter 3 Part 2:** IDO (Initial DEX Offering)
2. **Explain decentralized fundraising** via DEX platforms
3. **Use PancakeSwap IDO** as primary example
4. **Compare IDO vs IEO** centralized vs decentralized trade-offs
5. **Cover risks:** rug pulls, front-running, impermanent loss

## 📂 INPUT/OUTPUT FILES

**INPUT:**
- `chapter-03\01-ieo-initial-exchange-offering.md` (for comparison)
- Research: PancakeSwap IDO statistics, rug pull data

**OUTPUT:**
- `chapter-03\02-ido-initial-dex-offering.md` (~3,500 words)

## 📊 DETAILED STEPS

### Step 1: Research IDO Ecosystem (45 min)
- When did IDO emerge? (2020, DeFi summer)
- Major platforms: PancakeSwap, Uniswap, Polkastarter
- Success stories vs scams ratio
- Regulatory concerns (completely permissionless)

### Step 2: Write IDO Fundamentals (1.5 hours)
```markdown
## 3.2 IDO - Fundraising Phân Tán

### 3.2.1 Từ IEO Đến IDO
- IEO problem: Exchange gatekeepers, centralized control
- DeFi boom 2020: demand for permissionless systems
- IDO solution: Automated Market Maker (AMM) platforms

### 3.2.2 IDO Hoạt Động Như Thế Nào?
- Project creates liquidity pool on DEX
- Users buy tokens directly from pool
- No exchange approval needed
- Instant trading after sale

### 3.2.3 PancakeSwap: Case Study
**Primary Example:**
- Platform: BSC (Binance Smart Chain) DEX
- IFO (Initial Farm Offering) model:
  - Users stake CAKE tokens
  - Commit CAKE or BNB to IDO
  - Receive new tokens
- Notable IDOs: [research 2-3 successful projects]
- Accessibility: Anyone with wallet can participate

### 3.2.4 IDO Business Model
**For DEX Platforms:**
- Trading fees from new pool
- Increased liquidity and users
- No vetting responsibility (automated)

**For Projects:**
- Lower cost (no listing fees)
- Instant liquidity
- Permissionless listing
- Risk: No credibility signal from platform

### 3.2.5 Risks and Scams
**Rug Pulls:**
- Example: Squid Game token (2021)
  - Price pumped 230,000% in days
  - Developers removed liquidity
  - Investors lost millions
- Prevention: Liquidity locks, audits, team doxxing

**Front-Running:**
- Bots detect transactions
- Submit higher gas to buy first
- Hurts retail investors

**Impermanent Loss:**
- For liquidity providers
- Price volatility reduces returns
```

### Step 3: Add Comparisons (30 min)
Table: IEO vs IDO
| Factor | IEO | IDO |
|--------|-----|-----|
| Platform | Centralized Exchange | Decentralized Exchange |
| Vetting | Exchange review | None (permissionless) |
| Cost | High (listing fees) | Low (gas fees only) |
| Accessibility | KYC required | Wallet only |
| Risk | Exchange trust | Rug pull risk |
| Regulation | Clear (exchange liable) | Unclear (no intermediary) |

### Step 4: Link to DeFi (15 min)
- IDO is part of DeFi ecosystem
- Transition to Chapter 5 (DeFi deeper dive)

## ✅ SUCCESS CRITERIA

- [ ] File `02-ido-initial-dex-offering.md` created (~3,500 words)
- [ ] PancakeSwap IDO process explained with examples
- [ ] Rug pull case study (Squid Game or similar)
- [ ] IEO vs IDO comparison table
- [ ] Risk section covers front-running, impermanent loss
- [ ] Transition to launchpads (TASK-13)

## ⏱️ TIME BREAKDOWN
- Research: 45 min
- Write fundamentals: 90 min
- Comparisons: 30 min
- Link to DeFi: 15 min
- **Total:** 3 hours

---

**NEXT TASK:** TASK-13 (Launchpads & Airdrops)

---

**END OF TASK 12**
