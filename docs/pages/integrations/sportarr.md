# Sportarr

!!! info
    This integration allows for notifications from [Sportarr](https://sportarr.net/), a sports PVR for Usenet and torrents. It works like Sonarr and Radarr, but for sports events.

---

## Trigger Options

### Triggers

- `Grab` - Receive a notification for a `Grab` event, when something is sent to the download client
    - Optional notification fields: Instance, Indexer, Quality, Size, Poster, Banner, Status, Venue, City, Country, Description, League, Sport, Timestamp, Home team, Away team, Home score, Away score
- `Imported` - Receive a notification for a `Download` event that is not an upgrade, when media is imported to its root folder
    - Optional notification fields: Instance, Indexer, Quality, Size, Filename, plus the same event fields as `Grab`
- `Upgrade` - Receive a notification for a `Download` event that Sportarr flags as an upgrade, when existing media is replaced with a better quality. If no Upgrade channel is set, the Imported channel is used
    - Optional notification fields: same as `Imported`
- `Series Added` - Receive a notification for a `SeriesAdd` event, when a series or event is added
    - Optional notification fields: Instance, plus the event fields from `Grab` (Poster through Away score)
- `Series Deleted` - Receive a notification for a `SeriesDelete` or `EpisodeFileDelete` event, when a series, event, or episode file is deleted
    - Optional notification fields: Instance, Quality, Size, Filename, plus the event fields from `Grab` (Poster through Away score)
- `Rename` - Receive a notification for a `Rename` event, when files are renamed
    - Optional notification fields: Instance, Path, Poster, Banner
- `Updates` - Receive a notification for an `ApplicationUpdate` event
- `Health Check` - Receive a notification for a `Health` event with a health type. The color follows the health level: Ok green, Notice blue, Warning yellow, Error red
- `Health Restored` - Receive a notification for a `Health` event with no health type, which the site treats as a restored health issue
- `Manual Interaction` - Receive a notification for a `ManualInteractionRequired` event, when a download needs a manual import
    - Optional notification fields: Instance, Filename, Size, Confidence, Poster, Banner
- `Recording Started`, `Recording Completed`, and `Recording Failed` - Receive a notification for the `RecordingStarted`, `RecordingCompleted`, and `RecordingFailed` events
    - Optional notification fields: Instance, Poster, Banner, Status, Venue, City, Country, Description, League, Sport, Timestamp, Home team, Away team, Home score, Away score. The same field selection applies to all three triggers.

### Channels

- Sportarr channel picker for each trigger

---

## Configuration

Click the **cog icon** to open the configuration options for Sportarr.

Most triggers have the following options:

1. Notification color
2. Notification pings
3. Notification layout
4. Toggle which optional fields to include in notifications

`Series Deleted` has separate ping and layout settings for series deletes and episode file deletes. `Health Check` has pings and layout only. `Health Restored` has no options.

The **Remove forced `Sportarr` from instance name** setting strips the forced `Sportarr` prefix from the instance name shown in notifications.

!!! note
    Poster, rating, and link fields from the metadata database are not available yet, because Sportarr payloads do not include external IDs.

---

## Instructions

1. In Sportarr go to Settings → Notifications → Webhook and add a **Webhook** notification
1. Paste the webhook URL shown on the Sportarr integration page on the Notifiarr website into the URL field
1. Enable the triggers you want sent to Notifiarr
1. Enable the integration on the Notifiarr website and pick a Discord channel for each trigger
1. Customize the optional notification fields for each trigger

It is highly recommended you add an API key specific to this integration in your profile since Sportarr is a third-party app. The integration-specific webhook URL uses that key.
