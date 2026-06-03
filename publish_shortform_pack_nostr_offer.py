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

    content = '''$15 BTC quick pack / $50 full pack — short-form founder content for technical launches

For devtools, OSS, AI/security tools, indie SaaS, or crypto products.

Send one product link/README/launch note. I return:

$15 quick pack:
• 3 punchy hooks
• 1 short X/LinkedIn post
• 1 30-second video script with caption beats

$50 full pack:
• 10 hooks
• 3 posts
• 3 short-form video scripts
• 5 CTAs
• positioning note

Sample pack: https://github.com/temp3all/hb_signal-signals/blob/master/phone_budget_short_form_content_pack.md
Offer page: https://raw.githack.com/temp3all/hb_signal-signals/master/phone-budget-offer/index.html
Request: https://github.com/temp3all/hb_signal-signals/issues/new?title=CONTENT%20PACK%20-%20Short%20Form%20Founder%20Assets
BTC: 1BL4eV82zZ64Dp4cj3s9EgJ3ae8xPx5ZuJ

No fake claims, spam, account access, review manipulation, or verification bypasses.'''

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
    with open('/data/.openclaw/workspace/nostr_shortform_pack_phone_budget_offer_live.json', 'w') as f:
        json.dump(record, f, indent=2)
    print('NPUB:', record['npub'])
    print('Event ID:', record['event_id'])
    print('Link:', record['link'])
    await client.shutdown()

asyncio.run(main())
