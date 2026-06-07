# Emby

!!! info
    This integration allows for notifications from the Emby media app

---

## Trigger options

![trigger-channels.png](../../assets/screenshots/integrations/emby/trigger-channels.png)

### Triggers

- `Play / Test` - Receive a notification when media starts playing. Also used for testing the integration
- `Pause` - Receive a notification when media playback is paused
- `Resume` - Receive a notification when media playback is resumed
- `Stop` - Receive a notification when media playback is stopped
- `Finished` - Receive a notification when media has finished playing (scrobble)
- `New Items` - Receive a notification when a new item is added to the library
- `User Authentication` - Receive a notification on user login, failed login, or lockout
- `Plugin Installed` - Receive a notification when a plugin is installed
- `Plugin Updated` - Receive a notification when a plugin is updated
- `Plugin Uninstalled` - Receive a notification when a plugin is uninstalled
- `Update Available` - Receive a notification when an Emby server update is available
- `Server Restart` - Receive a notification when the Emby server restarts
- `Mark Favorite` - Receive a notification when a user marks an item as a favorite
- `Mark Watched` - Receive a notification when a user marks an item as watched
- `Mark Unwatched` - Receive a notification when a user marks an item as unwatched

### Channels

- Setup the channel(s) to use for sending Emby notifications

---

## Configuration

![open-configuration.png](../../assets/screenshots/integrations/emby/open-configuration.png)

Click the **cog icon** to open the configuration options for Emby.

![configuration.png](../../assets/screenshots/integrations/emby/configuration.png)

1. Enable triggers and pick colors for each trigger

### Integration Settings

- `Split by Rating` - Send notifications with selected content ratings to a separate channel
- `Unmonitor movies on finish` - Automatically unmonitor a movie after a user finishes watching (Patron feature, requires valid Radarr information in client)
- `Unmonitor episodes on finish` - Automatically unmonitor an episode after a user finishes watching (Patron feature, requires valid Sonarr information in client)

---

### Instructions

![instructions.png](../../assets/screenshots/integrations/emby/instructions.png)

1. This needs to be done in Emby to enable webhooks
