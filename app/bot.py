from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from app.config import config
from app.middleware.AuthMiddleware import AuthMiddleware

GAME_TAGS = {
    "!bone": "🎲",
    "!dart": "🎯",
    "!slot": "🎰",
    "!goal": "⚽",
    "!hoop": "🏀",
    "!pins": "🎳"
}

HELP_TEXT = (
    "🚀 **Quick Games:**\n" +
    "\n".join([f"`{tag}` — {emoji}" for tag, emoji in GAME_TAGS.items()])
)

async def start():
    bot = Bot(token=config.bot_token)
    dp = Dispatcher()

    @dp.message(Command("start"))
    async def cmd_start(message: types.Message):
        await message.answer("👺 я тебя запомнил\n\n")

    @dp.message(Command("help"))
    @dp.message(F.text.contains(f"@{config.bot_username}"))
    async def show_help(message: types.Message):
        await message.reply(HELP_TEXT, parse_mode="Markdown")

    @dp.message(F.text.startswith("!"))
    async def game_handler(message: types.Message):
        command = message.text.lower().split()[0]
        if command in GAME_TAGS:
            await message.answer_dice(emoji=GAME_TAGS[command])

    try:
        me = await bot.get_me()
        config.bot_username = me.username
        print(f"Bot @{config.bot_username} is online with '!' prefix")
        await dp.start_polling(bot, drop_pending_updates=True)
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        await bot.session.close()