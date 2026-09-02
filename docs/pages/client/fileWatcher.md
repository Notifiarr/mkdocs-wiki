# Notifiarr Client File Watcher

The File Watcher feature monitors files for lines matching a regular expression, similar to `tail -f file | grep pattern`. When a matching line is found, a notification is triggered.

!!! note
    You must enable the **Log Watcher** integration and select a notification channel on the Notifiarr website for file watcher notifications to be delivered.

---

## Configuration

Each file watcher instance has the following settings:

| Setting | Environment Variable | Description |
| --------- | --------------------- | ------------- |
| **Path** | `DN_WATCH_FILE_{n}_PATH` | File path to monitor |
| **Disabled** | `DN_WATCH_FILE_{n}_DISABLED` | Toggle the watcher on or off |
| **Regex** | `DN_WATCH_FILE_{n}_REGEX` | Regular expression to match against file lines |
| **Skip** | `DN_WATCH_FILE_{n}_SKIP` | Lines matching this expression are ignored |
| **Poll** | `DN_WATCH_FILE_{n}_POLL` | Enable file polling when filesystem events are not available |
| **Pipe** | `DN_WATCH_FILE_{n}_PIPE` | Enable if the path is a named FIFO pipe |
| **Must Exist** | `DN_WATCH_FILE_{n}_MUST_EXIST` | Require the file to exist at startup |
| **Log Match** | `DN_WATCH_FILE_{n}_LOG_MATCH` | Write matched lines to the Notifiarr application log |

### Adding Watchers

Click the **+** button to add a new file watcher instance. Multiple watchers can be configured, each monitoring a different file with its own regex pattern.

### Regex Tester

Use the built-in regular expression tester to verify your patterns match the expected log lines before saving.

---

## Instructions

1. Navigate to the File Watcher page in the Notifiarr client web UI
2. Add a new watcher instance and set the file path and regex pattern
3. Adjust optional settings (polling, pipe mode, etc.) as needed
4. Save the configuration
5. Enable the Log Watcher integration on the Notifiarr website and select a channel
