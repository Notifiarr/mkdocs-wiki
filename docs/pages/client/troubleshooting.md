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

## Duplicate Clients

If you have duplicate clients on the website:

1. Make sure your client has a [static hostname](afterInstall.md#hostname).
1. Then [see these instructions](../../pages/website/clientConfig.md#resolving-duplicate-clients)
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
    The `--reset` command creates a local admin password as a recovery fallback. This is only needed if you can't login with your Notifiarr.com credentials. After reset, you can login with username `admin` and the generated password, then set up your normal authentication.

- If you still can't login, restart the container.

## Useful CLI Flags

The Notifiarr client binary accepts several command-line flags useful for debugging:

- `--ps` - Print the system process list. Helpful when creating Process health checks to see exact process names.
- `--curl <url>` - GET a URL and display response headers and payload. Useful for testing connectivity to app instances. Use `--header "Key: Value"` to add request headers.
- `--version` - Print the full version string and exit.
- `--write <path>` - Write a new default config file to the specified path. Use `-` to overwrite the current config file path.
- `--config <path>` / `-c <path>` - Specify the config file path. Can also be set with the `DN_CONFIG_FILE` environment variable.
- `--extraconfig <path>` / `-e <path>` - Load additional config files. Can be specified multiple times.
- `--prefix <prefix>` / `-p <prefix>` - Change the environment variable prefix (default: `DN`).

## Config File Compression

When you save the configuration from the Web UI, the config file is bzip2 compressed.
Set the `DN_ENCODE_CONFIG_FILE` environment variable to `false` to keep the config file
in plain text. See the [Gibberish Config File](#gibberish-config-file) section for
decompression instructions.
