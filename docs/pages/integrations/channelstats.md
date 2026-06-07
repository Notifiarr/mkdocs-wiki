# Channel stats

!!! Prerequisites
    This integration requires both a [client](https://notifiarr.wiki/pages/client/install/) setup and the configuration of the [dashboard](https://notifiarr.wiki/pages/integrations/dashboard/) integration, as the channel stats will pull data from there.

!!! info
    `Channel stats` requires you to enable the `manage channels` and `connect` permissions within your discord settings for the notifiarr bot.

!!! warning
    Do not attempt to change any of the permissions or settings of the channels that are created by this integration. They are very specific, so they are read-only to users.

## Setup

Setup for `channel stats` is a little different than the rest; you don't need an API key, nor do you choose any channels. Since we have to give the bot the above permissions, it instead creates voice channels with the appropriate data that you enable.

While most of the information is pulled from the dashboard integration, things such as `New Movies` or `New Episodes` utilize the `Imported` trigger for the corresponding Starr integration. If you plan to use the GitHub triggers, you will need to also setup the GitHub integration.

![channel-stats.png](../../assets/screenshots/integrations/channel-stats/channel-stats.png)

!!! info
    You will also need the Plex client setup if you plan to use the available Plex triggers.

Each stat creates a Discord voice channel displaying the corresponding value. You can customize the display name for each stat.

### Discord

- `Discord: Users` - Number of members in the server

### Notifications

- `Notifications: Daily` - Number of notifications sent today
- `Notifications: Total` - Total notifications Notifiarr has ever sent

### Lidarr

- `Lidarr: Albums added today` - Number of albums added today
- `Lidarr: Albums upgraded today` - Number of albums upgraded today
- `Lidarr: Total instance N tracks` - Total tracks per instance (choose On Disk or In Database)

### Radarr

- `Radarr: Movies added today` - Number of movies added today
- `Radarr: Movies upgraded today` - Number of movies upgraded today
- `Radarr: Total instance N movies` - Total movies per instance (choose On Disk or In Database)

### Readarr

- `Readarr: Books added today` - Number of books added today
- `Readarr: Books upgraded today` - Number of books upgraded today
- `Readarr: Total instance N books` - Total books per instance (choose On Disk or In Database)

### Sonarr

- `Sonarr: Episodes added today` - Number of episodes added today
- `Sonarr: Episodes upgraded today` - Number of episodes upgraded today
- `Sonarr: Total instance N episodes` - Total episodes per instance (choose On Disk or In Database)
- `Sonarr: Total instance N series` - Total series per instance

### GitHub

Requires the GitHub integration to be set up.

- `Github: Repository` - The repository to pull stats from (e.g. Notifiarr/website)
- `Github: Repository watchers` - Number of watchers on the repository
- `Github: Repository stars` - Number of stars on the repository
- `Github: Repository issues` - Number of open issues on the repository

### Plex

Requires the Plex client to be set up.

- `Plex: Streaming` - Current number of Plex streams
- `Plex: Transcoding` - Current number of transcodes on the server
- `Plex: Traffic` - Current Plex traffic
- `Plex: Lan Traffic` - Current Plex traffic on your LAN
- `Plex: Wan Traffic` - Current Plex traffic on your WAN

!!! note
    The "Total instance N" stats support multiple instances. Each instance can independently choose between displaying the On Disk or In Database count.

## Example

![example.png](../../assets/screenshots/integrations/channel-stats/example.png)
