import disnake
from disnake.ext import commands

class events(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Event activated")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        role = member.guild.get_role(1133605779061088276)

        embed = disnake.Embed(
            title=f"Добро пожаловать, {member.mention}!",
            description="Имя сервера: Данные утеряны..\nIP: Данные засекречены..\nПорт: Данные засекречены..",
            color=0xf702d9
        )

        if channel is not None:
            await member.add_roles(role)
            await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(events(bot))