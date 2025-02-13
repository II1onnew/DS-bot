import os

import disnake
from disnake.ext import commands

intents = disnake.Intents.default()
intents.message_content = True
intents.guilds = True
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)


@bot.command()
@commands.is_owner()
@bot.event
async def on_ready():
  print(f"Бот {bot.user} готов к работе! \nВерсия: 1.0.1 \nПатч: 0.2")
  await bot.change_presence(status=disnake.Status.do_not_disturb, activity=disnake.Activity(type=disnake.ActivityType.watching, name="за сервером"))


@bot.command()
async def load(ctx, extension):
    if ctx.author.id == 1050091676703666236:
        bot.load_extension(f"cogs.{extension}")
        await ctx.send(embed=disnake.Embed(title="Запуск подсистемы...", description=f"Подсистема {extension} запускается!", color=0xFFA200))
    else:
        await ctx.message.delete()
        await ctx.send(embed=disnake.Embed(title="Ошибка!", description="У вас нет доступа к системам бота!", color=0xFF0000), delete_after=15)

@bot.command()
async def unload(ctx, extension):
    if ctx.author.id == 1050091676703666236:
        bot.unload_extension(f"cogs.{extension}")
        await ctx.send(embed=disnake.Embed(title="Отключение подсистемы...", description=f"Подсистема {extension} отключается!", color=0xFFA200))
    else:
        await ctx.message.delete()
        await ctx.send(embed=disnake.Embed(title="Ошибка!", description="У вас нет доступа к системам бота!", color=0xFF0000), delete_after=15)

@bot.command()
async def reload(ctx, extension):
    if ctx.author.id == 1050091676703666236:
        bot.reload_extension(f"cogs.{extension}")
        await ctx.send(embed=disnake.Embed(title="Перезагрузка подсистемы...", description=f"Подсистема {extension} перезагружается!", color=0xFFA200))
    else:
        await ctx.message.delete()
        await ctx.send(embed=disnake.Embed(title="Ошибка!", description="У вас нет доступа к системам бота!", color=0xFF0000), delete_after=15)

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        try:
            bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"Loaded cog: {filename[:-3]}")
        except Exception as e:
            print(f"Failed to load cog {filename[:-3]}: {e}")

bot.run("BOT TOKEN")
