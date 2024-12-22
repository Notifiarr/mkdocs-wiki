---
title: API Errors
description: 
published: true
date: 2023-07-26T22:37:37.535Z
tags: 
editor: markdown
dateCreated: 2022-02-02T03:47:09.185Z
---

# API Error Help

## 5**

Cloudflare issues, try again and it will go away

## 401

You have an invalid apikey.

- Check that when you copy and pasted it you did not copy extra spaces
- Make sure you do not have an ENV variable set that is incorrect since that overrides the conf file
- Make sure if it is an integration specific key that it is the correct integration you are using it for

## 400

### Network Integration Disabled

If you see this in your log file it means you have something in the local notifiarr client that is trying to send a service check but you do not have the integration enabled. Your options are:

1. Change the interval setting in the local client to disabled and it will not up check the service
2. Enable the Network integration on the notifiarr website and pick a channel so you can be informed when things are down
