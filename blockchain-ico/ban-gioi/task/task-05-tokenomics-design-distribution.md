# TASK 05: VIẾT CHƯƠNG VỀ THIẾT KẾ TOKENOMICS & PHÂN PHỐI

**Ngày tạo:** 18/11/2025  
**Ưu tiên:** Rất Cao  
**Thời gian:** 6-8 ngày

**FILE KẾT QUẢ:** `blockchain-ico\ban-gioi\internal-book\chuong-05-tokenomics-design-distribution.md`

---

## MỤC TIÊU

Viết chương chi tiết về thiết kế tokenomics và phân phối token cho BG, bao gồm:
- Total supply design và rationale
- Token allocation chi tiết từng category
- Vesting schedules cho team, advisors, investors
- Emission schedule và inflation control
- Supply management và deflationary mechanisms
- Comparisons với successful projects

---

## YÊU CẦU VIẾT

✅ Narrative flow, 100% tiếng Việt, case studies  
❌ Không bullets rời, không Anh-Việt mix

---

## CẤU TRÚC CHƯƠNG

### Phần 1: Total Supply Design (3,000-3,500 từ)

**Vấn đề:** Nên có bao nhiêu token?

**Nội dung:**
- Hard cap vs No cap
  - Bitcoin: 21M (scarcity model)
  - Ethereum: No cap (utility model)
  - BNB: 200M → 100M (burn to target)
  
- Psychology of numbers
  - 100M vs 1B vs 10B
  - User perception
  - Price psychology
  
- BG Recommendation: 1 Billion BG
  - Rationale: Easy mental math
  - Room for growth
  - Divisibility: 18 decimals
  
**Case studies:**
- Bitcoin: 21M scarcity premium
- Ethereum: Unlimited → Ultra-sound (-2% post-Merge)
- BNB: Quarterly burns từ $200M → $100M target
- SHIB: 1 Quadrillion (too many → confusion)

### Phần 2: Token Allocation (4,000-5,000 từ)

**Distribution Breakdown:**

**Community Rewards: 40% (400M)**
- Learn-to-earn: 200M
- Teach-to-earn: 100M
- Content creation: 50M
- Community growth: 50M
- Emission: 5 years linear

**Ecosystem Fund: 20% (200M)**
- Partnerships: 80M
- Grants: 60M
- Liquidity incentives: 40M
- Marketing: 20M
- Controlled by DAO later

**Team: 15% (150M)**
- Founders: 100M
- Core team: 50M
- Vesting: 4 years, 1-year cliff
- Rationale: Align long-term

**Investors (Community Sale): 10% (100M)**
- Public sale: 80M
- Strategic: 20M
- Vesting: 20% TGE, 80% over 6-12 months

**Liquidity: 10% (100M)**
- DEX pairs: 60M (BG/ETH, BG/USDC)
- CEX if needed: 40M
- Locked LP tokens

**Advisors: 2% (20M)**
- Education experts: 10M
- Tech advisors: 5M
- Business advisors: 5M
- Vesting: 2 years

**Treasury: 5% (50M)**
- Emergency fund
- Future initiatives
- Multi-sig controlled

**Why This Allocation:**
- Community-first: 40% earned
- Long-term aligned: 15% team vested
- Fair sale: 10% only
- Sustainable ecosystem: 20% fund

**Comparisons:**

| Project | Community | Team | Sale | Ecosystem |
|---------|-----------|------|------|----------|
| Ethereum | 0% | 15% | 75% | 10% |
| Uniswap | 60% | 21% | 0% | 19% |
| Compound | 56% | 26% | 0% | 18% |
| BG (Proposal) | 40% | 15% | 10% | 20% |

### Phần 3: Vesting Schedules (3,000-3,500 từ)

**Team Vesting (Critical):**

**Structure:**
- Cliff: 12 months (no tokens)
- Then: Linear 36 months
- Total: 4 years
- Monthly unlock: 1/48 after cliff

