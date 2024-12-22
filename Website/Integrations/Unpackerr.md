---
title: Unpackerr
description: 
published: true
date: 2023-07-26T22:38:20.074Z
tags: 
editor: markdown
dateCreated: 2021-05-23T02:26:42.821Z
---

> This integration provides [Unpackerr](https://golift.io/unpackerr) notifications and reactions.
{.is-info}

You may choose to have either a reaction placed on existing Starr notifications, or receive a stand alone message for Unpackerr notifications, or both. Selecting the *Reactions* box enables or disables the Reaction emoji. 

As a premium feature you may elect to have Unpackerr notifications automatically add Custom Formats to your Starr apps. These custom formats downgrade the priority on the release group that gave you a packed download. That means in time your Starr apps will choose to download fewer and fewer packed items.

#### Reaction example

![reaction.png](/unpackerr/reaction.png)

#### Notifiation Example
![extracted_notification.png](/unpackerr/extracted_notification.png)


---

## Trigger options

![trigger-channels.png](/unpackerr/trigger-channels.png)

### Triggers

Select the notification messages you want to appear in your chat server. You may deselect all of them if you only want reactions.

- `Processing` - Send notification when Unpackerr has started processing (Extracting, Extracted)
- `Imported` - Send notification when Unpackerr has marked it imported
- `Failed` - Send notification when Unpackerr fails to unpack
- `Update Available` - Not part of Unpackerr, this is a check Notifiarr does

### Channel

- Which channel to send Unpackerr notifications to

---

## Configuration

![open-configuration.png](/unpackerr/open-configuration.png)

Click the **cog icon** to open the configuration options for Unpackerr.

![configuration.png](/unpackerr/configuration.png)

1. Pick the colors for notification triggers
1. Add a reaction to the grab/download from \*arr

### Instructions

- You should create an application-specific key for Unpackerr.
- Add a snippet like the following to your unpackerr config file.
- Replace `api_key_from_notifiarr_com` with your notifiarr.com API key.
- Adjust other settings as needed. See [Unpackerr](https://github.com/Unpackerr/unpackerr#webhooks) repo for documentation.

```
[[webhook]]
  url     = "https://notifiarr.com/api/v1/notification/unpackerr/api_key_from_notifiarr_com"
  name    = "Notifiarr" # Set this to hide the URL in logs.
  silent  = true        # do not log success (less log spam)
  events  = [0]         # list of event ids to include, 0 == all.
  exclude = []          # list of apps to exclude, e.g. ["radarr", "lidarr"]
```

