from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Hi {message.from_user.first_name}!</b>
I am AnimeFunChat music Bot, a bot that lets you play music in your Telegram groups voice chat.
To add in your group contact us at @AnimeFunChat
[‎](https://i.imgur.com/1uELGhj.mp4)
Use /help To know my cotrols...
Contact @Dojeto if you are facing any issues....
Use the buttons below to know more about me.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➲ Support US", url="https://t.me/Animewatcherz"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "SpamChat", url="https://t.me/Animixchat"
                    ),
                    InlineKeyboardButton(
                        "Channel 🔈", url="https://t.me/GodlyDemon"
                    ),
                    InlineKeyboardButton(
                        "Games 😈", url="https://t.me/immortalchallengers" )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/AnimeFunChat"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Ahoy {message.from_user.first_name}! Contact @KazutoSupport if you need any help...</b>
╓**The commands and there use is explained here-:**
╠`/ytp` To search the song on Youtube and play the first matching result 
╠`/play` Reply this in response to a link or any audio file it will be played
╠`/skip` to skip current song 
╠`/stop or /end or /kill` to stop the streaming of song 
╠`/resume` to resume the playback. \n╠Inline search is also supported.
╙`/pause` to pause the stream
┣**Note:-** `This is a private bot for @AnimeFunChat We may or may not let you use it....`
**To add in your group contact us at @AnimeFunChat**
[‎](https://i.imgur.com/6FPYhnO.mp4)
Contact @Dojeto if you are facing any issues....
Use the buttons below to know more about me.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➲ Support US", url="https://t.me/Animewatcherz"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "SpamChat", url="https://t.me/Animixchat"
                    ),
                    InlineKeyboardButton(
                        "Channel 🔈", url="https://t.me/GodlyDemon"
                    ),
                    InlineKeyboardButton(
                        "Games 😈", url="https://t.me/immortalchallengers" )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/AnimeFunChat"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("arise")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
