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

1. In your Watchtower compose file, enable the report and set the notification URL. The site shows the URL with a `generic://` scheme and `?template=json` at the end:

    ```text
    WATCHTOWER_NOTIFICATION_REPORT=true
    WATCHTOWER_NOTIFICATION_URL=generic://notifiarr.com/api/v1/notification/watchtower/YOUR_API_KEY?template=json
    ```

2. Optional: add `&server=NAME` to the end of the URL to show which server sent the notification
3. Enable the triggers you want on the Notifiarr website
4. Restart or recreate the Watchtower container. It sends a `Checking` notification
