# Passthrough
!!! info
    This integration allows for notifications from custom scripts. This means you can create any script you want to run and add a webhook with the JSON payload below so you get notified about it.


By sending them through this integration you can keep track of how many it has sent, when the last one was, status code, etc

## Payload field breakdown
```
notification: {
    update: false, // Optional (Bool) - This is used to update an existing message with the same id, true will update existing & false will always post new
    name: "Local App", // Required (Str) - This is the name of the custom app/script, should be unique
    event: "0" // Optional (Str) - This is used to pass a unique id for this notification if necessary
},
discord: {
    color: "", // Optional (Str) - The color you want to use for the notification, 6 digit HTML color code
    ping: {
        pingUser: 123456789, // Optional (Int) - If you want to ping a user with this notification, add their discord id
        pingRole: 0 // Optional (Int) - If you want to ping a role with this notification, add the role discord id
    },
    images: {
        thumbnail: "http://website.com/image.png", //-- Optional (Str) - Add a valid URL to a thumbnail
        image: "http://website.com/image.png" //-- Optional (Str) - Add a valid URL to an image that will be on the bottom of the notification
    },
    text: {
        title: "Notification Title", // Optional (Str)
        icon: "http://website.com/image.png", // Optional (Str) - Add a valid URL
        content: "", //-- Optional - (Str) This text goes above the embed and is what is seen in toast notifications and wearables
        description: "", // Optional if fields is used (Str) - This text goes between the title and the embeds
        fields: [{ // Optional if description is used (List) - This is a list of items to put in the notification, 25 max fields allowed
            title: "Field",
            text: "Field Text",
            inline: false
        }, {
            title: "Field", // (Str)
            text: "Field Text", // (Str)
            inline: false // (Bool)
        }],
        footer: "Footer text" // Optional (Str)
    },
    ids: {
        channel: 1234567890 // Required (Int) - This is the channel to send the notification to on your server
    }
}
```

## Payload Example 1
- This would send a new notification
```
{
    "notification": {
        "update": false,
        "name": "1:1 App",
        "event": "12345"
    },
    "discord": {
        "color": "FFFFFF",
        "ping": {
            "pingUser": 0,
            "pingRole": 0
        },
        "images": {
            "thumbnail": "",
            "image": ""
        },
        "text": {
            "title": "Notification Title",
            "icon": "",
            "content": "Content of the notification here",
            "description": "Body of the notification here",
            "fields": [],
            "footer": "Footer Text"
        },
        "ids": {
            "channel": 735481457153277994
        }
    }
}
```

## Payload Example 2
- This would update an existing notification

```
{
    "notification": {
        "update": true,
        "name": "Update App",
        "event": ""
    },
    "discord": {
        "color": "000000",
        "ping": {
            "pingUser": 543077981707436033,
            "pingRole": 0
        },
        "images": {
            "thumbnail": "https://notifiarr.com/images/logo/notifiarr.png",
            "image": ""
        },
        "text": {
            "title": "Notification Title",
            "icon": "",
            "content": "Content of the notification here",
            "description": "Body of the notification here",
            "fields": [{
                "title": "Field Title",
                "text": "Inline true",
                "inline": true
            }, {
                "title": "Field Title",
                "text": "Inline true",
                "inline": true
            }, {
                "title": "Field Title",
                "text": "Inline false",
                "inline": false
            }],
            "footer": ""
        },
        "ids": {
            "channel": 735481457153277994
        }
    }
}
```

## Python example usage

```python
import json
import subprocess

NOTIFIARR_PY = '/path/to/notifiarr.py'

....

webhook = "python " + NOTIFIARR_PY + " -e \" Errors\" -c 631827062348512345 -m \"FFA500\" -t \"Error ("+ str(counter) +"/"+ str(totalErrors) +")\" -b \"URLs found with errors\" -g \"" + json.dumps(inlineFields).replace('"', r'\"') + "\" -f \"" + json.dumps(singleFields).replace('"', r'\"') + "\" -a \"https://notifiarr.com/images/logo/notifiarr.png\" -z \"Passthrough Integration\""
subprocess.call(webhook)
```

