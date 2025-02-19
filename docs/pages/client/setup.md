# Setup

- [Setup](#setup)
  - [Troubleshooting](#troubleshooting)
    - [Resolving Duplicate Clients](#resolving-duplicate-clients)
    - [Tmp Not Found](#tmp-not-found)
  - [Notifiarr Website](#notifiarr-website)
  - [Web UI](#web-ui)
  - [.conf File](#conf-file)
    - [Log Files](#log-files)
      - [Detailed Debugging](#detailed-debugging)
      - [Clearing Logs](#clearing-logs)
  - [Hostname](#hostname)
    - [WSL2 users](#wsl2-users)
  - [ENV Variables](#env-variables)
    - [Client](#client)
    - [Secret Settings](#secret-settings)
    - [System Snapshot](#system-snapshot)
      - [Snapshot Sudoers](#snapshot-sudoers)
      - [Snapshot Packages](#snapshot-packages)
      - [Snapshot Configuration](#snapshot-configuration)
      - [MySQL Snapshots](#mysql-snapshots)
    - [Lidarr](#lidarr)
    - [Prowlarr](#prowlarr)
    - [Radarr](#radarr)
    - [Readarr](#readarr)
    - [Sonarr](#sonarr)
    - [Downloaders](#downloaders)
      - [QbitTorrent](#qbittorrent)
      - [rTorrent](#rtorrent)
      - [SABnzbd](#sabnzbd)
      - [Deluge](#deluge)
      - [NZBGet](#nzbget)
    - [Plex](#plex)
    - [Tautulli](#tautulli)
    - [Service Checks](#service-checks)
  - [Reverse Proxy](#reverse-proxy)
  - [Docker Compose](#docker-compose)

## Troubleshooting

- Find help on Discord: [Notifiarr](https://discord.gg/AURf8Yz) (preferred) or [Go Lift](https://golift.io/discord) (if you like Go).

### Tmp not found

Corruption checks require a temp folder to write the db file. This may be a couple hundred megabytes or more. Set the `TMPDIR` environment variable to a writable path, or mount `/tmp` to resolve the error.

### Resolving Duplicate Clients

- If you have duplicate clients on the website and are [setting a hostname after the fact](#hostname), [see these instructions](/Website/ClientConfiguration#resolving-duplicate-clients) for resolving the duplicates after setting a hostname.

## Notifiarr Website

There are non-integration related settings and triggers are configured on the Notifiarr site in the `Notifiarr Client Configuration` popup (button is located at the top of the setup page. You can get some insight about that [on the wiki](/Website/ClientConfiguration) as well. Integration specific timers and settings are found in the Client Configuration of each Integration that uses the Client.

## Web UI

1. Open the conf file, set your Notifiarr API Key and restart the client.

    ```conf
    ## This API key must be copied 
    from your notifiarr.com account.
    api_key = "api-key-from-notifiarr.com"
    ```

1. Point your browser to the client (default port: `5454`). This can be something like:

    - `http://localhost:5454`
    - `http://192.168.1.10:5454`

1. Use the username (default: `admin`) and the api mey you setup in the conf file to login to the app. Now you can configure and setup the client via the UI including changing your password.

### Docker Users

When a new docker image is deployed and an empty /config folder is mounted the app will do two things:

- If the API Key is not configured via an enviormental variable or invalid: Create a new ui_password and print it into the log file.
- Write a brand new config file with this password already saved

## .conf File

- You can use env variables, the conf file, or the UI.
- The UI is recommended which requires a [one time setting](#web-ui)
- Must provide the "All" API key from your [Profile page on notifiarr.com](https://notifiarr.com/user.php?page=profile)
  - **The Notifiarr application uses the API key for bi-directional authorization between the Site and the Client.**
  
> **Unraid Users**
You must configure the Notifiarr API Key in the Unraid Template/ Container Settings. If you wish to use Plex then you'll also need to set the Plex Token and Plex URL in the template as well. The other integrations can be defined in notifiarr.conf
{.is-danger}
> **Docker Users**
Note that Docker Environmental Variables - and thus the Unraid Template - override the Config file.
{.is-info}

### Compressed Conf File

- After accessing Notifiarr Client's Webui, upon saving to prevent user caused issues from editing the conf file, the conf file is compressed and will look like gibberish
- In the rare case the UI is not accessible and the conf file must be edited, you will need to decompress the file with `bzcat` prior to making your edits

```bash
bzcat /path/to/notifiarr.conf > /output/path/to/notifiarr_decomp.conf
```

### Log Files

You can set a log file in the config for apt/deb linux installs. You should do that. Otherwise, find your logs here:

- Linux: `/var/log/notifiarr`
  - Log paths for linux apt/deb installations are hardcoded
- FreeBSD: `/var/log/syslog` (w/ default syslog)
- Homebrew: `/usr/local/var/log/app.log`
- macOS: `~/.notifiarr/notifiarr.log`
- Windows: `<home folder>/.notifiarr/notifiarr.log`

In the Client UI log settings can be found under `Logging` in Settings => Configuration. Logs can be viewed in the UI under Insights => Logs.

#### Detailed Debugging

In the Client UI log settings can be found under `Logging` in Settings => Configuration.

- Enable `Debug Logging`

Logs can be viewed in the UI under Insights => Logs.

#### Clearing Logs

- To `clear` logs to make troubleshooting easier - stop the client and rename/remove the log file, the restart the client.

- If you have not previously enabled debug logs you do not need to clear anything.

## Hostname

It is important that a static hostname is set so the site can keep track of multiple clients for the settings. Some examples of how to do that:

- Docker Run users add `-h notifiarr` to your docker run command
- Docker Compose users add `hostname: notifiarr` to your yaml
- Unraid users add `-h notifiarr` to Extra Parameters
- TrueNAS and Kubernetes hostnames will be automatically pulled based on the pod name since they dont offer static hostnames
![truecharts_install.jpg](/truecharts_install.jpg)

Failure to set a hostname will result in [duplicate clients that will need to be resolved once a hostname is set](/Website/ClientConfiguration#duplicate-clients).

### WSL2 users

- Add a volume to your Notifiarr container (This is used for a unique uuid for each client instance)

```none
/etc/machine-id:/etc/machine-id
```

## ENV Variables

Config File and Docker Environmental Variables are listed below

- Any variable not provided takes the default.
- Environmental Variables take precedent over config file settings
- Must provide an API key from [notifiarr.com](https://notifiarr.com).
  - **The Notifiarr application uses the API key for bi-directional authorization.**
- You may provide multiple Sonarr, Radarr or Readarr instances using `DN_SONARR_1_URL`, `DN_SONARR_2_URL`, etc or by duplicating the starr block in the conf file. Note the header of `[[radarr]]`, `[[sonarr]]`, `[[readarr]]`, etc. is required.

### Client

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

All applications below (starr, downloaders, Tautulli, Plex) have a `timeout` setting.
If the configuration for an application is missing the timeout, the global timeout (above) is used.

### Secret Settings

Recommend not messing with these unless instructed to do so.

| Config Name | Variable Name     | Default / Note                                                                                    |
| ----------- | ----------------- | ------------------------------------------------------------------------------------------------- |
| extra_keys  | `DN_EXTRA_KEYS_0` | `[]` (empty list) / Add keys to allow API requests from places besides notifiarr.com              |
| mode        | `DN_MODE`         | `production` / Change application mode: `development` or `production`                             |
| debug       | `DN_DEBUG`        | `false` / Adds payloads and other stuff to the log output; very verbose/noisy                     |
| debug_log   | `DN_DEBUG_LOG`    | `""` / Set a file system path to write debug logs to a dedicated file                             |
| max_body    | `DN_MAX_BODY`     | Unlimited, `0` / Maximum debug-log body size (integer) for payloads to and from notifiarr.com     |
|             | `TMPDIR`          | `%TMP%` on Windows. Varies depending on system; must be writable if using Backup Corruption Check |

_Note: You may disable the GUI (menu item) on Windows by setting the env variable `USEGUI` to `false`._

### System Snapshot

> See the [Installation Page](/Client/Installation#system-snapshot)
{.is-info}

#### Snapshot Sudoers

> See the [Installation Page](/Client/Installation#snapshot-sudoers)
{.is-info}

#### Snapshot Packages

> See the [Installation Page](/Client/Installation#snapshot-packages)
{.is-info}

#### Snapshot Configuration

> See the [Installation Page](/Client/Installation#snapshot-configuration)
{.is-info}

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
| lidarr.http_user | `DN_LIDARR_0_HTTP_USER` | Provide username if Lidarr uses basic auth (uncommon) and BCC enabled |
| lidarr.http_pass | `DN_LIDARR_0_HTTP_PASS` | Provide password if Lidarr uses basic auth (uncommon) and BCC enabled |
| lidarr.max_body  | `DN_LIDARR_0_MAX_BODY`  | `0` (off) / How much of the response body is logged when debug is on  |

- **BCC = Backup Corruption Check**

### Prowlarr

| Config Name        | Variable Name             | Note                                                                    |
| ------------------ | ------------------------- | ----------------------------------------------------------------------- |
| prowlarr.name      | `DN_PROWLARR_0_NAME`      | No Default. Setting a name enables service checks                       |
| prowlarr.url       | `DN_PROWLARR_0_URL`       | No Default. Something like: `http://prowlarr:9696`                      |
| prowlarr.api_key   | `DN_PROWLARR_0_API_KEY`   | No Default. Provide URL and API key if you use Readarr                  |
| prowlarr.username  | `DN_PROWLARR_0_USERNAME`  | Provide username if using backup corruption check and auth is enabled   |
| prowlarr.password  | `DN_PROWLARR_0_PASSWORD`  | Provide password if using backup corruption check and auth is enabled   |
| prowlarr.http_user | `DN_PROWLARR_0_HTTP_USER` | Provide username if Prowlarr uses basic auth (uncommon) and BCC enabled |
| prowlarr.http_pass | `DN_PROWLARR_0_HTTP_PASS` | Provide password if Prowlarr uses basic auth (uncommon) and BCC enabled |
| prowlarr.max_body  | `DN_PROWLARR_0_MAX_BODY`  | `0` (off) / How much of the response body is logged when debug is on    |

### Radarr

| Config Name      | Variable Name           | Note                                                                  |
| ---------------- | ----------------------- | --------------------------------------------------------------------- |
| radarr.name      | `DN_RADARR_0_NAME`      | No Default. Setting a name enables service checks.                    |
| radarr.url       | `DN_RADARR_0_URL`       | No Default. Something like: `http://localhost:7878`                   |
| radarr.api_key   | `DN_RADARR_0_API_KEY`   | No Default. Provide URL and API key if you use Radarr                 |
| radarr.username  | `DN_RADARR_0_USERNAME`  | Provide username if using backup corruption check and auth is enabled |
| radarr.password  | `DN_RADARR_0_PASSWORD`  | Provide password if using backup corruption check and auth is enabled |
| radarr.http_user | `DN_RADARR_0_HTTP_USER` | Provide username if Radarr uses basic auth (uncommon) and BCC enabled |
| radarr.http_pass | `DN_RADARR_0_HTTP_PASS` | Provide password if Radarr uses basic auth (uncommon) and BCC enabled |
| radarr.max_body  | `DN_RADARR_0_MAX_BODY`  | `0` (off) / How much of the response body is logged when debug is on. |

### Readarr

| Config Name       | Variable Name            | Note                                                                   |
| ----------------- | ------------------------ | ---------------------------------------------------------------------- |
| readarr.name      | `DN_READARR_0_NAME`      | No Default. Setting a name enables service checks                      |
| readarr.url       | `DN_READARR_0_URL`       | No Default. Something like: `http://localhost:8787`                    |
| readarr.api_key   | `DN_READARR_0_API_KEY`   | No Default. Provide URL and API key if you use Readarr                 |
| readarr.username  | `DN_READARR_0_USERNAME`  | Provide username if using backup corruption check and auth is enabled  |
| readarr.password  | `DN_READARR_0_PASSWORD`  | Provide password if using backup corruption check and auth is enabled  |
| readarr.http_user | `DN_READARR_0_HTTP_USER` | Provide username if Readarr uses basic auth (uncommon) and BCC enabled |
| readarr.http_pass | `DN_READARR_0_HTTP_PASS` | Provide password if Readarr uses basic auth (uncommon) and BCC enabled |
| readarr.max_body  | `DN_READARR_0_MAX_BODY`  | `0` (off) / How much of the response body is logged when debug is on.  |

### Sonarr

| Config Name      | Variable Name           | Note                                                                  |
| ---------------- | ----------------------- | --------------------------------------------------------------------- |
| sonarr.name      | `DN_SONARR_0_NAME`      | No Default. Setting a name enables service checks                     |
| sonarr.url       | `DN_SONARR_0_URL`       | No Default. Something like: `http://localhost:8989`                   |
| sonarr.api_key   | `DN_SONARR_0_API_KEY`   | No Default. Provide URL and API key if you use Sonarr                 |
| sonarr.username  | `DN_SONARR_0_USERNAME`  | Provide username if using backup corruption check and auth is enabled |
| sonarr.password  | `DN_SONARR_0_PASSWORD`  | Provide password if using backup corruption check and auth is enabled |
| sonarr.http_user | `DN_SONARR_0_HTTP_USER` | Provide username if Sonarr uses basic auth (uncommon) and BCC enabled |
| sonarr.http_pass | `DN_SONARR_0_HTTP_PASS` | Provide password if Sonarr uses basic auth (uncommon) and BCC enabled |
| sonarr.max_body  | `DN_SONARR_0_MAX_BODY`  | `0` (off) / How much of the response body is logged when debug is on. |

### Downloaders

You can add supported downloaders so they show up on the dashboard integration.
You may easily add service checks to these downloaders by adding a name.
Any number of downloaders of any type may be configured.

These all also have `interval` and `timeout` represented as a Go Duration.
Examples: `1m`, `1m30s`, `3m15s`, `1h5m`. Valid units are`s`,`m`, and`h`. Combining units is additive.

#### QbitTorrent

| Config Name    | Variable Name         | Note                                                          |
| -------------- | --------------------- | ------------------------------------------------------------- |
| qbit.name      | `DN_QBIT_0_NAME`      | No Default. Setting a name enables service checks             |
| qbit.url       | `DN_QBIT_0_URL`       | No Default. Something like: `http://localhost:8080`           |
| qbit.user      | `DN_QBIT_0_USER`      | No Default. Provide URL, user and pass if you use Qbit        |
| qbit.pass      | `DN_QBIT_0_PASS`      | No Default. Provide URL, user and pass if you use Qbit        |
| qbit.http_user | `DN_QBIT_0_HTTP_USER` | Provide this username if Qbit is behind basic auth (uncommon) |
| qbit.http_pass | `DN_QBIT_0_HTTP_PASS` | Provide this password if Qbit is behind basic auth (uncommon) |

#### rTorrent

| Config Name   | Variable Name        | Note                                                       |
| ------------- | -------------------- | ---------------------------------------------------------- |
| rtorrent.name | `DN_RTORRENT_0_NAME` | No Default. Setting a name enables service checks          |
| rtorrent.url  | `DN_RTORRENT_0_URL`  | No Default. Something like: `http://localhost:5000`        |
| rtorrent.user | `DN_RTORRENT_0_USER` | No Default. Provide URL, user and pass if you use rTorrent |
| rtorrent.pass | `DN_RTORRENT_0_PASS` | No Default. Provide URL, user and pass if you use rTorrent |

#### SABnzbd

| Config Name     | Variable Name          | Note                                                        |
| --------------- | ---------------------- | ----------------------------------------------------------- |
| sabnzbd.name    | `DN_SABNZBD_0_NAME`    | No Default. Setting a name enables service checks           |
| sabnzbd.url     | `DN_SABNZBD_0_URL`     | No Default. Something like: `http://localhost:8080/sabnzbd` |
| sabnzbd.api_key | `DN_SABNZBD_0_API_KEY` | No Default. Provide URL and API key if you use SABnzbd      |

#### Deluge

| Config Name      | Variable Name           | Note                                                            |
| ---------------- | ----------------------- | --------------------------------------------------------------- |
| deluge.name      | `DN_DELUGE_0_NAME`      | No Default. Setting a name enables service checks               |
| deluge.url       | `DN_DELUGE_0_URL`       | No Default. Something like: `http://localhost:8080`             |
| deluge.password  | `DN_DELUGE_0_PASSWORD`  | No Default. Provide URL and password key if you use Deluge      |
| deluge.http_user | `DN_DELUGE_0_HTTP_USER` | Provide this username if Deluge is behind basic auth (uncommon) |
| deluge.http_pass | `DN_DELUGE_0_HTTP_PASS` | Provide this password if Deluge is behind basic auth (uncommon) |

#### NZBGet

| Config Name | Variable Name      | Note                                                            |
| ----------- | ------------------ | --------------------------------------------------------------- |
| nzbget.name | `DN_NZBGET_0_NAME` | No Default. Setting a name enables service checks               |
| nzbget.url  | `DN_NZBGET_0_URL`  | No Default. Something like: `http://localhost:6789`             |
| nzbget.user | `DN_NZBGET_0_USER` | No Default. Provide URL username and password if you use NZBGet |
| nzbget.pass | `DN_NZBGET_0_PASS` | No Default. Provide URL username and password if you use NZBGet |

### Plex

This application can also send Plex sessions to Notifiarr so you can receive notifications when users interact with your server.
This has three different features:

- Notify all sessions on a longer interval (30+ minutes).
- Notify on session nearing completion (percent complete).
- Notify on session change (Plex Webhook) ie. pause/resume.

You [must provide Plex Token](https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/) for this to work.
You may also need to add a webhook to Plex so it sends notices to this application.

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
Providing Tautulli allows Notifiarr to use the "Friendly Name" for your Plex users and it allows you to easily enable a service check.

| Config Name      | Variable Name         | Note                                                                    |
| ---------------- | --------------------- | ----------------------------------------------------------------------- |
| tautulli.name    | `DN_TAUTULLI_NAME`    | No Default. Setting a name enables service checks of Tautulli           |
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

When `type` is set to `process`, the `expect` parameter becomes a special variable.
You may set it to `restart` to send a notification when the process restarts.
You may set it to `running` to alert if the process is found running (negative check).
You may set it to `count:min:max`. ie `count:1:2` means alert if process count is below 1 or above 2.
You may combine these with commas. ie `restart,count:1:3`.

By default `check` is the value to find in the process list. It uses a simple string match.
Unless you wrap the value in slashes, then it becomes a regex.
ie. use this `expect = "/^/usr/bin/smtpd$/"` to match an exact string.

Run `notifiarr --ps` to view the process list from Notifiarr's point of view.

## Docker Compose

> See the [Installation Page](/Client/Installation#docker-compose)
{.is-info}


## Snapshot Dependencies

This application can take a snapshot of your system at an interval and send
you a notification. Snapshot means system health like cpu, memory, disk, raid, users, etc.
Other data available in the snapshot: mysql health, `iotop`, `iostat` and `top` data.
Some of this may only be available on Linux, but other platforms have similar abilities.

If you monitor drive health you must have smartmontools (`smartctl`) installed.
If you use smartctl on Linux, you must enable sudo. Add the sudoers entry below to
`/etc/sudoers` and fix the path to `smartctl` if yours differs. If you monitor
raid and use MegaCli (LSI card), add the appropriate sudoers entry for that too.

To monitor application disk I/O you may install `iotop` and add the sudoers entry
for it, shown below. This feature is enabled on the website.

### Snapshot Sudoers

The following sudoers entries are used by various snapshot features. Add them if you use the respective feature.
You can usually just put the following content into `/etc/sudoers` or `/etc/sudoers.d/00-notifiarr`.
Make sure the 00-notifiarr file has the proper permissions needed `chmod 400 /etc/sudoers.d/00-notifiarr`.

```yml
# Allows drive health monitoring on macOS, Linux/Docker and FreeBSD.
notifiarr ALL=(root) NOPASSWD:/usr/sbin/smartctl *

# Allows disk utilization monitoring on Linux (non-Docker).
notifiarr ALL=(root) NOPASSWD:/usr/sbin/iotop *

# Allows monitoring megaraid volumes on macOS, Linux/Docker and FreeBSD.
# Rarely needed, and you'll know if you need this.
notifiarr ALL=(root) NOPASSWD:/usr/sbin/MegaCli64 -LDInfo -Lall -aALL
```

### Snapshot Packages

#### Windows
 `smartmontools` - get it here <https://sourceforge.net/projects/smartmontools/>

#### Linux

  - Debian/Ubuntu: `apt install smartmontools`
  - RedHat/CentOS: `yum install smartmontools`
- **Docker**:    It's already in the container. Lucky you! Just run the container in `--privileged` mode.
- **Synology**: `opkg install smartmontools`, but first get Entware:
  - Entware (synology):  <https://github.com/Entware/Entware-ng/wiki/Install-on-Synology-NAS>
  - Entware Package List:  <https://github.com/Entware/Entware-ng/wiki/Install-on-Synology-NAS>