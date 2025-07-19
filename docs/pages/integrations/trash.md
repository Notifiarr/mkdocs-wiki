# TRaSH

!!! info "TRaSH"

    This integration allows you to setup and sync TRaSH guides with Radarr and Sonarr. Keep in mind this requires the Notifiarr client.

!!! warning "patrons/subscribers"
    **Patron Feature** - Acessible to [Patrons and Subscribers](../../pages/faq/faq.md#q-what-are-the-user-level-differences) only

!!! note
    If you have questions about what the formats, profiles, scores, etc do then please use the TRaSH [discord](https://trash-guides.info/discord) server for help or check their guide. This wiki is for setting up and getting things in sync.

## Client Setup

- TRaSH Integration requires the notifiarr client to be running locally, [configured and working (i.e. communicating with) on the Notifiarr site](../../pages/website/clientConfig.md), and the Starr Apps configured.
- Add Starr Apps to the Client in the `Starr Apps` Tab of the Local Client
  - Note that `Time Out` for the Starr Apps **cannot** be set to `Disabled` for the app to be enabled
  - Note that a `Name` value **is required** for the Starr Apps you wish to sync

### Integration Card

![trigger-channels.png](../../assets/screenshots/integrations/trash/trigger-channels.png)

`CFs/Scores` - The amount of CF's and scores you have synced.

`Channel` - Which channel to send TRaSH update notifications to (when TRaSH updates them, removes them, when you sync them or unsync them)

## Getting Started

Click the **cog icon** in the card header to open the configuration options for TRaSH. To get started, you will need to go to Help → How-to.

![how-to.png](../../assets/screenshots/integrations/trash/how-to.png.png)

## Client Settings

here you can change the interval for your sync

![client-sync.png](../../assets/screenshots/integrations/trash/client-sync.png)

### Notifications

Here we can individually set what we would want to be notified for.

![notifications.png](../../assets/screenshots/integrations/trash/notifications.png.png)

### Profiles

here we can manange existing profiles or add new profiles/link predefined TRaSH profiles. For this guide we are going too add the TRaSH **HD Bluray + WEB** profile

![profiles-add-new.png](../../assets/screenshots/integrations/trash/profiles-add-new.png)

!!! info
    After selecting the profile as shown above you will be directed to the profile settings.

![profiles-1.png](../../assets/screenshots/integrations/trash/profiles-1.png)

`Sync` - syncing the profile.

`Starr instance profile` - if you want to create a new profile, or overide a existing profile.

`Profile name` - profile name **Needs to be unique**.

!!! Note
    If you plan too use TRaSH as default you can stop here and save your settings. Below we will got into customizing the profile, quality, and CF's.

!!! warning SAVE PROFILE SYNC
    **MAKE SURE TO SAVE YOUR PROFILE SYNC, THIS IS DIFFERENT FROM SAVE CLIENT SETTINGS**



### Profile Customization

!!! info
    Check-box means you want too sync TRaSH values and cannot change them in your ARR's as they will revert back after each sync is made. Uncheck any that you want too customize, And do so inside of your ARR's.

![profile-customization-1.png](../../assets/screenshots/integrations/trash/profile-customization-1.png)

`Language` - If you want too always sync your language, **Disable this if you plan too use something other then TRaSH default.

`Upgrades allowed` - Enable to allow upgrades.

`Minimum score` - Minimum score to download.

`Minimum upgrade score` - Minimum score differnce too allow upgrade. **defaulted to 1**

`Cutoff score` - When quality cutoff is met. **default set 10000**

### Quality Settings

!!! warning
    If you plan on changing the qualities in the profile, you will need to enable the allow custom quality order/groupings, if this is not enabled any changes made to the quality grouping will be reverted after each sync.

![quality.png](../../assets/screenshots/integrations/trash/quality.png)

`Cutoff quality` - Enable to use the default cutoff here it would be `Bluray-1080p`

`Qualities` - Match TRaSH qualities, or allow Custom qualities.

### Custom Formats "CF"

![custom-formats-1.png](../../assets/screenshots/integrations/trash/custom-formats-1.png)

`Add` - Choose if you want all new formats automatically added, only add missing formats, or add no formats.

`Remove` - Remove cf scores from this profile, or allow cf scores for this profile.

`Groups` - All available cf groups, You can choose the drop down too show all that are available.

### Formats

!!! info
    Here you will find all of the available TRaSH guide formats. You can find more info on these at [TRaSH Guides](https://trash-guides.info/)

![formats-1.png](../../assets/screenshots/integrations/trash/formats-1.png)

`Sync TRaSH CF names` - If you want to sync the names for the TRaSH CFs.

`Interactive flowchart` - Useful interactive flow charts for TRaSH.

### Scores

Here you can setup custom scores too your liking, and choose to sync them.

![scores-1.png](../../assets/screenshots/integrations/trash/scores-1.png)

`Filter` - filter between avialable profiles.

`Multiplier` - (multiplier * TRaSH = your score)

`Starr score/Custom` - Set a custom score of your choice.

`Sync` - Check-box to enable sync.

## Quality

Here you can edit quality names within a specific group and choose too sync them too your starr instance. 

![quality-1.png](../../assets/screenshots/integrations/trash/quality-1.png)

`Definition group`- Here you can choose the starr profile.

`Rename Field` - This is where you can customize the name of a quality.

`Sync` - Check-box to enable sync.

### Naming

Here you can choose a default TRaSH naming scheme for your media files/folders.

![naming-1.png](../../assets/screenshots/integrations/trash/naming-1.png)

### Delete Formats

![formats-1.png](../../assets/screenshots/integrations/trash/delete-formats.png)

`Fix Map` - Open the Custom Format map tool.

`Enable sync` - Enable sync for all CF's.

`Enable sync + scores` - Enable sync and scores. Will trigger a sync for starr instance

`Unlink starr` - Unlink your starr id from the map.

`Relink starr` - Relink your starr ip/map.

`Delete map` - Delete map **BE CAREFUL THIS WILL DELETE ALL YOUR SYNC SETTINGS**

`Delete Selected CFs/Delete Selected CFs & Map` delete your CF's and map

`  Fresh Start CFs/All` Fresh start CF's or ALL.
