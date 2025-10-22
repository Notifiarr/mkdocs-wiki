# Notifiarr Client Configuration

!!!danger "Deprecated Page"
    This page is deprecated and the application configuration is now documented in the
    application [Web UI](gui.md). Log into the user interface in a web browser to read
    about all the configuration options.

**Use the Web UI to change the application configuration.**

## `.conf` File

The config file used to be the preferred way to change the application's behavior,
but now days the config file is compressed and direct edits are discouraged.
The format has become too much to properly document. If you're configuring your
client with automation such as puppet or ansible, then you should use environment
variables for configuration. It's possible the config file format may change in the
future, and the env variables are more likely to remain unaffected.

## Configuration Options

Config File and Environment Variables are listed below.
The up-to-date data now lives in the client's Web UI.

- Any variable not provided takes the default.
- Environmental Variables take precedent over config file settings.
- Must provide an "All" API key from [notifiarr.com](https://notifiarr.com).
  - **The Notifiarr application uses the API key for bi-directional authorization.**
- You may provide multiple Sonarr, Radarr or Readarr instances using `DN_SONARR_1_URL`,
  `DN_SONARR_2_URL`, etc or by duplicating the starr block in the conf file.
- Note the header of `[[radarr]]`, `[[sonarr]]`, `[[readarr]]`, etc. is required.

**The following data is out of date, and may not be updated very often.**

### Global Configuration

| Config Name   | Variable Name      | Default / Note                                                               |
| ------------- | ------------------ | ---------------------------------------------------------------------------- |
| api_key       | `DN_API_KEY`       | **Required** / API Key from Notifiarr.com                                    |
| auto_update   | `DN_AUTO_UPDATE`   | `off` / Set to `daily` to turn on automatic updates (windows only)           |
| bind_addr     | `DN_BIND_ADDR`     | `0.0.0.0:5454` / The IP and port to listen on                                |
| quiet         | `DN_QUIET`         | `false` / Turns off output. Set a log_file if this is true                   |
| ui_password   | `DN_UI_PASSWORD`   | None by default. Set a username:password & change the password to encrypt it |
| urlbase       | `DN_URLBASE`       | default: `/` Change the web root with this setting                           |
| upstreams     | `DN_UPSTREAMS_0`   | List of upstream networks that can set X-Forwarded-For                       |
| ssl_key_file  | `DN_SSL_KEY_FILE`  | Providing SSL files turns on the SSL listener                                |
| ssl_cert_file | `DN_SSL_CERT_FILE` | Providing SSL files turns on the SSL listener                                |
| log_file      | `DN_LOG_FILE`      | None by default. Optionally provide a file path to save app logs             |
| http_log      | `DN_HTTP_LOG`      | None by default. Provide a file path to save HTTP request logs               |
| log_file_mb   | `DN_LOG_FILE_MB`   | `100` / Max size of log files in megabytes                                   |
| log_files     | `DN_LOG_FILES`     | `10` / Log files to keep after rotating. `0` disables rotation               |
| file_mode     | `DN_FILE_MODE`     | `"0600"` / Unix octal filemode for new log files                             |
| timeout       | `DN_TIMEOUT`       | `60s` / Global API Timeouts (all apps default)                               |

### Secret Settings

Recommend not messing with these unless instructed to do so.

| Config Name | Variable Name     | Default / Note                                                                                    |
| ----------- | ----------------- | ------------------------------------------------------------------------------------------------- |
| extra_keys  | `DN_EXTRA_KEYS_0` | `[]` (empty list) / Add keys to allow API requests from places besides notifiarr.com              |
| debug       | `DN_DEBUG`        | `false` / Adds payloads and other stuff to the log output; very verbose/noisy                     |
| debug_log   | `DN_DEBUG_LOG`    | `""` / Set a file system path to write debug logs to a dedicated file                             |
| max_body    | `DN_MAX_BODY`     | Unlimited, `0` / Maximum debug-log body size (integer) for payloads to and from notifiarr.com     |
|             | `TMPDIR`          | `%TMP%` on Windows. Varies depending on system; must be writable if using Backup Corruption Check |

*Note: You may disable the GUI (menu item) on Windows and MacOS by setting the env variable `USEGUI` to `false`.*

### Snapshots

Many of the snapshot settings are on the website, but a few are configured locally.

#### Nvidia

The app can collect Nvidia GPU stats for snapshot notifications.

| Config Name              | Variable Name                 | Note                                           |
| ------------------------ | ----------------------------- | ---------------------------------------------- |
| snapshot.nvidia.disabled | `DN_SNAPSHOT_NVIDIA_DISABLED` | Set this to true to turn off this feature.    |

**Busids and smi path are missing. ^** This is incomplete.

#### MySQL

You may add mysql credentials to your notifiarr configuration to snapshot mysql
service health. This feature snapshots `SHOW PROCESSLIST` and `SHOW STATUS` data.

Access to a database is not required. Example Grant:

```mysql
GRANT PROCESS ON *.* to 'notifiarr'@'localhost'
```

| Config Name         | Variable Name            | Note                                           |
| ------------------- | ------------------------ | ---------------------------------------------- |
| snapshot.mysql.name | `DN_SNAPSHOT_MYSQL_NAME` | Setting a name enables service checks of MySQL |
| snapshot.mysql.host | `DN_SNAPSHOT_MYSQL_HOST` | Something like: `localhost:3306`               |
| snapshot.mysql.user | `DN_SNAPSHOT_MYSQL_USER` | Username in the GRANT statement                |
| snapshot.mysql.pass | `DN_SNAPSHOT_MYSQL_PASS` | Password for the user in the GRANT statement   |

### Lidarr

| Config Name      | Variable Name           | Note                                                                  |
| ---------------- | ----------------------- | --------------------------------------------------------------------- |
| lidarr.name      | `DN_LIDARR_0_NAME`      | No Default. Setting a name enables service checks                     |
| lidarr.url       | `DN_LIDARR_0_URL`       | No Default. Something like: `http://lidarr:8686`                      |
| lidarr.api_key   | `DN_LIDARR_0_API_KEY`   | No Default. Provide URL and API key if you use Readarr                |
| lidarr.username  | `DN_LIDARR_0_USERNAME`  | Provide username if using backup corruption check and auth is enabled |
| lidarr.password  | `DN_LIDARR_0_PASSWORD`  | Provide password if using backup corruption check and auth is enabled |

- **BCC = Backup Corruption Check**

### Prowlarr

| Config Name        | Variable Name             | Note                                                                    |
| ------------------ | ------------------------- | ----------------------------------------------------------------------- |
| prowlarr.name      | `DN_PROWLARR_0_NAME`      | No Default. Setting a name enables service checks                       |
| prowlarr.url       | `DN_PROWLARR_0_URL`       | No Default. Something like: `http://prowlarr:9696`                      |
| prowlarr.api_key   | `DN_PROWLARR_0_API_KEY`   | No Default. Provide URL and API key if you use Readarr                  |
| prowlarr.username  | `DN_PROWLARR_0_USERNAME`  | Provide username if using backup corruption check and auth is enabled   |
| prowlarr.password  | `DN_PROWLARR_0_PASSWORD`  | Provide password if using backup corruption check and auth is enabled   |

### Radarr

| Config Name      | Variable Name           | Note                                                                  |
| ---------------- | ----------------------- | --------------------------------------------------------------------- |
| radarr.name      | `DN_RADARR_0_NAME`      | No Default. Setting a name enables service checks.                    |
| radarr.url       | `DN_RADARR_0_URL`       | No Default. Something like: `http://localhost:7878`                   |
| radarr.api_key   | `DN_RADARR_0_API_KEY`   | No Default. Provide URL and API key if you use Radarr                 |
| radarr.username  | `DN_RADARR_0_USERNAME`  | Provide username if using backup corruption check and auth is enabled |
| radarr.password  | `DN_RADARR_0_PASSWORD`  | Provide password if using backup corruption check and auth is enabled |

### Readarr

| Config Name       | Variable Name            | Note                                                                   |
| ----------------- | ------------------------ | ---------------------------------------------------------------------- |
| readarr.name      | `DN_READARR_0_NAME`      | No Default. Setting a name enables service checks                      |
| readarr.url       | `DN_READARR_0_URL`       | No Default. Something like: `http://localhost:8787`                    |
| readarr.api_key   | `DN_READARR_0_API_KEY`   | No Default. Provide URL and API key if you use Readarr                 |
| readarr.username  | `DN_READARR_0_USERNAME`  | Provide username if using backup corruption check and auth is enabled  |
| readarr.password  | `DN_READARR_0_PASSWORD`  | Provide password if using backup corruption check and auth is enabled  |

### Sonarr

| Config Name      | Variable Name           | Note                                                                  |
| ---------------- | ----------------------- | --------------------------------------------------------------------- |
| sonarr.name      | `DN_SONARR_0_NAME`      | No Default. Setting a name enables service checks                     |
| sonarr.url       | `DN_SONARR_0_URL`       | No Default. Something like: `http://localhost:8989`                   |
| sonarr.api_key   | `DN_SONARR_0_API_KEY`   | No Default. Provide URL and API key if you use Sonarr                 |
| sonarr.username  | `DN_SONARR_0_USERNAME`  | Provide username if using backup corruption check and auth is enabled |
| sonarr.password  | `DN_SONARR_0_PASSWORD`  | Provide password if using backup corruption check and auth is enabled |

### Downloaders

You can add supported downloaders so they show up on the
dashboard integration. You may easily add service checks
to these downloaders by setting a check `interval` to a
positive value like `1m`.Any number of downloaders of any
type may be configured.

These all also have `interval` and `timeout` represented as a Go Duration.
Examples: `1m`, `1m30s`, `3m15s`, `1h5m`. Valid units are`s`,`m`, and`h`.
Combining units is additive.

#### QbitTorrent

| Config Name    | Variable Name         | Note                                                          |
| -------------- | --------------------- | ------------------------------------------------------------- |
| qbit.name      | `DN_QBIT_0_NAME`      | Defaults to the URL if left unset.                            |
| qbit.url       | `DN_QBIT_0_URL`       | No Default. Something like: `http://localhost:8080`           |
| qbit.user      | `DN_QBIT_0_USER`      | No Default. Provide URL, user and pass if you use Qbit        |
| qbit.pass      | `DN_QBIT_0_PASS`      | No Default. Provide URL, user and pass if you use Qbit        |
| qbit.http_user | `DN_QBIT_0_HTTP_USER` | Provide this username if Qbit is behind basic auth (uncommon) |
| qbit.http_pass | `DN_QBIT_0_HTTP_PASS` | Provide this password if Qbit is behind basic auth (uncommon) |

#### rTorrent

| Config Name   | Variable Name        | Note                                                       |
| ------------- | -------------------- | ---------------------------------------------------------- |
| rtorrent.name | `DN_RTORRENT_0_NAME` | Defaults to the URL if left unset.                         |
| rtorrent.url  | `DN_RTORRENT_0_URL`  | No Default. Something like: `http://localhost:5000`        |
| rtorrent.user | `DN_RTORRENT_0_USER` | No Default. Provide URL, user and pass if you use rTorrent |
| rtorrent.pass | `DN_RTORRENT_0_PASS` | No Default. Provide URL, user and pass if you use rTorrent |

#### SABnzbd

| Config Name     | Variable Name          | Note                                                        |
| --------------- | ---------------------- | ----------------------------------------------------------- |
| sabnzbd.name    | `DN_SABNZBD_0_NAME`    | Defaults to the URL if left unset.                          |
| sabnzbd.url     | `DN_SABNZBD_0_URL`     | No Default. Something like: `http://localhost:8080/sabnzbd` |
| sabnzbd.api_key | `DN_SABNZBD_0_API_KEY` | No Default. Provide URL and API key if you use SABnzbd      |

#### Deluge

| Config Name      | Variable Name           | Note                                                            |
| ---------------- | ----------------------- | --------------------------------------------------------------- |
| deluge.name      | `DN_DELUGE_0_NAME`      | Defaults to the URL if left unset.                              |
| deluge.url       | `DN_DELUGE_0_URL`       | No Default. Something like: `http://localhost:8080`             |
| deluge.password  | `DN_DELUGE_0_PASSWORD`  | No Default. Provide URL and password key if you use Deluge      |
| deluge.http_user | `DN_DELUGE_0_HTTP_USER` | Provide this username if Deluge is behind basic auth (uncommon) |
| deluge.http_pass | `DN_DELUGE_0_HTTP_PASS` | Provide this password if Deluge is behind basic auth (uncommon) |

#### NZBGet

| Config Name | Variable Name      | Note                                                            |
| ----------- | ------------------ | --------------------------------------------------------------- |
| nzbget.name | `DN_NZBGET_0_NAME` | Defaults to the URL if left unset.                              |
| nzbget.url  | `DN_NZBGET_0_URL`  | No Default. Something like: `http://localhost:6789`             |
| nzbget.user | `DN_NZBGET_0_USER` | No Default. Provide URL username and password if you use NZBGet |
| nzbget.pass | `DN_NZBGET_0_PASS` | No Default. Provide URL username and password if you use NZBGet |

### Plex

This application can also send Plex sessions to Notifiarr so you can receive notifications when users interact with your server.
This has three different features:

- Notify all sessions on a longer interval (30+ minutes).
- Notify on session nearing completion (percent complete).
- Notify on session change (Plex Webhook) ie. pause/resume.
- See Plex Webhook in the [After Install](afterInstall.md#plex-webhook) page for more info.

| Config Name | Variable Name   | Note                                                                                                                                            |
| ----------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| plex.url    | `DN_PLEX_URL`   | `http://localhost:32400` / local URL to your plex server                                                                                        |
| plex.token  | `DN_PLEX_TOKEN` | Required. [Must provide Plex Token](https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/) for this to work. |

### Tautulli

Only 1 Tautulli instance may be configured per client.
Providing Tautulli allows Notifiarr to use the "Friendly Name" for
your Plex users and it allows you to easily enable a service check.

| Config Name      | Variable Name         | Note                                                                    |
| ---------------- | --------------------- | ----------------------------------------------------------------------- |
| tautulli.name    | `DN_TAUTULLI_NAME`    | Defaults to the URL if left unset.                                      |
| tautulli.url     | `DN_TAUTULLI_URL`     | No Default. Something like: `http://localhost:8181`                     |
| tautulli.api_key | `DN_TAUTULLI_API_KEY` | No Default. Provide URL and API key if you want name maps from Tautulli |

### Endpoint URL Relay

The application can poll (download) a URL on a schedule and relay it as a notification.
**This is incomplete.**

### Service Checks

The Notifiarr client can also check URLs for health. If you set names on your Starr apps they will be automatically checked and reports sent to Notifiarr.
If you provide a log file for service checks, those logs will no longer write to the app log nor to console stdout.

| Config Name       | Variable Name          | Note                                                                |
| ----------------- | ---------------------- | ------------------------------------------------------------------- |
| services.log_file | `DN_SERVICES_LOG_FILE` | If a file path is provided, service check logs write there          |
| services.interval | `DN_SERVICES_INTERVAL` | `10m`, How often to send service states to Notifiarr; minimum: `5m` |
| services.parallel | `DN_SERVICES_PARALLEL` | `1`, How many services can be checked at once; 1 is plenty          |

You can also create ad-hoc service checks for things like Bazarr.

| Config Name      | Variable Name           | Note                                         |
| ---------------- | ----------------------- | -------------------------------------------- |
| service.name     | `DN_SERVICE_0_NAME`     | Services must have a unique name             |
| service.type     | `DN_SERVICE_0_TYPE`     | Type must be one of `http`, `tcp`, `process` |
| service.check    | `DN_SERVICE_0_CHECK`    | The `URL`, or `host/ip:port` to check        |
| service.expect   | `DN_SERVICE_0_EXPECT`   | `200`, For HTTP, the return code to expect   |
| service.timeout  | `DN_SERVICE_0_TIMEOUT`  | `15s`, How long to wait for service response |
| service.interval | `DN_SERVICE_0_INTERVAL` | `5m`, How often to check the service         |

!!! info "Web UI"
    It's a lot easier to configure service checks in the Web UI.

When `type` is set to `process`, the `expect` parameter becomes a special variable.
You may set it to `restart` to send a notification when the process restarts.
You may set it to `running` to alert if the process is found running (negative check).
You may set it to `count:min:max`. ie `count:1:2` means alert if process count is below 1 or above 2.
You may combine these with commas. ie `restart,count:1:3`.

By default `check` is the value to find in the process list. It uses a simple string match.
Unless you wrap the value in slashes, then it becomes a regex.
ie. use this `expect = "/^/usr/bin/smtpd$/"` to match an exact string.

!!! tip "Notifiarr is a CLI app too"
    Run `notifiarr --ps` to view the process list from Notifiarr's point of view.
