# Technical Launch Clarity Checklist

A 10-minute checklist for devtools, AI tools, security/privacy products, open-source launches, and indie SaaS pages.

Use it before posting to Hacker News, Product Hunt, Reddit, GitHub, X, Nostr, or founder communities.

## 1. First-screen clarity

Your first screen should answer these in under 8 seconds:

- What is it?
- Who is it for?
- What painful task does it make easier?
- Why should a stranger trust it enough to click?
- What should they do next?

Quick rewrite formula:

> `[Product] helps [specific user] do [painful job] without [common friction/risk].`

Examples:

- `Local replay for developers who need to debug user sessions without shipping event data to a third-party recorder.`
- `Encrypted secret sharing for teams that need one-time links without trusting a hosted backend.`
- `Package-manager config hardening for JavaScript/Python teams before dependency mistakes become incidents.`

## 2. Hero / README opening

Bad opening signs:

- Starts with a vague category: "A modern platform for..."
- Leads with implementation before use case
- Says "simple" but does not show the exact simple action
- Claims privacy/security without naming the trust boundary
- Has no visible next action

Better opening structure:

1. One-line outcome
2. Who it is for
3. One concrete example workflow
4. Trust/risk note
5. CTA

Paste-ready skeleton:

```text
[Product] lets [audience] [specific outcome] without [friction/risk].

Use it when you need to [example workflow]. It runs/works by [trust-relevant detail], so [privacy/security/reliability benefit].

Try it: [primary CTA]
Docs/demo: [secondary CTA]
```

## 3. Trust and risk reversal

Technical buyers hesitate when they cannot quickly answer:

- Does this require my production data?
- Does this need account access?
- What leaves my machine/network?
- What breaks if I try it?
- How do I undo it?
- Is there a demo before setup?

Add a short "Trust boundary" box:

```text
Trust boundary:
- No account required for local/demo use.
- [Data type] stays [where].
- [External service] only sees [limited data], if enabled.
- Safe test path: [command/demo/sample project].
- Undo: [one command or deletion step].
```

## 4. CTA ladder

One CTA is not enough. Use a low-friction ladder:

- **Skim:** screenshot/GIF/demo video
- **Try:** live demo, sample input, sandbox, one command
- **Trust:** docs, architecture, threat model, limits
- **Adopt:** install, deploy, sign up, open issue, join waitlist

## 5. Launch-post checklist

Before publishing, confirm the post has:

- A concrete title: `Show HN: [Product] – [specific outcome] for [specific user]`
- One sentence on why it exists
- One practical use case
- One limitation or honest tradeoff
- One screenshot/GIF/demo link
- One request for feedback
- No exaggerated revenue/security claims

Paste-ready launch close:

```text
I’d especially value feedback from [specific audience] on [specific question].
```

## 6. Quick scoring rubric

Score each 0-2:

- Outcome clarity
- Audience specificity
- Demo/try path
- Trust boundary
- CTA clarity
- Proof/sample quality
- Honest limitation

Total:

- 0-5: strangers will bounce
- 6-9: usable but leaky
- 10-14: ready to launch/test

## Paid quick pass

If you want this done for one repo/page/launch post:

- **$15 BTC quick pass:** one focused rewrite, 2 CTA options, 3 short hooks
- **$50 BTC full pack:** clarity audit, hero/README rewrite, 3 CTAs, 5 post hooks, trust/risk notes

Offer page: https://raw.githack.com/temp3all/hb_signal-signals/master/phone-budget-offer/index.html

BTC: `1BL4eV82zZ64Dp4cj3s9EgJ3ae8xPx5ZuJ`

Open request: https://github.com/temp3all/hb_signal-signals/issues/new?title=FIX%20-%20Launch%20Clarity%20Pack

No fake claims, spam, account access, review manipulation, or verification bypasses.
