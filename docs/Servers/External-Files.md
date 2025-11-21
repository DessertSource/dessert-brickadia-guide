---
icon: lucide/file-cog
tags:
    - Server Management
    - External Configuration
---

# External Server Files

This page refers to the configuration files that store information about
your server's parameters and settings. Note that you must have a text
editor to open these.

## Banlist.json

=== "Windows"

    This file is located in
    ```
	C:\Users\[username]\AppData\Local\Brickadia\Saved\Server\Banlist.json
	```

The ban list file is tied to in-server bans. In a text editor, it usually
looks like this:

``` json
{
	"banList":
	{
		"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx": // # (1)!
		{
			"bannerId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", // # (2)!
			"created": "2024.11.20-13.02.25", // # (3)!
			"expires": "2025.11.20-13.02.25",
			"reason": "Banned for a year" // # (4)!
		},
		"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx":
		{
			"bannerId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
			"created": "2025.11.20-13.05.16",
			"expires": "2025.11.20-13.04.16", // # (5)!
			"reason": "Severe rule-breaking violation"
		}
	}
}
```

1. This is the banned player's UUID.
2. This is the UUID of the player who banned the player above.
3. The initial ban date and the ban expiration date.
The dates are based on the year-month-day format, and they are
aligned to the GMT timezone (+/-0).
4. This is the ban reason.
5. For permanent bans, the expiration date and time goes backward.

## RoleAssignments.json

=== "Windows"

    This file is located in:

    ```
	C:\Users\[username]\AppData\Local\Brickadia\Saved\Server\RoleAssignments.json
	```

This file determines which players get which roles. In a text editor, it usually
looks like this:

``` json
{
    "savedPlayerRoles":
    {
        "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx": // # (1)!
        {
            "roles": [ // # (2)!
                "Admin"
            ]
        },
		"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx":
		{
            "roles": [
                "Moderator"
            ]
        },
		"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx":
		{
            "roles": [
                "Muted",
				"Building Blocked"
            ]
        }
    }
}
```

1. This is the player UUID the roles are attached to.
2. A list of all roles attached to this user. Remember that they are strings
referencing role names. Can have multiple roles at once.

If you find that suspicious activity has been occurring, you can do a full
deletion of someone's roles in the file. Remove everything related to the
problematic user(s).

## PlayerNameCache.json

=== "Windows"

    This file is located in:

    ```
	C:\Users\[username]\AppData\Local\Brickadia\Saved\Server\PlayerNameCache.json
	```

This file stores the names of all players who have joined your server,
including those who were only there during a short period of time.

Both the display name and the player name are saved for the same player UUID.

In a text editor, it usually looks like this:

``` json
{
	"savedPlayerNames": // # (1)!
	{
		"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx": "stereoboyy",
		"yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy": "woemoe"
	},
	"savedPlayerDisplayNames": // # (2)!
	{
		"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx": "Stereo Boy(2)",
		"yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy": "woemoe"
	}
}
```

1. Player names refer to unique player names. These cannot be the same
in anyway between player to player.
2. Display names are able to be the same amongst many players.

If players change their name, the names next to the UUID will reflect that.
There is no reason to modify or configure this file, as it only serves
as a useful reference for using commands on certain users.

## RoleSetup.json

=== "Windows"

    This file is located in:

    ```
	C:\Users\[username]\AppData\Local\Brickadia\Saved\Server\RoleSetup.json
	```

This file stores the permission states for each role in the server.

In a text editor, it usually looks like this:

``` json
{
	"roles": [
		{
			"name": "Moderator", // # (1)!
			"permissions": [],
			"color": // # (2)!
			{
				"b": 255,
				"g": 255,
				"r": 0,
				"a": 255
			},
			"bHasColor": true // # (3)!
		},
		{
			"name": "Admin", 
			"permissions": [
				{
					"name": "BR.Permission.AlwaysLeaveMinigame",
					"state": "Allowed" // # (4)!
				},
				// Many permissions later...
				{
					"name": "BR.Permission.TP.Others",
					"state": "Allowed"
				}
			],
			"color":
			{
				"b": 113,
				"g": 204,
				"r": 46,
				"a": 255
			},
			"bHasColor": true
		}
	"defaultRole": // # (5)!
	{
		"name": "Default",
		"permissions": [
			{
				"name": "BR.Permission.Building",
				"state": "Allowed"
			},
			// Many permissions later...
			{
				"name": "BR.Permission.TP",
				"state": "Allowed"
			}
		],
		"color":
		{
			"b": 0,
			"g": 255,
			"r": 255,
			"a": 255
		},
		"bHasColor": true
	},
	"ownerRoleColor": // # (6)!
	{
		"b": 0,
		"g": 50,
		"r": 255,
		"a": 255
	},
	"bOwnerRoleHasColor": true,  // # (7)!
	"version": "HierarchicalPermissionTags"
}
```

1. The name of the created role.
2. The color that will be applied to a player's name when *bHasColor* is true.
3. Determines if the role overrides player name color. If true, apply the color
parameter above. If false, leave the role colorless.
4. These are permission tags and their states.
5. The configuration for the default role. Deleting this will just make the
game recreate the role itself without a name and all permissions allowed.
6. The color of the owner's role.
7. Determines if the owner's role should have a different name color.

## GameUserSettings.ini

### Client

### Dedicated Server

