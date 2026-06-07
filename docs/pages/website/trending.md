# Trending

The Trending page shows the most popular media across all Notifiarr users over the last 30 days, organized into four columns.

![trending-1.png](../../assets/screenshots/website/trending-1.png)

## Sections

1. **Radarr** - Most grabbed movies among all users with Radarr enabled
1. **Plex Movies** - Most watched movies among all users with Plex enabled
1. **Sonarr** - Most grabbed series among all users with Sonarr enabled
1. **Plex Series** - Most watched series among all users with Plex enabled

Each item displays a poster, title, and external links (TMDB/IMDB for movies, TVDB/IMDB for series).

### Add to *arr

If the Media Requests integration is enabled and your client is connected with the required default settings configured (quality profile, root folder, etc.), each trending item will show buttons to add it directly to your Radarr or Sonarr instance(s).

## JSON Lists

![trending-2.png](../../assets/screenshots/website/trending-2.png)

At the bottom of the page are JSON list URLs that can be used as custom lists in your *arr applications.

### Movie JSON Lists

- `Radarr` - Only Radarr grabs
- `Plex` - Only Plex watched movies
- `Both` - Combined Radarr and Plex movie data

### Series JSON Lists

- `Sonarr` - Only Sonarr grabs
- `Plex` - Only Plex watched series
- `Both` - Combined Sonarr and Plex series data

### Series Exclusion Filter

The series JSON lists include an exclusion filter with checkboxes for TVDB networks. Check the networks you want to exclude, then append the generated `&filter=` parameter to the list URL.
