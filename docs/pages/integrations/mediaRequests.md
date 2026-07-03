# Media Requests

!!! info
    This integration allows for requesting media via Discord.

## Currently Supported Applications

- Lidarr >= v1
- Radarr >= v4
- Readarr >= v1
- Sonarr >= v4

## Trigger options

![triggers.png](../../assets/screenshots/integrations/mediarequests/triggers.png)

### Triggers

- `Lidarr` - Enable Lidarr requests for an instance
- `Radarr` - Enable Radarr requests for an instance
- `Readarr`- Enable Readarr requests for an instance
- `Sonarr`- Enable Sonarr requests for an instance

### Channel

- Pick the channel on your server to monitor for requests and send optional approval messages.

---

## Configuration

### Global configuration

![open-configuration.png](../../assets/screenshots/integrations/mediarequests/open-configuration.png)

Click the **cog icon** to open the configuration options for *arr apps.

![configuration.png](../../assets/screenshots/integrations/mediarequests/configuration.png)

1. The client to use for Media Requests
1. Default \*arr apps; opening them allows for individual configuration. Details below.
1. The `+` button adds another instance of an \*arr app. This also needs to be configured in the Notifiarr client config (or ENV if you use that). Details below.
1. User based granular options
1. Cleanup will remove all the ping/pong messages when adding things, leaving only the final message.
1. Default keywords that control the bot, change them however you want.

### Settings

- `Client Connection` - Which client is used to make requests. Any local clients linked to your account will show.
- `Starr` - Default \*arr app instances. Open each to configure individual instance settings. The + button adds another instance.
- `Users` - Manage Discord users and their permissions for requests.
- `Require Approval` - When enabled, users need approval before requests are added. Open user settings to configure which users can approve. Users who can approve are not required to get approval.
- `Message Cleanup` - Cleanup message history after requests are complete. The bot requires Manage Messages permission for this.
- `Request Imported Message` - Custom message sent when a request is imported/filled.
- `Request Imported Notify` - Where to send the imported notification: post in request channel or post in DM.
- `Request Added Notify` - Where to send the added notification: post in request channel or post in DM.
- `Requests per day (per user)` - Limit the number of requests per user per day. Zero means no limit. User-specific limits will override this.

### Message Colors

- `Ping/Pong` - Color for normal back and forth messages
- `Success` - Color for when media is added to a starr app
- `Soft error` - Color for when media already exists, for example
- `Hard error` - Color for when the starr app throws an error or the client is down

### Bot UI Keywords

These keywords control how users interact with the bot in Discord. Each can be customized to your preference.

| Keyword | Default | Description |
| --------- | --------- | ------------- |
| `search` | search | Opens the search/request UI (always enabled) |
| `discover` | discover | Browse available media (can be disabled) |
| `approve` | approve | Approve pending requests (always enabled) |
| `follow` | follow | Follow a request for updates (can be disabled) |

### Bot Ping/Pong Keywords

| Keyword | Default | Description |
| --------- | --------- | ------------- |
| `help` | help | Show help information (always enabled) |
| `cancel` | cancel | Cancel an active request session (always enabled) |
| `details` | details | Show details about media (can be disabled) |
| `move` | move | Move media between instances (can be disabled) |

### Multiple instances

![configuration-2.png](../../assets/screenshots/integrations/mediarequests/configuration-2.png)

1. Add another instance of an \*arr app to be used for anything related to the Notifiarr client.

## App settings

![app-settings.png](../../assets/screenshots/integrations/mediarequests/app-settings.png)

1. Keyword the bot looks for when adding something. add ***movie*** batman for example.
1. Settings used when adding media to \*arr.

### User settings

![user-settings.png](../../assets/screenshots/integrations/mediarequests/user-settings.png)

1. Discord users that can be used to assign permissions to
1. User details
1. App settings for the user

### Instructions

![instructions.png](../../assets/screenshots/integrations/mediarequests/instructions.png)

A basic overview on how to use the integration. This may change from time to time on the site without updating the screenshot here.

### Discord Troubleshooting

- Type `cancel` to end any existing or stuck requests
- Type `help` to ensure the bot has access to the channel and can respond