## Notifiarr script
- Can be called from any script (example above)
### Python
```python
import argparse
import json
import requests

#
# Example
# python notifiarr.py -e "System Backup" -c 735481457153277994 -m "FFA500" -t "Backup Failed" -f "[{\"Reason\": \"Permissions error\"}, {\"Severity\": \"Critical\"}]" -a "https://notifiarr.com/images/logo/notifiarr.png" -z "Passthrough Integration"
# python notifiarr.py -e "System Backup" -c 735481457153277994 -m "FFA500" -t "Backup Failed" -b "Critical permissions error" -a "https://notifiarr.com/images/logo/notifiarr.png" -z "Passthrough Integration"
#

# The apikey from Passthrough integration (located in Basic Instructions)
NOTIFIARR_APIKEY = ''

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Example: python notifiarr.py -e "System Backup" -c 735481457153277994 -m "FFA500" -t "Backup Failed" -f "[{\\"Reason\\": \\"Permissions error\\"}, {\\"Severity\\": \\"Critical\\"}]" -g "[{\\"Reason\\": \\"Permissions error\\"}, {\\"Severity\\": \\"Critical\\"}]" -a "https://notifiarr.com/images/logo/notifiarr.png" -z "Passthrough Integration"')
    parser.add_argument('-e', '--event', dest='event', help='notification type (rclone for example)', type=str, required=True, metavar='')
    parser.add_argument('-c', '--channel', dest='channel', help='valid discord channel id', type=int, required=True, metavar='')
    parser.add_argument('-t', '--title', dest='title', help='text title of message (rclone started for example)', type=str, required=True, metavar='')
    parser.add_argument('-b', '--body', dest='body', help='if fields is not used, text body for message', type=str, metavar='')
    parser.add_argument('-f', '--fields', dest='fields_not_inline', help='if body is not used, valid JSON list of fields [{title,text},{title,text}] max 25 list items (not inline)', type=str, metavar='')
    parser.add_argument('-g', '--inline', dest='fields_inline', help='if body is not used, valid JSON list of fields [{title,text},{title,text}] max 25 list items (inline)', type=str, metavar='')
    parser.add_argument('-z', '--footer', dest='footer', help='text footer of message', default='', type=str, metavar='')
    parser.add_argument('-a', '--avatar', dest='avatar', help='valid url to image', default='', type=str, metavar='')
    parser.add_argument('-i', '--thumbnail', dest='thumbnail', help='valid url to image', default='', type=str, metavar='')
    parser.add_argument('-m', '--color', dest='color', help='6 digit html code for the color', default='', type=str, metavar='')
    parser.add_argument('-u', '--ping-user', dest='ping_user', help='valid discord user id', default=0, type=int, metavar='')
    parser.add_argument('-r', '--ping-role', dest='ping_role', help='valid discord role id', default=0, type=int, metavar='')
    args = parser.parse_args()

    if not NOTIFIARR_APIKEY:
        raise Exception('ERROR: Edit the script and add your Notifiarr apikey')

    if not args.body and not args.fields_not_inline and not args.fields_inline:
        raise Exception('ERROR: Either -b/--body or -f/--fields or -g/--inline is required')

    inlineFields = []
    singleFields = []

    if args.fields_inline:
        inlineFields = [{'title': t, 'text': x, 'inline': True} for f in json.loads(args.fields_inline) for t, x in f.items()] if args.fields_inline else []

    if args.fields_not_inline:
        singleFields = [{'title': t, 'text': x, 'inline': False} for f in json.loads(args.fields_not_inline) for t, x in f.items()] if args.fields_not_inline else []

    fields = inlineFields + singleFields

    # BUILD THE TEMPLATE
    notifiarr_payload = {
        'notification': {
            'update': False,
            'name': args.event,
            'event': 0
        },
        'discord': {
            'color': args.color,
            'ping': {
                'pingUser': args.ping_user,
                'pingRole': args.ping_role
            },
            'images': {
                'thumbnail': args.thumbnail,
                'image': ''
            },
            'text': {
                'title': args.title,
                'icon': args.avatar,
                'content': '',
                'description': args.body,
                'fields': fields,
                'footer': args.footer
            },
            'ids': {
                'channel': args.channel
            }
        }
    }

    # PUSH THE WEBHOOK
    r = requests.post(f'https://notifiarr.com/api/v1/notification/passthrough/{NOTIFIARR_APIKEY}', data=json.dumps(notifiarr_payload), headers={'Content-type': 'application/json', 'Accept': 'text/plain'})
    #print(r.text)
```