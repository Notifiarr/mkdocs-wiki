# Synology

!!! info
    This integration allows for notifications from [Synology](https://www.synology.com/) NAS devices. Receive notifications for informational, warning, and critical events from your Synology system.

---

## Trigger Options

### Triggers

- `Info` - Receive a notification for informational Synology events
- `Warning` - Receive a notification for warning-level Synology events
- `Critical` - Receive a notification for critical/error Synology events

### Channels

- Synology channel picker for each trigger

---

## Configuration

Click the **cog icon** to open the configuration options for Synology.

Each trigger has the following options:

1. Notification color
2. Notification pings
3. Notification layout

### Settings

- **Fuzzy Matching** - Enable fuzzy matching to try to match the notification reason to the correct severity level. Synology does not send the group, severity, or exact reason in its notifications. Without fuzzy matching, all notifications will go to the Info channel.
- **Fuzzy Match Limit** - Choose how many fuzzy match results to display:
    - `Highest match only` - Show only the best match
    - `Top 3 matches` - Show the top 3 matches

---

## Instructions

1. Configure your Synology NAS to send webhook notifications to your Notifiarr webhook URL
2. Enable the Synology integration on the Notifiarr website
3. Enable the triggers for the severity levels you want to monitor
4. Optionally enable fuzzy matching for better notification routing
5. Test the notification to ensure it is working
