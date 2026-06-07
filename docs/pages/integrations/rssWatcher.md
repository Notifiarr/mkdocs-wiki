# RSS Watcher

## Integration Card

![integration_card.png](../../assets/screenshots/integrations/rsswatcher/integration_card.png)

1. Configuration
2. Channel picker for the feeds

### Channel Picker

![discord_channel_setup.png](../../assets/screenshots/integrations/rsswatcher/discord_channel_setup.png)

1. List of channels `Dropdown menu`
2. Test bot channel permissions
3. Copy Channel to all

## Configuration

![integration_settings.png](../../assets/screenshots/integrations/rsswatcher/integration_settings.png)

1. Page to configure the RSS Watcher.
2. Custom Icon `Subscriber Feature`
3. Example screenshots of what you can expect the notification to look like.

### Preset Feeds

Toggle on the preset RSS feeds you want to receive notifications from. In addition to the standard preset feeds, there are two special feeds:

- **Movie News** - Sourced from `filmjabber.com`. When enabled, you can select which sub-feeds to include:
    - Recent theaters
    - Upcoming theaters
    - Recent physical
    - Upcoming physical
- **Show News** - Sourced from `ismyshowcancelled.com`. When enabled, you can select which sub-feeds to include:
    - Announced
    - Renewed
    - Cancelled

### Custom Feeds

You can add your own RSS feeds with the following settings:

1. **Active** - Enable or disable the custom feed
2. **Name** - A display name for the custom feed
3. **URL** - The URL for the RSS feed (must be a valid Atom RSS feed)
4. **Include** - An inclusive regex filter to only post matching items
5. **Delete** - Remove an existing custom feed

!!! note
    Open the channel picker after adding a feed to assign its channel.