**Example: Founder với 50M tokens**
- Month 0-12: 0 tokens
- Month 13: 50M / 48 = 1.04M unlock
- Month 14-48: 1.04M/month
- After 4 years: 100% unlocked

**Why 4 years:**
- Industry standard
- Proves commitment
- Aligns incentives
- Reduces early dumps

**Case study: Ethereum Team Vesting**
- Vitalik: Sold very little
- Core team: Long-term holders
- Result: Aligned with success

**Case study: EOS Team Exit**
- Dan Larimer left after 3 years
- Third project he abandoned
- Community trust damaged
- Lesson: Vesting not enough, need commitment

**Investor Vesting:**

**Structure:**
- TGE: 20% unlock
- Linear: 6-12 months
- Monthly or continuous

**Rationale:**
- Some liquidity immediately
- Prevents dumps
- Fair for believers
- Market stability

**Advisor Vesting:**
- Cliff: 6 months
- Linear: 18 months
- Total: 2 years
- Shorter than team (advisory role)

### Phần 4: Emission Schedule (3,500-4,000 từ)

**Community Rewards Emission:**

**Model: Decreasing Emission**
- Year 1: 150M (37.5% of 400M)
- Year 2: 100M (25%)
- Year 3: 75M (18.75%)
- Year 4: 50M (12.5%)
- Year 5: 25M (6.25%)
- Total: 400M over 5 years

**Rationale:**
- Early: High rewards → Bootstrap network
- Later: Lower rewards → Sustainable
- Follows Bitcoin halving philosophy

**Daily Emission (Year 1):**
- 150M / 365 = ~411K BG/day
- Distributed:
  - Learning: 200K BG
  - Teaching: 100K BG
  - Content: 50K BG
  - Community: 61K BG

**Inflation Rate:**

**Year 1:**
- Starting supply: 200M (liquidity + sales)
- Emission: 150M
- Inflation: 75%
- High but acceptable for growth phase

**Year 2:**
- Supply: 350M
- Emission: 100M
- Inflation: 28.5%
- Decreasing

**Year 5:**
- Supply: 500M
- Emission: 25M
- Inflation: 5%
- Low, sustainable

**Long-term (Year 5+):**
- Emission ends
- Burns > New issuance
- Deflationary
- Supply decreases over time

**Case studies:**

**Bitcoin Halving:**
- Every 4 years: Emission cut 50%
- 50 → 25 → 12.5 → 6.25 → 3.125 BTC/block
- Creates scarcity
- Price appreciation historically follows

**Ethereum Post-Merge:**
- Pre-Merge: ~4.5% inflation
- Post-Merge: ~0.5% inflation
- With EIP-1559 burns: -2% to -5%
- Deflationary = "Ultra-sound money"

**Curve CRV:**
- High emission early (2020-2022)
- Decreasing emission over 300 years
- Locks via veCRV reduce circulating

### Phần 5: Supply Management (2,500-3,000 từ)

**Deflationary Mechanisms:**

**1. Transaction Burns (5%)**
- Every BG transfer: 5% burned
- Example: Send 100 BG → 95 received, 5 burned
- Permanent removal
- Decreases supply over time

**2. NFT Minting Burns**
- Certificate NFT: 20-50 BG burned
- Achievement NFT: 10-20 BG
- Profile NFT: 50-100 BG
- High engagement → More burns

**3. Platform Fee Burns**
- Marketplace: 2.5% fee
- 50% burned, 50% treasury
- Example: $100 transaction → $2.50 fee → $1.25 burned

**4. Buyback & Burn (Primary)**
- 30-50% profit → Buy BG
- 100% bought → Burned
- Quarterly execution
- Transparent reporting

**Calculation Example:**

**Scenario: Year 3**
- Circulating: 400M BG
- Quarterly profit: $200K
- Buyback allocation: 40% = $80K
- BG price: $0.10
- Buy: 800K BG
- Burn: 800K BG
- New circulating: 399.2M

