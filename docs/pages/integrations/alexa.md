# Alexa

!!! info
    This integration lets you control Notifiarr with voice commands through an Amazon Alexa skill. Check Plex sessions, request movies and shows, get network status, and more.

!!! warning "Beta"
    The Alexa skill is marked **beta** on the Notifiarr website. Behavior and available commands may change.

---

## Requirements

- An active Notifiarr **Subscriber** account. Anyone can add the skill in the Alexa app, but only active subscribers can link an account and use it.
- A Notifiarr client for the network status, command, and media request voice commands.

---

## Instructions

1. Open the Alexa app, go to **Skills**, and search for **Notifiarr**
1. Enable the skill and link your Notifiarr account
1. Open the Alexa integration page on the Notifiarr website to see the link status. It shows `Active` when linked and `Inactive` when the link has expired.

---

## Voice commands

Every request starts with `Alexa, ask notifer bot`. The skill name is spelled "notifier" because Alexa transcribes it more reliably that way. The examples below leave this phrase out.

| Say | What it does |
| :- | :- |
| `my account overview` | Reads your account level, join date, last visit, and notification counts |
| `for my network status` | Reads how many services the client monitors and how many are online. Alexa asks which client to use if more than one client monitors services |
| `who is streaming` | Reads the current Plex streams, who is watching, and on which device |
| `to request the movie batman from 1989` | Searches Radarr for the movie and asks follow-up questions if there are many matches |
| `to request the series <name>` | Searches Sonarr for the series and asks follow-up questions if there are many matches |
| `to trigger plex restart` | Runs a [client command](../client/commands.md) by name |
| `for trending movies` | Reads the trending movies. Series and animated movies or series also work |

### Requests

- Use `request` or `grab` for a movie or a series. Do not use `add`, because Alexa reserves that keyword.
- Include the year when you know it. It narrows the matches.
- If there are too many matches, Alexa asks follow-up questions, such as whether you want an animated version.

### Commands

- The words after `trigger` are the command name.
- You do not need to say which client the command belongs to. Alexa searches all clients for a match.
- The word order does not have to match, so `restart plex` also works.
- If more than one command matches, Alexa lists them and does not run any.

---

## Request settings

Click **Customize** next to the request example on the Alexa integration page to choose how Alexa adds media. Set a client on the [Media Requests](mediaRequests.md) integration first.

For each of Radarr and Sonarr you pick the instance, the quality profile, and the root folder. Both also have these options:

- Search on add
- Monitor

Radarr also has minimum availability and collection options. Sonarr also has series type, monitor season, and season folder options.
