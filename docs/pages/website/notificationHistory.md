# Notification History

Not all notifications are logged, only those needed for updating messages or tracking changes. Up to 32 days is stored based on your privacy settings.

![notification-history.png](../../assets/screenshots/website/notification-history.png)

## Statistics

The top of the page shows two summary tables:

### Time-Based Breakdown

Notification counts broken down by time period: `1 hr`, `6 hrs`, `12 hrs`, `24 hrs`, `1 wk`, `2 wks`, `3 wks`, `1 mon`, and `Site` total.

### Per-Integration Breakdown

Notification counts per integration: Better Uptime, Lidarr, Plex, Radarr, Readarr, Snapshot, Sonarr, Unpackerr, and Website Status.

## History Tab

A sortable table showing all notification history with the following columns:

- `ID` - Notification identifier
- `Sent` - When the notification was sent (formatted per your profile date format)
- `Source` - Which integration sent it. If a Discord server is configured and a message ID exists, the source links directly to the Discord message
- `Trigger` - The event type that triggered the notification (e.g., Grab, Import, etc.)
- `Title` - The media or event title
- Actions column with external links and a blacklist icon for Sonarr/Plex series

## Blacklist Tab

The Blacklist tab shows all series you have blacklisted from notifications. Blacklisted series will not generate notifications from Sonarr or Plex.

- Click the ban icon on any Sonarr or Plex series in the History tab to add it to the blacklist
- Click the ban icon in the Blacklist tab to remove it
