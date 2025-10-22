# Client Troubleshooting

- Find help on Discord: [Notifiarr](https://discord.gg/AURf8Yz) (preferred) or [Go Lift](https://golift.io/discord) (if you like Go).

### Tmp not found

Corruption checks require a temp folder to write the db file. This may be a couple hundred megabytes or more.
Set the `TMPDIR` environment variable to a writable path, or mount `/tmp` to resolve the error.

### Resolving Duplicate Clients

If you have duplicate clients on the website and are setting a hostname after the fact,
[see these instructions](../../pages/website/clientConfig.md#resolving-duplicate-clients)
for resolving the duplicates after setting a hostname.

### Compressed Config File

Once you click save in the Web UI, the config file is compressed.
It will look like gibberish when you try to edit it.
In the rare case the UI is not accessible and the conf file must be edited,
you will need to decompress the file with `bzcat` prior to making your edits.
Example:

```bash
bzcat /path/to/notifiarr.conf > /output/path/to/notifiarr_decomp.conf
```

### Clearing Logs

- To `clear` logs to make troubleshooting easier - stop the client
  and rename/remove the log file, then restart the client.
- If you have not previously enabled debug logs you do not need to clear anything.
