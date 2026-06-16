---
icon: lucide/message-circle-more
tags:
    - Essentials
    - Chat
    - Social
---

# Chat

To get started with chat, press ++t++ to start typing your message.

![Typing hello world in chat](../../assets/media/essentials/chat/chat-type.png)

You can format your chat messages to add bold, italic or underlined text. Everything you need to know about chat formatting is available in this page: [:lucide-message-circle-code: Chat Formatting](./chat-formatting.md).

![Formatting the word "world" to be bold](../../assets/media/essentials/chat/chat-formatting-preview.png)

Once you finish typing your message, you can now press ++enter++, which sends your message to the server chat.

![User with the name Dessert with the message "Hello World!" attached](../../assets/media/essentials/chat/chat-user.png)

The name colors of chat indicates the highest role (with a role color set) that the player has. Roles have varying colors.

## Commands

You can also execute a variety of commands through chat.
All you have to do is start with a slash.

When you send a command to the chat, it will execute certain functions in the server or on your client.

Type `/help` for a list of executable commands, which can be found here: [:lucide-terminal: Chat Commands](./chat-commands.md).

!!! note

    Some chat commands may be admin only. Check your permissions.

Sending a command will not trigger the typing indicator.

## Typing indicator

![Chat indicator](../../assets/media/essentials/chat/chat-indicator.png)

This will appear above the chat if you, someone else or a group of people are typing, which can be nice to have when you want to know if you're talking over someone or queue your message later.

If there are too many people typing at once, the game will count the total amount of people typing for you and show that instead.

This will not apply to commands.
The game detects when you start a command using a slash.

## Chat bubbles

![Chat bubble](../../assets/media/essentials/chat/chat-bubble.png)

A chat bubble will appear temporarily above another player's head when they send a message.

## Chat in free mouse mode

Entering free mouse mode using ++m++ lets you do the following:

Selecting text directly in the input box when you type into chat:

![Selecting text in chat](../../assets/media/essentials/chat/chat-select.png)

Accessing emotes with the smiley emote button **:material-emoticon-excited:**{.button .tiny}:

![Chat emotes menu](../../assets/media/essentials/chat/chat-emotes.png)

## Scrolling chat

![Scrolling chat](../../assets/media/essentials/chat/chat-scroll.png)

You can scroll up/down the chat if the conversation is too fast for you.

- ++page-up++ to scroll up the chat.
- ++page-dn++ to scroll down the chat when you are done.

Note that you will only be able to read your own chat history, so it can only go so far back to the moment you joined each server in a single session.

Tired of scrolling the chat and just want to get to the start or end quickly?

- Hold ++lctrl++ and press ++page-up++ to instantly show the oldest messages.
- Hold ++lctrl++ and press ++page-dn++ to instantly show the newest messages.

## Chat customization

There are plenty of ways to customize your experience with in-game chat.

To access the options for chat customization:

1. Open the ++escape++ menu or go to the main menu.
2. Click the **:material-cog:{.button .item .blue} Options**{.button .large} button.
3. Click the **:material-mailbox:{.button .item .dark-green} General**{.button .large} button to access the "General Options" menu.
4. Scroll down until you see the "Chat" header.

![The Chat section in the General options menu](../../assets/media/essentials/chat/general-options-chat.png)

### :lucide-message-square-x: Hiding user messages

Want a quiet and focused experience without distracting chat in the background?
You can hide user messages by turning on the "Hide User Messages" option.

This will silence future chat messages from users, but it will not wipe current chat history or silence system messages from servers (server configuration changes, autosave notifications, etc).

!!! note

    There is currently no indicator to see if a player is hiding user messages on their end.
    
    If you see someone being abnormally silent or unresponsive to your chat messages, this is the most likely reason.

When you are ready to see chat again, turn off the "Hide User Messages" option to recieve future chat messages.

### :lucide-message-square-dashed: Hiding chat bubbles

If you find the chat bubbles often clutter your screen too much, turn on the "Hide Message Bubbles" option to hide them.

### :lucide-panel-right-dashed: Display Width

The width of the chat window.
Relative to the game's screen size.

Less width is compact and saves screen space.
Inversely, more width allows the chat to display lengthy messages.

Can be set from 25% to 100%.

=== "25%"

    ![Screenshot of chat with Display Width set to 25%](../../assets/media/essentials/chat/chat-display-width-25.jpg)

=== "50%"

    ![Screenshot of chat with Display Width set to 50%](../../assets/media/essentials/chat/chat-display-width-50.jpg)

=== "75%"

    ![Screenshot of chat with Display Width set to 75%](../../assets/media/essentials/chat/chat-display-width-75.jpg)

=== "100%"

    ![Screenshot of chat with Display Width set to 100%](../../assets/media/essentials/chat/chat-display-width-100.jpg)

### :lucide-scaling: Display Scale

The scale of text in the chat window.
Respects the display width.
You may need to add more width or decrease maximum displayed messages if your messages start breaking up into new lines.

Can be set from 25% to 400%.

!!! note

    The maximum message count has been manually set lower when the display scale gets larger for aesthetic reasons. If your display scale is too large it can overflow into the keybindings display.

=== "25%"

    ![Screenshot of chat with Display Scale set to 25%](../../assets/media/essentials/chat/chat-display-scale-25.jpg)

=== "50%"

    ![Screenshot of chat with Display Scale set to 50%](../../assets/media/essentials/chat/chat-display-scale-50.jpg)

=== "75%"

    ![Screenshot of chat with Display Scale set to 75%](../../assets/media/essentials/chat/chat-display-scale-75.jpg)

=== "100%"

    ![Screenshot of chat with Display Scale set to 100%](../../assets/media/essentials/chat/chat-display-scale-100.jpg)

=== "200%"

    ![Screenshot of chat with Display Scale set to 100%](../../assets/media/essentials/chat/chat-display-scale-200.jpg)

### :lucide-timer: Display Timeout

The interval at which new messages disappear.
Longer intervals help with reading new messages.

Can be set beyond 30 seconds if you manually type in your desired time value.

### :lucide-messages-square: Max Displayed Messages

The maximum number of new messages you can recieve in chat before having to scroll up.

Can be set from 1 to 20 messages.

=== "4 messages"

    ![Screenshot of chat with Max Displayed Messages set to 4](../../assets/media/essentials/chat/chat-messages-4.jpg)

=== "8 messages"

    ![Screenshot of chat with Max Displayed Messages set to 8](../../assets/media/essentials/chat/chat-messages-8.jpg)

=== "12 messages"

    ![Screenshot of chat with Max Displayed Messages set to 12](../../assets/media/essentials/chat/chat-messages-12.jpg)

=== "16 messages"

    ![Screenshot of chat with Max Displayed Messages set to 16](../../assets/media/essentials/chat/chat-messages-16.jpg)

=== "20 messages"

    ![Screenshot of chat with Max Displayed Messages set to 20](../../assets/media/essentials/chat/chat-messages-20.jpg)
