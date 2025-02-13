import disnake
import re
import time

from disnake.ext import commands

class Command(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Command activated")

        # Хелп

    @commands.command()
    async def help(self, ctx):
        await ctx.send(embed=disnake.Embed(title=f"Информация о командах:", description=f"🎩**Администрация:**\nsay - отправляет сообщения от имени бота\n!say <сообщение>\nclear - очищает чат\n!clear <число>\n\n**❌Модерация**\nkick - кикает участника\n!kick <Участник> <Причина>\n ban - Банит участника\n!ban <Участник> <Причина>\n\n**👨Интересно:**\nСкоро будут...\n",
    color=0xFFA200))
        await ctx.message.delete()

        # Админ команды:

    @commands.command(name="say", usage="<Сообщение>")
    async def say(self, ctx, *, message):
        if ctx.author.id == 1048105445706977280 or any(role.permissions.administrator for role in ctx.author.roles):
            await ctx.send(message)
            await ctx.message.delete()
        else:
            await ctx.send(embed=disnake.Embed(title="Ошибка!",description=f"{ctx.author.mention}, у вас недостаточно прав для выполнения данной команды!",color=0xFF0000),delete_after=10)


    @commands.command()
    @commands.has_permissions()
    async def clear(self, ctx, amount=40):
       await ctx.channel.purge(limit=amount)

        # Модер команды:

    @commands.command(name="kick", usage ="<Участник> <Причина>")
    @commands.has_permissions(kick_members=True, administrator=True)
    async def kick(self, ctx, member: disnake.Member, *, reason="Нарушение правил"):
        await ctx.send(embed=disnake.Embed(title=f"**Кик**", description=f"{ctx.author.mention}, исключил пользователя {member.mention}.\nПричина: {reason}", color=0xFFA200), delete_after=10)
        await ctx.message.delete()
        await member.kick(reason=reason)


    @commands.command(name="ban", usage ="<Пользователь> <Причина>")
    @commands.has_permissions(ban_members=True, administrator=True)
    async def ban(self, ctx, member: disnake.Member, *, reason="Нарушение правил"):
        await ctx.send(embed=disnake.Embed(title=f"**Бан**", description=f"{ctx.author.mention}, забанил пользователя {member.mention}.\nПричина: {reason}", color=0xFFA200), delete_after=10)
        await ctx.message.delete()
        await member.ban(reason=reason)


        # Развлечение: в ящик..

    #@command.slash_command()
    #async def Avatar(self, interaction, member = disnake.Member=None)
        #user = member or interaction.author
        #embed = disnake.Embed(title = "Avatar", color = "0x2f3136")
        #embed.set_image(url=user.display_avatar.url)
        #await interaction.responce.send_message(embed=embed)


    @commands.command()
    async def Info(self, ctx):
        await ctx.send(embed=disnake.Embed(title=f"**Информация о боте:**", description=f"Имя: Time/and\Space.\nВерсия: 1.0.2.\nПатч: 0.3", color=0xFFA200))
        await ctx.message.delete()
#Все права
'''
add_reactions #Добавлять реакции
administrator #Администратор
attach_files #Прикреплять файлы
ban_members #Банить участников
change_nickname #Изменеить никнейм
connect #Подключаться к голосовым каналам
create_instant_invite #Создание мгновенного приглашения
create_private_threads #Создавать приватные ветки
create_public_threads #Создавать публичные ветки
deafen_members #Выключить звук у участников
embed_links #Встраивать ссылки в эмбед
external_emojis #Сторонние эмодзи
external_stickers #Сторонние стикеры
kick_members #Выгонять участников
manage_channels #Управлять каналами
manage_emojis #Управлять эмодзи
manage_emojis_and_stickers #Управлять эмодзи и стикерами
manage_events #Управлять ивентами (Событиями)
manage_guild #Управлять сервером
manage_messages #Удалять сообщения
manage_nicknames #Изменять никнеймы участникам
manage_permissions #Управлять правами
manage_roles #Управлять ролями
manage_threads #Управлять ветками
manage_webhooks #Управлять вебхуками
mention_everyone #Упоминать все роли (everyone, here и все другие)
moderate_members #Вроде как тайм-аут (Мут)
move_members #Перемещать участников в другие голосовые каналы
mute_members #Отключать микрофон у участников
priority_speaker #Приоритетный режим
read_message_history #Читать историю сообщений
request_to_speak #Поднять руку в требунах
send_messages #Отправлять сообщения
send_messages_in_threads #Отправлять сообщения в ветках
send_tts_messages #Отправлять tts сообщения
speak #Говорить в голосовом канале
start_embedded_activities #Вроде как запускать активности в войсе
stream #Включать стрим
use_external_emojis #Это вроде то же что и на строке 17
use_external_stickers #Это вроде то же что и на строке 18
use_slash_commands #Использовать слеш команды
use_voice_activation #Использовать активацию по голосу в голосовом канале
view_audit_log #Просматривать журнал аудита
view_channel #Просматривать канал
view_guild_insights #Просматривать информацию о сервере
'''

@commands.Cog.listener()
async def on_commands_error(self, ctx, error):
        print(error)


def setup(bot):
    bot.add_cog(Command(bot))
