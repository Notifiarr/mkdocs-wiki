# Tracearr

!!! info
    This integration allows for notifications from [Tracearr](https://tracearr.com/), a real-time monitor for Plex, Jellyfin, and Emby servers that tracks streams, analyzes playback, and detects account sharing.

---

## Trigger Options

### Triggers

- `Violations` - Receive a notification when a rule violation is detected
    - Optional notification fields: User, Rule, Severity, Minutes
- `New device` - Receive a notification when a new device is seen
    - Optional notification fields: User, Device, Platform, Location
- `Started` - Receive a notification when a stream starts
    - Optional notification fields: User, Stream type, Quality, Device, Location, Poster, Background
- `Stopped` - Receive a notification when a stream stops
    - Optional notification fields: User, Poster, Background
- `Server offline` - Receive a notification when a media server goes down
    - Optional notification fields: Server name, Server type
- `Server online` - Receive a notification when a media server comes back up
    - Optional notification fields: Server name, Server type

### Channels

- Tracearr channel picker for each trigger

---

## Configuration

Click the **cog icon** to open the configuration options for Tracearr.

Each trigger has the following options:

1. Notification color
2. Notification pings
3. Notification layout
4. Toggle which optional fields to include in notifications

---

## Instructions

1. In Tracearr go to Settings → Notifications
1. Add a notification destination using the **JSON Webhook** format
1. Paste the webhook URL shown on the Tracearr integration page on the Notifiarr website
1. Enable the triggers you want on the Notifiarr website and pick a Discord channel for each

It is highly recommended you add an API key specific to this integration in your profile since Tracearr is a third-party app. The integration-specific webhook URL uses that key.
