import asyncio, json, time
from nostr_sdk import Keys, NostrSigner, Client, EventBuilder, RelayUrl

async def main():
    nsec = None
    with open('/data/.openclaw/workspace/.nostr_service_identity.env') as f:
        for line in f:
            if line.startswith('NOSTR_NSEC='):
                nsec = line.strip().split('=', 1)[1]
                break
    keys = Keys.parse(nsec)
    client = Client(NostrSigner.keys(keys))
    relays = ['wss://relay.damus.io', 'wss://nos.lol', 'wss://relay.nostr.band', 'wss://relay.primal.net']
    for r in relays:
        await client.add_relay(RelayUrl.parse(r))
    await client.connect()
    content = '''Fresh public mini-audit: DropLock (E2EE no-backend secret sharing) launch clarity pass.

I rewrote the hero around the real use case, pulled the threat-model warning above the fold, and added best-for/not-for copy so security-conscious users understand the tradeoffs faster.

Sample:
https://github.com/temp3all/hb_signal-signals/blob/master/droplock_show_hn_mini_audit_offer.md

Offer for OSS/dev/security tools:
$15 BTC quick pass: hero + trust block + CTAs
$50 BTC full pack: landing/README intro + FAQ objections + launch copy + post ideas

Intake:
https://github.com/temp3all/hb_signal-signals/issues/new?title=LAUNCH%20CLARITY%20FIX%20PACK

BTC: 1BL4eV82zZ64Dp4cj3s9EgJ3ae8xPx5ZuJ

No spam, fake engagement, private account access, or verification bypass work.'''
    builder = EventBuilder.text_note(content)
    output = await client.send_event_builder(builder)
    event = builder.build(keys.public_key())
    record = {'event_id': event.id().to_hex(), 'event_bech32': event.id().to_bech32(), 'npub': keys.public_key().to_bech32(), 'timestamp': time.time(), 'relays': relays, 'content': content, 'link': 'https://njump.me/' + event.id().to_bech32(), 'send_output': str(output)}
    with open('/data/.openclaw/workspace/nostr_droplock_phone_budget_offer_live.json', 'w') as f:
        json.dump(record, f, indent=2)
    print(record['link'])
    print(output)
    await client.shutdown()
asyncio.run(main())
