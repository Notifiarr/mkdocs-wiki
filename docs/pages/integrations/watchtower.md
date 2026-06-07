# Watchtower

!!! info
    This integration allows for notifications from [Watchtower](https://containrrr.dev/watchtower/) when container updates are checked and found.

---

## Trigger Options

### Triggers

- `Checking` - Receive a notification when Watchtower checks for container updates
- `Updates` - Receive a notification when container updates are available

### Channels

- Watchtower channel picker for each trigger

---

## Configuration

Click the **cog icon** to open the configuration options for Watchtower.

1. Notification pings for each trigger
2. Notification layout customization for each trigger

### Settings

- `Full image names` - Show the full Docker image name without truncating with `...`

---

## Instructions

1. Configure Watchtower to send notifications to your Notifiarr webhook URL
2. In your Watchtower configuration, set the notification URL:

    ```
    https://notifiarr.com/api/v1/notification/watchtower/YOUR_API_KEY
    ```

3. Enable the triggers you want on the Notifiarr website
4. Test the notification to ensure it is working
