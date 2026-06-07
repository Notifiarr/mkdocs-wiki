# GitHub

!!!info
     This integration allows for notifications from public and private GitHub repositories.

---

## Trigger options

![trigger-channels.png](../../assets/screenshots/integrations/github/trigger-channels.png)

1. Triggers
    - List of all repositories and organizations with notifications enabled

---

## Configuration

![open-configuration.png](../../assets/screenshots/integrations/github/open-configuration.png)

Click the **cog icon** to open the configuration options for GitHub. The configuration is organized into three tabs: Organization/Repository, Discord Server, and Notifications.

![configuration.png](../../assets/screenshots/integrations/github/configuration-1.png)
![configuration.png](../../assets/screenshots/integrations/github/configuration-2.png)
![configuration.png](../../assets/screenshots/integrations/github/configuration-3.png)

### Organization/Repository Tab

1. **Organizations** - Add the organization URL. You have to be able to manage the selected Organization so you can add webhooks.
1. **Remove Organization** - Remove an existing organization. Keep in mind this removes all repositories linked to it.
1. **Private Repos** - Add private repositories manually, one `org/repository` per line (e.g. `Notifiarr/Notifiarr`). You need to add a webhook to the org so do not add it if you cannot do that.

### Discord Server Tab

1. **Add Server** - Add a discord server by its Server ID. The default server is available but this allows you to push notifications to other servers. The bot must be invited to any server you try to use here.
1. **Remove Server** - Remove a discord server (the default server cannot be removed).

### Notifications Tab

#### General Notification Settings

- `Content` - Choose between `All notification fields` or `Less notification fields` to control the amount of detail in notifications
- `Ignore users` - Ignore messages from specific users; comma separated list of usernames

#### Organization Level Settings

Set a default server and channel for an entire organization. Individual triggers are controlled on GitHub and will send to the selected channel(s). Using organization level settings makes repository settings optional.

#### Repository Level Settings

1. Pick a repository from the dropdown - they are pulled automatically based on the organizations added (including private repos)
1. Copy the `Server` or `Channel` selection to all triggers using the arrow icons
1. Set the server and channel for each available GitHub trigger individually

!!! tip
    All triggers should be enabled on GitHub and will send to the selected channel(s).

---

### Instructions

![instructions.png](../../assets/screenshots/integrations/github/instructions.png)

!!!note
     This is how you add the webhook to GitHub and then how you add the organization in the GitHub integration
