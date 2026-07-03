# Notifiarr Client Endpoints

Endpoints allow the Notifiarr client to fetch data from local services on a schedule and relay the results to the Notifiarr website. This is useful for pulling data from services like PiHole, custom APIs, or any HTTP endpoint and sending it to Notifiarr for processing and notifications.

---

## Configuration

Each endpoint instance has the following settings:

| Setting | Environment Variable | Description |
| --------- | --------------------- | ------------- |
| **Name** | `ENDPOINT_{n}_NAME` | Name of the endpoint (required, must be unique) |
| **Template** | `ENDPOINT_{n}_TEMPLATE` | Payload template name used by the website to parse the response into notifications (required) |
| **Follow Redirects** | — | Follow HTTP redirects when fetching the URL |
| **Timeout** | `ENDPOINT_{n}_TIMEOUT` | HTTP request timeout duration |
| **Method** | `ENDPOINT_{n}_METHOD` | HTTP method: GET, POST, PUT, DELETE, PATCH, HEAD, OPTIONS |
| **URL** | `ENDPOINT_{n}_URL` | The URL to fetch (must begin with `http://` or `https://`) |
| **Body** | `ENDPOINT_{n}_BODY` | Request body for POST/PUT/PATCH requests |
| **Query** | `ENDPOINT_{n}_QUERY` | Query parameters, one `key=value` per line |
| **Headers** | `ENDPOINT_{n}_HEADER` | HTTP headers, one `key: value` per line |
| **Valid SSL** | `ENDPOINT_{n}_VALID_SSL` | Validate the HTTPS certificate when fetching the URL. Disable for self-signed certificates (default: `false`) |

### Scheduling

Each endpoint includes a full scheduling system:

- **Frequency** - No Schedule, Minutely, Hourly, Daily, Weekly, Monthly
- **At Times** - Specify hours, minutes, and seconds for execution
- **Days of Week** - Select specific days for weekly schedules
- **Days of Month** - Select specific days (1-31) for monthly schedules

A human-readable description of the schedule is displayed automatically.

### Adding Endpoints

Click the **+** button to add a new endpoint instance. Multiple endpoints can be configured, each fetching from a different URL on its own schedule.

---

## Instructions

1. Navigate to the Endpoints page in the Notifiarr client web UI
2. Add a new endpoint and configure the name, URL, and template
3. Set the HTTP method and any required headers or body content
4. Configure the schedule for how often the endpoint should be fetched
5. Save the configuration
