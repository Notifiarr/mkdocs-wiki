# Fail2ban

- To make setup easier; set the following variables

## Variables

```bash
F2BAPI_KEY="your_notifiarr_api_key_here"
F2B_HOST="$(hostname)"
```

## Instructions

1. **Open a shell** on the server where Fail2ban is installed.

2. **Change to the Fail2ban actions directory.**
   Adjust the path if your installation is different.

   ```bash
   cd /etc/fail2ban/action.d/
   ```

3. **Download the Notifiarr Fail2ban action file.**

   ```bash
   curl -o notifiarr.conf https://notifiarr.com/scripts/fail2ban/notifiarr.conf
   ```

4. **Configure the Notification - Option A: Edit the `notifiarr.conf` file and update the hostname and API key.**

   ```bash
   nano notifiarr.conf
   ```

5. **Configure the Notification - Option B: Use sed to Update the hostname and API key:**

     ```bash
     # Replace `YOUR_SERVERNAME_HERE` with your server's hostname:
     sed -i "s/YOUR_SERVERNAME_HERE/${F2B_HOST}/g" notifiarr.conf
     # Replace `YOUR_NOTIFIARR_API_KEY_HERE` with your API key:
     sed -i "s/YOUR_NOTIFIARR_API_KEY_HERE/${F2BAPI_KEY}/g" notifiarr.conf
     ```

6. **Configure your `jail.local` file:**

   Open your jail configuration:

   ```bash
   nano /etc/fail2ban/jail.local
   ```

   Add `notifiarr` as an action to the relevant jails or default settings:

   ```text
   action = notifiarr[bantime="%(bantime)s", port="%(port)s", protocol="%(protocol)s"]
   ```

7. **Restart Fail2ban to apply the changes.**

   ```bash
   fail2ban-client restart
   ```
