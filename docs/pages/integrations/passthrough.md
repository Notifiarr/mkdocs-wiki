# Passthrough

!!! info
    This integration allows for notifications from custom scripts. This means you can create any script you want to run and add a webhook with the JSON payload below so you get notified about it.

By sending them through this integration you can keep track of how many it has sent, when the last one was, status code, etc

![passthrough.png](../../assets/screenshots/integrations/passthrough/passthrough.png)

## Payload field breakdown

```json
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

```json
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

```json
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

## Python Example Usage

```python
import json
import subprocess

NOTIFIARR_PY = '/path/to/notifiarr.py'

....

webhook = "python " + NOTIFIARR_PY + " -e \" Errors\" -c 631827062348512345 -m \"FFA500\" -t \"Error ("+ str(counter) +"/"+ str(totalErrors) +")\" -b \"URLs found with errors\" -g \"" + json.dumps(inlineFields).replace('"', r'\"') + "\" -f \"" + json.dumps(singleFields).replace('"', r'\"') + "\" -a \"https://notifiarr.com/images/logo/notifiarr.png\" -z \"Passthrough Integration\""
subprocess.call(webhook)
```

## Powershell Example Usage

```powershell
$payload = @{
    notification = @{
        update = $false
        name = "My Notifiarr App"
        event = "0"
    }
    discord = @{
        color = "00FF00"
        ping = @{
            pingUser = $PING_USER_ID # Replace with your Discord user ID
            pingRole = $PING_ROLE_ID # Replace with your Discord role ID
        }
        images = @{
            thumbnail = "https://gh.notifiarr.com/images/icons/notifiarr.png"
            image = "https://gh.notifiarr.com/images/icons/notifiarr.png"
        }
        text = @{
            title = "My Notifiarr Title"
            icon = "https://gh.notifiarr.com/images/icons/notifiarr.png"
            content = "My Notifiarr Content"
            description = "My Notifiarr Description"
            fields = @(
            @{ title = 'Field 1'
                text = 'This is a normal field'
                inline = $false
                }
            @{ title = 'Field 2'
                text = 'This is an inline field'
                inline = $true
                }
            @{ title = 'Field 3'
                    text = "* **This**
                        * *is*
                            * ~~a~~
                                * __*Markdown*__
                                    * ~~*field*~~"
                inline = $false
                }
            )
            footer = "My Notifiarr Footer Text"
        }
        ids = @{
            channel = $DISCORD_CHANNEL_ID # Replace with your Discord channel ID
        }
    }
}

    $jsonPayload = $payload | ConvertTo-Json -Depth 10 -Compress

    $params = @{
        Uri = "https://notifiarr.com/api/v1/notification/passthrough/$NOTIFIARR_APIKEY" # Replace with your Notifiarr API key
        Method = "POST"
        Body = $jsonPayload
        ContentType = "application/json"
        Headers = @{
            "Accept" = "text/plain"
        }
    }

    $response = Invoke-RestMethod @params

    if ($request.details.response -eq 'Pass through payload processed.'){
        Write-Host "Notification sent successfully!" -ForegroundColor Green
    } else {
        Write-Warning "Failed to send notification."
        Write-Host "Response: $($response.result.details)"
    }
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

### Powershell

- This is a sample function meant to be reused in one or more scripts. It allows you to send payload fields as parameters, and it will build the payload for you.
- It contains a helper function to validate the fields you pass in, and it will throw an error if they are not valid.

