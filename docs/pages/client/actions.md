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
- Updating the dashboard
- Syncing MDB lists
- Syncing Starr profiles and custom formats
- Checking for stuck download items
- Running configured endpoints and commands
- Uploading logs
- Updating snapshots
- Checking Starr database corruption and backups

Each action that supports manual execution has a **Run** button.
