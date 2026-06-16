---
icon: lucide/message-circle-code
tags:
    - Basics
---

# Chat formatting

Brickadia offers standard rich text support for formatting your messages in chat.

For reference, this is plain text:

```
Text
```

> **User:**{.font-rb .chat .username} <span class="font-rb chat">Text</span>

A preview of your text will show when you are formatting your chat message.

## :lucide-bold: Bold text

Add two asterisks on each side to make text bold in your message.

```
**Text**
```

> **User:**{.font-rb .chat .username} **Text**{.font-rb .chat}

## :lucide-italic: Italic text

Add just one asterisk on each side to italicize text in your message.

```
*Text*
```

> **User:**{.font-rb .chat .username} *Text*{.font-rb .chat}

## :lucide-underline: Underline text

Add 2 underscores on each side to underline text in your message.

```
__Text__
```

> **User:**{.font-rb .chat .username} <span class="font-rb chat"><u>Text</u></span>

## Mixed formatting

This section lists every possible combination of basic formatting in chat.

### Bold + italic

```
***Text***
```

> **User:**{.font-rb .chat .username} ***Text***{.font-rb .chat}

### Bold + underline

```
__**Text**__
```

> **User:**{.font-rb .chat .username} <span class="font-rb chat"><u><b>Text</b></u></span>

### Italic + underline

```
___Text___
```

> **User:**{.font-rb .chat .username} <span class="font-rb chat"><u><i>Text</i></u></span>

`__*Text*__` also works, but the above method is faster.

### Bold + italic + underline

```
___**Text**___
```

> **User:**{.font-rb .chat .username} <span class="font-rb chat"><b><u><i>Text</i></u></b></span>

`__***Text***__` also works.
This is up to your own preference.

## :lucide-link: Links

Anything that has `http://` or `https://` in front will be automatically turned into a link.

```
https://brickadia.com/
```

<span style="color: #00FFFF; text-decoration: underline dotted;" class="font-rb chat">https://brickadia.com/</span>

Additional formatting will not work for links.

## :lucide-smile: Emotes/Emoji

Add a colon on each side, around the name of an emote.

```
:bunny:
```

> **User:**{.font-rb .chat .username} ![Bunny emote](../../assets/media/essentials/chat/bunny-emote.webp){.img .borderless width="22" style="vertical-align: middle;" title="bunny"}

Unicode emotes do not currently work and appear as the unknown character symbol.

The smiley emote button **:material-emoticon-excited:**{.button .tiny} provides you the library of Brickadia Discord emotes for use.

!!! note

    The emote library of the Brickadia discord may change after a major update. Some emotes may not match between the game and the Dscord server.

## :lucide-code: Code

Add the grave accent on each side to turn normal text into monospaced text.
Used for when you need to specify code or commands.

```
`HighResShot 2`
```

> **User:**{.font-rb .chat .username} <span style="color: #bebebeff;" class="font-rbm chat">HighResShot 2</span>

Additional formatting will not work for code.
