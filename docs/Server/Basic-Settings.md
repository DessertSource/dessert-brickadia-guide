---
icon: lucide/square-menu
tags:
    - Server Management
---

# Basic Server Settings

These are simple settings that you can set up your server easily with.
Players are able to change these
settings on a simple click.

While changes like the password and player limit are instant, the server
name and description may take a while to update, as the game only pings
the master server between periods of time.

!!! note

    The server name and description is subject to global moderation when
    running a *PUBLIC* server. Do not put anything in these boxes that are 
    suggestive or offensive. While this won't ban you from playing the game,
    it may get your server blacklisted from the server browser.

    You may contact BrickBot on the official Discord if you are in doubt
    about your server name or description breaking any rules. It wastes
    no more time than if you were to DM the moderators who are better
    reached by the bot, as you will contribute to mixing professional
    and personal private messages on their behalf.

## Server Name

Server name that will be mostly displayed upon hosting a public server.
Does not support formatting, only plain text is allowed. 

It is not necessary to include your name in the server name, unless you
have enlisted someone else to host for you in their name. The game logs
by default who is hosting the server as a statistic.

For example, if *Dessert* wants to run a dedicated server under their name,
but they don't have the capability to do so... they start contacting their
friend *Source* for help. On the server browser, it says
"*Dessert's Candy Land*" as the name, with the text "hosted by *Source*".

## Description

Description of what your server offers.
Does not support formatting, only plain text is allowed.
You can make it as long or as brief as you'd like, but be careful about
making it long as it cuts off at a certain point in the server browser.

## Player Limit

Total amount of players that can be online at once in your server. Includes
multiple instances of one person running Brickadia. Maximum player limit is 30.

It is not recommended to edit the player limit externally beyond 30, as it is
currently unsupported and problems may arise from pushing the hard player limit.

## Password

Server password. This is enforced upon other players who try to join your server.

As such, if your server is private for one reason or another, it is a good idea
to make your password:

* :lucide-case-upper: Include uppercase characters (A, B, C...)
* :lucide-case-lower: Include lowercase characters (a, b, c...)
* :lucide-arrow-down-0-1: Include numbers (0, 1, 2...)
* :lucide-dollar-sign: Include symbols (@, #, $...)
* :lucide-ruler-dimension-line: Has a length of 12 or more characters

...all at once. Leaving your password simple may leave your server
password vulnerable to brute force in particular.

!!! danger "And this has to be said..."

    Please do not make this the same password you sign in with on any
    other account. Make them all different if you have not done that.
    Trust me, you will save a lot of time spent on getting support
    to retrieve your accounts from exploits or [social engineering](https://en.wikipedia.org/wiki/Social_engineering_(security)).

It is not required to follow these basic guidelines of making a
password, but if you are creating a world that involves multiple people for
playtesting purposes, it is recommended to do so.

## Server Type

This is available when starting a game.

There are three kinds of servers you can run in the game.

* :lucide-user: **Single Player:** Runs a single player session.
* :lucide-user-plus: **Unlisted:** This will run a server, but it will not
be listed  on the global server browser. Great for doing multiplayer with share
codes only without having to send any kind of password.
* :lucide-users: **Public:** This will run a server that will be listed on 
the global server browser.

The server will stop running if you quit Brickadia. For permanent servers,
consult the [Dedicated Servers]() section.
