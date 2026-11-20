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

1. This requires DSM 7.2 or later. In DSM go to Control Panel → Notifications → Webhooks and click **Add**
2. Pick `Custom` for the provider and `All` for the rule, then click Next
3. Set the name to `Notifiarr` and the subject to `host=%HOSTNAME%`. Copy the webhook URL from the Notifiarr Synology integration page into the `Webhook URL` field. Tick the option to send notifications in English, then click Next
4. Set the method to `POST` and the content type to `application/json`, then click Apply
5. On DSM 7.2.2, add `"hostname": "{your-syno-hostname}"` to the HTTP Body section. DSM 7.2.2 merges the hostname into the message, and the site reads the host from this field
6. Enable the triggers for the severity levels you want to monitor
7. Optionally enable fuzzy matching for better notification routing
