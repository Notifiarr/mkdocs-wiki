# Additional Client Setup

## Log Files

Find your logs here:

- Linux: `/var/log/notifiarr/{app,http,services}.log`
  - Log paths for linux apt/deb installations are hardcoded
- FreeBSD: `/var/log/syslog` (w/ default syslog)
- macOS: `~/.notifiarr/Notifiarr.log`
- Windows: `<home folder>/.notifiarr/Notifiarr.log`

In the Web UI log settings can be found under `Logging` in *Settings => Configuration*.
Logs can be viewed in the UI under *Insights => Log Files*.

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
