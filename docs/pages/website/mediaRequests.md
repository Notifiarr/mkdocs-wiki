# Media Requests

The Media Requests page has two tabs: **History** and **Gaps**.

## History

![media-requests-1.png](../../assets/screenshots/website/media-requests-1.png)

1. History tab will show you all your request history from the bot
2. Radarr collections (`Subscriber` feature, details below)
3. Total requests per \*arr app
4. Details about each request made
5. Action buttons for things that are pending if approval is used (This can also be done with the bot)

!!! note
    If the Media Requests integration is not enabled, a message will be shown to enable it first. The integration supports Lidarr, Radarr, Readarr, and Sonarr requests.

### Requests by App

A summary table showing the total request count for each \*arr application: Lidarr, Radarr, Readarr, and Sonarr.

### Tags by App

A table displaying the configured tags for each \*arr application:

- `App` tags - Tags configured at the application level
- `User` tags - Tags configured per Discord user via folder mapping
- `Update missing tags` - Click the refresh icon to retroactively apply tags to requests that are missing them

### Request Details

A sortable table of all requests with columns: `ID`, `Added`, `Source`, `Title`, `User`, `Notified`, `Approved`, `Denied`, and action buttons.

- Titles link to their respective external database (TMDB for Radarr, TVDB for Sonarr, MusicBrainz for Lidarr, Goodreads for Readarr)
- Pending requests show `Details`, `Approve`, and `Deny` buttons

## Collections Monitoring (Gaps)

![media-requests-1.png](../../assets/screenshots/website/media-requests-3.png)

1. Turn monitoring on/off per instance
1. Sync happens automatically every 12 hours, refresh icon will do an instant sync
1. Filter the table of collections

![media-requests-1.png](../../assets/screenshots/website/media-requests-2.png)

1. Manual checkbox, something you are going to add now
1. Monitor checkbox, something you want to automatically have monitored so when new movies are added to the collection, they are automatically added to your library
1. Exclude checkbox, something you do not want to monitor during automation
1. TMDb collection name and link to the collection
1. List of movies in the collection and if you have them or not
1. Percentage of the collection that is completed
1. A check before the movie means the movie is in Radarr's list exclusion and will not be added even if automatically monitoring the collection
1. Manual settings if you want to add missing movies from collections now
1. Monitor settings for how automation will be handled
