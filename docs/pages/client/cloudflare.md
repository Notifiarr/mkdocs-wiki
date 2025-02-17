# Notifiarr Client - Cloudflare Configuration

> None of this is required or necessary. **We recommend NOT exposing your 
Notifiarr client to the Internet at all. In other words, don't do any of this.** But you can if you want to access your local Notifiarr Client from the internet
{.is-danger}

Many users use Cloudflare's "Cloudflare Tunnel" feature or additional Cloudflare security features to provide / protect external access to their Notifiarr Client box.  Specific configuration required for Cloudflare's various options are detailed below.

- [Cloudflare Tunnel](#cloudflare-tunnel)
- [Cloudflare Web Access Firewall (WAF)](#waf-rule)
- [Notifiarr Site Access Only](#increased-security)
{.links-list}

## Cloudflare Tunnel

> This assumes that you already have a Cloudflare Tunnel set up on your system. If you want to get started with Cloudflare Tunnels follow this YouTube guide first: [Cloudflare Tunnel: Creating Tunnels via GUI - Bypass CG-NAT
 by IBRACORP](https://www.youtube.com/watch?v=RUJy9fjoiy4)
{.is-info}

1. Login to your Cloudflare teams account at [dash.teams.Cloudflare.com](https://dash.teams.Cloudflare.com/)
1. Click **Tunnels** and then **configure** next to the Cloudflare Tunnel you would like to use
![cf-tunnel-configure_sm2.png](/faq/cf-tunnel-configure_sm2.png)
1. In your Tunnel section click on **Public Hostname** and add a new hostname by clicking on **Add a public hostname**
![cf-tunnel-configure_publichostname.png](/faq/cf-tunnel-configure_publichostname.png)
1. Fill in the public hostname information

- `Subdomain`: Notifiarr (or whatever else you want it to be)
- `Domain`: choose one of your domains
- `Service`: HTTP + Your Local IP Address for Notifiarr
![cf-tunnel-configure_hostnamepage.png](/faq/cf-tunnel-configure_hostnamepage.png)

1. Save Hostname

That's it! Your client is now exposed to the internet!
