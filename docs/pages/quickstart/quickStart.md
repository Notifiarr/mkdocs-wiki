# Quick Start

Almost everything needed is available in different parts of the wiki. This will point to each one to get you up and running.

## Assumptions

- You already have an account setup on notifiarr.com with a valid apikey to use in the client but if you dont, stop here and go make one.
- You have [setup the notifiarr client](../client/install.md) if you plan to use it. To know if you will need it or not you can view the faq [for information on if it is required](../faq/faq.md#q-is-the-notifiarr-client-required)

## Client Connection

Once the client is setup locally and you can see it internally (example: `localhost:5454`) and externally (example: `http://<your-external-ip>:5454` or `https://notifiarr.<your-domain>.com`) then you need to tell the site how to talk to it. You can [see how to do this here.](../../pages/website/clientConfig.md#clients-setup) If it isn't green on the site then the URL is not going to work and needs fixed. This can be many factors but common ones are a bad port forward, a cloudflare block, bad configuration, timeout, etc.

Use curl and test it (the `/api/version` is important and validates the apikey check from the site to the client)

```bash
curl -I -H "x-api-key: \<notifiarr-apikey-here\>" -H "Content-Type: application/json" \<client-connection-here\>/api/version
```

Example:

```bash
curl -I -H "x-api-key: 123456-7890-12345-6789-0123456789" -H "Content-Type: application/json" https://notifiarr.my-domain-dns.com/api/version
```

If this does not return a 200 response with a JSON payload, it isn't right. Check your port forwarding / reverse proxy / cloudflare configuration. You can also check the time it takes to get a response. The client needs to respond within 7 seconds.

```bash
curl --write-out '%{time_total}' -I -H "x-api-key: \<notifiarr-apikey-here\>" -H "Content-Type: application/json" \<client-connection-here\>/api/version
```

Example:

```bash
curl --write-out '%{time_total}' -I -H "x-api-key: 123456-7890-12345-6789-0123456789" -H "Content-Type: application/json" https://notifiarr.my-domain-dns.com/api/version
```

If this takes more than 7 seconds it will not work. You'll need to figure out which app is taking so long to respond or is timing out.

## Integrations

First thing, [turn on a couple](../../pages/website/integrationsSetup.md#main-setup) that you want to use (or all of them at once that you want to use if you want but less is more while learning). Once you have them turned on the page will reload and you'll see a card for each one. If you cant figure out how to turn things on etc, each integration has a wiki page for it (well most do). Click the `Wiki` link in the integration card to get more information about that specific one.
