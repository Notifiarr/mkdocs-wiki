# Notifiarr Client Configuration

Log into the Web UI to configure the client. Skim through the rest of this page for important information.

## Web UI

When you open the application on MacOS or Windows for the first time, you're
prompted for your API key. Enter it. This is an "All" key from notifiarr.com.

If you're on Linux or FreeBSD and installed with root, you should set the API
key in the config file @ `/etc/notifiarr/notifiarr.conf` or
`/usr/local/etc/notifiarr/notifiarr.conf`. If you installed on a seed box, set
the API key in the config file in your home folder.

You will use the API key as the password to login into the client's WebUI for
the first time. You can set a dedicated password after logging in. The default
username is `admin`.

The login URL will usually look like one of these. The default listen port is `5454`.

- `http://localhost:5454`
- `http://notifiarr`
- `http://192.168.1.10:5454`

## Docker Users

When a new docker image is deployed with an empty `/config` folder mounted, the app will do two things:

- *If the API Key is not configured or invalid:* Create a new Web UI `admin` and print it into the log file and docker logs.
- Write a brand new config file with this password already saved.
- Find the password by running `docker logs Notifiarr`.

!!! danger "Unraid Users"
    The Official Unraid Template for Notifiarr Client contains the API Key and Plex Token as pre-defined inputs.
    Normally, you can just go ahead and set those there. Alternatively, you can delete them from the template, and
    configure these values using the client's Web UI. For consistency, we recommend setting the API key and Plex token
    in the Unraid template.

!!! info "Docker Users"
    Note that Environment Variables - and the Unraid Template - override settings in the Config file.

## `.conf` File

The config file used to be the preferred way to change the application's behavior,
but now days the config file is compressed and direct edits are discouraged.
The format has become too much to properly document. If you're configuring your
client with automation such as puppet or ansible, then you should use environment
variables for configuration. It's possible the config file format may change in the
future, and the env variables are more likely to remain unaffected.

**Use the WebUI to change the application configuration.**

- Must provide the "All" API key from your
  [Profile page on notifiarr.com](https://notifiarr.com/user.php?page=profile)
- **The Notifiarr client uses the API key for bi-directional authorization between the Site and the Client.**

## Hostname

It is important that a static hostname is set so the site can keep track of multiple clients' settings.
Some examples of how to do that:

- Docker Run users add `-h notifiarr` to your `docker run` command.
- Docker Compose users add `hostname: notifiarr` to your docker-compose.yaml file.
- Unraid users add `-h notifiarr` to `Extra Parameters`.
- Kubernetes hostnames are automatically determined based on the pod name.

!!! note
    Failure to set a hostname will result in duplicate clients that need to be
    [fixed once a hostname is set](../../pages/website/clientConfig.md#resolving-duplicate-clients).

### WSL2 users

Add this volume to your Notifiarr container. This is used for a unique UUID for each client instance.

```yaml
volumes:
  /etc/machine-id:/etc/machine-id
```

## Configuration Options

Config File and Environment Variables are listed below.
**This data is often out of date.**
The up-to-date data now lives in the client's Web UI.

- Any variable not provided takes the default.
- Environmental Variables take precedent over config file settings.
- Must provide an "All" API key from [notifiarr.com](https://notifiarr.com).
  - **The Notifiarr application uses the API key for bi-directional authorization.**
- You may provide multiple Sonarr, Radarr or Readarr instances using `DN_SONARR_1_URL`,
  `DN_SONARR_2_URL`, etc or by duplicating the starr block in the conf file.
- Note the header of `[[radarr]]`, `[[sonarr]]`, `[[readarr]]`, etc. is required.

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

#### MySQL Snapshots

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

You [must provide the Plex Token](https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/) for this to work.
You also need to add a webhook to Plex so it sends notices to this application.

- In Plex Media Server, add this URL to webhooks:
  - `http://localhost:5454/plex?token=plex-token-here`
- Replace `localhost` with the IP or host of the notifiarr application.
- Replace `plex-token-here` with your plex token.
- **The Notifiarr application uses the Plex token to authorize incoming webhooks.**

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
