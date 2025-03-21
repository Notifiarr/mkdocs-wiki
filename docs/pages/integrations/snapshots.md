![overview.png](/snapshots/overview.png)
1. Reloads the integration.
1. Opens the integrations settings.
1. A list of locations which have the Notifiarr client installed.
1. Opens up the Discord channel selection menu.

---

## Integration Settings Menu

![open_config.png](/snapshots/open_config.png)

Click the **cog icon** to open the integration settings for the Snapshot integration.

![settings.png](/snapshots/settings.png)

1. `Basic Instructions` - Gives you basic guidelines on how to setup this integration.
1. `Integration Settings` - Allows the user to further configure the integration.
1. `Extra Settings` - Adjust the extra settings for this integration.
1. `Client Settings` - Allows the user to set what should be reported in the snapshot and select which client to use
1. `Custom Icon` - Assign another icon to notifications from this integration. (Subscriber Feature)
1. `Screenshots` - Shows the expected output once all correctly configured.
1. `Save` - Saves all your Configured settings and closes the Integration Settings Menu.

---

## Integration Settings

Before all the configuration options are available you must "Pick a client" from the drop-down list. This will typically be the hostname you have for your locally installed Notifiarr client.

![integration_settings1.png](/snapshots/integration_settings1.png)

These are all the configurable options available to the user.

![integration_settings.png](/snapshots/integration_settings.png)

1. `Pick a client` - Select the local Notifiarr client you wish to configure for alerting.
1. `Trigger` - What the Snapshot integration will alert on.
The following Trigger options are available.
![trigger_options.png](/snapshots/trigger_options.png)
1. `Comparator` - Allows the user to configure alerts using one of the following, =, <=, >=, contains OR does not contain.
1. `Value` - What value shall be used to trigger the alert.
1. `@mention` - Pick a user or role and Discord will ping you if there is an alert.
1. `Add or Delete` - Here you can delete any existing alerts you may have or you can add a new alert.
1. Select this if you only want notifications when an alert is triggered. If left unchecked, you will receive continous notifications as specified in the interval selection time (e.g. every 30min). This is found under client settings and discussed below.

### Triggers and Allowed Values

The triggers used by the snapshot integration have the following allowed values.

1. `Raid` - Using the Comparator "contains" with a Value of "_" will alert of a failure.
1. `MegaCLI` - Using the Comparator "contains" with a Value of "degraded".
1. `Load` - Value can be a decimal or whole number.
1. `Users` - Value can be a whole Number.
1. `Drive Age (Days)` - Value can be a number in days.
1. `Drive Temp` - Value can be a decimal or whole number.
1. `Drive SMART` - Using the Comparator "contains" with a Value of either "fail" OR "pass"
1. `Storage (Free GB)` - Value can be a whole number or decimal followed by G for Gigabyte or T for Terabyte. e.g. 500G or 0.5T
1. `Quota (Free GB)` - Value can be a whole number or decimal followed by G for Gigabyte or T for Terabyte. e.g. 500G or 0.5T
1. `CPU Temp` - Value can be a decimal or whole number.
1. `CPU Load` - Value can be a decimal or whole number.
1. `RAM Load` - Value can be a decimal or whole number.

---

## Extra Settings

Allows the user to update existing messages and change between Fahrenheit and Celsius.

![extra_settings.jpg](/snapshots/extra_settings.jpg)

---

## Client Settings

Here are all the different settings for your client. These selections will determin what notifications will be monitored and reported on.

![client_settings.jpg](/snapshots/client_settings.jpg)

---

## Custom Icon

If you are AWESOME and are one of our Sub's then you will see this option and can upload your own custom icon.

![custom_icon.jpg](/snapshots/custom_icon.jpg)


