# Duplicacy

!!! info
    This integration allows for notifications from [Duplicacy](https://duplicacy.com/) when backup operations succeed or fail.

---

## Trigger Options

### Triggers

- `Success` - Receive a notification when a backup completes successfully
    - Optional notification fields: New files, New chunks, New metadata, Uploaded metadata, Total files
- `Error` - Receive a notification when a backup fails

### Channels

- Duplicacy channel picker for each trigger

---

## Configuration

Click the **cog icon** to open the configuration options for Duplicacy.

1. Notification pings for each trigger
2. Toggle which fields to include in success notifications:
    - **New files** - Number of new files backed up
    - **New chunks** - Number of new chunks created
    - **New metadata** - New metadata entries
    - **Uploaded metadata** - Metadata uploaded during backup
    - **Total files** - Total file count in the backup

---

## Instructions

1. Configure Duplicacy to send webhook notifications to your Notifiarr webhook URL
2. Enable the triggers you want on the Notifiarr website
3. Test the notification to ensure it is working
