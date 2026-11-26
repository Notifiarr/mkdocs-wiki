# Notifiarr Client Configuration

This page lists general client settings that other pages do not cover. Set each one in the Web UI under **Settings** > **Configuration**, in the config file, or as an environment variable. Environment variables start with `DN_` unless you change the prefix with `--prefix`.

For related settings, see [Reverse Proxy](reverseProxy.md) for `urlbase` and `upstreams`, and [Install](install.md) for `ui_password` and the log file paths.

---

## Network

| Config key | Environment variable | Default | Description |
| :- | :- | :- | :- |
| `bind_addr` | `DN_BIND_ADDR` | `0.0.0.0:5454` | The IP and port the client listens on. Use `0.0.0.0` for all interfaces, or `127.0.0.1:5454` to listen only on localhost, for example behind a local proxy. The client uses this address to receive Plex webhooks and Media Request commands |
| `timeout` | `DN_TIMEOUT` | `1m` | Timeout for the web server and for requests to Notifiarr.com |
| `retries` | `DN_RETRIES` | `4` | How many times to retry a failed request to Notifiarr.com. Cloudflare sometimes returns a 521 and a retry fixes it. `0` uses the default of 4. Use `1` to turn retrying off |
| `no_compress` | `DN_NO_COMPRESS` | `false` | Turn off compression of payloads sent to the website |
| `ssl_key_file` | `DN_SSL_KEY_FILE` | empty | Path to the SSL key file in PEM format |
| `ssl_cert_file` | `DN_SSL_CERT_FILE` | empty | Path to the SSL certificate file in PEM format |

Set both `ssl_key_file` and `ssl_cert_file` to make the client listen with HTTPS. The client must be able to read both files.

---

## API keys

| Config key | Environment variable | Description |
| :- | :- | :- |
| `extra_keys` | `DN_EXTRA_KEYS` | More API keys for third-party tools. The client HTTP API accepts them in the `X-API-Key` header, the same as the main `api_key`. The Web UI takes one key per line |

---

## Logging

| Config key | Environment variable | Default | Description |
| :- | :- | :- | :- |
| `trace` | `DN_TRACE` | `false` | Log function entry and exit with request IDs. Use it for deep debugging. It is very verbose |
| `max_body` | `DN_MAX_BODY` | `102400` | The most payload data, in bytes, that debug logging writes for a request. `0` means no limit |
| `log_file_mb` | `DN_LOG_FILE_MB` | `5` | The size in megabytes at which a log file rotates |
| `log_files` | `DN_LOG_FILES` | `10` | How many files to keep for each log |
| `file_mode` | `DN_FILE_MODE` | `0600` | The Unix file mode for new log files, such as `0600`, `0640`, or `0644`. Ignored on Windows |
| `no_uploads` | `DN_NO_UPLOADS` | `false` | Set to `true` to stop Notifiarr.com from asking the client to upload its log files |

---

## System

| Config key | Environment variable | Default | Description |
| :- | :- | :- | :- |
| `serial` | `DN_SERIAL` | `false` | Set to `true` to use fewer threads when polling apps. It spreads CPU use out and lowers memory use |
