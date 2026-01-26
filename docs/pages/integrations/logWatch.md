# Log Watcher

The Log Watcher (aka File Watcher) allows the Notifiarr Client to monitor log files for lines matching regular expressions. This is similar to `tail -f file | grep pattern` - you get notifications when log files contain new lines matching your patterns.

## Configuration

Add `[[watch_file]]` blocks to your `notifiarr.conf`:

```toml
[[watch_file]]
  path       = '/var/log/radarr/radarr.debug.txt'
  regex      = '(?i)(\|warn\||\|error\||^\[v5.+\])'
  skip       = '(?i)Invalid date found|Validation failed'
  poll       = false
  pipe       = false
  must_exist = false
  log_match  = true
  disabled   = false
```

### Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `path` | string | *required* | Full path to the log file to watch |
| `regex` | string | *required* | Regular expression to match - matching lines trigger notifications |
| `skip` | string | `''` | Regular expression for lines to ignore (even if they match `regex`) |
| `poll` | bool | `false` | Use polling instead of inotify (useful for network mounts) |
| `pipe` | bool | `false` | Treat path as a named pipe (FIFO) instead of a file |
| `must_exist` | bool | `false` | Fail if the file doesn't exist at startup |
| `log_match` | bool | `true` | Log matched lines to notifiarr debug log |
| `disabled` | bool | `false` | Disable this watcher without removing the config |

!!! tip "Regex Tips"
    - Use `(?i)` at the start for case-insensitive matching
    - Use `|` to match multiple patterns: `error|warn|fatal`
    - Escape special characters: `\[`, `\.`, `\|`
    - If your skip expression contains `'`, replace it with `.?`

## Community Patterns

### *arr Applications

These patterns catch warnings, errors, and stack traces while filtering common noise.

#### Radarr

```toml
[[watch_file]]
  path  = '/var/log/radarr/radarr.debug.txt'
  regex = '(?i)(\|warn\||\|error\||^\[v5.+\]|database is locked)'
  skip  = '(?i)Download client failed to add torrent|Movie with IMDBId|It will not be added|Invalid date found|Validation failed|An unhandled exception has occurred while executing the request.|HttpClient error|TaskManager failed while processing|Task Error|Name does not resolve|429.TooManyRequests'
```

#### Sonarr

```toml
[[watch_file]]
  path  = '/var/log/sonarr/sonarr.debug.txt'
  regex = '(?i)(\|warn\||\|error\||^\[v[0-9].+\]|database is locked)'
  skip  = '(?i)Download client failed to add torrent|Invalid date found|Validation failed|An unhandled exception has occurred while executing the request.|Unable to find exact quality|HttpClient error|TaskManager failed while processing|Task Error|Name does not resolve|InvalidDateException|429.TooManyRequests'
```

#### Prowlarr

```toml
[[watch_file]]
  path  = '/var/log/prowlarr/prowlarr.debug.txt'
  regex = '(?i)(\|warn\||\|error\||^\[v[0-9].+\])'
  skip  = '(?i)Validation failed|An unhandled exception has occurred while executing the request|(?:CinemaZ|PrivateHD)[.a-z0-9/=&?: ]+404\.NotFound|HttpClient error|System.Net.CookieException|TaskManager failed while processing|Task Error|Name does not resolve|NzbDrone.Common.Http.HttpException: HTTP request failed|Retrying in'
```

#### Readarr

```toml
[[watch_file]]
  path  = '/var/log/readarr/readarr.debug.txt'
  regex = '(?i)(\|warn\||\|error\||^\[v[0-9].+\])'
  skip  = '(?i)Validation failed|An unhandled exception has occurred while executing the request.|HttpClient error'
```

#### Lidarr

```toml
[[watch_file]]
  path  = '/var/log/lidarr/lidarr.debug.txt'
  regex = '(?i)(\|warn\||\|error\||^\[v[0-9].+\])'
  skip  = '(?i)Validation failed|An unhandled exception has occurred while executing the request.|HttpClient error'
```

### Other Applications

#### Kometa (formerly Plex Meta Manager)

```toml
[[watch_file]]
  path  = '/var/log/kometa/meta.log'
  regex = '(?i)(\[ERROR\]|\[CRITICAL\])'
  skip  = '(?i)Convert Error:|ID not found|TVDb Error: Name not found|Plex Error: No Items found in Plex|Trakt Error: No TVDb ID found for|TMDb Error: No Movie found for TMDb ID'
```

#### Nginx Error Log

```toml
[[watch_file]]
  path  = '/var/log/nginx/error.log'
  regex = '(?i)(emerg|alert|crit|\[error\].*upstream.*failed|502|503|504|connect\(\) failed|no live upstreams)'
  skip  = '(?i)(client closed connection|upstream timed out.*reading response header|recv\(\) failed|connection reset by peer|SSL_do_handshake)'
```

#### Rustic Backup

```toml
[[watch_file]]
  path  = '/var/log/rustic/rustic.log'
  regex = '(\[ERROR\]|\[WARN\]|starting to backup|successfully saved|backup of.*done)'
  skip  = '(?i)(flush_task.*graceful shutdown|Requesting graceful shutdown|read_end_buffer_size|write_end_buffer_size|repository opendal.*password is correct)'
```

## Pattern Reference

### Common *arr Log Patterns

| Pattern | Matches |
|---------|---------|
| `\|warn\|` | Warning log level |
| `\|error\|` | Error log level |
| `^\[v5.+\]` | Stack traces (version header) |
| `database is locked` | SQLite locking issues |

### Common Skip Patterns

| Pattern | Reason to Skip |
|---------|---------------|
| `Invalid date found` | Indexer feed parsing noise |
| `Validation failed` | API validation errors |
| `HttpClient error` | Transient network issues |
| `429.TooManyRequests` | Rate limiting (expected) |
| `Name does not resolve` | DNS failures (transient) |
| `Download client failed to add torrent` | Often due to duplicate detection |

## Troubleshooting

### File Not Being Watched

1. Verify the path exists: `ls -la /path/to/log`
2. Check file permissions - notifiarr user must have read access
3. Try `poll = true` for network-mounted files
4. Check notifiarr logs: `journalctl -u notifiarr | grep -i watch`

### Too Many Notifications

1. Add patterns to `skip` for false positives
2. Use more specific `regex` patterns
3. Consider watching `.debug.txt` instead of `.txt` for less verbose logs

### No Notifications

1. Test your regex at [regex101.com](https://regex101.com/) with Go flavor
2. Verify `disabled = false`
3. Check that lines actually match with: `tail -f /path/to/log | grep -E 'your-regex'`
4. Review notifiarr debug log for "watch" entries
