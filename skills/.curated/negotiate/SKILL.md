---
name: negotiate
description: Use when preparing for, responding during, or analyzing a pricing/commercial negotiation. Builds a personal negotiation advisor with prep, live, and analyze modes using BATNA, reservation point, target price, ZOPA, anchoring, MESO packages, and cognitive-bias checks.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [negotiation, pricing, sales, BATNA, MESO, anchoring, cognitive-bias]
    related_skills: []
---

# NEGOTIATE

## Overview

Use this skill as a personal negotiation advisor for pricing, sales, freelance, salary, procurement, and commercial deal conversations.

It works in three modes:

1. `prep` - build a pre-call negotiation brief.
2. `live` - draft a short response while negotiation is happening.
3. `analyze` - debrief the exchange, identify what moved the deal, and flag cognitive biases.

The goal is not to “win” by being clever. The goal is disciplined deal control: know your walk-away line before emotion enters, make anchors intentionally, create several acceptable paths, and avoid bad concessions.

Research base used in this skill:

- BATNA: best alternative to negotiated agreement. Your leverage comes from real alternatives, not confidence theater.
- Reservation point / walk-away line: point of indifference between taking deal and using your BATNA.
- Target point: ambitious but defensible outcome you are aiming for.
- ZOPA: zone of possible agreement; overlap between acceptable outcomes for both sides.
- Anchoring: first numbers strongly shape later numbers. Precise anchors often feel better-supported than round anchors, but too much precision can signal inflexibility.
- MESO: multiple equivalent simultaneous offers. Present up to three packages you value similarly so counterpart reveals priorities and chooses path, not just discount.
- Cognitive biases: anchoring, midpoint/splitting-the-difference pull, loss aversion, sunk cost, overconfidence, confirmation bias, reciprocity pressure, scarcity pressure, and fixed-pie thinking.

## When to Use

Use this skill for:

- Pricing calls with clients.
- Proposal review before signature.
- Salary / compensation negotiation.
- Retainers, pilots, renewal, procurement, scope-vs-price tradeoffs.
- “Budget is X” objections.
- Post-call debriefs when you want to learn what happened.

Do not use this skill for:

- Legal advice or contract-law interpretation.
- Manipulative pressure against unsophisticated or vulnerable people.
- One-shot haggling where relationship does not matter.
- Cases where truthfulness, safety, or compliance are uncertain. Get facts first.

## Mode Router

If user does not specify mode, infer it:

- Before meeting / proposal / call: use `prep`.
- User gives counterpart message and needs answer now: use `live`.
- User describes what happened: use `analyze`.

If data is missing but the situation is live, do not interrogate. Make assumptions explicit and produce response.

## Required Inputs

For best output, gather:

- Deal type: service, product, salary, procurement, partnership.
- Counterpart: role, company, buying authority, urgency.
- Offer: what is included, timeline, deliverables, risk, cost to serve.
- Your economics: desired price, minimum acceptable price, margin, capacity.
- Alternatives: other leads, current pipeline, ability to walk away.
- Their signals: stated budget, deadline, objections, decision criteria.
- Relationship goal: transactional, long-term, strategic logo, referral.
- Non-price variables: scope, payment terms, timeline, exclusivity, support, success metrics, cancellation, intro/referral, case study.

If exact economics are absent, estimate ranges and label them as assumptions.

## PREP Mode

Produce a compact negotiation brief.

### PREP Output Format

```
NEGOTIATE / prep

1. Situation
- Deal:
- Counterpart:
- Goal:
- Main risk:

2. Numbers
- Target price:
- Reservation point / red line:
- Opening anchor:
- Expected first objection:
- ZOPA estimate:

3. BATNA
- Best alternative:
- Strength: strong / medium / weak
- Proof:
- Action to improve BATNA before call:

4. Value thesis
- Outcome buyer wants:
- Cost of doing nothing:
- Why now:
- Why you:

5. Anchoring plan
- First number:
- Why precise / round:
- Justification sentence:
- If they anchor low:

6. MESO packages
A. Premium:
B. Core:
C. Lean:
Guardrail: no package below red line unless it removes enough scope/risk.

7. Concession rules
- Give only if receiving:
- Concession ladder:
- Forbidden concession:
- Walk-away phrase:

8. Bias watchlist
- Their likely biases:
- Your likely biases:
- Trap to avoid:

9. Call script
- Open:
- Budget question:
- Low anchor response:
- Close:
```

### Number Rules

- Target price should be above acceptable outcome but defensible from value, market, urgency, or cost.
- Reservation point must include opportunity cost and delivery risk, not just cash minimum.
- Opening anchor should usually be above target and inside plausible ZOPA.
- Use precise anchor when you have rationale: `18,400` feels calculated. Use round number when relationship, simplicity, or enterprise procurement matters more.
- Never create a “lean” package by simply discounting same work. Remove scope, speed, access, support, rights, payment flexibility, or risk.

### BATNA Strength Rating

Strong BATNA:
- Real alternative exists, with timing and economics.
- You can say no without major damage.

Medium BATNA:
- Alternatives plausible but not committed.
- You can delay, reduce scope, or pursue pipeline.

