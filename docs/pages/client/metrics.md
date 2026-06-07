# Notifiarr Client Metrics

The Metrics page displays runtime metric counters for the Notifiarr client. All counters reset when the application restarts.

!!! info
    The client exposes these metrics via Prometheus for use with Grafana dashboards.

---

## Metric Categories

### Log Files

Counters for log file activity.

### API Requests

Counters for incoming API requests to the client.

### HTTP Requests

Counters for incoming HTTP requests, including websocket tunnel requests.

### Website Requests

Counters for requests made to notifiarr.com.

### File Watcher

Statistics for configured file watchers.

### Application Requests

Request statistics grouped by configured application. Each application shows its own set of sub-counters.

### Triggered Actions

Execution counts for triggers, timers, and schedules. Each action shows its own set of sub-counters.

---

## Usage

- Navigate to the Metrics page in the Notifiarr client web UI
- Click **Update Backend** to refresh the displayed data
- Application uptime is shown at the top of the page
