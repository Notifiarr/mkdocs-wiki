# Cross Seed

!!! info
    This integration allows for notifications from [Cross Seed](https://www.cross-seed.org/) when search results and lookups are processed.

---

## Trigger Options

### Triggers

- `Results` - Receive a notification when cross-seed search results are found
    - Optional: Include Poster and Background/Banner images in notifications

!!! note
    `Lookup` is not a separately toggleable trigger — it is a notification sub-type under **Results**, with its own color selector but no independent channel picker.

### Channels

- Cross Seed channel picker for each trigger

---

## Configuration

Click the **cog icon** to open the configuration options for Cross Seed.

1. Notification color selector for search results
2. Notification color selector for lookups
3. Notification pings for paused results
4. Notification layout customization

### Settings

- `Exclude types` - Choose result types to exclude from notifications:
    - **Saved** - Exclude saved results
    - **Injected** - Exclude injected results
    - **Failure** - Exclude failed results

---

## Instructions

1. Configure the webhook in Cross Seed to point to your Notifiarr webhook URL
2. Enable the triggers you want on the Notifiarr website
3. Test the notification to ensure it is working
