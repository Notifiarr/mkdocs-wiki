# Apprise

!!! info
    [Apprise](https://github.com/caronc/apprise) allows you to send notifications from Notifiarr to hundreds of notification services. This page covers how Apprise connects to Notifiarr — for the full list of Apprise notification services, see [appriseit.com](https://appriseit.com/).

---

## How It Works

Apprise can send notifications **to** Notifiarr using the Notifiarr notification service plugin. This lets you route alerts from any Apprise-compatible source into your Notifiarr Discord channels.

For full setup instructions, see [Apprise's Notifiarr documentation](https://appriseit.com/services/notifiarr/).

---

## URL Format

```text
notifiarr://{api_key}/{channel_id}
notifiarr://{api_key}/{channel1_id}/{channel2_id}/{channelN_id}
```

---

## Requirements

| Parameter | Required | Description |
|-----------|----------|-------------|
| `api_key` | Yes | Your **global** Notifiarr API key (integration-specific keys will not work) |
| `channel_id` | Yes | Numeric Discord channel ID (enable Developer Mode in Discord to find this) |

---

## Optional Parameters

| Parameter | Description |
|-----------|-------------|
| `source` / `from` | Label describing the notification origin |
| `event` | Existing event ID to update instead of creating a new notification |

!!! warning
    As of this writing, the upstream Apprise webhook to Notifiarr only supports one user/role mention per payload.
