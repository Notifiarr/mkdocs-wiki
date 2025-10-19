# Log Watcher

aka File Watcher

This allows the Notifiarr Client to watch (log) files for lines matching a regular expression. This is similar to tail -f file | grep string and allows you to send notifications when, for instance, a log file has a new line written that matches a regular expression.

***Coming Soon***
!!! info
    If creating a skip expression that contains `'` replace the apostrophe with `.?`

## Regular Expressions & Skip Expressions

Below are community suggested expressions

| App | Regular Expression | Skip Expression | Regular Explanation | Skip Explanation |
| --- | ------------------ | --------------- | ------------------- | ---------------- |
| Radarr | `(?i)(\|warn\||\|error\||^\[v5.+\])` | `(?i)Movie with IMDBId|It will not be added|Invalid date found|Validation failed|An unhandled exception has occurred while executing the request.|HttpClient error` | Notify on all Warnings, Errors, and Stack Traces (Version Number) | Skip movie add errors. Skip Indexer Feed invalid date Errors. Skip Errors   saying there was an Error |
| Sonarr   | `(?i)(\|warn\||\|error\||^\[v4.+\])` | `(?i)Invalid date found|Validation failed|An unhandled exception has occurred while executing the request.|Unable to find exact quality|HttpClient error`            | Notify on all Warnings, Errors, and Stack Traces (Version Number)                      | Skip Indexer Feed invalid date Errors. Skip Errors saying there was an   Error. Skip unknown quality errors. |
| Prowlarr | `(?i)(\|warn\||\|error\||^\[v1.+\])`            | `(?i)Validation failed|An unhandled exception has occurred while executing the request|[?:CinemaZ|PrivateHD](.a-z0-9/=&?: )+404\.NotFound|HttpClient error`          | Notify on all Warnings, Errors, and Stack Traces (Version Number)                      | Skip Errors saying there was an error. Skip Cinemaz/PrivateHD 404   (NotFound Errors)                        |
| Readarr  | `(?i)(\|warn\||\|error\||^\[v1.+\])`            | `(?i)Validation failed|An unhandled exception has occurred while executing the request.|HttpClient error`                                                              | Notify on all Warnings, Errors, and Stack Traces (Version Number)                      | Skip Errors saying there was an error.                                                                       |
| Lidarr   | `(?i)(\|warn\||\|error\||^\[v2.+\])`            | `(?i)Validation failed|An unhandled exception has occurred while executing the request.|HttpClient error`                                                              | Notify on all Warnings, Errors, and Stack Traces (Version Number)                      | Skip Errors saying there was an error.                                                                       |
| PMM      | `(?i)(\[ERROR\])`              | `(?i)(Convert Error:|ID not found|TVDb Error: Name not found|Plex Error: No Items found in Plex|Trakt Error: No TVDb ID found for|TMDb Error: No Movie found for TMDb ID)`                                                                                                                                                       | Notify on Errors | Exclude common errors of unable to find/map ids or Plex searches returning no items.                                                                                                        |
