# DropLock Show HN mini-audit — 24h launch clarity sample

Source reviewed: https://droplock.apitman.com/  
HN lead: `Show HN: DropLock – E2EE secret sharing web app with no backend`  
Goal of this sample: show the kind of fast, concrete launch/README clarity pass available as a $15 quick pass or $50 full pack.

## What already works

- The product promise is strong: no backend, local encryption, link-fragment delivery, and a very visible CSP/security posture.
- The page explains the threat model more honestly than most tiny security tools.
- The “open lock box / locked link” metaphor is good; it can become the main conversion device.

## Conversion gaps spotted

### 1) The hero undersells the exact use case
Current visible framing: **“Simple safe secret sharing.”**

That is accurate, but generic. It does not immediately tell a visitor why this exists instead of Signal, Bitwarden Send, magic-wormhole, PrivateBin, or encrypted email.

**Sharper hero option:**

> Share one secret without accounts, servers, or copy-pasting into someone else’s database.

**Subheadline:**

> DropLock creates a one-use “lock box” link in your browser. Someone can lock a message for you; only the same browser profile that created the box can open it.

### 2) The trust tradeoff is buried after the workflow
The “link replacement / compare over two channels” warning is important. For a security tool, this is not a liability if framed well — it proves honesty.

**Suggested trust block above the fold:**

> No backend means no recovery and no account safety net. DropLock protects against server storage and casual interception, not against someone swapping the lock-box link before the sender sees it. For high-stakes secrets, compare the link over a second channel.

### 3) The page needs a “best for / not for” box
This reduces support burden and makes the tool feel safer.

**Best for**
- Sending an API key/password once to someone you already know
- Short notes that should not live in a SaaS database
- Low-friction encrypted handoff without accounts

**Not for**
- Long-term storage
- Anonymous high-stakes whistleblowing
- Secrets you need to reopen from another device/browser
- Situations where link substitution is a realistic attacker model and you cannot verify the link out-of-band

## Paste-ready revised top section

```text
DropLock

Share one secret without accounts, servers, or copy-pasting into someone else’s database.

Create a lock-box link in this browser. Send it to someone. They type a secret, lock it locally, and send back a locked link that only this same browser profile can open.

Best for quick handoffs like API keys, passwords, recovery notes, or private one-off messages.

Important: DropLock has no backend and no recovery. If someone can replace your lock-box link before the sender sees it, they can trick the sender into locking the secret for them. For high-stakes secrets, compare the link over a second channel.
```

## 3 CTA options

1. **Create my lock-box link**
2. **Lock a secret for someone**
3. **Read the threat model first**

## $15 / $50 paid follow-up offer

If useful, I can turn this into a full 24h launch clarity pass:

- $15 quick pass: revised hero + trust block + CTA labels
- $50 full pack: full landing-page rewrite, README intro, HN launch comment, FAQ objections, and 5 follow-up post ideas

Payment/intake: https://github.com/temp3all/hb_signal-signals/tree/master/phone-budget-offer
