---
toc_depth: 1
---

# Notifiarr Client Installation

Click your OS in the table of contents and follow the provided directions to get the client installed.
**Review the [After Install](../../pages/client/afterInstall.md) page for next steps.**

## Linux

- Linux repository hosting provided by
[![packagecloud](https://docs.golift.io/integrations/packagecloud-full.png "PackageCloud.io")](http://packagecloud.io)

This works on any system with `apt` or `yum`. **If your system does not use APT or YUM**,
download a binary from the [Releases](https://github.com/Notifiarr/notifiarr/releases) page and install it.

!!! important
    When you install from a deb or apt package, the logs folder `/var/log/notifiarr` and config
    folder `/etc/notifiarr` are automatically created. The `notifiarr` user and group are also
    created; the application runs as `notifiarr:notifiarr`. If you remove the package, these things
    will not be fully removed. If you do not install from a package, they will not be created
    automatically either.

1. Install the Go Lift package repo and Notifiarr with this command:

    ```bash
    curl -s https://golift.io/repo.sh | sudo bash -s - notifiarr
    ```

1. After install, edit the config, set your apikey, and restart the service:

    ```bash
    sudo nano /etc/notifiarr/notifiarr.conf
    sudo systemctl restart notifiarr
    ```

## Arch Linux

- This one is special; hope you know what you're doing.
- Build a package with `makepkg` using the [`aur` source](https://github.com/golift/aur)

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

## TrueNAS Scale <!-- Make the line number below match this line's number. -->

!!! warning "TrueNAS"
    If you figure out how to install Notifiarr on TrueNAS, please
    [update these instructions](https://github.com/Notifiarr/mkdocs-wiki/blob/main/docs/pages/client/install.md?plain=1#L57).
    Notifiarr support and developers have very little experience with TrueNAS.

## macOS

1. Download the signed `dmg` file from the [Releases](https://github.com/Notifiarr/notifiarr/releases) page.
1. Mount it and copy *Notifiarr.app* to */Applications* then double-click it there.
1. When you open it for the first time it will create a config file and log file:
    1. `~/.notifiarr/notifiarr.conf`
    1. `~/.notifiarr/Notifiarr.log`
1. Use the menu bar icon to access the WebUI.
1. Head on over to [After Install](afterInstall.md).

## Windows

!!! info
    Suggested location and structure based on experience with permissions.

### Desired Outcome

- `C:\ProgramData\notifiarr\notifiarr.amd64.exe` - The Application.
- `C:\ProgramData\notifiarr\notifiarr.conf` - The config file. Just the add the API key.
- `C:\ProgramData\notifiarr\logs` - Folder for log files.

### Create the folders

1. Open C:\ProgramData and create a folder `notifiarr`
1. Create a new folder named `logs`, so you now have `C:\ProgramData\notifiarr\logs`
    - When you add the log paths in the client UI (later steps), make sure you point them to a file such as:
      - `C:\ProgramData\notifiarr\logs\app.log`
      - `C:\ProgramData\notifiarr\logs\debug.log`
      - `C:\ProgramData\notifiarr\logs\http.log`

### New Install

1. Download `notifiarr.amd64.exe.zip` from [the Releases page](https://github.com/Notifiarr/notifiarr/releases)
1. Save it in `C:\ProgramData\notifiarr`
1. Open the folder that was created from extracting and copy the `.exe` + example `.conf` files up one directory so it is located at:
    - `C:\ProgramData\notifiarr\notifiarr.amd64.exe`
    - `C:\ProgramData\notifiarr\notifiarr.conf.example`
1. You can now delete the `.zip` file that was downloaded and the folder that was extracted
1. Rename `notifiarr.conf.example` to `notifiarr.conf`

### Fix Existing Install

1. Stop the client
1. Copy the existing `.exe` to `C:\ProgramData\notifiarr\notifiarr.amd64.exe`
1. Copy the existing conf file to `C:\ProgramData\notifiarr\notifiarr.conf`
1. If the `C:\users\<your home folder>\.notifiarr` folder exists, delete it

### Autostart & Password

- At this point, the structure should look like the [Desired Outcome mentioned above](#desired-outcome).

1. Right click on the `.exe` and create a shortcut
1. Windows logo key + R, type `shell:startup`, then select OK. This opens the Startup folder.
1. Copy and paste the newly created shortcut from its current location to the opened Startup folder.
1. Double click on the shortcut and the client is now running
1. If this is the first time you have ran it:
    1. Option A: Look at the notifiarr.log (or app.log) and you will see the password at the top of the file.
    1. Option B: Right click on the notifiarr icon and pick Logs -> View and get the login credentials from there.

## Synology

1. Run the below command while ssh'd in to the NAS.
    It will run the [Syno Install Script located on the Notifiarr Repository](https://github.com/Notifiarr/notifiarr/blob/main/userscripts/install.sh)

```bash
curl -sSL https://raw.githubusercontent.com/Notifiarr/notifiarr/main/userscripts/install-synology.sh | sudo bash
```

## Docker

This project builds automatically in [Docker Cloud](https://hub.docker.com/r/golift/notifiarr)
and creates [ready-to-use multi-architecture images](https://hub.docker.com/r/golift/notifiarr/tags).
The `latest` tag is always a tagged release in GitHub.
It also builds in a GitHub Action and publishes to GHCR (ghcr.io).

### Compose

A sample docker compose file may be found
[in the Github repo here](https://github.com/Notifiarr/notifiarr/blob/main/examples/compose.yml).

### `docker run`

1. Mount an empty `/config` folder and the application will automatically write the config file there.
1. Pull the image from docker hub or ghcr and run it.
1. You must enable `privileged` to use `smartctl` (`monitor_drives`) and/or `MegaCli` (`monitor_raid`).
1. Map the `/var/run/utmp` volume if you want to count users.
1. Mount any volumes you want to report storage space for.
    1. Where you mount it sets the 'name'. e.g. `/mnt/nas/data:/synonas`

!!! warning "Static Hostname"
    Why `-h notifiarr` ?
    You MUST [set a static hostname](../../pages/client/afterInstall.md#hostname).
    Each client is identified by hostname.

```bash
docker pull golift/notifiarr
docker run --name Notifiarr -h notifiarr --restart unless-stopped \
    --privileged -p 5454:5454 -v /path/to/notifiarrconfig/:/config \
    -v /var/run/utmp:/var/run/utmp -v /etc/machine-id:/etc/machine-id golift/notifiarr
docker logs Notifiarr
```

### Docker Environment Variables

You can find all the environment variables in the client's Web UI.
You can run the app without a config file like this,
but it's not recommended and only for advanced-needs.

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
    This is community provided. The Notifiarr developers have very little experience with Home Assistant OS.

[Home Assistant Addon](https://github.com/zanyraspi/home-assistant-addons),
the person to ask for help is `@ZanY` on the Notifiarr discord.
If they are no longer a member, try their Github.

## Proxmox

!!! warning "Proxmox Users"
    This is community provided. The Notifiarr developers have very little experience with Proxmox.

- [Proxmox Helper script](https://community-scripts.github.io/ProxmoxVE/scripts?id=notifiarr)

## UltraCC Seedbox

!!! warning "UltraCC Seedbox Users"
    This is community provided. The Notifiarr developers have very little experience with UltraCC.

### Install Client

The outcome of these steps is that you make a new folder named `notifiarr` in your home folder,
and it contains the `notifiarr` binary and `notifiarr.conf` config file. We're also adding a user-level
systemd service unit file to your home folder, enabling it (so it starts when the server boots).

When you finish here, head on over to the [After Install](./afterInstall.md) page for next steps.

1. SSH into your Ultra Seedbox.
1. In your home folder type `mkdir notifiarr`
1. Type `cd notifiarr`
1. On [Github](https://github.com/Notifiarr/notifiarr/releases) find the latest release asset labeled `notifiarr.amd64.linux.gz`,
    right click on that and click copy link.
1. Download it; Back on your terminal type `wget '<paste link>'`
1. Decompress it; Type `gzip -d notifiarr.amd64.linux.gz`
1. Rename it; Type `mv notifiarr.amd64.linux notifiarr`
1. Make it executable; Type `chmod +x notifiarr`
1. Download config file; Type `wget -O notifiarr.conf https://raw.githubusercontent.com/Notifiarr/notifiarr/refs/heads/main/examples/notifiarr.conf.example`

### Install Service Unit

1. Type `mkdir -p /home/$USER/.config/systemd/user`
1. Type `cd /home/$USER/.config/systemd/user`
1. Type `id` to see your username.
1. Type `nano notifiarr.service`
    1. Copy and paste the following content.
    1. Replace `YOUR-API-KEY-FROM-NOTIFIARR.COM` with your API key.
    1. **Replace `$USER` with your username.**
    1. Press `ctrl+x` and then `y` to save the file and close the editor.
        [Nano cheatsheet](https://www.nano-editor.org/dist/latest/cheatsheet.html).

    ```none
    # Systemd service unit for notifiarr.

    [Unit]
    Description=notifiarr - Official chat integration client for Notifiarr.com

    [Service]
    ExecStart=/home/$USER/notifiarr/notifiarr
    Restart=always
    RestartSec=10
    Type=simple
    WorkingDirectory=/home/$USER/notifiarr
    Environment=DN_API_KEY=YOUR-API-KEY-FROM-NOTIFIARR.COM
    Environment=DN_LOG_FILE=/home/$USER/notifiarr/app.log
    Environment=DN_HTTP_LOG=/home/$USER/notifiarr/http.log
    Environment=DN_DEBUG_LOG=/home/$USR/notifiarr/debug.log
    Environment=DN_SERVICES_LOG_FILE=/home/$USER/notifiarr/services.log
    Environment=DN_QUIET=true

    [Install]
    WantedBy=default.target
    ```

### Start Client

Use these commands to control systemd. Systemd is what launches apps like notifiarr client.
The `stop` and `restart` commands are not listed below, but you can use those too if you need them.

1. Type `systemctl --user enable notifiarr` to make notifiarr auto-start.
1. Type `systemctl --user start notifiarr` to start notifiarr now.
1. Type `systemctl --user status notifiarr` to check if there are any errors.
1. Type `systemctl --user daemon-reload` if you make changes to the above file (to re-load it).
1. On your browser go to `http://your-ultraseedbox-url:5454`

### Configure Proxy

Setting up the proxy is optional, but recommended so you can access the client like your other apps.

1. Log into your Notifarr client and change the base url to `/notifiarr` and save changes
1. Go back to your ssh console
1. Type `cd /home/$USER/.apps/nginx/proxy.d`
1. Type `nano notifiarr.conf`
1. Paste the following content without changing it.
    1. Press `ctrl+x` and then `y` to save the file and close the editor.
        [Nano cheatsheet](https://www.nano-editor.org/dist/latest/cheatsheet.html).

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
    proxy_set_header X-Forwarded-For $remote_addr;
    set $notifiarr http://127.0.0.1:5454;
    proxy_pass $notifiarr$request_uri;
}
```

1. Type `systemctl --user restart nginx`
1. Now you should be able to browse to `https://your-ultraseedbox-url/notifiarr`
