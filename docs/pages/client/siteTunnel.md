# Notifiarr Client Site Tunnel

The Notifiarr client maintains a persistent websocket connection to notifiarr.com using a Mulery tunnel. This allows the website to communicate with your client without requiring an open port or static IP address.

This page lets you select which tunnel server to use as your primary connection and configure a backup tunnel in case the primary becomes inaccessible.

---

## Tunnel Selection

### Primary Tunnel

Select the tunnel server with the lowest latency to your client. Click **Ping Tunnels** to measure the response time for each available server, then select the fastest one as your primary.

Each tunnel entry shows:

- **Location** - Geographic location of the tunnel server
- **Socket URL** - The websocket endpoint

### Backup Tunnel

Select a secondary tunnel server from the dropdown. This tunnel will be used automatically if the primary tunnel becomes unreachable.

---

## Tunnel Stats

The stats table shows connection information for each tunnel socket:

| Column | Description |
|--------|-------------|
| **Socket** | The tunnel endpoint URL (highlighted if active) |
| **Disconnects** | Number of disconnections since client start |
| **Pool Size** | Connection pool size |
| **Connecting** | Number of connections being established |
| **Idle** | Number of idle connections |
| **Running** | Number of active connections |
| **Last Connection** | Timestamp of the last connection |
| **Last Active Check** | Timestamp of the last activity check |

!!! note
    Stats displayed on this page may be stale. Click **Update Backend** to refresh the data from the client.
