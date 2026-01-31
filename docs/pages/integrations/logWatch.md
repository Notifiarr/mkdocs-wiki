# Log Watcher

The Log Watcher (aka File Watcher) allows the Notifiarr Client to monitor log files for lines matching regular expressions. This is similar to `tail -f file | grep pattern` - you get notifications when log files contain new lines matching your patterns.

## Configuration

Add a new Log Watcher entry in the Notifiarr Client UI under **Configuration** > **Log Watch**.

### Fields

| Field | Required | Default | Description |
|-------|----------|---------|-------------|
| **Path** | Yes | - | Full path to the log file to watch |
| **Regex** | Yes | - | Regular expression to match - matching lines trigger notifications |
| **Skip** | No | *empty* | Regular expression for lines to ignore (even if they match Regex) |
| **Poll** | No | `false` | Use polling instead of inotify (useful for network mounts) |
| **Pipe** | No | `false` | Treat path as a named pipe (FIFO) instead of a file |
| **Must Exist** | No | `false` | Fail if the file doesn't exist at startup |
| **Log Match** | No | `true` | Log matched lines to notifiarr debug log |

!!! tip "Regex Tips"
    - Use `(?i)` at the start for case-insensitive matching
    - Use `|` to match multiple patterns: `error|warn|fatal`
    - Escape special characters: `\[`, `\.`, `\|`
    - If your skip expression contains `'`, replace it with `.?`

## Community Patterns

### *arr Applications

These patterns catch warnings, errors, and stack traces while filtering common noise.

---

#### Radarr

**Path:**
```text
/var/log/radarr/radarr.debug.txt
```

**Regex:**
```text
(?i)(\|warn\||\|error\||^\[v[0-9].+\]|database is locked)
```

??? info "Why this regex?"
    - `(?i)` - Case-insensitive matching for all patterns
    - `\|warn\|` - Matches `|Warn|` log level delimiter in *arr logs
    - `\|error\|` - Matches `|Error|` log level delimiter
    - `^\[v[0-9].+\]` - Matches stack traces that start with any version header (v4, v5, v6, etc.)
    - `database is locked` - SQLite locking issues that indicate problems

**Skip:**
```text
(?i)Download client failed to add torrent|Movie with IMDBId|It will not be added|Invalid date found|Validation failed|An unhandled exception has occurred while executing the request.|HttpClient error|TaskManager failed while processing|Task Error|Name does not resolve|429.TooManyRequests
```

??? info "Why skip these?"
    - `Download client failed to add torrent` - Usually duplicate detection, not a real error
    - `Movie with IMDBId` / `It will not be added` - Informational about skipped movies
    - `Invalid date found` - Common indexer feed parsing noise
    - `Validation failed` - API validation errors (usually user input issues)
    - `An unhandled exception...` - Generic wrapper, the actual error is elsewhere
    - `HttpClient error` - Transient network issues that resolve themselves
    - `TaskManager failed` / `Task Error` - Background task noise
    - `Name does not resolve` - DNS failures that are usually transient
    - `429.TooManyRequests` - Rate limiting (expected behavior)

---

#### Sonarr

**Path:**
```text
/var/log/sonarr/sonarr.debug.txt
```

**Regex:**
```text
(?i)(\|warn\||\|error\||^\[v[0-9].+\]|database is locked)
```

??? info "Why this regex?"
    - Same pattern as Radarr - matches warnings, errors, stack traces, and database locks

**Skip:**
```text
(?i)Download client failed to add torrent|Invalid date found|Validation failed|An unhandled exception has occurred while executing the request.|Unable to find exact quality|HttpClient error|TaskManager failed while processing|Task Error|Name does not resolve|InvalidDateException|429.TooManyRequests
```

??? info "Why skip these?"
    - Same reasons as Radarr, plus:
    - `Unable to find exact quality` - Quality parsing noise from release names
    - `InvalidDateException` - Date parsing errors from indexers

---

#### Prowlarr

**Path:**
```text
/var/log/prowlarr/prowlarr.debug.txt
```

**Regex:**
```text
(?i)(\|warn\||\|error\||^\[v[0-9].+\])
```

**Skip:**
```text
(?i)Validation failed|An unhandled exception has occurred while executing the request|(?:CinemaZ|PrivateHD)[.a-z0-9/=&?: ]+404\.NotFound|HttpClient error|System.Net.CookieException|TaskManager failed while processing|Task Error|Name does not resolve|NzbDrone.Common.Http.HttpException: HTTP request failed|Retrying in
```

??? info "Why skip these?"
    - `(?:CinemaZ|PrivateHD)...404` - Known indexers that return 404 for certain searches
    - `System.Net.CookieException` - Cookie handling issues that don't affect functionality
    - `HTTP request failed` / `Retrying in` - Transient errors with automatic retry

---

#### Readarr

**Path:**
```text
/var/log/readarr/readarr.debug.txt
```

**Regex:**
```text
(?i)(\|warn\||\|error\||^\[v[0-9].+\])
```

