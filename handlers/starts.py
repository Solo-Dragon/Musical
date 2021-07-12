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

➲ Use /help To know my cotrols...

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
                        "💬 Group", url="https://t.me/AnimeFunChat"
                    ),
                    InlineKeyboardButton(
                        "Channel 🔈", url="https://t.me/GodlyDemon"
                    ),
                    InlineKeyboardButton(
                        "Offtopic 😈", url="https://t.me/immortalchallengers" )
                ],
                [
                    InlineKeyboardButton(
                        "SpamChat", url="https://t.me/Animixchat"
                    )
                ]
            ]
        )
    )
