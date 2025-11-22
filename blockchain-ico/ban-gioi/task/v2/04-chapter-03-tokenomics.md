# TASK 03: VIẾT CHƯƠNG 3 - TOKENOMICS CƠ BẢN (VERSION 2.0)

**Ngày tạo:** 22/11/2025  
**Ưu tiên:** Cao Nhất (Critical)  
**Thời gian ước tính:** 7-10 ngày

**FILE KẾT QUẢ:** `blockchain-ico\ban-gioi\internal-book-v2\chuong-03-tokenomics.md`

---

## MỤC TIÊU CHƯƠNG

Viết lại TOÀN BỘ Chương 3 - đây là chương phức tạp nhất với nhiều thay đổi:
- Dynamic supply model (mint/burn như Ethereum)
- Market-driven halving mechanism
- Dynamic burn rates based on price tiers
- Anti-whale mechanisms
- New distribution (no BGS, platform holds zero BG)

**Thay đổi chính so với V1:**
- Status: Major revisions (~70% content change - highest)
- Word count: 8,000 từ (V1: 6,500) - Longest chapter
- Focus: Mathematical models, economic mechanisms

---

## CẤU TRÚC CHƯƠNG

### Phần 1: Supply Mechanism Revolution (1,500 từ)
**V1 vs V2 comparison:**
- ❌ Fixed 1B supply → Problems: Inflexible, artificial scarcity
- ✅ Dynamic mint/burn → Benefits: Adaptive, market-responsive

**Ethereum EIP-1559 case study:**
- Base fee burn mechanism
- 4.7M+ ETH burned ($12B+ value)
- Net deflation periods when demand high

**Formula:**
```
New_Supply(t) = Supply(t-1) + Minted_Rewards(t) - Burned_Fees(t)
```

### Phần 2: Market-Driven Halving (1,800 từ)
**Không như Bitcoin (time-based), BG dùng milestone-based:**

**Halving Triggers:**
1. TVL in staking > $10M → 50% reduction
2. MAU > 5M → 25% reduction  
3. Annual revenue > $5M → 12.5% reduction
4. Market cap > $100M → 6.25% reduction

**Formula:**
```
Current_Reward = Base_Reward × (0.5 ^ halving_count)
Phase 1: 100 BG/day
Phase 2: 50 BG/day  
Phase 3: 25 BG/day
Phase 4: 12.5 BG/day
```

**Case studies:**
- Bitcoin halving history (2012, 2016, 2020, 2024)
- Helium (HNT) 2-year halvings
- Counter-example: Axie SLP (no halving = hyperinflation)

### Phần 3: Dynamic Burn Mechanisms (1,800 từ)
**Three-tier price-responsive system:**

**Tier 1 - Normal Market (Price ≤ 1.2× target):**
- Premium subs: 50% burn
- NFT certs: 50% burn
- Platform fees: 50% burn

**Tier 2 - Hot Market (1.2× < Price ≤ 2× target):**
- Premium: 75% burn
- NFT: 75% burn
- Fees: 70% burn

**Tier 3 - Overheated (Price > 2× target):**
- Premium: 90% burn
- NFT: 90% burn
- Fees: 85% burn
- PLUS: 1% transfer tax (all burned)

**Technical implementation:**
- Chainlink/Band Protocol price oracle
- Smart contract auto-adjusts every 24h
- Public dashboard for transparency

**Case studies:**
- BNB quarterly burns: $9.5B+ total
- MakerDAO stability fee burns

### Phần 4: Distribution (No Platform Holdings) (1,500 từ)
**New allocation pie chart:**
- 40% Community Rewards (Learn/Teach-to-Earn)
- 25% Team/Advisors (4-year vesting)
- 20% Ecosystem Fund (multisig, not platform)
- 15% Public Sale

**❌ Platform Treasury: 0%**

**Why zero platform holdings:**
- No conflict of interest
- Platform revenue = fiat (VND/USD)
- Token circulation pure
- Regulatory clarity (not a security)

**Comparison:**
- Brave Browser: BAT circulates, Brave Inc earns fiat
- Failed: Terra (LFG held massive UST = death spiral)

### Phần 5: Anti-Whale Mechanisms (1,400 từ)
**Progressive transaction tax:**
```
< 1K BG: 0% tax
1K-10K: 0.5% tax (burned)
10K-100K: 1% tax  
≥ 100K: 2% tax
```

**Quadratic voting:**
```
Voting_Power = sqrt(veBG_balance)
100 veBG → 10 power
10,000 veBG → 100 power (100x stake = 10x power only)
```

**Governance wallet cap:**
- Max 100,000 veBG counts for voting per wallet
- Sybil detection via on-chain analysis

**Staking lockup penalty:**
- Early unstake: 10% penalty (burned)
- Minimum stake: 30 days for max rewards

**Case studies:**
- Olympus DAO quadratic voting success
- Mango Markets: Whale manipulation with $110M
- Beanstalk flash loan attack ($182M)

---

## TÀI LIỆU THAM KHẢO

### Must-read:
- Ethereum EIP-1559 full documentation
- Bitcoin halving economics research
- BNB burn mechanism analysis
- Terra/Luna collapse post-mortem
- Axie Infinity tokenomics failure analysis

### Data cần verify:
- ETH burned: >4.7M (check latest EtherScan)
- BNB total burn: $9.5B+ (verify Binance reports)
- Bitcoin halving dates: 2012, 2016, 2020, 2024
- Helium HNT halving schedule

---

**Thời hạn:** 10 ngày (longest task)
**Output:** 8,000 từ markdown
**Priority:** CRITICAL - foundation cho toàn bộ economics