# Notifiarr Client HTTP API

The Notifiarr client runs a web server, on port `5454` by default, that exposes an HTTP API. The Notifiarr website uses it, and you can call it from your own scripts. This page covers the general endpoints. The Web UI also has a **Client API Documentation** page, linked from the Web UI home page, with every endpoint and its parameters.

---

## Basics

- All API paths start with `/api`. If you set a `urlbase`, put it in front of `/api`.
- Send your client API key in the `X-API-Key` header. Keys in the `extra_keys` config setting also work.
- A missing or wrong key returns HTTP `401`.
- Replies are JSON in the form `{"status": "200: OK", "message": ...}`.
- Instance numbers start at `1`. The first Radarr instance is `/api/radarr/1/...`.

```bash
curl -H "X-API-Key: YOUR-API-KEY" http://127.0.0.1:5454/api/info
```

---

## Client endpoints

| Method | Path | Description |
| :- | :- | :- |
| GET | `/api/info` | Client configuration, including the instance IDs and names you can use with other endpoints |
| GET | `/api/version` | Client information plus the up-status and version of each configured app |
| GET | `/api/version/{app}/{instance}` | The same, for one app instance. Plex and Tautulli only support instance `1` |
| GET | `/api/ping` | `true` or `false` for every configured Starr instance |
| GET | `/api/ping/{apps}` | The same for one or more Starr apps, separated by commas, such as `/api/ping/radarr,sonarr` |
| GET | `/api/ping/{app}/{instance}` | The same for one instance |
| GET | `/api/services/list` | Results of the service checks |
| GET | `/api/triggers` | The list of actions and website timers |
| GET | `/metrics` | Prometheus metrics. See [Metrics](metrics.md) |

The `/api/metrics` path also works for metrics. With a `urlbase`, `<urlbase>/metrics` works too.

---

## Trigger endpoints

Use `GET /api/trigger/{trigger}` to run an [action](actions.md). Some triggers take extra content as `GET /api/trigger/{trigger}/{content}`.

| Trigger | Content | Description |
| :- | :- | :- |
| `reload` | | Reload the client |
| `reconfig` | | Reconfigure the actions |
| `services` | | Run all service checks |
| `sessions` | | Collect Plex sessions |
| `dashboard` | | Send a dashboard notification |
| `snapshot` | | Send a system snapshot notification |
| `stuckitems` | | Send a stuck items notification |
| `gaps` | | Send Radarr collection gaps |
| `mdblist` | | Send libraries for MDBList |
| `cfsync` | Optional instance number | Sync TRaSH profiles and formats to Radarr |
| `rpsync` | Optional instance number | Sync TRaSH profiles and formats to Sonarr |
| `corrupt` | App name | Start a database backup corruption check |
| `backup` | App name | Send the list of backup files |
| `emptyplextrash` | Library keys | Empty the Plex trash |
| `uploadlog` | File | Upload a log file to Notifiarr.com |
| `notification` | Text | Send a client notification |
| `clientlogs` | `true` or `false` | Turn client error log sharing on or off |
| `custom` | Timer ID from `/api/triggers` | Run a custom timer from the website |
| `command` | Command hash | Run a [command](commands.md). `POST` accepts `args` form values |
| `endpoint` | Endpoint name | Run an [endpoint](endpoints.md) |

An unknown trigger returns HTTP `400`.

---

## Plex endpoints

These need the Plex integration. Use instance `1` for Plex.

| Method | Path | Description |
| :- | :- | :- |
| GET | `/api/plex/1/sessions` | Current Plex sessions |
| GET | `/api/plex/1/directory` | The Plex library directory |
| GET | `/api/plex/1/emptytrash/{libraryKey}` | Empty the trash for a library |
| GET | `/api/plex/1/markwatched/{itemKey}` | Mark an item as watched |
| GET | `/api/plex/1/kill` | End a session. Needs the `sessionId` and `reason` query parameters |

---

## Starr app endpoints

The client relays requests to your Radarr, Sonarr, Lidarr, Readarr, and Prowlarr instances. The paths follow `/api/{app}/{instance}/...`, for example `/api/radarr/1/qualityProfiles` or `/api/sonarr/1/rootFolder`. They cover adding and searching media, quality and release profiles, custom formats, naming, tags, root folders, and notifications. Prowlarr only supports notifications.

`POST /api/trash/{app}` retrieves custom format data from several instances of `radarr`, `sonarr`, or `lidarr`.

See the Client API Documentation page in the Web UI for the full list.
