# Hotio

!!! info
     This integration allows for notifications from Hotio.

## Currently supported

- Pullio

---

## Trigger options

![trigger-channels.png](../../assets/screenshots/integrations/hotio/trigger-channels.png)

1. Triggers
    - `Pullio` - Enable notifications from Pullio
1. Channel
    - Pick the channel on your server to send Pullio notifications to.

---

## Configuration

![open-configuration.png](../../assets/screenshots/integrations/hotio/open-configuration.png)

Click the **cog icon** to open the configuration options for Hotio apps.

![configuration.png](../../assets/screenshots/integrations/hotio/configuration.png)

### Triggers

There are three trigger states for Pullio, each with its own settings:

- `Available update` - Notifies when an update is available for a container
    - Notification color
    - Notification pings
    - Notification layout
- `Successful update` - Notifies when a container update completes successfully
    - Notification color
    - Notification pings
    - Notification layout
- `Failed update` - Notifies when a container update fails
    - Notification color
    - Notification pings
    - Notification layout

---

### Instructions

![instructions.png](../../assets/screenshots/integrations/hotio/instructions.png)

The compose entry to enable Notifiarr with Pullio

!!! note
     for images: If you do not specify an avatar image in the app compose one will be used from the site so you do not have to worry about image hosting sites.
