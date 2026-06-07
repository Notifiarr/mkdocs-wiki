# Reddit

!!! info
    This integration allows for notifications from subreddits you choose to watch

---

## Monitoring overview

![overview1.png](../../assets/screenshots/integrations/reddit/overview1.png)

This will list all subreddits you are monitoring.

---

## Configuration

![open_config.png](../../assets/screenshots/integrations/reddit/open_config.png)

Click the **cog icon** to open the configuration options for the Reddit integration.

![configuration2.png](../../assets/screenshots/integrations/reddit/configuration2.png)

### Existing Subreddits

Each monitored subreddit has the following settings:

1. `Channel` - Pick a Discord channel for the subreddit notification to go to
2. `/r/` - The subreddit name
3. `Exclude regex` - Only notify if the title or user does **not** contain this regex pattern
4. `Include regex` - Only notify if the title or user **does** contain this regex pattern
5. `Domain` - Use a custom domain in place of reddit for those using libreddit or similar frontends (e.g. `https://reddit.com`)
6. `Update` - Save changes to the subreddit's settings
7. `Delete` - Remove the subreddit from being monitored

### Adding a New Subreddit

1. `Channel` - Pick a channel for the subreddit notification to go to
2. `/r/` - Enter the subreddit name (e.g. `OpenSignups`)
3. `Exclude regex` - Optional regex pattern to exclude matching posts
4. `Include regex` - Optional regex pattern to only include matching posts
5. `Domain` - Optional custom domain to use in notification links
6. `Add` - Add the subreddit to your account to monitor