**Annual:**
- 4 quarters × 800K = 3.2M burned
- Burn rate: 0.8%/year from buyback
- Plus burns from transactions, NFTs
- Total burn: 2-3%/year

**Long-term Projection:**

**Year 5:**
- Emission ends: 0
- Burns continue: 2-3%/year
- Supply: Decreasing
- Price pressure: Upward

**Year 10:**
- Original 1B → ~700-800M remaining
- Scarcity increases
- Demand (if successful) increases
- Economics: Deflationary

**Case study: BNB Burns**
- Started 200M supply
- Target: 100M (50% burn)
- Quarterly burns: $13B+ total burned
- Mechanism: 20% profit + trading fees
- Result: Supply↓, Price↑ (long-term)

### Phần 6: Comparisons & Best Practices (2,000-2,500 từ)

**Learning from Successes:**

**Uniswap UNI:**
- ✅ 60% community (airdrop + liquidity mining)
- ✅ 21% team (4-year vest)
- ✅ 18% investors (4-year vest)
- ✅ Fair launch, no pre-mine
- Result: Widely distributed, strong community

**MakerDAO MKR:**
- ✅ No pre-mine
- ✅ Burns from fees (deflationary)
- ✅ Governance aligned
- Result: Sustainable, profitable

**Ethereum:**
- ⚠️ 75% ICO (too high)
- ✅ 15% Foundation/Team
- ✅ Long-term vision
- ✅ Eventually deflationary (EIP-1559)
- Result: Successful despite high ICO%

**Learning from Failures:**

**Axie Infinity SLP:**
- ❌ Infinite supply
- ❌ No burns initially
- ❌ Emission >> Demand
- Result: SLP $0.40 → $0.001 (99.75% drop)
- Fix: Added burns late, but damage done

**Terra UST/LUNA:**
- ❌ Infinite LUNA minting
- ❌ Death spiral mechanics
- ❌ No circuit breakers
- Result: $60B evaporated

**EOS:**
- ❌ 10% team (but founder left)
- ❌ No clear value accrual
- ❌ Inflation with no burns
- Result: Failed to deliver

**Best Practices for BG:**
1. ✅ Community-first allocation (40%)
2. ✅ Team vested long-term (4 years)
3. ✅ Limited sale (10%)
4. ✅ Decreasing emission (halving-like)
5. ✅ Multiple burn mechanisms
6. ✅ Buyback from profits
7. ✅ Transparent reporting

### Phần 7: Kết Luận (1,500-2,000 từ)

**Final BG Tokenomics:**

- Total: 1B BG
- Community: 40% (earn over 5 years)
- Ecosystem: 20% (controlled release)
- Team: 15% (4-year vest)
- Sale: 10% (limited)
- Liquidity: 10%
- Advisors: 2% (2-year vest)
- Treasury: 3%

**Emissions:**
- Year 1-5: Decreasing schedule
- Year 5+: Zero emission
- Burns: Continuous
- Long-term: Deflationary

**Why This Works:**
- Aligns all stakeholders
- Rewards actual usage
- Sustainable economics
- Scarcity over time
- Proven models

**Action Items:**
1. Finalize exact numbers
2. Legal review
3. Smart contract development
4. Audit vesting contracts
5. Prepare documentation
6. Community education

---

## CHECKLIST

- [ ] All allocations justified
- [ ] Vesting schedules detailed
- [ ] Emission math verified
- [ ] Case studies with data
- [ ] Comparisons accurate
- [ ] 100% tiếng Việt
- [ ] Narrative flow

---

## TÀI LIỆU THAM KHẢO

- Bitcoin halving schedule
- Ethereum tokenomics evolution
- Uniswap UNI allocation
- MakerDAO MKR burns
- BNB burn history
- Axie SLP hyperinflation
- Terra/Luna death spiral
- Industry research: Messari, Dune Analytics

---

**Thời hạn:** 8 ngày  
**Output:** 16,000-20,000 từ
