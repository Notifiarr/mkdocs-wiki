# Bazarr

!!! info
    This integration allows for notifications from Bazarr and will also add reactions to notifications if a subtitle was found for it and you are using reactions.

---

## Current Versions

![version](https://img.shields.io/badge/dynamic/json?query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Fhotio%2Fbazarr%2Frelease%2FVERSION.json&label=Latest%20Version&style=for-the-badge&color=526cfe){ .off-glb }
![version](https://img.shields.io/badge/dynamic/json?query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Fhotio%2Fbazarr%2Fnightly%2FVERSION.json&label=Latest%20Version&style=for-the-badge&color=526cfe){ .off-glb }

---

## Trigger options

![triggers-channels.png](../../assets/screenshots/integrations/bazarr/triggers-channels.png)

---

### Triggers

- `Info` - Currently all notifications use this type
- `Warning` - To date, Bazarr doesn't use this type
- `Success` - To date, Bazarr doesn't use this type
- `Failure` - To date, Bazarr doesn't use this type

---

### Channel

- Bazarr shares the *arr channel unless Granular Setup is used, clicking the link on the site will move to the channel setup location.

---

## Configuration

![open-configuration.png](../../assets/screenshots/integrations/bazarr/open-configuration.png)

Click the **cog icon** to open the configuration options for Bazarr.

![configuration.png](../../assets/screenshots/integrations/bazarr/configuration.png)

1. Open integration specific instructions
1. Choose the notification format
1. Enable reactions for `*arr` notifications when a subtitle is found if the associated `*arr` notification can be found

Reaction example:

![reaction.png](../../assets/screenshots/integrations/bazarr/reaction.png)

---

## Instructions

![instructions.png](../../assets/screenshots/integrations/bazarr/instructions.png)

1. How to enable notifications from within Bazarr
1. The URL to use in Bazarr
1. Test the notification from Notifiarr to Discord

!!! note
     This will ensure your server, channel and permissions are set properly in Discord
