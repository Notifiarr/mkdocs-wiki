# Notifiarr Client Commands

Commands allow the Notifiarr client to execute custom scripts or shell commands. Commands can be triggered from the client web UI, the Notifiarr website, or from a connected chat server (Discord, Slack, or Telegram).

!!! warning
    Modified commands must be saved before they can be run from the web UI.

---

## Configuration

Each command instance has the following settings:

| Setting | Environment Variable | Description |
| --------- | --------------------- | ------------- |
| **Name** | `COMMANDS_{n}_NAME` | Command name, shown in logs and notifications (required, must be unique) |
| **Notify** | `COMMANDS_{n}_NOTIFY` | Send a notification after command execution, including command output |
| **Command** | `COMMANDS_{n}_COMMAND` | The command or script to run (required) |
| **Shell** | — | Wrap the command in a shell (`/bin/bash` on Linux, `cmd.exe` on Windows) |
| **Log Output** | `COMMANDS_{n}_LOG` | Write command output to the application log |
| **Timeout** | `COMMANDS_{n}_TIMEOUT` | Maximum run duration before the command is terminated (default: 15s) |

### Command Arguments

Commands support custom positional arguments using regex syntax `({regex})`. When a command contains argument patterns, users are prompted to provide values that match the specified regex before execution.

### Regex Tester

Use the built-in regular expression tester to verify argument patterns.

### Adding Commands

Click the **+** button to add a new command instance. Multiple commands can be configured.

---

## Command Output

Each command shows execution statistics:

- **Last execution** - When the command was last run
- **Execution count** - Total number of times the command has been executed
- **Failure count** - Number of failed executions
- **Last command** - The exact command string that was executed
- **Output** - The stdout/stderr output from the last execution

---

## Instructions

1. Navigate to the Commands page in the Notifiarr client web UI
2. Add a new command with a name and the command string to execute
3. Optionally enable notifications and logging
4. Save the configuration
5. Run the command from the web UI, the Notifiarr website, or a chat server