**Skip:**
```text
(?i)Validation failed|An unhandled exception has occurred while executing the request.|HttpClient error
```

---

#### Lidarr

**Path:**
```text
/var/log/lidarr/lidarr.debug.txt
```

**Regex:**
```text
(?i)(\|warn\||\|error\||^\[v[0-9].+\])
```

**Skip:**
```text
(?i)Validation failed|An unhandled exception has occurred while executing the request.|HttpClient error
```

---

### Other Applications

#### Kometa (formerly Plex Meta Manager)

**Path:**
```text
/var/log/kometa/meta.log
```

**Regex:**
```text
(?i)(\[ERROR\]|\[CRITICAL\])
```

??? info "Why this regex?"
    - Kometa uses `[ERROR]` and `[CRITICAL]` log level markers
    - Only matches actual errors, not warnings (which are often informational)

**Skip:**
```text
(?i)Convert Error:|ID not found|TVDb Error: Name not found|Plex Error: No Items found in Plex|Trakt Error: No TVDb ID found for|TMDb Error: No Movie found for TMDb ID
```

??? info "Why skip these?"
    - `Convert Error` - Image conversion issues that don't affect functionality
    - `ID not found` / `Name not found` - Missing metadata that can't be fixed
    - `No Items found in Plex` - Empty collections (expected for new libraries)
    - `No TVDb ID found` / `No Movie found` - External service lookup failures

---

#### Nginx Error Log

**Path:**
```text
/var/log/nginx/error.log
```

**Regex:**
```text
(?i)(emerg|alert|crit|\[error\].*upstream.*failed|502|503|504|connect\(\) failed|no live upstreams)
```

??? info "Why this regex?"
    - `emerg|alert|crit` - Nginx severity levels for serious issues
    - `\[error\].*upstream.*failed` - Backend connection failures
    - `502|503|504` - Gateway errors indicating backend problems
    - `connect\(\) failed` - Can't reach upstream servers
    - `no live upstreams` - All backends are down

**Skip:**
```text
(?i)(client closed connection|upstream timed out.*reading response header|recv\(\) failed|connection reset by peer|SSL_do_handshake)
```

??? info "Why skip these?"
    - `client closed connection` - User navigated away or closed browser
    - `upstream timed out` - Often caused by slow backends, not errors
    - `recv\(\) failed` / `connection reset` - Network glitches
    - `SSL_do_handshake` - SSL negotiation failures from bots/scanners

---

#### Rustic Backup

**Path:**
```text
/var/log/rustic/rustic.log
```

**Regex:**
```text
(\[ERROR\]|\[WARN\]|starting to backup|successfully saved|backup of.*done)
```

??? info "Why this regex?"
    - `\[ERROR\]|\[WARN\]` - Actual problems with backups
    - `starting to backup` - Notification that backup started
    - `successfully saved|backup of.*done` - Confirmation backup completed

**Skip:**
```text
(?i)(flush_task.*graceful shutdown|Requesting graceful shutdown|read_end_buffer_size|write_end_buffer_size|repository opendal.*password is correct)
```

??? info "Why skip these?"
    - `graceful shutdown` - Normal shutdown messages
    - `buffer_size` - Configuration warnings that don't affect functionality
    - `password is correct` - Informational message, not an error

---

## Pattern Reference

### Common *arr Log Patterns

| Pattern | Matches |
|---------|---------|
| `\|warn\|` | Warning log level in *arr format: `2024-01-30 12:00:00.000\|Warn\|...` |
| `\|error\|` | Error log level in *arr format |
| `^\[v[0-9].+\]` | Stack traces that start with any version header (e.g., `[v5.0.0.1234]`) |
| `database is locked` | SQLite concurrency issues |

### Common Skip Patterns

| Pattern | Reason to Skip |
|---------|---------------|
| `Invalid date found` | Indexer feed parsing - benign noise |
| `Validation failed` | User input issues, not system errors |
| `HttpClient error` | Transient network issues that auto-resolve |
| `429.TooManyRequests` | Rate limiting - expected behavior |
| `Name does not resolve` | DNS failures - usually transient |
| `Download client failed to add torrent` | Usually duplicate detection |

## Troubleshooting

### File Not Being Watched

1. Verify the path exists: `ls -la /path/to/log`
2. Check file permissions - notifiarr user must have read access
3. Try enabling **Poll** for network-mounted files
4. Check notifiarr logs: `journalctl -u notifiarr | grep -i watch`

### Too Many Notifications

1. Add patterns to **Skip** for false positives
2. Use more specific **Regex** patterns
3. Consider watching `.debug.txt` instead of `.txt` for less verbose logs

### No Notifications

1. Test your regex at [regex101.com](https://regex101.com/) with Go flavor
2. Verify the watcher is not disabled
3. Check that lines actually match with: `tail -f /path/to/log | grep -E 'your-regex'`
4. Review notifiarr debug log for "watch" entries
