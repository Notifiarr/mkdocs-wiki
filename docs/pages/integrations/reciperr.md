# Reciperr

!!! info
    This integration allows for notifications from [Reciperr](https://reciperr.com/) when movies or lists are added. Reciperr connects with Radarr to automatically add movies and lists based on recipes.

---

## Trigger Options

### Triggers

- `Movies` - Receive a notification when a movie is added via a recipe
- `Lists` - Receive a notification when a list is added via a recipe
- `Remote add: Movies` - Allow remote adding of movies through Reciperr
- `Remote add: Lists` - Allow remote adding of lists through Reciperr

### Channels

- Reciperr channel picker for each trigger

---

## Configuration

Click the **cog icon** to open the configuration options for Reciperr.

1. Notification color for Movies trigger
2. Notification color for Lists trigger
3. Notification pings for Remote add: Movies
4. Notification pings for Remote add: Lists

### Movie Settings

- **Add Movies Monitored** - Toggle whether added movies should be monitored
- **Minimum Availability** - Set the minimum availability for added movies (Released, In Cinemas, Announced)
- **Quality Profile** - Select the Radarr quality profile for added movies
- **Root Folder** - Select the Radarr root folder for added movies
- **Tag** - Select a Radarr tag to apply to added movies

### List Settings

- **Enable Automatic Add** - Toggle automatic adding of movies from lists
- **Add Movies Monitored** - Toggle whether list movies should be monitored
- **Search on Add** - Toggle whether to search for movies when added
- **Minimum Availability** - Set the minimum availability for list movies (Released, In Cinemas, Announced)
- **Quality Profile** - Select the Radarr quality profile for list movies
- **Root Folder** - Select the Radarr root folder for list movies

!!! note
    Movie and list settings require a working Radarr instance configured in the Notifiarr client. The quality profiles, root folders, and tags are pulled from your Radarr instance 1.

---

## Instructions

1. Enable the Reciperr integration on the Notifiarr website
2. Configure the triggers you want to use
3. Set up your movie and list settings with the appropriate Radarr configuration
4. Configure Reciperr to send webhook notifications to your Notifiarr webhook URL
5. Test the notification to ensure it is working
