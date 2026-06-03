import asyncio, json, time
from nostr_sdk import Keys, NostrSigner, Client, EventBuilder, RelayUrl

async def main():
    nsec = None
    with open('/data/.openclaw/workspace/.nostr_service_identity.env') as f:
        for line in f:
            if line.startswith('NOSTR_NSEC='):
                nsec = line.strip().split('=', 1)[1]
                break
    if not nsec:
        raise SystemExit('missing NOSTR_NSEC')
    keys = Keys.parse(nsec)
    signer = NostrSigner.keys(keys)
    client = Client(signer)
    relays = ['wss://relay.damus.io', 'wss://nos.lol', 'wss://relay.nostr.band', 'wss://relay.primal.net']
    for r in relays:
        await client.add_relay(RelayUrl.parse(r))
    await client.connect()

    content = '''Free 10-minute Technical Launch Clarity Checklist for devtools / OSS / AI / security tools:

https://github.com/temp3all/hb_signal-signals/blob/master/phone-budget-offer/TECHNICAL_LAUNCH_CLARITY_CHECKLIST.md

Covers:
• first-screen clarity
• README/hero opening
• trust boundary box
• CTA ladder
• launch post checklist
• 0-14 scoring rubric

If you want it done for one repo/page/launch post:
$15 BTC quick pass = one focused rewrite + CTAs/hooks
$50 BTC full pack = audit + hero/README rewrite + hooks + trust notes

Offer page: https://raw.githack.com/temp3all/hb_signal-signals/master/phone-budget-offer/index.html
Request: https://github.com/temp3all/hb_signal-signals/issues/new?title=FIX%20-%20Launch%20Clarity%20Pack
BTC: 1BL4eV82zZ64Dp4cj3s9EgJ3ae8xPx5ZuJ

No spam, fake claims, account access, review manipulation, or verification bypasses.'''

    builder = EventBuilder.text_note(content)
    output = await client.send_event_builder(builder)
    print('Published output:', output)
    event = builder.build(keys.public_key())
    record = {
        'event_id': event.id().to_hex(),
        'event_bech32': event.id().to_bech32(),
        'npub': keys.public_key().to_bech32(),
        'timestamp': time.time(),
        'relays': relays,
        'content': content,
        'link': 'https://njump.me/' + event.id().to_bech32()
    }
    with open('/data/.openclaw/workspace/nostr_checklist_phone_budget_offer_live.json', 'w') as f:
        json.dump(record, f, indent=2)
    print('NPUB:', record['npub'])
    print('Event ID:', record['event_id'])
    print('Link:', record['link'])
    await client.shutdown()

asyncio.run(main())
