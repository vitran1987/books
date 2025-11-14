# TASK 07: Reorganize Ch2 Supply Design

**Status:** 🔴 Not Started
**Priority:** ⭐⭐⭐ HIGH
**Estimated Time:** 2.5 hours
**Phase:** 2 - Chapter 2 Token Economics
**Dependencies:** TASK-06 (token types complete)

---

## 📋 OBJECTIVES

1. **Streamline file 03** (Supply Design)
2. **Assign Binance Coin (BNB) burn** as PRIMARY example
3. **Cover supply mechanisms:** fixed, inflationary, deflationary, dynamic
4. **Remove duplicate Bitcoin halving** explanation (if in overview)
5. **Add business implications** of each supply model

## 📂 INPUT/OUTPUT FILES

**INPUT:**
- `chapter-02\03-thiet-ke-nguon-cung.md`
- `TASK-05-chapter-2-inventory.xlsx`
- Condensed overview (to check Bitcoin halving duplication)

**OUTPUT:**
- `chapter-02\02-token-supply-design.md` (~3,000 words)

## 📊 DETAILED STEPS

### Step 1: Define Supply Models (1 hour)
```markdown
# 2.2 Thiết Kế Nguồn Cung Token

## 2.2.1 Fixed Supply (Nguồn Cung Cố Định)
**Primary Example: Bitcoin Halving Schedule**
- 21 million cap
- Halving every 210,000 blocks
- Business logic: scarcity-driven value
- Chart: Supply curve over time

## 2.2.2 Deflationary Supply (Giảm Dần)
**Primary Example: Binance Coin (BNB) Quarterly Burns**
[FULL DETAIL - this is THE primary home for BNB story]
- Started with 200M BNB (2017)
- Quarterly burn based on trading volume
- Target: burn to 100M BNB total
- Auto-burn mechanism (2021 upgrade)
- Business impact: ↓supply + ↑demand = price support
- Real data: Q1 2024 burned X BNB, worth $Y

## 2.2.3 Inflationary Supply
**Primary Example: Ethereum post-Merge**
- Staking rewards create new ETH
- Burned through EIP-1559
- Net inflation ~0.5% annually

## 2.2.4 Dynamic Supply
**Primary Example: Ampleforth (AMPL) rebasing**
- Supply adjusts based on price oracle
- Elastic supply mechanism
```

### Step 2: Add Business Context (45 min)
For each model, explain:
- When to use this supply design
- Trade-offs (scarcity vs flexibility)
- Real-world business outcomes
- Regulatory considerations

### Step 3: Remove Duplicates (30 min)
- Check if BNB burn story appears in overview or file 05
- Check if Bitcoin halving is duplicated in overview
- Keep DETAILED version here, make others brief cross-refs

### Step 4: Verify Data (15 min)
- Confirm latest BNB burn data (Binance announcements)
- Verify Bitcoin halving schedule
- Check Ethereum inflation rate post-Merge

## ✅ SUCCESS CRITERIA

- [ ] File `02-token-supply-design.md` created (~3,000 words)
- [ ] BNB burn is PRIMARY home (full quarterly data)
- [ ] 4 supply models clearly defined
- [ ] Business context for each model
- [ ] All data verified and current
- [ ] No duplication with overview or other chapters

## ⏱️ TIME BREAKDOWN
- Define supply models: 60 min
- Add business context: 45 min
- Remove duplicates: 30 min
- Verify data: 15 min
- **Total:** 2.5 hours

---

**NEXT TASK:** TASK-08 (Distribution mechanisms)

---

**END OF TASK 07**
