# FAQ

## Why is a Discord Server needed?

- You need to have a discord server to invite the bot to so the notifications have a place to go.

## What is Notifiarr's (website) IP Address

- Some more security conscious users restrict incoming traffic to only certain IP addresses.
- The Notifiarr Website's IP address is rather "sticky" and rarely changes. However, you can always find the current IP address by getting the IP of the domain listed below.

```bash
ping origin-proxy.notifiarr.com
```

## Q. Is the Notifiarr client required?

- The client is only required for certain integrations/features. If you open the `Manage Integrations` on the site, it will display in the bottom right corner as well which need the client.

### Integrations

- Channel Stats
- Dashboard
- MDBList (Adding lists & movies to Radarr, Adding shows to Sonarr)
- Media Requests
- Network
- Plex
- Lidarr (Backup, Corruption & Stuck Queue notifications)
- Prowlarr (Backup, Corruption & Stuck Queue notifications)
- Radarr (Backup, Corruption & Stuck Queue notifications)
- Readarr (Backup, Corruption & Stuck Queue notifications)
- Reciperr (Adding lists & movies to Radarr)
- Snapshot
- Sonarr (Backup, Corruption & Stuck Queue notifications)
- TRaSH Custom Format & Profile Sync (Patron)
- Client Commands
  - Discord triggering, automation, and advanced features (Sub)

### Features

- Radarr Collections
- Automatic unmonitoring of movies/episodes after finish
- Automatic refresh of TBA episodes
- Automatic plex session killing per user/device based on rules
- Stuck queue item notifications
- Starr backup/corruption check notifications

## Q. How do I monitor the queue for stuck items?

- Open the [Client Settings](../../pages/website/clientConfig.md) on the site and expand the **Starr** section to set the notify times.

- It will notify once when it thinks it is stuck and then update the existing message every 5 minutes until it is imported so you can see the amount of time it is stuck and why. Messages go to the shared `Errors` channel.

- If you want the notifications to stop coming for a specific item, click the `Acknowledge` link in the notification. This is useful if something has a low amount of peers for example so it could take some time to complete it.

## Q. How do I test/troubleshoot Plex?

### Locating the Plex Token

- [See this post in the Plex Forums](https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/)

!!! info
     The Plex Token is required for the Notifiarr Client to send commands to Plex

### Connection

- You can run a curl command and make sure you get an `200 OK` response returned.

```bash
curl -I -H "X-Plex-Token: <token>" <url>/status/sessions
```

- `<token>` The plex token from your config (Unraid: ENV | All: UI) Ex: `ZQonMnitLFbFsuaLXT9Yj`
- `<url>` The plex URL from your config (ENV or conf file). Ex: `http://localhost:32400`

  - Expected result: HTTP/1.1 200 OK
  - Incorrect result: HTTP/1.1 401 Unauthorized

- Adjust the token and url until it is 200.
- Update the Notifiarr Client's configuration with the correct url and token
- Restart the Notifiarr Client

### Notifications & Sessions

If session info is missing from notifications or the sessions notification is not working:

- Make sure you dont have duplicated clients in the [Client Settings](../../pages/website/clientConfig.md)
- Make sure you have a [client](../../pages/website/clientConfig.md) setup for Plex
- Make sure you have selected the **Activity** checkbox in the Plex section of the [Client Settings](../../pages/website/clientConfig.md)
- Try to increase the **Activity Delay** in the Plex section of the [Client Settings](https://notifiarr.wiki/en/Website/ClientConfiguration) as this will give Plex more time to get the session available in the endpoint
- Note 1: The sessions notifications will only send when there is at least one item being played or paused
- Note 2: It doesn't matter what Tautulli shows or the Plex Dashboard shows, they both use the same sessions endpoint. If you where to look at them at the same time as the notification is sent (when it doesn't work) they would also not show the session yet. How long it takes Plex & your (possibly low powered or over worked) server to make the session available in the endpoint is out of our control which is why we added the delay option

## Q. What are the user level differences

- **User**: Anyone who makes an account for free
- **Patron**: Anyone who [supports the project once](https://github.com/sponsors/Notifiarr)
- **Subscriber**: Anyone who [supports the project monthly](https://github.com/sponsors/Notifiarr)

!!! note
    Patron and Sub also have extra channels available on Discord with roles and colors

## Limitations

| User | Patron | Subscriber | Integration | Setting |
| :- | :- | :- | :- | :- |
| 12,000 / day 500 / hour | 24,000 / day 1,000 / hour| Unlimited | Core | Notifications |
| All but TRaSH Sync | All | All | Core | Integrations |
| 7 days | 14 days | Unlimited | Network | Status retention (used for the network status page to show uptime and for detail links in notifications) |
| 14 days | 30 days | Unlimited | Plex | Session retention (used for tracking transcodes by device, app, user, media type, etc and sessions notifications) |
| 7 days | 14 days | Unlimited | Website Status | Incident retention (used for network status page to show uptime) |
