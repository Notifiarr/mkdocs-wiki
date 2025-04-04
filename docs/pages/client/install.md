## Linux

*Linux repository hosting provided by* &nbsp;[![packagecloud](https://docs.golift.io/integrations/packagecloud-full.png "PackageCloud.io")](http://packagecloud.io)

This works on any system with `apt` or `yum`. **If your system does not use APT or YUM**, download a binary from the [Releases](https://github.com/Notifiarr/notifiarr/releases) page and install it.

!!! important
    On Linux, Notifiarr runs as `user:group` of `notifiarr:notifiarr`.

1. Install the Go Lift package repo and Notifiarr with this command:

    ```bash
    curl -s https://golift.io/repo.sh | sudo bash -s - notifiarr
    ```

1. After install, edit the config, set your apikey, and restart the service:

    ```bash
    sudo nano /etc/notifiarr/notifiarr.conf
    sudo systemctl restart notifiarr
    ```

!!! info
    See [Configuration Instructions Here](../../pages/client/configuration.md#web-gui)

## Arch Linux

- This one is special; hope you know what you're doing.
- Build a package with `makepkg` using the [`aur` source](https://github.com/golift/aur)

!!! info
    See [Configuration Instructions Here](../../pages/client/configuration.md#web-gui)

## FreeBSD

1. Download a `txz` package from the [Releases](https://github.com/Notifiarr/notifiarr/releases) page.
1. Install it, edit config, start it.
1. On FreeBSD, Notifiarr runs as `user:group` of `notifiarr:notifiarr`.

Example of the above in shell form:

```shell
wget -qO- https://raw.githubusercontent.com/Notifiarr/notifiarr/main/userscripts/install.sh | sudo bash
vi /usr/local/etc/notifiarr/notifiarr.conf
service notifiarr start
```

!!! info
    See [Configuration Instructions Here](../../pages/client/configuration.md#web-gui)

## TrueNAS Scale

!!! warning "TrueNAS"
    Please be aware none of us (Devs, Suppprt, etc.) use this but hopefully for those who do this is helpful.

- Consider moving away from TrueNAS Scale, and more specifically **you must move away from TrueCharts for Notifiarr** as Notifiarr v0.7.1 is broken / unsupported and TrueCharts will not upgrade the chart.
- The next TrueNAS Scale OS release will no longer support TrueCharts after their next OS release in 3 months (~10/2024)
- For additional information:
    - [Please see some commentary and screenshots on the Notifiarr Discord](https://discord.com/channels/764440599066574859/1261063207859261441/1261085647142391829)
    - [Refer to TrueNAS Forums as to why TrueCharts Team are no longer updating their apps](https://forums.truenas.com/t/the-future-of-electric-eel-and-apps/5409)
    - [Be weary of asking for TrueCharts support in the TrueNAS Discord. Per Reddit: Users have been banned](https://old.reddit.com/r/truenas/comments/1e0vf5h/trucharts_banning_talking_about_scale/)
- No current TrueNAS Scale users have been able to to write documentation for Notifiarr.
    - [Heavy's Guide](https://heavysetup.info/applications/notifiarr/notifiarr/) **is depreciated and will eventually be removed. It may stop working or be out of date at any time.**

## macOS

### macOS App

!!! note
    This is the recommend installation method for macOS.

1. Download the signed `dmg` file from the [Releases](https://github.com/Notifiarr/notifiarr/releases) page.
1. When you open it for the first time it will create a config file and log file:
    1. `~/.notifiarr/notifiarr.conf`
    1. `~/.notifiarr/notifiarr.log`
1. Edit the config file and reload or restart the app from the menu bar.

!!! info
    See [Configuration Instructions Here](../../pages/client/configuration.md#web-gui)

### Homebrew

!!! warning "Homebrew users"
    Homebrew is not recommend, and may be discontinued in the future.

1. Install Notifiarr
1. Edit config file at `/usr/local/etc/notifiarr/notifiarr.conf`
1. Start it.

The above in shell form:

```shell
brew install golift/mugs/notifiarr
vi /usr/local/etc/notifiarr/notifiarr.conf
brew services start notifiarr
```

## Windows

!!! info
    Suggested location and structure based on expierence with permissions

### Desired Outcome

- `C:\ProgramData\notifiarr\notifiarr.amd64.exe` - The Application
- `C:\ProgramData\notifiarr\notifiarr.conf` - The config file. Should only be used to configure the apikey and enable the webui.
- `C:\ProgramData\notifiarr\logs` - Folder for log files

### Create the folders

1. Open C:\ProgramData and create a folder `notifiarr`
1. Create a new folder named `logs`, so you now have `C:\ProgramData\notifiarr\logs`
    - When you add the log paths in the client UI (later steps), make sure you point them to a file such as:
      - `C:\ProgramData\notifiarr\logs\app.log`
      - `C:\ProgramData\notifiarr\logs\debug.log`
      - `C:\ProgramData\notifiarr\logs\http.log`

### If this is a new install

1. Download `notifiarr.amd64.exe.zip` from [the Releases page](https://github.com/Notifiarr/notifiarr/releases)
1. Save it in `C:\ProgramData\notifiarr`
1. Open the folder that was created from extracting and copy the `.exe` + example `.conf` files up one directory so it is located at:
    - `C:\ProgramData\notifiarr\notifiarr.amd64.exe`
    - `C:\ProgramData\notifiarr\notifiarr.conf.example`
1. You can now delete the `.zip` file that was downloaded and the folder that was extracted
1. Rename `notifiarr.conf.example` to `notifiarr.conf`

### If this is an existing install being "fixed"

1. Stop the client
1. Copy the existing `.exe` to `C:\ProgramData\notifiarr\notifiarr.amd64.exe`
1. Copy the existing conf file to `C:\ProgramData\notifiarr\notifiarr.conf`
1. If the `C:\users\<your home folder>\.notifiarr` folder exists, delete it

### New and existing installs

- At this point, the structure should look like the [Desired Outcome mentioned above](#desired-outcome).

1. Right click on the `.exe` and create a shortcut
    - Windows 11 users:
        - Right click on the shortcut and pick properties
    - Change the target path to `C:\Windows\System32\conhost.exe C:\ProgramData\notifiarr\notifiarr.amd64.exe` which will minimize the console to the tray when it is ran
1. Windows logo key + R, type `shell:startup`, then select OK. This opens the Startup folder.
1. Copy and paste the newly created shortcut from its current location to the opened Startup folder.
1. Double click on the shortcut and the client is now running
1. If this is the first time you have ran it:
    - Option A: Look at the notifiarr.log (or app.log) and you will see a the credentials in the log
    - Option B: Right click on the notifiarr icon and pick Logs -> View and get the login credentials from there
    - Option C: Open the notifiarr.conf and look at the top for `ui_password` to get the credentials

!!! info
    See [Configuration Instructions Here](../../pages/client/configuration.md#web-gui)

## Synology

1. Run the below command while ssh'd in to the NAS. It will run the [Syno Install Script located on the Notifiarr Repository](https://github.com/Notifiarr/notifiarr/blob/main/userscripts/install.sh)

```bash
curl -sSL https://raw.githubusercontent.com/Notifiarr/notifiarr/main/userscripts/install-synology.sh | sudo bash
```

!!! info
    See [Configuration Instructions Here](../../pages/client/configuration.md#web-gui)

## Docker

This project builds automatically in [Docker Cloud](https://hub.docker.com/r/golift/notifiarr) and creates [ready-to-use multi-architecture images](https://hub.docker.com/r/golift/notifiarr/tags). The `latest` tag is always a tagged release in GitHub.

### Compose

A sample docker compose file may be found [in the Github repo here](https://github.com/Notifiarr/notifiarr/blob/main/examples/compose.yml).

!!! warning "Unraid Users"
    You must configure a Notifiarr API Key in the Unraid Template. If you wish to use Plex then you'll also need to set the Plex Token and Plex URL in the template as well.

!!! info "Docker Users"
    Note that Docker Environmental Variables - and thus the Unraid Template - override the Config file.

### Docker Config File

1. Copy the [example config file](https://github.com/Notifiarr/notifiarr/blob/main/examples/notifiarr.conf.example) from Notifiarr Client repo.
1. Then grab the image from docker hub and run it.
1. You must enable `privileged` to use `smartctl` (`monitor_drives`) and/or `MegaCli` (`monitor_raid`).
1. Map the `/var/run/utmp` volume if you want to count users.
1. Mount any volumes you want to report storage space for. Where does not matter, "where" is the "name". e.g. `/mnt/nas/data:/synonas`

!!! warning
    You MUST [set a static hostname](../../pages/client/configuration.md#hostname) Each client is identified by hostname.

```bash
docker pull golift/notifiarr
docker run --name notifiarr -h notifiarr --restart unless-stopped --privileged -p 5454:5454 -v /path/to/notifiarrconfig/:/config -v /var/run/utmp:/var/run/utmp -v /etc/machine-id:/etc/machine-id golift/notifiarr
docker logs notifiarr
```

### Docker Environment Variables

See below for more information about which environment variables are available.

```shell
docker pull golift/notifiarr
docker run --hostname $(hostname) -d --privileged \
  -v /var/run/utmp:/var/run/utmp \
  -e "DN_API_KEY=abcdef-12345-bcfead-43312-bbbaaa-123" \
  -e "DN_SONARR_0_URL=http://localhost:8989" \
  -e "DN_SONARR_0_API_KEY=kjsdkasjdaksdj" \
  golift/notifiarr
docker logs <container id from docker run>
```

## Home Assistant OS

!!! warning "Home Assistant OS Users"
    Please be aware none of us (Devs, Support, etc.) use this but hopefully for those who do this is helpful.

[Home Assistant Addon](https://github.com/zanyraspi/home-assistant-addons), the person to ask for help is `@ZanY` on the Notifiarr discord (if they are no longer a member, try their Github)

## Proxmox

!!! warning "Proxmox Users"
    Please be aware none of us (Devs, Support, etc.) use this but hopefully for those who do this is helpful.

- [Proxmox Helper script](https://helper-scripts.com/scripts?id=Notifiarr) provided by the community

## UltraCC Seedbox

!!! warning "UltraCC Seedbox Users"
    Please be aware none of us (Devs, Support, etc.) use this but hopefully for those who do this is helpful.

1. SSH into your Ultra Seedbox
1. On your landing directory type `mkdir notifiarr`
1. Type `cd notifiarr`
1. On [Github](https://github.com/Notifiarr/notifiarr/releases) find the latest release asset labelled notifiarr.amd64.linux.gz, right  click on that and click copy link.
1. Back on your terminal type `wget '<paste link>'`
1. Type `gzip -d notifiarr.*`
1. Type `mv notifiarr.* notifiarr`
1. Type `chmod +x notifiarr`
1. In the notifiarr folder create notifiarr.conf from this: [Github page](https://github.com/Notifiarr/notifiarr/blob/main/examples/notifiarr.conf.example)
1. Type `cd /home/$USER/.config/systemd/user`
1. Type `nano notifiarr.service`
1. Paste the below

```none
# Systemd service unit for notifiarr.

[Unit]
Description=notifiarr - Official chat integration client for Notifiarr.com

[Service]
ExecStart=/home/$USER/notifiarr/notifiarr \$DAEMON_OPTS
Restart=always
RestartSec=10
Type=simple
WorkingDirectory=/home/$USER/notifiarr
Environment=DN_LOG_FILE/home/$USER/notifiarr/app.log
Environment=DN_HTTP_LOG=/home/$USER/notifiarr/http.log
Environment=DN_DEBUG_LOG=/home/$USR/notifiarr/debug.log
Environment=DN_SERVICES_LOG_FILE=/home/$USER/notifiarr/services.log
Environment=DN_QUIET=true

[Install]
WantedBy=default.target
```

1. Type `systemctl --user enable notifiarr`
1. Type `systemctl --user start notifiarr`
1. Type `systemctl --user status notifiarr` to check if there are any errors.
1. On your browser go to http://[ultraseedbox url]:5454
1. Log into your Notifarr client and change the base url to /notifiarr and save changes
1. Go back to your ssh console
1. Type `cd /home/$USER/.apps/nginx/proxy.d`
1. Type `nano notifiarr.conf`
1. Paste the below

```nginx
location /notifiarr {
    # <put proxy auth directives here> Optional:
    # proxy_set_header X-WebAuth-User $auth_user;
    proxy_set_header X-Forwarded-For $remote_addr;
    set $notifiarr http://127.0.0.1:5454;
    proxy_pass $notifiarr$request_uri;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection $http_connection;
    proxy_set_header Host $host;
}
# Notifiarr Client
location /notifiarr/api {
deny all; # remove this line if you really want to expose the API.
    proxy_set_header X-Forwarded-For $remote_addr;
    set $notifiarr http://127.0.0.1:5454;
    proxy_pass $notifiarr$request_uri;
}
```

1. Type `systemctl --user restart nginx`
1. Now you should be able to browse to https://[ultraseedbox url]/notifiarr