Weak BATNA:
- You need deal, alternatives vague, or counterpart knows urgency.
- In this case: reduce asks, trade scope, avoid bluffing, improve BATNA fast.

## LIVE Mode

Goal: short, usable language. No lecture.

### LIVE Output Format

```
NEGOTIATE / live

Send this:
"..."

Why:
- Bias/tactic addressed:
- What it preserves:
- Next move if they say yes/no:
```

### Live Response Patterns

#### If they say: “My budget is 9,000”

Use curiosity before concession:

```
What would you expect to be included for 9,000?
```

or

```
I hear you. At 9,000, which outcome matters most: speed, depth, or support after delivery?
```

Purpose: reveal their reservation point, priorities, and whether budget is real constraint or anchor.

#### If their number is below your red line

```
That is below where I can deliver this responsibly. We can either reduce scope to fit that number, or keep the outcome intact around [core price]. Which direction is more useful?
```

#### If they ask to split difference

```
I would not split it mechanically, because the gap is mostly scope/risk, not just price. I can move if we also adjust [scope/payment/timeline/support].
```

#### If they cherry-pick MESO packages

```
Those pieces work together economically. If we combine them differently, I need to rebalance one of price, timeline, or support. Here are two clean options.
```

#### If they ask for discount

```
I can reduce price if we reduce what I am carrying. For example: less support, longer timeline, upfront payment, or narrower deliverable. Which tradeoff is easiest?
```

#### If they are silent after anchor

```
What part feels off: total price, timing, scope, or confidence in outcome?
```

#### If they say “too expensive”

```
Compared to what option?
```

Then:

```
If the comparison is [cheaper alternative], the difference is mainly [risk/outcome/speed/support]. If that part is not valuable, lean package is better fit.
```

#### If they need internal approval

```
What will the approver compare this against, and what would make it easy for them to say yes?
```

#### If you want to close without sounding desperate

```
If [core package] matches the outcome, I can hold the slot until [date]. After that I need to release capacity.
```

## ANALYZE Mode

Use after call, transcript, notes, or outcome.

### ANALYZE Output Format

```
NEGOTIATE / analyze

1. Outcome
- Opened at:
- Their anchor:
- Final:
- Final vs target:
- Final vs red line:

2. What worked
- Move:
- Why it worked:
- Evidence:

3. What leaked value
- Moment:
- Bias/tactic:
- Better response:

4. Bias map
- Anchoring:
- Midpoint bias:
- Loss aversion:
- Reciprocity pressure:
- Overconfidence / fear:
- Fixed-pie thinking:

5. Counterpart priorities inferred
- Must-have:
- Nice-to-have:
- Constraint:
- Real objection vs stated objection:

6. Next playbook
- Keep:
- Change:
- New default anchor:
- New MESO packages:
- Follow-up message:
```

### Bias Detection Guide

Anchoring:
- First number became reference point.
- Counteroffers moved around it.
- Defense: return to your prepared target/red line or re-anchor with package.

Midpoint bias / split-the-difference:
- You feel fair answer is halfway between two numbers.
- This rewards extreme low anchors.
- Defense: tie movement to scope or reciprocal concession.

Loss aversion:
- You overvalue avoiding deal loss versus protecting margin.
- Signals: “I came this far, should not lose it now.”
- Defense: compare final offer to BATNA and red line.

Sunk cost:
- Time invested pushes you toward bad yes.
- Defense: ignore past effort; decide from now forward.

Reciprocity pressure:
- They make small concession and you feel obligated to match larger concession.
- Defense: trade proportionally and explicitly.

Overconfidence:
- You assume they will accept because call feels warm.
- Defense: ask decision process and alternatives.

Confirmation bias:
- You interpret every signal as proof they will buy.
- Defense: list disconfirming evidence.

Fixed-pie thinking:
- Both sides treat price as only variable.
- Defense: add package variables.

Scarcity pressure:
- “Only today,” “last chance,” “budget closes now.”
- Defense: verify deadline and separate real constraint from pressure.

## MESO Builder

A good MESO set has three packages, each defensible and internally coherent.

Use these variables:

- Scope: deliverables, modules, stakeholders, revisions.
- Speed: delivery date, priority access, turnaround time.
- Support: async support, calls, warranty, handoff.
- Risk: guarantee, cancellation, success criteria, dependency owner.
- Payment: upfront, installments, success fee, retainer.
- Rights: usage, exclusivity, ownership, case study.
- Access: seniority, direct access, reporting cadence.

Template:

```
A. Premium - [high outcome / fast / more support]
Price: [anchor high]
Includes:
Excludes:
Best for:

B. Core - [target deal]
Price: [target or near target]
Includes:
Excludes:
Best for:

C. Lean - [above red line or scoped down]
Price: [minimum acceptable]
Includes:
Excludes:
Best for:
```

Rules:

- No more than three offers; too many choices overwhelm.
- All packages should be acceptable to you.
- If counterpart combines best parts of all packages, rebuild set instead of accepting cherry-pick.
- Name packages by outcome, not by cheap/expensive psychology: “Fast Launch,” “Core Build,” “Focused Sprint.”

