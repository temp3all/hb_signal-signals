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

    content = '''$15 BTC quick pass / $50 full pack — technical copy + research cleanup

Fast help for devtools, OSS, AI/security tools, indie SaaS, or messy technical notes.

$15 quick pass:
• rewrite one headline/README intro/profile bio/messy paragraph
• 2 CTA options
• 3 short launch/social hooks

$50 full pack:
• clarity/friction audit
• sharper hero/README opening
• 3 CTA options
• 5 launch/social hooks
• trust/risk-reversal notes

Offer/proof page: https://raw.githack.com/temp3all/hb_signal-signals/master/phone-budget-offer/index.html
Request via GitHub issue: https://github.com/temp3all/hb_signal-signals/issues/new?title=FIX%20-%20Quick%20Pass%20or%20Launch%20Clarity%20Pack
BTC: 1BL4eV82zZ64Dp4cj3s9EgJ3ae8xPx5ZuJ

No spam, fake claims, review manipulation, account access, or verification bypasses.'''

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
    with open('/data/.openclaw/workspace/nostr_quickpass_phone_budget_offer_live.json', 'w') as f:
        json.dump(record, f, indent=2)
    print('NPUB:', record['npub'])
    print('Event ID:', record['event_id'])
    print('Link:', record['link'])
    await client.shutdown()

asyncio.run(main())
