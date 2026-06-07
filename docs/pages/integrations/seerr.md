# Seerr

!!! info
    In February 2026 the upstream [Jellyseerr](https://github.com/Fallenbagel/jellyseerr) and [Overseerr](https://github.com/sct/overseerr) projects merged into a single application called [**Seerr**](https://seerr.dev). Notifiarr's **Seerr** integration replaces the previous separate Jellyseerr and Overseerr integrations and works with any Seerr instance — including existing Jellyseerr / Overseerr installations during the upstream sunset period.

    Upstream announcement: [docs.seerr.dev — Seerr Release: Unifying Overseerr and Jellyseerr](https://docs.seerr.dev/blog/seerr-release/).

---

## Trigger options

1. Triggers
    - `Pending` - Receive a notification when a new request is pending
    - `Approved` - Receive a notification when a request is approved
    - `Auto approved` - Receive a notification when a request is automatically approved
    - `Declined` - Receive a notification when a request is declined
    - `Available` - Receive a notification when requested media becomes available
    - `Failed` - Receive a notification when a request fails
    - `Issues` - Receive a notification when an issue is created or commented on
1. Channel
    - Pick the channel for each trigger's notifications

---

## Configuration

1. Enable triggers and pick colors for each trigger
1. Expand the notification content settings via the customize button

Each trigger (except `Issues`) has the following notification content options:

- `Thumbnail` - Show the media poster
- `Requester` - Show who requested the media
- `Request Id` - Show the request ID
- `Overview` - Show the media overview/summary
- `Status` - Show the request status
- `Network` - Show the network/studio
- `Links` - Show links to external sites
- `Rating: IMDb` - Show the IMDb rating
- `Rating: TMDb` - Show the TMDb rating
- `Rating: TVDb` - Show the TVDb rating
- `Rating: RT` - Show the Rotten Tomatoes rating
- `Rating: MC` - Show the Metacritic rating
- `Awards` - Show award information
- `Ping requester` - Ping the requester in the notification
- `Background` - Show a background image
- `Runtime` - Show the media runtime
- `Seasons requested` - Show which seasons were requested
- `Content Rating` - Show the content rating

The `Issues` trigger has:

- `Thumbnail` - Show the media poster
- `Background` - Show a background image

### Settings

- `Local URL` - Add the local URL to your Seerr (or pre-migration Jellyseerr / Overseerr) instance if you want direct links for movies and shows.

!!! note
    **Be sure to save settings**

---

## Instructions

In Seerr (or your existing Jellyseerr / Overseerr instance during migration):

1. Open **Notifications Settings**
2. Select the **Webhook** agent
3. Enable the webhook agent
4. Set the notification URL to:

    ```text
    https://notifiarr.com/api/v1/notification/seerr/YOUR_API_KEY
    ```

    Generate an integration-specific API key for Seerr on your Notifiarr profile.

5. Select the notification types you want to receive
6. Save changes and confirm the webhook is enabled