``` ini
;METADATA=(Diff=true, UseCommands=true)
[Server__BRServerSettings_Color BRServerSettings_Color]
(Groups=((Colors=((B=255,G=255,R=255,A=255),(B=184,G=184,R=184,A=255),(B=136,G=136,R=136,A=255),(B=114,G=114,R=114,A=255),(B=90,G=90,R=90,A=255),(B=57,G=57,R=57,A=255),(B=35,G=35,R=35,A=255),(B=24,G=24,R=24,A=255),(B=17,G=17,R=17,A=255),(B=6,G=6,R=6,A=255),(B=2,G=2,R=2,A=255),(B=0,G=0,R=0,A=255)),Name="Grayscale"),(Colors=((B=9,G=5,R=87,A=255),(B=6,G=6,R=235,A=255),(B=3,G=29,R=255,A=255),(B=6,G=73,R=246,A=255),(B=6,G=157,R=235,A=255),(B=4,G=164,R=61,A=255),(B=5,G=139,R=9,A=255),(B=255,G=16,R=3,A=255),(B=255,G=244,R=12,A=255),(B=85,G=35,R=163,A=255),(B=72,G=8,R=48,A=255),(B=49,G=6,R=14,A=255)),Name="Plastic"),(Colors=((B=25,G=25,R=41,A=255),(B=73,G=71,R=96,A=255),(B=134,G=131,R=181,A=255),(B=27,G=44,R=45,A=255),(B=65,G=109,R=114,A=255),(B=100,G=139,R=144,A=255),(B=28,G=45,R=27,A=255),(B=68,G=114,R=65,A=255),(B=103,G=144,R=100,A=255),(B=41,G=39,R=30,A=255),(B=96,G=92,R=71,A=255),(B=181,G=171,R=131,A=255)),Name="Metallic"),(Colors=((B=2,G=5,R=23,A=255),(B=5,G=16,R=90,A=255),(B=1,G=20,R=77,A=255),(B=7,G=30,R=77,A=255),(B=18,G=60,R=144,A=255),(B=62,G=104,R=166,A=255),(B=78,G=159,R=255,A=255),(B=78,G=121,R=255,A=255),(B=13,G=20,R=50,A=255),(B=3,G=12,R=21,A=255),(B=13,G=33,R=51,A=255),(B=58,G=163,R=194,A=255)),Name="Earthy"),(Colors=((B=1,G=2,R=19,A=255),(B=1,G=4,R=73,A=255),(B=18,G=23,R=190,A=255),(B=53,G=59,R=190,A=255),(B=156,G=149,R=255,A=255),(B=38,G=79,R=255,A=255),(B=2,G=41,R=255,A=255),(B=27,G=54,R=171,A=255),(B=5,G=64,R=109,A=255),(B=8,G=99,R=171,A=255),(B=11,G=146,R=255,A=255),(B=47,G=175,R=255,A=255)),Name="Warm"),(Colors=((B=1,G=37,R=22,A=255),(B=12,G=80,R=67,A=255),(B=30,G=144,R=122,A=255),(B=81,G=255,R=101,A=255),(B=47,G=204,R=13,A=255),(B=0,G=77,R=0,A=255),(B=11,G=54,R=11,A=255),(B=3,G=30,R=5,A=255),(B=5,G=18,R=5,A=255),(B=27,G=43,R=8,A=255),(B=53,G=96,R=9,A=255),(B=66,G=146,R=8,A=255)),Name="Nature"),(Colors=((B=17,G=13,R=5,A=255),(B=44,G=30,R=11,A=255),(B=64,G=34,R=1,A=255),(B=122,G=65,R=0,A=255),(B=200,G=118,R=8,A=255),(B=171,G=152,R=5,A=255),(B=163,G=147,R=80,A=255),(B=255,G=250,R=134,A=255),(B=242,G=119,R=86,A=255),(B=235,G=55,R=37,A=255),(B=156,G=25,R=12,A=255),(B=44,G=4,R=1,A=255)),Name="Cool"),(Colors=((B=30,G=0,R=8,A=255),(B=57,G=0,R=18,A=255),(B=100,G=19,R=56,A=255),(B=255,G=45,R=141,A=255),(B=255,G=93,R=255,A=255),(B=255,G=149,R=253,A=255),(B=116,G=58,R=255,A=255),(B=55,G=18,R=91,A=255),(B=255,G=24,R=255,A=255),(B=55,G=0,R=255,A=255),(B=29,G=0,R=127,A=255),(B=55,G=0,R=55,A=255)),Name="Neon")),Description="The default palette.")

[Server__BP_ServerSettings_General_C BP_ServerSettings_General_C]
ServerTypeIndex2=1
ServerName=Brickadia Server
ServerDescription=greatest server on earth
ServerPassword=this-is-not-a-real-password
MaxPlayers=4
bPubliclyListed=True
WelcomeMessage="<color=\"0055ff\">Welcome to <b>{2}</>, {1}.</>"
bGlobalRulesetSelfDamage=True
bGlobalRulesetPhysicsDamage=False
bGlobalRulesetEnableCameraBlockedEffects=False
UploadTimeout=5.000000
MaxPrefabBricks=1000
MaxPrefabComponents=20
MaxPrefabSize=(X=1000,Y=1000,Z=1000)
MaxPhysicsObjects=2000
MaxPhysicsObjectsPerUser=50
MaxPlacementBricks=2000
MaxPlacementEntities=10
bEnforceApplicatorLimits=False
TemplatePlacementTimeout=2.000000
MaxSelectionBoxSize=(X=1000,Y=1000,Z=1000)
MaxSelectedBricks=1000
SelectionTimeout=2.000000
```
