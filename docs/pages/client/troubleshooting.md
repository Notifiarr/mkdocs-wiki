---
# When this page gets too long, set this to 1.
toc_depth: 2
---
# Client Troubleshooting

- Find help on [Notifiarr's Discord](http://notifiarr.com/discord) (preferred).
- Or [Go Lift](https://golift.io/discord) if you want to chat about the client *code*.

Find tips for common problems on this page.

## Tmp not found

Corruption checks require a temp folder to write the db file. This may be a couple hundred megabytes or more.
Set the `TMPDIR` environment variable to a writable path, or mount `/tmp` to resolve the error.

## Unraid: Execution error / Bad parameter

Starting the container on Unraid shows an **Execution error** dialog that says **Bad parameter**.
That dialog is generic and does not name the cause. Get the real error first:

1. Open the *Docker* tab, click the container, and choose *Edit*. Click *Apply* and read the output.
   Unraid prints the full `docker run` command and Docker's error text there.
1. Or run `docker start Notifiarr` in the Unraid terminal. Use your container's name.

Then match the error:

| Error text | Fix |
| --- | --- |
| `exec: "/init": permission denied` (or any `permission denied`) | Someone ran *New Permissions* on `appdata` instead of *Docker Safe New Perms*. Stop Docker, rebuild the Docker directory or restore `appdata` from backup, then reinstall from *Apps > Previous Apps*. |
| Same dialog, no `docker run` error, and other containers fail too | Docker's state or `docker.img` is damaged. Delete `/mnt/user/system/docker/installed/` or recreate `docker.img` (*Settings > Docker*), then reinstall from *Apps > Previous Apps*. |

Template items to check while you are in the editor:

- *Extra Parameters* should only hold `-h notifiarr`. Any other value is passed straight to `docker run`, and its error shows in the output above.
- Keep the `/config` path, `/etc/machine-id`, and `/var/run/utmp` mappings from the template. See [Install](install.md).

Sources: [Unraid Docker troubleshooting](https://docs.unraid.net/unraid-os/troubleshooting/common-issues/docker-troubleshooting/),
Unraid forum threads [177037](https://forums.unraid.net/topic/177037-completely-screwed-up-ran-new-permissions-on-every-share-including-appdata-now-no-containers-work-with-execution-error-bad-parameter-message/)
and [131566](https://forums.unraid.net/topic/131566-docker-container-starting-problem-error-execution-error-bad-parameter/).

## Duplicate Clients

If you have duplicate clients on the website:

1. Make sure your client has a [static hostname](afterInstall.md#hostname).
1. Then [see these instructions](../website/clientConfig.md#resolving-duplicate-clients)
    to remove the duplicates.

## Gibberish Config File

Once you click save in the Web UI, the config file is compressed.
It will look like gibberish when you try to edit it.
In the rare case the UI is not accessible and the conf file must be edited,
you will need to decompress the file with `bzcat` prior to making your edits.
Example:

```bash
bzcat /path/to/notifiarr.conf > /output/path/to/notifiarr_decomp.conf
# or
mv /path/to/notifiarr.conf /path/to/notifiarr.conf.bz
bunzip2 /path/to/notifiarr.conf.bz
```

## Clearing Logs

- To `clear` logs to make troubleshooting easier - stop the client
  and rename/remove the log file(s), then restart the client.
- If you have not previously enabled debug logs you do not need to clear anything.

## Forgotten Passwords

### Fresh Installs

Execute the below command to print the unencrypted first-start password.
**This only works for brand new installations.**

```bash
# Fix the path yourself:
grep ui_password  /path/to/notifiarr/notifiarr.conf

# Unraid usually:
grep ui_password  /mnt/user/appdata/Notifiarr/notifiarr.conf
```

### Linux & FreeBSD

- Run these commands to reset the password and restart the application.

```bash
# Reset password.
notifiarr --reset
# Restart client (linux).
systemctl restart notifiarr
```

### Windows

- Run this command, and then restart the application.

```bash
notifiarr.exe --reset
```

### Docker & Unraid

- Run these two commands in your host system's terminal (console or ssh) while the Notifiarr container is running.
   *If your container is named `notifiarr` then replace `Notifiarr` with the lowercase version.*

```bash
docker exec Notifiarr /notifiarr --reset
docker kill --signal=HUP Notifiarr
```

!!! note "About Reset"
    The `--reset` command creates a local admin password as a recovery fallback. This is only needed if you can't login with your Notifiarr.com credentials. After reset, login with username `admin` and the generated password.

- If you still can't login, restart the container.

### Change the Reset Password

The generated `admin` password is random. Once you're logged in, change it to something you'll remember so you don't have to reset again:

1. Click your username in the bottom-left of the Web UI menu.
1. Open the *Trust Profile* page.
1. Enter the current (reset) password, set a new password of at least 9 characters, and save. You can also configure an auth proxy header here instead.

See [Set a password](afterInstall.md#set-a-password) for more detail.

## Useful CLI Flags

The Notifiarr client binary accepts several command-line flags useful for debugging:

- `--ps` - Print the system process list. Helpful when creating Process health checks to see exact process names.
- `--curl <url>` - GET a URL and display response headers and payload. Useful for testing connectivity to app instances. Use `--header "Key: Value"` to add request headers.
- `--version` - Print the full version string and exit.
- `-v` - Print the short version string and exit.
- `--write <path>` / `-w <path>` - Write a config file to the specified path. Pass `example` or `---` to write a fresh default-template config to `<config path>.new` next to your existing config. The client never overwrites an existing config file.
- `--config <path>` / `-c <path>` - Specify the config file path. Can also be set with the `DN_CONFIG_FILE` environment variable.
- `--extraconfig <path>` / `-e <path>` - Load additional config files. Can be specified multiple times.
- `--prefix <prefix>` / `-p <prefix>` - Change the environment variable prefix (default: `DN`).

## Config File Compression

When you save the configuration from the Web UI, the config file is bzip2 compressed.
Set the `DN_ENCODE_CONFIG_FILE` environment variable to `false` to keep the config file
in plain text. See the [Gibberish Config File](#gibberish-config-file) section for
decompression instructions.
