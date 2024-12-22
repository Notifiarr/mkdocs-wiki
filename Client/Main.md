---
title: Client: Features
description: 
published: true
date: 2023-09-07T08:24:31.786Z
tags: 
editor: markdown
dateCreated: 2021-05-22T01:08:20.353Z
---

<img src="https://docs.notifiarr.com/img/repo-logo.png">

To take full advantage of all the notification features that Notifiarr provides, we offer a client you may run on premises. This client acts as a reverse proxy into your Starr apps, and in some cases other apps like your downloaders.

## Features

The Notifiarr client provides many enhancements to the Notifiarr experience. Here are a few: 

- Enables **Media Requests**. Add content from your chat server.
- Configurable **Network and Service Health checks**. Get notified when something goes down.
- **Plex webhook relay**. Plex sends many webhooks; we use the client to filter them.
- **Starr app proxy**. This feature enables access to starr APIs with your Notifiarr API key (or a custom api key).
- Configurable **System Snapshots**. Get notifications containing system metrics. Examples:
	- **CPU**, **Memory**, **Storage**, Raid Health: **MegaRaid**, **mdadm**, disk health: **smartctl**
  - **Nvidia**: nvidia-smi, **MySQL**: display top queries
- **TRaSH Custom format** Sonarr and Radarr sync.
- Get notifications for **downloads stuck in your starr app** queues.
	- Configure automated actions for these items.
- Daily dashboard notification for all starr, media and download apps.
- Hourly **Plex Sessions** notifications.
- **Sqlite database corruption checks** for Starr apps.
- **Watch / Tail [log] files** and get notifications for matched lines.
- **Command Relay**. Run scripts or commands on your server right from a chat channel.
- Act as a timer/trigger for certain Notifiarr Website actions
  - **Discord Cleanup**


The application itself is full featured and built securely. 
- Configurable upstreams by IP or CIDR.
- Supports proxy authentication.
- Configurable app, debug, http and service-check log files.
- Built in log file rotation.
- Parallel service checks for those with a lot of services.
- Supports HTTPS SSL certificate validation.
- Supports serving SSL with a valid TLS certificate and key.
- Configurable bind address (port) and url-base (subfolder proxy friendly).
- Beautiful UI. Can be themed.
- Log file viewer and log file tailing support using websockets.
- Automatic secure tunnel creation / communication established to the Notifiarr website
  - No exposure of the Local Client via a reverse proxy or port forward is required
  - Local Client creates a tunnel back home via a socket
## Installation

See the [Installation](/Client/Installation) page.

## Source Code

The client is open source and [available on Github](https://github.com/Notifiarr/notifiarr).


