# Better Stack

!!! info
     This integration allows for notifications from Better stack utilizing their webhook system

---

## Trigger options

![triggers-channels.png](../../assets/screenshots/integrations/betterstack/triggers-channels.png)

1. Triggers
    - `Started` - Sent when Better Uptime detects an issue with a site you are monitoring
    - `Ack` (Acknowledged) - Sent when you mark the issue as acknowledged through Better Uptime
    - `Resoled` - Sent when the site you are monitoring returns a successful response
1. Channel
    - Pick a channel from your server to send these notifications

---

## Configuration

![open-configuration.png](../../assets/screenshots/integrations/betterstack/open-configuration.png)

Click the **cog icon** to open the configuration options for Better Uptime.

![configuration.png](../../assets/screenshots/integrations/betterstack/configuration.png)

1. Notification colors for each trigger type
1. Notification content options that you can turn on/off to show in the notifications
1. Better Uptime team id that is used to link the Incident in the notification

!!! note
     This integration sends a single notification for all triggers. After the first one is sent, the rest will update the existing notification in the chain.
