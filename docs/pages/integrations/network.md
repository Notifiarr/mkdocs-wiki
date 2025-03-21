> This integration allows for notifications from the local Notifiarr client app to monitor network machines or services.
{.is-info}

## Network Overview

![overview.png](/network/overview.png)

1. Reloads the integration.
1. Opens the integrations settings.
1. A list of everything you are monitoring with the Notifiarr client and show a green arrow if it is available or red arrow if it isn't.
1. Opens up the Discord channel selection menu.

---

## Integration Settings Menu

![open_config.png](/network/open_config.png)

Click the **cog icon** to open the integration settings for the Network integration.

![settings1.png](/network/settings1.png)

1. `Basic Instructions` - Gives you basic guidelines on how to setup this integration in the UI.
1. `Triggers` - Adjust which webhooks will send notifications to you.
1. `Integration Settings` - Allows the user to further configure the integration.
1. `Extra Settings` - Adjust the extra settings for this integration.
1. `Client Settings` - Allows the user to set the scanning interval.
1. `Custom Icon` - Assign another icon to notifications from this integration. (Subscriber Feature)
1. `Screenshots` - Shows the expected output once all correctly configured.
1. `Save` - Saves all your Configured settings and closes the Integration Settings Menu.

---

## Basic Instructions

Detailed instructions are shown in the Client UI section of the wiki.

![setup.png](/network/setup.png)

1. `Service Checks` - Allows the user to configure the destination service and type of check to be done.
1. `+` - Adds additional line items.

## Integration Settings

These are all the configurable options available to the user.

## Triggers
![triggers.png](/network/triggers.png)

Select the individual trigger colour that will be displayed on Discord notifications.

## Integration Settings
![integration_settings.png](/network/integration_settings.png)

1. `Status` - This will post a message with the current status of selected items and update its self accordingly.
1. `Exclude` - This will allow specific items to be ignored when they go down or come up, typically during expected maintenance.

## Extra Settings
![extra_settings.png](/network/extra_settings.png)

1. `Status Page` - Enables a web page status overview of all your monitored items. Past events are also shown.
1. `Website Status` - Include current status of websites being tracked with the Website Status integration.
1. `Network Integration API` - Enable this by assigning a unique API key to the Network Integration on the Homepage of the Notifiarr website.

## Client Settings
![client_settings.png](/network/client_settings.png)

1. `Mute Client Down Alerts` - Select this to stop down alerts.
1. `Interval` - Select from the drop down list the check time in minutes. Or to disable all checks.

## Custom Icon
![custom_icon.png](/network/custom_icon.png)

Assign another icon to notifications from this integration (Subscriber Feature) 

