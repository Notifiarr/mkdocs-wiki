# Discord App

!!! info
    The Discord App integration provides advanced Discord server management features including message tracking, member traffic monitoring, channel cleanup, threading, off-topic management, reminders, forum management, role triggers, warnings, and more.

---

## Features

### Deleted Messages

Track and log deleted messages in your Discord server. Sends a notification when a message is deleted.

- Notification color customization
- Option to ignore deleted bot messages
- Option to ignore specific channels

### Edited Messages

Track message edits in your Discord server.

- Show new message content
- Show old message content
- Show diff between old and new
- Notification color customization
- Option to ignore edited bot messages
- Option to ignore specific channels

### Member Traffic

Monitor member joins and leaves in your Discord server.

- `Join` - Receive a notification when a member joins
- `Leave` - Receive a notification when a member leaves
- Notification color customization for each event

### Cleanup

Keyword-triggered message cleanup in Discord channels.

- Configure a keyword that triggers cleanup (e.g., `!cleanup`)
- Restrict to specific channels or allow in all channels
- Restrict to specific roles or allow any role
- Notification color customization
- Optional: Disable role permission response

### Threading

Automatically create threads from messages in specified channels.

- Select which channels to auto-thread
- Customize the thread creation message

### Off-Topic

Move off-topic discussions to a designated channel.

- Configure a keyword to trigger off-topic move (e.g., `!offtopic`)
- Restrict to specific channels or allow in all channels
- Restrict to specific roles or allow any role
- Customize the label, title, and message
- Choose message type (embed or text)
- Configure pre-user message text
- Set a default off-topic channel
- Optional: Disable role permission response

### Reminders

Allow users to set reminders in Discord.

- Configure a keyword to trigger reminders
- Restrict to specific channels or allow in all channels
- Restrict to specific roles or allow any role/user
- Optional: Disable role permission response

### Forum Pings

Configure automatic pings for forum channel posts.

- Set up per-channel ping rules
- Ping all roles on new posts, or ping specific roles based on forum labels
- Add/update/delete label-based ping rules per channel

### Forum Messages

Configure automatic messages for forum channel posts.

- Set default messages for posts without labels
- Set label-specific messages per channel
- Add/update/delete label-based messages

### Role Triggers

Configure role-based trigger actions.

- Assign triggers to specific Discord roles
- Configure which channel receives role trigger notifications

### Message Attachments

Configure rules for message attachments in Discord channels.

- Restrict to specific roles or channels
- Set attachment rules and custom messages
- Per-channel attachment rules with custom responses

### Codeblock Enforcement

Encourage or require code to be posted in codeblocks.

- Configure a keyword to trigger codeblock reminders
- Customize the reminder message
- Restrict to specific roles
- Optional: Disable role permission response

### Warnings

Issue, view, and delete warnings for Discord members.

- **Add warning** - Keyword, channel, and role configuration
- **View warnings** - Keyword, channel, and role configuration
- **Delete warning** - Keyword, channel, and role configuration
- Each warning action has its own channel/role restrictions
- Optional: Disable role permission response for each

### Thread Archive

Automatically archive stale threads.

- Configure stale threshold in hours
- Customize the archive message
- Select which channels to monitor
- Restrict to specific roles

### Spam Trap

Automatically moderate spam/compromised accounts posting in designated "trap" channels.

- Configure one or more trap channels — any message posted in a trap channel triggers moderation immediately
- Exclude specific roles from moderation (excluded roles still produce an ignored mod-log notice instead)
- `Kick if member longer than (days)` - Members newer than this threshold are **banned**; members older than it are **kicked** (temporary ban, messages deleted after 15 minutes, then unbanned). Default is 30 days.
- Notification color customization
- Requires the bot to have the **Ban Members** and **Manage Messages** permissions, and the bot's role must be **higher than** the target user's highest role
- Trap channel(s) must allow **@everyone** (or the roles you expect spammers to use) to **send messages**, otherwise the trap will not trigger

### Ban Sync

Participate in ban synchronization across Notifiarr-connected Discord servers.

---

## Channels

- The Discord App integration is organized into 7 tabs in the Notifiarr UI — **Roles**, **Users**, **Cleanup**, **Forums**, **Messages**, **Threads**, and **Traffic** — with configurable channel/role pickers per feature area.

---

## Instructions

1. Enable the Discord App integration on the Notifiarr website
2. Configure the features you want to use
3. The Notifiarr bot must be in your Discord server with appropriate permissions
4. Each feature can be independently enabled and configured
