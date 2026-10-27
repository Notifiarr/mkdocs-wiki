# Watchsync

!!! info
    This integration allows for notifications from [Watchsync](https://github.com/Notifiarr/watchsync), a tool that keeps users, libraries, and watch history in sync across multiple media apps. It is also used for disaster recovery of that history, to populate a new database.

---

## Trigger Options

### Triggers

- `User login` - Receive a notification for a `userLogin` event. The notification shows the username when Watchsync sends one
- `User update` - Receive a notification for a `userUpdate` event. The notification shows the username when Watchsync sends one
- `Connection error` - Receive a notification for a `connectionError` event
    - Optional notification fields: Media app, Message
- `Sync webhook` - Receive a notification for a `syncWebhook` event. Fields come from the payload: ID, type, mode, libraries, users, source and destination apps, progress, scan, and library counts (movies, series, episodes). Title, poster, and banner come from the website's metadata lookup
    - Optional notification fields: Id, Type, Mode, Libraries, User, Media app, Progress, Scan, Library stats, Poster, Banner, Title, Season, Episode, Name, Overview, Year, Rated, Network, Links
- `Sync overview` - Receive a notification for a `syncOverview` event, with per-app counts of created, linked, removed, added, updated, finished, and in-progress items. The site skips the notification when the payload has no changes, unless the status is `error` or `cancelled`. The color is red for `error` and yellow for `cancelled`
    - Optional notification fields: Id, Type, Trigger, Mode, Status, Runtime, Libraries, Users, Media apps
- `Backup` - Receive a notification for a `backup` event. The color is red when the status is `failed`
    - Optional notification fields: Type, Status, Runtime, Size

### Channels

- Watchsync channel picker for each trigger

---

## Configuration

Click the **cog icon** to open the configuration options for Watchsync.

Each trigger has the following options:

1. Notification color
2. Notification pings
3. Notification layout
4. Toggle which optional fields to include in notifications (`User login` and `User update` have no optional fields)

`Sync overview` also has a **Disabled types** filter. Sync types selected there do not send an overview notification.

---

## Instructions

1. In Watchsync go to Notifications and add Notifiarr
1. Use the webhook URL shown on the Watchsync integration page on the Notifiarr website
1. Enable the triggers you want on the Notifiarr website and pick a Discord channel for each

It is highly recommended you add an API key specific to this integration in your profile since Watchsync is a third-party app. The integration-specific webhook URL uses that key.
