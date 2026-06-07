# qBit Manage

!!! info
    This integration allows for notifications from [qBit Manage](https://github.com/StuffAnThings/qbit_manage) for torrent management operations. qBit Manage sends webhook notifications to Notifiarr for various torrent lifecycle events.

---

## Trigger Options

### Triggers

- `Error` - Receive a notification when qBit Manage encounters an error
- `Start` - Receive a notification when qBit Manage starts a run
- `End` - Receive a notification when qBit Manage completes a run
- `Cross seed` - Receive a notification for cross-seed operations
- `Tag cross seed` - Receive a notification when cross-seed tags are applied
- `Recheck` - Receive a notification for torrent rechecks
    - Optional: Include Poster and Background/Banner images
- `Tag update` - Receive a notification when torrent tags are updated
    - Optional: Include Poster and Background/Banner images
- `Category update` - Receive a notification when torrent categories are changed
    - Optional: Include Poster and Background/Banner images
- `Remove unregistered` - Receive a notification when unregistered torrents are removed
    - Optional: Include Poster and Background/Banner images
- `Tag tracker error` - Receive a notification when torrents are tagged for potential tracker errors
    - Optional: Include Poster and Background/Banner images
- `Untag tracker error` - Receive a notification when tracker error tags are removed
    - Optional: Include Poster and Background/Banner images
- `Remove orphaned` - Receive a notification when orphaned files are removed
- `Tag no hardlinks` - Receive a notification when torrents are tagged as having no hardlinks
    - Optional: Include Poster and Background/Banner images
- `Untag no hardlinks` - Receive a notification when no-hardlinks tags are removed
    - Optional: Include Poster and Background/Banner images
- `Share limit changes` - Receive a notification when share limits are applied
    - Optional: Include Poster and Background/Banner images
- `Cleanup share limits` - Receive a notification when share limit cleanup runs
    - Optional: Include Poster and Background/Banner images
- `Empty recycle bin` - Receive a notification when the recycle bin is emptied

### Channels

- Qbit Manage channel picker for each trigger

---

## Configuration

Click the **cog icon** to open the configuration options for Qbit Manage.

Each trigger has its own configuration options:

1. Notification color selector per trigger
2. Notification pings per trigger
3. Poster and Background/Banner display options (where applicable)

---

## Instructions

1. In your qBit Manage configuration, add the Notifiarr webhook:

    ```yaml
    webhooks:
      notifiarr:
        apikey: YOUR_API_KEY
    ```

2. Enable the triggers you want on the Notifiarr website
3. Test the notification to ensure it is working

!!! note
    For more information on configuring qBit Manage webhooks, refer to the [qBit Manage Wiki](https://github.com/StuffAnThings/qbit_manage/wiki)
