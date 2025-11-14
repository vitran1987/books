# TASK 03: Reorganize Ch1 Files 02,03,05,06-08

**Status:** ✅ COMPLETED
**Priority:** ⭐⭐⭐ HIGH
**Estimated Time:** 4 hours
**Phase:** 1 - Chapter 1 Restructure
**Dependencies:** TASK-02 (merged history file)

---

## 📋 OBJECTIVES

1. **Reorganize 6 remaining Chapter 1 files** into logical sections
2. **Remove duplicate examples** that appear in overview or other chapters
3. **Create focused subsections** for token types, utilities, valuation
4. **Streamline case studies** - keep only relevant to Chapter 1 themes
5. **Prepare foundation** for Lessons Learned section (TASK-04)

## 📂 INPUT/OUTPUT FILES

**INPUT:**

- `chapter-01\02-token-types.md`
- `chapter-01\03-token-utility.md`
- `chapter-01\05-valuation.md`
- `chapter-01\06-risks.md`
- `chapter-01\07-regulatory.md`
- `chapter-01\08-future-trends.md`
- `TASK-01-content-inventory.xlsx` (audit results)

**OUTPUT:**

- `chapter-01\02-ico-mechanics.md` (merged token types + utility)
- `chapter-01\03-valuation-risks.md` (merged valuation + risks)
- Move regulatory content → Chapter 4
- Move future trends → Chapter 10
- `task\outputs\TASK-03-reorganization-log.md`

## 📊 DETAILED STEPS

### Step 1: Merge Token Content (1.5 hours)

Combine files 02 and 03 into `02-ico-mechanics.md`:

- Token standards (ERC-20, ERC-721)
- Utility vs Security classification
- Primary use cases (payment, governance, access)
- Remove examples covered in Chapter 2

### Step 2: Merge Valuation + Risks (1 hour)

Combine files 05 and 06 into `03-valuation-risks.md`:

- Network value metrics
- Token velocity concepts
- Common risks (scams, technical failures)
- Reference Chapter 2 for specific valuation models

### Step 3: Redistribute Content (1 hour)

- Move file 07 content → Chapter 4 (regulations)
- Move file 08 content → Chapter 10 (future)
- Update cross-references

### Step 4: Document Changes (30 min)

Create reorganization log:

- What was merged
- What was moved
- What was deleted
- Word count changes

## ✅ SUCCESS CRITERIA

- [ ] Files 02+03 merged into `02-ico-mechanics.md` (~3,500 words)
- [ ] Files 05+06 merged into `03-valuation-risks.md` (~3,000 words)
- [ ] Regulatory content moved to Chapter 4 notes
- [ ] Future trends moved to Chapter 10 notes
- [ ] No duplicate examples from overview
- [ ] Reorganization log complete

## ⏱️ TIME BREAKDOWN

- Merge token files: 90 min
- Merge valuation/risks: 60 min
- Redistribute content: 60 min
- Documentation: 30 min
- **Total:** 4 hours

---

**NEXT TASK:** TASK-04 (Create Lessons Learned)

---

**END OF TASK 03**
