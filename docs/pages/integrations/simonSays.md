# Simon Says

!!! info
    Simon Says is a Discord bot command integration that allows you to create custom keyword-triggered actions in your Discord server. Actions include generic responses, movie/series lookups, and GitHub issue creation.

---

## Action Types

### Generic

Create custom keyword-triggered responses. When a user types the keyword in a monitored channel, the bot responds with your configured message.

- Supports embedded images: `[image=https://linktoimage.com/someImage.jpg]`
- Supports thumbnails: `[thumbnail=https://linktoimage.com/someThumbnail.jpg]`
- Force message break: `[message-break]`
- Optional: Disable embed formatting with the `No embed` option

### Movie Info

Look up movie information using a keyword. Requires Radarr configured on the client.

- Example: `!movie the batman` - Returns information about the movie

### Series Info

Look up series information using a keyword. Requires Sonarr configured on the client.

- Example: `!show vikings` - Returns information about the series

### GitHub

Create GitHub issues directly from Discord using a keyword.

- Requires a GitHub organization and repository
- Requires a tag in the repo to block spam: `notifiarr-bot-YOUR_DISCORD_SERVER_ID`

---

## Configuration

Each action has the following settings:

1. **Keyword** - The trigger word/phrase (e.g., `!help`). Supports aliases with comma separation (e.g., `!help, !helpme`)
2. **Channels** - Which Discord channels to monitor, or select `All channels` to watch everywhere
3. **Roles** - Which roles can use the keyword, or select `Any role` or `Any user` for unrestricted access
4. **Response** - The bot's reply (for generic actions)
5. **Description** - A description of what the action does

### List Response

Use `!simonsays` in any monitored channel to get a list of available commands. Configure how the list is displayed:

- **DM list of commands** - Send the list as a direct message
- **Post link to list** - Post a link to the command list in the channel

---

## Instructions

1. Navigate to the Simon Says integration on the Notifiarr website
2. Select the action type (Generic, Movie, Series, or GitHub)
3. Configure the keyword, channels, roles, and response
4. Save the action
5. Test by typing the keyword in a monitored Discord channel
