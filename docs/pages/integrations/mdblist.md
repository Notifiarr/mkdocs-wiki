# MDBList

## What is MDBList

MDBList is a 3rd party service that allows you to curate lists of shows and movies from various sources and [can be found here](https://mdblist.com), this integration is meant to do three things:

1. Allow for the ability to add individual shows or movies to Radarr or Sonarr using the add button on the show item on the MDBList website
2. Sync lists created on MDBList into Sonarr and Radarr automatically
3. Sync a list of IDs from your local collection to MDBList which can be used within the filtering of a list, to exclude, for example, all collected shows or movies

## Prerequisites

1. Notifiarr setup and working with Discord, Sonarr, and Radarr integrations
2. Account with MDBList
3. API key created on the Notifiarr website and assigned for use with MDBList, this can be generated and found in your profile, under the API Keys section
4. On MDBList, go to Preferences → Notifiarr, paste the API key allocated to the MDBList integration, and enable “Automatically add lists to Radarr (if configured in Notifiarr)”

## Trigger options

- `List Add` - Receive a notification when MDBList sends a new list to add to the starr apps
- `List Updates` - Receive a notification when MDBList sends an updated list to add to the starr apps
- `Add Movie` - Receive a notification when a movie is added from the MDBList website
- `Add Show` - Receive a notification when a show is added from the MDBList website

Each trigger has notification color and notification ping settings.

## Steps to configure integration

1. From within the Notifiarr website add the MDBList integration
2. Configure your Discord channels
3. Enable the triggers you want (e.g. `Add Movie` and `Add Show`) by enabling the toggles as shown below.

![mdblist-movieaddtoggle.jpg](../../assets/screenshots/integrations/mdblist/mdblist-movieaddtoggle.jpg)

We now need to configure some additional settings from within the integration, to tell Notifiarr what settings to use when adding a movie or show.

## Configuration

!!! note
    Currently you cannot send things (movies, shows, lists) to different instances and you cannot have different settings per instance. This is a limitation on the side of MDBList.

The configuration has five tabs:

### Radarr lists

Settings for adding MDBList lists to Radarr.

- `Add lists to Radarr` - Enable/disable adding lists to Radarr
- `Instance` - Which Radarr instance to use (save and reopen after changing to update quality profile and root folder)
- `Enable Automatic Add` - Automatically add items from lists
- `Add Movies Monitored` - Add movies as monitored
- `Search on Add` - Search for movies when added
- `Minimum Availability` - Released, In Cinemas, or Announced
- `Quality Profile` - Quality profile to use from Radarr
- `Root Folder` - Root folder path from Radarr
- `List Tags` - Comma-separated tags to apply to list items

### Radarr movies

Settings for adding individual movies from the MDBList website to Radarr.

- `Add movies to Radarr` - Enable/disable adding movies to Radarr
- `Instance` - Which Radarr instance to use
- `Add Movie Monitored` - Add movie as monitored
- `Search on Add` - Search for movie when added
- `Quality Profile` - Quality profile to use from Radarr
- `Minimum Availability` - Released, In Cinemas, or Announced
- `Root Folder` - Root folder path from Radarr
- `Movie Tag` - Tag to apply to movies

### Sonarr lists

Settings for adding MDBList lists to Sonarr.

- `Add lists to Sonarr` - Enable/disable adding lists to Sonarr
- `Instance` - Which Sonarr instance to use
- `Enable Automatic Add` - Automatically add items from lists
- `Add Series Monitored` - Add series as monitored
- `Search on Add` - Search for series when added
- `Season Monitoring` - All Seasons, Latest Season, Future Seasons, or None
- `Season Type` - Daily, Standard, or Anime
- `Quality Profile` - Quality profile to use from Sonarr
- `Root Folder` - Root folder path from Sonarr
- `Show Tag` - Tag to apply to list items

### Sonarr shows

Settings for adding individual shows from the MDBList website to Sonarr.

- `Add shows to Sonarr` - Enable/disable adding shows to Sonarr
- `Instance` - Which Sonarr instance to use
- `Add Show Monitored` - Add show as monitored
- `Search on Add` - Search for show when added
- `Season Monitoring` - All Seasons, Latest Season, Future Seasons, or None
- `Season Type` - Daily, Standard, or Anime
- `Quality Profile` - Quality profile to use from Sonarr
- `Root Folder` - Root folder path from Sonarr
- `Show Tag` - Tag to apply to shows

### Library sync (Patron)

Sync your local library information to MDBList for better filtering.

- `Sync Radarr information` - Send a list of movies you have for better filtering (only the TMDb ID and download status is sent)
- `Sync instance` - Which Radarr instance to sync
- `Sync Sonarr information` - Send a list of shows you have for better filtering (only the TVDb ID and download status is sent)
- `Sync instance` - Which Sonarr instance to sync
- `Ignore list add warning` - Suppress warnings when lists cannot be added

![mdblist-movieaddsettings2.jpg](../../assets/screenshots/integrations/mdblist/mdblist-movieaddsettings2.jpg)
