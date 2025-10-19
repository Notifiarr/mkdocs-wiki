
#### Client

![GitHub commit activity](https://img.shields.io/github/commit-activity/t/notifiarr/notifiarr?label=Commits&style=for-the-badge&color=526cfe)
![GitHub commit activity (branch)](https://img.shields.io/github/commit-activity/t/notifiarr/notifiarr/main?label=Stable%20(:latest)&style=for-the-badge&color=526cfe)
![GitHub commit activity (branch)](https://img.shields.io/github/commit-activity/t/notifiarr/notifiarr/unstable?label=Unstable%20(:unstable)&style=for-the-badge&color=526cfe)
![GitHub last commit (branch)](https://img.shields.io/github/last-commit/notifiarr/notifiarr/unstable?label=Last%20(:unstable)&style=for-the-badge&color=526cfe)
![GitHub contributors](https://img.shields.io/github/contributors/notifiarr/notifiarr?label=Contributors&style=for-the-badge&color=526cfe)
![GitHub issues](https://img.shields.io/github/issues/Notifiarr/notifiarr?&logo=github&style=for-the-badge&color=526cfe)
![GitHub issues](https://img.shields.io/github/issues-closed/Notifiarr/notifiarr?&logo=github&style=for-the-badge&color=526cfe)
![GitHub issues](https://img.shields.io/github/issues-pr/Notifiarr/notifiarr?&logo=github&style=for-the-badge&color=526cfe)
![GitHub issues](https://img.shields.io/github/issues-pr-closed/Notifiarr/notifiarr?&logo=github&style=for-the-badge&color=526cfe)
[![GitHub license](https://img.shields.io/github/license/Notifiarr/notifiarr?&logo=github&style=for-the-badge&color=526cfe)](https://github.com/Notifiarr/notifiarr/blob/main/LICENSE)

#### Site

![GitHub issues](https://img.shields.io/github/issues/Notifiarr/website?&logo=github&style=for-the-badge&color=526cfe)
![GitHub issues](https://img.shields.io/github/issues-closed/Notifiarr/website?&logo=github&style=for-the-badge&color=526cfe)

#### Support

[![Discord](https://img.shields.io/discord/764440599066574859?label=Discord&style=for-the-badge&color=7F00FF)](https://notifiarr.com/discord)

![Logo](assets/logo.png)

# Notifiarr

You just found one of the coolest tools on the Internet for a homelab enthusiast.
We do notifications. We do them right. We've been doing then for years and we'll keep doing them for years to come.
Notifiarr provides native custom integrations with dozens, maybe hundreds of applications and websites.
That means these applications or websites can send data to Notifiarr, and we'll format a message according to
your configuration then send it to your chat server.

What sets us apart from direct integrations are the options we provide to format your messages. We also maintain and provide, for your conveince, a local agent you may run on any server or network you wish to monitor. The agent is fully configurable to collect network and system data so you can get health reports from your servers.

Everything is configurable, even how much data we keep on our servers. You get to decide how long your transaction log files live for, or if your transactions even get logged at all.

## Support

Over on [discord](https://notifiarr.com/discord)
we have a big community, if you need assistance you can ask there by opening a support thread in the `#support` channel.
!!! info
    For Patron access - Link your GitHub from the Profile Page on the Notifiarr Website

## From the author

I built Notifiarr in late 2019 for [myself](https://github.com/austinwbest), and it was used by only myself until
August of 2020 when I opened it up for others to use. My goal has always been to have a single location for common
notification needs, so I am not jumping around 20 apps to do things. [Captain](https://github.com/davidnewhall)
joined the crew in December 2020, and the two of us run the servers and write the code for the client and website.

## Integrations

!!! note
    [How to setup integrations](pages/integrations/basicUsage.md#how-to-setup-integrations)

## Additional Features

- Fully configurable on what triggers to get notifications for. Each integration and many triggers in them can go to their own channels.
- Layout configuration for some notifications
- Content configuration for most notifications (color, content, etc)
- Media Requests Bot - Discord Bot for all 4 \*Arr apps with:
  - Media Requests
  - User Permissions
  - Approvals
  - Sonarr Profiles
  - Default Options
  - Series Following
  - Discover features
  - Multi-Instance Support
- Minimal Access - No \*Arr apikeys or anything of the sort is used or saved on the site.
  All requests to the client are verified with your Notifiarr apikey and thrown out if they don't match up
- TRaSH Custom Format Sync [*\*Patron Feature\**](pages/faq/faq.md#q-what-are-the-user-level-differences) -
  Automated continuous add/sync for the custom formats TRaSH has made to use with Radarr
- Radarr Collections - A fully automated way to monitor all your Radarr collections with auto add new
  items to your library as they are put into the collection on TMDb for any monitored collections, etc.
