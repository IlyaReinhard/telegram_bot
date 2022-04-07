from telethon import events

from punk import bot

@bot.on(events.ChatAction())
async def on_join(event: events.ChatAction.Event):
    if event.is_group and event.user_added and event.user_id == bot.me.id:
                await bot.send_message(event.chat.id, 'Категорически приветствую, господа!')