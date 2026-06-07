# qui

!!! info
    This integration allows for notifications from [qui](https://qui.gg/) for torrent management, backups, directory scans, orphan scans, cross-seed operations, and automation actions.

---

## Trigger Options

### Triggers

#### Torrent Triggers

- `Torrent added` - Receive a notification when a torrent is added
    - Optional notification fields: Release name, Tracker, Category, Tags, Poster, Banner, Instance, Added, Completed (ETA), Progress, State, Total size, Downloaded, Remaining, Speed, Seeders, Leechers, Release hash
- `Torrent completed` - Receive a notification when a torrent completes downloading
    - Optional notification fields: Release name, Tracker, Category, Tags, Poster, Banner, Instance, Release hash

#### Backup Triggers

- `Backup succeeded` - Receive a notification when a backup completes successfully
    - Optional notification fields: Instance, Started, Completed, Runtime, Backup type, Backup id, Backup count
- `Backup failed` - Receive a notification when a backup fails
    - Optional notification fields: Instance, Started, Completed, Runtime, Backup type, Backup id, Error messages

#### Directory Scan Triggers

- `Dir scan completed` - Receive a notification when a directory scan completes
    - Optional notification fields: Instance, Started, Completed, Runtime, Scan id, Scan matches, Scan added
- `Dir scan failed` - Receive a notification when a directory scan fails
    - Optional notification fields: Instance, Started, Completed, Runtime, Scan id, Error messages

#### Orphan Scan Triggers

- `Orphan scan completed` - Receive a notification when an orphan scan completes
    - Optional notification fields: Instance, Started, Completed, Runtime, Scan id, Files deleted, Folders deleted
- `Orphan scan failed` - Receive a notification when an orphan scan fails
    - Optional notification fields: Instance, Started, Completed, Runtime, Scan id, Error messages

#### Cross-Seed Triggers

- `Cross seed automation succeeded` - Receive a notification when cross-seed automation succeeds
    - Optional notification fields: Instance, Started, Completed, Runtime, Details, Releases
- `Cross seed automation failed` - Receive a notification when cross-seed automation fails
    - Optional notification fields: Instance, Started, Completed, Runtime, Details, Error messages, Releases
- `Cross seed search succeeded` - Receive a notification when a cross-seed search succeeds
    - Optional notification fields: Instance, Started, Completed, Runtime, Details
- `Cross seed search failed` - Receive a notification when a cross-seed search fails
    - Optional notification fields: Instance, Started, Completed, Runtime, Details, Error messages
- `Cross seed completion succeeded` - Receive a notification when a cross-seed completion succeeds
    - Optional notification fields: Instance, Started, Completed, Runtime, Details, Releases, Banner, Poster
- `Cross seed completion failed` - Receive a notification when a cross-seed completion fails
    - Optional notification fields: Instance, Started, Completed, Runtime, Details, Releases, Error messages, Release name, Banner, Poster
- `Cross seed webhook succeeded` - Receive a notification when a cross-seed webhook succeeds
    - Optional notification fields: Instance, Started, Completed, Runtime, Release name, Details, Releases, Banner, Poster
- `Cross seed webhook failed` - Receive a notification when a cross-seed webhook fails
    - Optional notification fields: Instance, Started, Completed, Runtime, Error messages, Banner, Poster

#### Automation Triggers

- `Automations actions applied` - Receive a notification when automation actions are applied
    - Optional notification fields: Instance, Automations, Error messages, Releases
- `Automations run failed` - Receive a notification when an automation run fails
    - Optional notification fields: Instance, Error messages

### Channels

- qui channel picker for each trigger

---

## Configuration

Click the **cog icon** to open the configuration options for qui.

Each trigger has the following options:

1. Notification color
2. Notification pings
3. Notification layout
4. Toggle which optional fields to include in notifications

---

## Instructions

1. Configure qui to send webhook notifications to your Notifiarr webhook URL
2. Enable the triggers you want on the Notifiarr website
3. Customize the optional notification fields for each trigger
4. Test the notification to ensure it is working