```powershell
function Send-NotifiarrPassthroughNotification {
    <#
    .SYNOPSIS
    Sends a Discord notification using a third-party passthrough integration.

    .DESCRIPTION
    This function sends a Discord notification by constructing the payload and sending it to the specified API endpoint.
    It validates high-level parameters and constructs the notification payload with appropriate formatting.
    The function supports a wide range of customization options including colors, fields, images, and user mentions.

    .PARAMETER AppName
    The name of the custom app/script that is sending the notification. Should be unique and non-empty.

    .PARAMETER ChannelId
    The Discord channel ID to send the notification to. Must be a numeric string.

    .PARAMETER Color
    The color of the notification embed. Can be a predefined name ("Success", "Warning", "Error") or a custom HEX color code without the # prefix.

    .PARAMETER Content
    Content text that appears above the embed and is seen in toast notifications.

    .PARAMETER Description
    The description text of the notification embed. Supports Discord markdown formatting.

    .PARAMETER Event
    A unique event ID for the notification. Used for message deduplication or tracking.

    .PARAMETER Footer
    The footer text to display at the bottom of the notification embed.

    .PARAMETER Fields
    A hashtable or array of hashtables representing fields to include in the notification embed.
    Each field must have 'title', 'text', and 'inline' keys. Maximum of 25 fields allowed.

    .PARAMETER Icon
    The URL of the icon to display in the notification. Must be a valid HTTP/HTTPS URL.

    .PARAMETER ImageUrl
    The URL of the main image to display in the notification embed. Must be a valid HTTP/HTTPS URL.

    .PARAMETER PingRole
    The Discord role ID to ping with the notification. Must be a numeric string.

    .PARAMETER PingUser
    The Discord user ID to ping with the notification. Must be a numeric string.

    .PARAMETER ThumbnailUrl
    The URL of the thumbnail image to display in the notification embed. Must be a valid HTTP/HTTPS URL.

    .PARAMETER Title
    The title of the notification embed.

    .PARAMETER Update
    Whether to update an existing message with the same ID instead of sending a new one. Defaults to $false.

    .PARAMETER WebhookUrl
    The API endpoint URL to send the notification to. Must be a valid HTTP/HTTPS URL.

    .OUTPUTS
    [PSCustomObject] An object with Status, Message, and ErrorDetail properties indicating the result of the operation.

    .EXAMPLE
    Send-NotifiarrPassthroughNotification -AppName "Monitoring" -ChannelId "123456789012345678" -WebhookUrl "https://api.example.com/webhook" -Title "Alert" -Description "System is running low on disk space" -Color "Warning"

    .EXAMPLE
    $fields = @(
        @{ title = "Server"; text = "PROD-WEB01"; inline = $true },
        @{ title = "Status"; text = "Online"; inline = $true }
    )
    Send-NotifiarrPassthroughNotification -AppName "StatusChecker" -ChannelId "123456789012345678" -WebhookUrl "https://api.example.com/webhook" -Fields $fields -Color "Success"

    .LINK
    https://notifiarr.wiki/en/Website/Integrations/Passthrough

    .NOTES
    This function cleans up sensitive information from memory after execution for security.
    #>
    [CmdletBinding(SupportsShouldProcess)]
    [OutputType([PSCustomObject])]
    param (
        [Parameter(Mandatory = $true, Position = 0)]
        [ValidateNotNullOrEmpty()]
        [string]
        $AppName,

        [Parameter(Mandatory = $true)]
        [ValidateNotNullOrEmpty()]
        [ValidatePattern('^\d+$')]
        [string]
        $ChannelId,

        [Parameter(Mandatory = $false)]
        [string]
        $Color,

        [Parameter(Mandatory = $false)]
        [string]
        $Content,

        [Parameter(Mandatory = $false)]
        [string]
        $Description,

        [Parameter(Mandatory = $false)]
        [string]
        $Event,

        [Parameter(Mandatory = $false)]
        [string]
        $Footer,

        [Parameter(Mandatory = $false)]
        [object]
        $Fields,

        [Parameter(Mandatory = $false)]
        [ValidatePattern('^https?://.+')]
        [string]
        $Icon,

        [Parameter(Mandatory = $false)]
        [ValidatePattern('^https?://.+')]
        [string]
        $ImageUrl,

        [Parameter(Mandatory = $false)]
        [ValidatePattern('^\d+$')]
        [string]
        $PingRole,

        [Parameter(Mandatory = $false)]
        [ValidatePattern('^\d+$')]
        [string]
        $PingUser,

        [Parameter(Mandatory = $false)]
        [ValidatePattern('^https?://.+')]
        [string]
        $ThumbnailUrl,

        [Parameter(Mandatory = $false)]
        [string]
        $Title,

        [Parameter(Mandatory = $false)]
        [bool]
        $Update = $false,

        [Parameter(Mandatory = $true)]
        [ValidatePattern('^https?://.+')]
        [string]
        $WebhookUrl
    )

    begin {
        # Initialize tracking variables for payload construction
        $processedColor = $null
        $validatedFields = $null

        # Initialize the result object with properties for standardized returns
        $result = [PSCustomObject]@{
            Status      = $null
            Message     = $null
            ErrorDetail = $null
        }

        # Map predefined color names to HEX codes for easier user experience
        $colorMap = @{
            Success = "00FF00" # Green
            Warning = "FFFF00" # Yellow
            Error   = "FF0000" # Red
        }

        # Build the base notification payload structure with required elements
        $payload = @{
            notification = [ordered]@{
                update = $Update
                name   = $AppName
            }
            discord      = [ordered]@{
                ids = @{
                    channel = $ChannelId
                }
            }
        }
    }

    process {
        if ($PSCmdlet.ShouldProcess("Discord Channel ID: $ChannelId", "Send Notification")) {
            try {
                # Process and validate fields if provided
                if ($PSBoundParameters.ContainsKey('Fields')) {
                    Write-Verbose "Fields parameter was provided, performing validation."
                    if ($Fields -is [hashtable]) {
                        Write-Verbose "Fields parameter is a single hashtable, converting to array."
                        $Fields = @($Fields)
                    }
                    $validatedFields = Confirm-NotifiarrPassthroughFields -Fields $Fields
                }

                # Process color parameter if provided
                if ($PSBoundParameters.ContainsKey('Color')) {
                    Write-Verbose "Color parameter was provided."
                    if ($colorMap.ContainsKey($Color)) {
                        Write-Verbose "Using predefined color: $Color."
                        $processedColor = $colorMap[$Color]
                    }
                    elseif ($Color -match '^[0-9A-Fa-f]{6}$') {
                        Write-Verbose "Using custom HEX color: $Color."
                        $processedColor = $Color
                    }
                    else {
                        Write-Verbose "Invalid color format: '$Color'. Using default (null)."
                    }
                }

                # Add optional notification parameters
                if ($PSBoundParameters.ContainsKey('Event')) {
                    $payload.notification['event'] = $Event
                }

                # Build discord object sections
                # Add color if specified
                if ($processedColor) {
                    $payload.discord['color'] = $processedColor
                }

                # Add ping object if any ping parameters are specified
                if ($PSBoundParameters.ContainsKey('PingUser') -or $PSBoundParameters.ContainsKey('PingRole')) {
                    $payload.discord['ping'] = @{}

                    if ($PSBoundParameters.ContainsKey('PingUser')) {
                        $payload.discord.ping['pingUser'] = $PingUser
                    }
                    if ($PSBoundParameters.ContainsKey('PingRole')) {
                        $payload.discord.ping['pingRole'] = $PingRole
                    }
                }

                # Add images object if any image parameters are specified
                if ($PSBoundParameters.ContainsKey('ThumbnailUrl') -or $PSBoundParameters.ContainsKey('ImageUrl')) {
                    $payload.discord['images'] = @{}
                    if ($PSBoundParameters.ContainsKey('ThumbnailUrl')) {
                        $payload.discord.images['thumbnail'] = $ThumbnailUrl
                    }
                    if ($PSBoundParameters.ContainsKey('ImageUrl')) {
                        $payload.discord.images['image'] = $ImageUrl
                    }
                }

                # Build text object with all text-related parameters
                $text = @{}
                if ($PSBoundParameters.ContainsKey('Title')) {
                    Write-Verbose "Adding title parameter to text object."
                    $text['title'] = $Title
                }
                if ($PSBoundParameters.ContainsKey('Icon')) {
                    Write-Verbose "Adding icon parameter to text object."
                    $text['icon'] = $Icon
                }
                if ($PSBoundParameters.ContainsKey('Content')) {
                    Write-Verbose "Adding content parameter to text object."
                    $text['content'] = $Content
                }
                if ($PSBoundParameters.ContainsKey('Description')) {
                    Write-Verbose "Adding description parameter to text object."
                    $text['description'] = $Description
                }
                if ($validatedFields) {
                    Write-Verbose "Adding fields parameter to text object."
                    $text['fields'] = @($validatedFields)
                }
                if ($PSBoundParameters.ContainsKey('Footer')) {
                    Write-Verbose "Adding footer parameter to text object."
                    $text['footer'] = $Footer
                }

                # Add text object if any text parameters were specified
                if ($text.Count -gt 0) {
                    $payload.discord['text'] = $text
                }

                # Convert the payload to JSON for transmission
                $jsonPayload = $payload | ConvertTo-Json -Depth 10 -Compress

                $jsonPayload

                Write-Verbose "Sending payload to webhook: $WebhookUrl"

                # Send the notification via REST API
                $response = Invoke-RestMethod -Uri $WebhookUrl -Method Post -Body $jsonPayload -ContentType 'application/json' -StatusCodeVariable 'statusCode' -ErrorAction Stop -SkipHttpErrorCheck

                # Process the API response and update result object
                if ($response.result -ne 'success') {
                    $result.Status = $false
                    $result.Message = "Failed to send notification: $($response.reason)"
                    $result.ErrorDetail = $response | ConvertTo-Json -Compress
                    Write-Warning "$($MyInvocation.MyCommand.Name) - Failed to send notification."
                }
                else {
                    $result.Status = $true
                    $result.Message = $response.details
                    Write-Verbose "$($MyInvocation.MyCommand.Name) - Notification sent successfully."
                }
            }
            catch {
                # Handle errors and populate the result object with error details
                $result.Status = $false
                $result.Message = "Failed to send notification due to an exception"
                $result.ErrorDetail = $_.Exception.Message

                Write-Warning "$($MyInvocation.MyCommand.Name) - Failed to send notification"
            }
        }
    }

    end {
        $result
    }
}

function Confirm-NotifiarrPassthroughFields {
    <#
    .SYNOPSIS
    Validates field objects for Discord notifications.

    .DESCRIPTION
    This function validates that each field in the provided array meets the requirements for Discord notification fields.
    Each field must be a hashtable with 'title', 'text', and 'inline' keys. The function ensures that there are no more than 25 fields
    and that each field contains properly typed values.

    .PARAMETER Fields
    An array of hashtables, each representing a field with 'title' (string), 'text' (string), and 'inline' (boolean) keys.
    Maximum of 25 fields are allowed per Discord API limitations.

    .OUTPUTS
    [array] The validated fields array, unchanged if all validation passes.

    .EXAMPLE
    $fields = @(
        @{ title = "Field 1"; text = "Field 1 Text"; inline = $false },
        @{ title = "Field 2"; text = "Field 2 Text"; inline = $true }
    )
    $validatedFields = Confirm-NotifiarrPassthroughFields -Fields $fields

    .NOTES
    This function performs strict validation and will throw exceptions for any validation failures.
    #>
    [CmdletBinding()]
    [OutputType([array])]
    param (
        [Parameter(Mandatory = $true)]
        [array]
        $Fields
    )

    # Ensure the fields array does not exceed Discord's maximum limit of 25 items
    if ($Fields.Count -gt 25) {
        throw "The fields array cannot contain more than 25 items."
    }

    # Validate each field in the array meets all requirements
    for ($i = 0; $i -lt $Fields.Count; $i++) {
        $field = $Fields[$i]

        # Ensure the field is a hashtable as required for proper processing
        if (-not ($field -is [hashtable])) {
            throw "Field #$($i + 1) must be a hashtable."
        }

        # Check for the presence of the 'title' key and validate its type
        if (-not $field.ContainsKey('title')) {
            throw "Field #$($i + 1) is missing the 'title' key."
        }
        if (-not ($field.title -is [string])) {
            throw "Field #$($i + 1) has an invalid 'title'. Expected a string but found $($field.title.GetType().Name)."
        }

        # Check for the presence of the 'text' key and validate its type
        if (-not $field.ContainsKey('text')) {
            throw "Field #$($i + 1) is missing the 'text' key."
        }
        if (-not ($field.text -is [string])) {
            throw "Field #$($i + 1) has an invalid 'text'. Expected a string but found $($field.text.GetType().Name)."
        }

        # Check for the presence of the 'inline' key and validate its type
        if (-not $field.ContainsKey('inline')) {
            throw "Field #$($i + 1) is missing the 'inline' key."
        }
        if (-not ($field.inline -is [bool])) {
            throw "Field #$($i + 1) has an invalid 'inline'. Expected a boolean but found $($field.inline.GetType().Name)."
        }
    }

    # Always return a proper array, even if only one element
    if ($Fields.Count -eq 1) {
        # Force return as array with only one element
        @($Fields[0])
    }
    else {
        # Return the validated fields array - no modification needed if validation passed
        $Fields
    }
}

    # Initialize notification parameters with standard values
    $notificationParams = @{
        AppName      = 'My Notifiarr App'
        ChannelId    = 1234567891011121314 # Replace with your Discord channel ID
        Color = 'Success'
        Content = 'My Notifiarr Content'
        Description = 'My Notifiarr Description'
        Footer       = "My Notifiarr Footer Text"
        Fields = @(
            @{ title = 'Field 1'
                text = 'This is a normal field'
                inline = $false
                }
            @{ title = 'Field 2'
                text = 'This is an inline field'
                inline = $true
                }
            @{ title = 'Field 3'
                    text = "* **This**
                        * *is*
                            * ~~a~~
                                * __*Markdown*__
                                    * ~~*field*~~"
                inline = $false
                }
        )
        Icon         = 'https://gh.notifiarr.com/images/icons/notifiarr.png'
        ImageUrl     = 'https://gh.notifiarr.com/images/icons/notifiarr.png'
        PingRole     = 1234567891011121314 # Replace with your Discord role ID
        PingUser     = 1234567891011121314 # Replace with your Discord user ID
        ThumbnailUrl = "https://gh.notifiarr.com/images/icons/notifiarr.png"
        Title        = 'My Notifiarr Title'
        WebhookUrl   = "https://notifiarr.com/api/v1/notification/passthrough/$NOTIFIARR_APIKEY" # Replace with your Notifiarr API key
    }

        # Send the notification using the function
        $result = Send-NotifiarrPassthroughNotification @notificationParams

        # Check the result and take action based on success or failure
        if ($result.Status) {
            Write-Host "Notification sent successfully!"
        }
        else {
            Write-Warning "Failed to send notification: $($result.Message)"
            if ($result.ErrorDetail) {
                Write-Warning "Error details: $($result.ErrorDetail)"
            }
        }
```
