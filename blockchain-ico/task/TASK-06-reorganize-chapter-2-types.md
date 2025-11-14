# TASK 06: Reorganize Ch2 Token Types

**Status:** 🔴 Not Started
**Priority:** ⭐⭐⭐ HIGH
**Estimated Time:** 2.5 hours
**Phase:** 2 - Chapter 2 Token Economics
**Dependencies:** TASK-05 (audit complete)

---

## 📋 OBJECTIVES

1. **Streamline files 01+02** (Introduction + Token Types)
2. **Remove duplicate classification** explanations
3. **Assign Bitcoin Pizza Day** as PRIMARY example in this file
4. **Create clear taxonomy** of token types (payment, utility, governance, security)
5. **Add business context** for each type with ONE primary example

## 📂 INPUT/OUTPUT FILES

**INPUT:**
- `chapter-02\01-gioi-thieu-token-economics.md`
- `chapter-02\02-cac-loai-token.md`
- `TASK-05-chapter-2-inventory.xlsx`

**OUTPUT:**
- `chapter-02\01-token-classification.md` (merged, ~3,500 words)
- Archive old files

## 📊 DETAILED STEPS

### Step 1: Merge Introduction (30 min)
- Keep token economics definition from file 01
- Remove redundant "what is a token" explanations
- Focus on WHY token economics matters for business

### Step 2: Create Token Type Taxonomy (1.5 hours)
Structure:
```markdown
# 2.1 Phân Loại Token

## 2.1.1 Payment Tokens (Token Thanh Toán)
**Primary Example: Bitcoin Pizza Day**
[Full story: 10,000 BTC for 2 pizzas, May 2010]
- Demonstrates token as medium of exchange
- Business lesson: early adoption volatility
- Cross-ref: Chapter 1 for Bitcoin history

## 2.1.2 Utility Tokens
**Primary Example: Ethereum Gas**
[How gas powers smart contracts]
- Not told in full elsewhere
- Link to file 03 for supply design

## 2.1.3 Governance Tokens
**Primary Example: Uniswap (UNI)**
[Brief overview, detailed in file 05 incentives]

## 2.1.4 Security Tokens
**Primary Example: tZERO**
[Regulated security token platform]
- Cross-ref Chapter 4 for legal classification
```

### Step 3: Remove Duplicates (30 min)
- Delete Bitcoin Pizza Day from overview (keep Ch2 as primary)
- Delete Ethereum gas explanation from overview
- Ensure each example appears ONCE with full detail

### Step 4: Add Cross-References (10 min)
- Link to Chapter 1 (ICO history)
- Link to Chapter 4 (Howey test, security classification)
- Link forward to file 03 (supply design examples)

## ✅ SUCCESS CRITERIA

- [ ] Merged file created (~3,500 words)
- [ ] Bitcoin Pizza Day is PRIMARY home (full detail)
- [ ] 4 token types clearly defined with business context
- [ ] ONE primary example per type
- [ ] No duplication with overview
- [ ] Cross-references added

## ⏱️ TIME BREAKDOWN
- Merge intro: 30 min
- Create taxonomy: 90 min
- Remove duplicates: 30 min
- Cross-references: 10 min
- **Total:** 2.5 hours

---

**NEXT TASK:** TASK-07 (Supply design)

---

**END OF TASK 06**
