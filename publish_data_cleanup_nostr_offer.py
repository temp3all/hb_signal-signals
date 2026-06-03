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

    content = '''$10-$25 BTC — quick data cleanup / research brief for founders and indie hackers

Send one small messy list, CSV/export, competitor notes dump, customer-feedback snippets, or research question.

I’ll return within 24h:
• cleaned structure or categorized notes
• 5-10 bullet summary
• key patterns / risks
• 3-7 next actions

Best for indie SaaS, devtools, OSS projects, small market scans, or messy research notes.

$10 quick clean / $25 research brief, BTC accepted.
Request: https://github.com/temp3all/hb_signal-signals/issues/new?title=DATA%20-%20Quick%20Clean%20or%20Research%20Brief
Full offer/proof: https://raw.githack.com/temp3all/hb_signal-signals/master/phone-budget-offer/index.html
BTC: 1BL4eV82zZ64Dp4cj3s9EgJ3ae8xPx5ZuJ

No private account access, spam lists, fake engagement, or verification bypasses.'''

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
    with open('/data/.openclaw/workspace/nostr_data_cleanup_phone_budget_offer_live.json', 'w') as f:
        json.dump(record, f, indent=2)
    print('NPUB:', record['npub'])
    print('Event ID:', record['event_id'])
    print('Link:', record['link'])
    await client.shutdown()

asyncio.run(main())
