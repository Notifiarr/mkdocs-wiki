# Package Manager

!!! info
    This integration provides notifications for package updates on Linux (APT) and Unraid systems. The Notifiarr client relays APT install and update hooks, and the website sends notifications to Discord. Unraid notifications come from the [Notifiarr agent script](https://github.com/Notifiarr/notifiarr/blob/main/userscripts/unraid-notifiarr.sh).

---

## Trigger Options

### Triggers

- `APT` - Receive a notification when APT installs or updates packages (Linux). The client relays dpkg install hooks; it does not poll for available updates
- `Unraid` - Receive a notification for Unraid package updates
    - `Unraid normal` - Normal priority Unraid notifications
    - `Unraid warning` - Warning priority Unraid notifications
    - `Unraid alert` - Alert/error priority Unraid notifications

### Channels

- Package Manager channel picker for each trigger

---

## Configuration

Click the **cog icon** to open the configuration options for Package Manager.

1. Notification color selector for APT notifications
2. Notification color selector for Unraid normal notifications
3. Notification color selector for Unraid warning notifications
4. Notification color selector for Unraid alert notifications
5. Notification pings for each trigger

### Settings

- `Thumbnails` - Enable thumbnails in Unraid notifications

---

## Instructions

1. Ensure the Notifiarr client is installed and running on your system
2. Enable the Package Manager integration on the Notifiarr website
3. Enable the triggers for your operating system (APT for Linux, Unraid for Unraid)
4. For APT, set `apt = true` in the client config file and restart the client. The deb package installs the dpkg hook that the client relays to the website
5. For Unraid, install the [Notifiarr agent script](https://github.com/Notifiarr/notifiarr/blob/main/userscripts/unraid-notifiarr.sh) as described at the top of that script
