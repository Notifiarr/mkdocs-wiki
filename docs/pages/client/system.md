# Notifiarr Client System

The System page displays read-only information about the Notifiarr client, the host operating system, network, and storage.

---

## Sections

### User Information

Displays your Notifiarr account details including patron status, subscriber status, and date format.

### Operating System

Shows the host system details:

- Hostname
- Unique host ID
- Platform (OS name, version, architecture)
- Kernel version
- Virtualization system (if detected)

### Client Information

Displays the running client application details:

- Application name
- Version and revision
- Start time and uptime

### Build Information

Shows build-time details:

- Branch
- Build user
- Build date
- Go version
- Binary integrity check (MD5 hash)

### Startup Parameters

Lists the runtime parameters:

- Binary path
- Config file path
- Environment prefix
- Extra config files
- User ID (UID) and Group ID (GID)
- IP address

### Network Information

Displays network configuration:

- IP address
- Gateway
- Netmask
- Network interface

### Storage Data

Table of all mounted storage devices showing total size, free space, used space, filesystem type, and mount options.

### Environment Variables

Lists all environment variables. Sensitive values (containing "secret", "password", "token", or "key") are hidden behind a spoiler toggle.