## Price Math Helpers

When numbers exist, calculate:

```
final_vs_red_line = (final - red_line) / red_line
final_vs_target = final / target
concession_from_anchor = (anchor - final) / anchor
```

Report as percentages, rounded to nearest whole percent unless precision matters.

Example:

- Target: 16,400
- Red line: 10,500
- Anchor: 18,400
- Final: 13,200

Findings:

- Final is 26% above red line.
- Final is 80% of target.
- Concession from anchor is 28%.

## Ethics and Relationship Guardrails

Do:

- Be truthful about alternatives and constraints.
- Separate price from scope.
- Help counterpart choose best fit.
- Protect your delivery quality.
- Make tradeoffs explicit.

Do not:

- Fabricate other clients or deadlines.
- Use fake scarcity.
- Hide material risks.
- Pressure someone into bad-fit purchase.
- Treat bias detection as permission to manipulate.


## Salary Negotiation Examples

Use the same three modes for compensation conversations. In salary negotiation, do not negotiate only base salary. Build total-compensation packages.

### PREP Example

```
/negotiate prep
I am negotiating salary for a Senior Product Manager role at a Series B startup.
Current offer: 42,000 ILS monthly base, 0.15% options, standard benefits.
Target: 49,000 ILS monthly base or equivalent total comp.
Red line: 43,500 ILS monthly base if title/level and equity improve.
BATNA: current role at 40,000 ILS, plus one active interview. Medium strength.
Important variables: base, signing bonus, options, title/level, remote days, start date, 6-month compensation review, learning budget, severance/notice.
```

Expected package shape:

```
A. Higher Cash
Base: 49,000 ILS
Equity: standard
Tradeoff: no signing bonus
Best for: immediate cash certainty

B. Balanced Growth
Base: 46,500 ILS
Equity: improved grant
Signing bonus: one-time bridge
Best for: fair total comp and upside

C. Level + Review
Base: 44,500 ILS
Title/level: upgraded or clarified scope
Review: written 6-month compensation review tied to milestones
Best for: company has base constraint but can move on career path
```

### LIVE Example: “This is the top of our range”

```
NEGOTIATE / live

Send this:
"I understand base may be constrained. I am still excited about the role. If base is fixed, can we look at total package — signing bonus, equity, title/level, or a written 6-month compensation review tied to milestones?"

Why:
- Bias/tactic addressed: prevents anchoring on base-only constraint.
- What it preserves: fit, relationship, and total compensation upside.
- Next move if they say yes/no: if yes, offer 2-3 packages; if no, ask what variable is actually flexible.
```

### LIVE Example: Offer Below Red Line

```
That is below where I can responsibly accept. I see strong fit here, so rather than force base only, could we make one of these work: higher signing bonus, stronger equity grant, adjusted level, or a 6-month review with agreed milestones?
```

### ANALYZE Example

```
/negotiate analyze
They opened at 42,000. I asked for 49,000. They said range is capped at 44,000. I proposed either 46,000 base, or 44,000 with higher equity and 6-month review. They chose 44,000 + better equity + review.
```

Analyze for:

- Whether “range cap” was hard or soft.
- Whether you fell into midpoint bias between their base and your ask.
- Whether total-comp MESO preserved value.
- Whether written review terms are concrete enough to matter.

Salary-specific guardrails:

- Do not bluff competing offers.
- Get title, level, equity terms, review timing, and bonus terms in writing.
- Ask who approves exceptions before treating “range” as final.
- Compare total comp to BATNA, not only base salary.

## Common Pitfalls

1. Weak BATNA theater.
   Do not claim “other clients waiting” unless true. If BATNA is weak, say so internally and improve terms through scope, payment, or risk control.

2. Red line after call starts.
   If you decide minimum while buyer is pressuring you, emotion sets price. Set it before.

3. Discounting same scope.
   A discount without a trade teaches buyer your first price was padded.

4. Over-precise fake math.
   Precise anchors work only when credible. `18,437` without rationale looks silly.

5. MESO packages not equivalent for you.
   If you secretly hate one package, remove it. Counterpart may choose it.

6. Too many packages.
   More than three creates confusion and cherry-picking.

7. Splitting difference from their low anchor.
   Midpoint between fair price and bad anchor is still bad deal.

8. Treating stated budget as truth.
   Budget can be real, soft, political, or just anchor. Ask what they expect included.

9. Ignoring implementation risk.
   If client is messy, red line goes up, not down.

10. Winning price, losing relationship.
   Use clear tradeoffs and respect. Long-term value matters.

## Verification Checklist

Before final answer, ensure:

- [ ] Mode is clear: prep, live, or analyze.
- [ ] Red line / reservation point is explicit or assumption-labeled.
- [ ] BATNA is named and rated.
- [ ] Opening anchor is defensible.
- [ ] MESO packages are no more than three and all acceptable.
- [ ] Any discount is paired with a tradeoff.
- [ ] Biases are named as risk signals, not magic tricks.
- [ ] Live response is short enough to send.
- [ ] Analyze mode includes what to keep/change next time.
