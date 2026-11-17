# Notifiarr Client Actions

The Actions page displays all internal Notifiarr client actions including triggers, timers, and schedules. These are executed by internal timers, scheduled tasks, and events from the Notifiarr website or a connected chat server.

!!! tip
    This page is primarily useful for troubleshooting. You can manually trigger any action to test functionality.

---

## Action Types

### Timers

Actions that execute on a repeating interval. Displays the interval duration for each timer.

### Schedules

Actions that execute on a cron-based schedule. Displays a human-readable description of the schedule.

### Triggers

Event-driven actions with no fixed timer or schedule. These fire in response to events from the website or chat server.

---

## View Modes

The page supports two display modes:

- **Cards** - Actions grouped by type (Timers, Schedules, Triggers) with individual cards showing the action name, execution counter, and interval/schedule
- **Table** - All actions in a single sortable table with columns: Type, Action, Counter, When

Use the toggle button in the header to switch between views. A text filter is available to search for specific actions.

---

## Available Actions

Actions include operations such as:

- Collecting Plex sessions
- Checking Plex for completed sessions
- Emptying Plex trash
- Updating the dashboard
- Syncing MDB lists
- Syncing Starr profiles and custom formats, for all instances or per instance
- Sending Radarr collection gaps
- Storing the Radarr, Sonarr, Lidarr, and Readarr download queues for each instance
- Sending cached stuck items and, for Patrons, cached downloading items
- Running configured endpoints and commands
- Uploading logs
- Updating snapshots
- Checking Starr database corruption and backups
- Polling Notifiarr for new settings
- Telling the Notifiarr website the client is still up
- Running custom cron timers provided by the website
- Checking for a new client version (Windows only, when Auto Update is enabled)
- Stopping all triggers and timers when the client reloads

Some of these only appear when the matching setting is configured. For example, the queue actions need a Starr instance.

!!! info "Timing of the background actions"
    - **Polling Notifiarr for new settings** repeats about every 4 minutes. It only exists while the client has no settings from the website.
    - **Telling the Notifiarr website the client is still up** repeats about every 15 minutes.
    - **Checking Plex for completed sessions** repeats about every minute. It exists only when Plex session tracking is configured.
    - **Custom cron timers** run at the interval the website provides. The client raises any interval under one minute to one minute.

Each action that supports manual execution has a **Run** button.
