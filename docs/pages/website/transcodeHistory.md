# Transcode History

Transcode History is a history of all Plex Streams Notifiarr received from your Plex Server.

!!! note
    The Plex integration must be active for this page to function. It pulls information from Play, Pause, and Session triggers.

It is required that you have a Notifiarr Profile retention of 1 or more days to see this data.

## Summary

At the top of the page is a summary table showing transcode counts vs. total stream counts for both Radarr (movies) and Sonarr (episodes).

## Graphs

![transcode-history-1.png](../../assets/screenshots/website/transcode-history-1.png)

1. Transcoding by video codec - Breakdown of video transcodes by codec, split by Radarr/Sonarr
1. Transcoding by audio codec - Breakdown of audio transcodes by codec, split by Radarr/Sonarr
1. Transcoding by device - Breakdown of transcodes per player device, split by Radarr/Sonarr
1. Transcoding by type - Audio vs. video transcode counts, split by Radarr/Sonarr

All charts are horizontal bar charts with Radarr and Sonarr shown as separate datasets.

## Recent History

![transcode-history-1.png](../../assets/screenshots/website/transcode-history-2.png)

A sortable table of recent transcode sessions with the following columns:

- `Played` - When the stream occurred
- `Type` - Movie or Episode
- `Title` - The media title (click to view session details)
- `Audio` - Audio codec information (click to view audio transcode details)
- `Video` - Video codec information (click to view video transcode details)
- `Rate` - Bandwidth usage and stream location (LAN/WAN)
- `User` - The Plex user
- `Device` - The player device
