# Client Reverse Proxy Configuration

!!! danger "Reverse Proxy Users"
      None of this is required or necessary. **We recommend NOT exposing your Notifiarr client to the Internet at all. In other words, don't do any of this.** But you can if you want to access your local Notifiarr Client from the internet

While you can certainly poke a hole your firewall and send the traffic directly to this app, it is recommended that you put it behind a reverse proxy if you're going to expose it. It's pretty easy.

- You'll want to tune the `upstreams` and `urlbase` client settings for your environment
    - If your reverse proxy IP is `192.168.3.45` then set `upstreams` in the Profile page of the local Notifiarr Client to `192.168.3.45/32`
- The `urlbase` on the local Notifiarr Client configuration page can be left at `/`, but change it if you serve this app from a subfolder like `/notifiarr`

## Cloudflare Users

Cloudflare Firewall / ZeroTrust users - See [this wiki entry](/Client/Client-Cloudflare) to ensure Notifiarr is allowed through Cloudflare

## NGINX Subfolder Example

- We'll assume you want to serve the client from `/notifiarr` and it's running on `127.0.0.1`
- Here's a sample nginx config to do that:

```nginx
# Notifiarr Client
location /notifiarr/api {
    deny all; # remove this line if you really want to expose the API.
    proxy_set_header X-Forwarded-For $remote_addr;
    set $notifiarr http://127.0.0.1:5454;
    proxy_pass $notifiarr$request_uri;
    auth_request off;
}

location /notifiarr {
    # <put proxy auth directives here> Optional:
    # proxy_set_header X-WebAuth-User $auth_user;
    proxy_set_header X-Forwarded-For $remote_addr;
    set $notifiarr http://127.0.0.1:5454;
    proxy_pass $notifiarr$request_uri;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection $http_connection;
    proxy_set_header Host $host;
}
```

Make sure the Nginx `location` path matches the `URL base` Notifiarr setting.
That's all there is to it.

## Reverse Proxy Authentication

!!! info
    If using Authelia or Organizr ensure they are passing the username header

There is working a SWAG example (with authelia, organizr, ldap) at the bottom of this page.

For example in NGINX: if `auth_user` is the variable your authentication app is passing (and it probably isn't) then your would need:

```nginx
proxy_set_header X-WebAuth-User $auth_user;
```

## Traefik

- If you are using Traefik, you **must** utilize a [plugin](https://github.com/tomMoulard/htransformation) to map the appropriate auth header.
- The below Traefik yaml created a middleware called `webauthheader` which maps Authelia's `Remote-User` header to Notifiarr's expected `X-WebAuth-User` header. You must then attach the `webauthheader` middleware to the Notifiarr client in Traefik.
- **Ensure you have configured the `/api` and `/plex` endpoints to bypass authentication.**

```yaml
http:
  middlewares:
    webauthheader:
      plugin:
        htransformation:
          Rules:
            - Name: 'Auth header rename'
              Header: 'Remote-User'
              Value: 'X-WebAuth-User'
              Type: 'Rename'
```

## NGINX Subdomain Example

- We'll assume you're running LSIO's SWAG [docker container](https://github.com/linuxserver/docker-swag)
- Non-SWAG users will need to update the file - including the `includes` as applicable

```nginx
## Version 2023/02/09
## TRaSH drop in for LSIO SWAG
## Originally from https://gist.github.com/TRaSH-/037235b0440b38c8964a2cbb64179cf3
## LSIO SWAG https://github.com/linuxserver/docker-swag

server {
    listen 443 ssl;
    listen [::]:443 ssl;

    server_name notifiarr.*;

    include /config/nginx/ssl.conf;
    include /config/nginx/proxy.conf;
    include /config/nginx/resolver.conf;

    client_max_body_size 0;

    # enable for ldap auth, fill in ldap details in ldap.conf
    #include /config/nginx/ldap.conf;

    # enable for Authelia
    #include /config/nginx/authelia-server.conf;

    set $upstream_app notifiarr;
    set $upstream_port 5454;
    set $upstream_proto http;
        
    location / {
        # enable the next two lines for http auth
        #auth_basic "Restricted";
        #auth_basic_user_file /config/nginx/.htpasswd;

        # enable the next two lines for organizr auth
        #include /config/nginx/orgauth.conf;
        #auth_request /organizr-auth/0;
        
        # enable the next two lines for ldap auth
        #auth_request /auth;
        #error_page 401 =200 /ldaplogin;

        # enable for Authelia
        #include /config/nginx/authelia-location.conf;

        proxy_set_header X-Forwarded-For $remote_addr;
        proxy_set_header X-WebAuth-User $auth_user;
        proxy_pass $upstream_proto://$upstream_app:$upstream_port;
    }
    
    # API path must not be protected by auth, authelia, ldap, etc.
    location ~ (/notifiarr)?/api {
	    	deny all; # remove this line if you really want to expose the API.
        proxy_set_header X-Forwarded-For $remote_addr;
        proxy_pass $upstream_proto://$upstream_app:$upstream_port;
    }
}
```

## Nginx Proxy Manager

- You will need a registered domain name with ddns services
- Add a subdomain thru aliases on your domain/ddns provider and point it to your external ip
- Add a proxy host in NPM

### Details Tab

1. Domain names: subdomain you just created
1. Scheme: `http`
1. Forwarded Hostname/IP: Your Internal LAN IP hosting Notifiarr E.g. `192.168.1.2`
1. Forward Port : The port Notifiarr is running on, default: `5454`
1. Check `Block common exploits`

### SSL Tab

1. Choose a certificate ( or make a fresh one pointing to your freshly made subdomain )
1. Check `Force SSL and HTTP/2 Support`
1. Save

You will need to use  Notifiarr Login/Password setup, not the webauth method with the above NPM configuration. See [Client UI](../../pages/client/gui.md) for more details

