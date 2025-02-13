import disnake
from disnake.ext import commands

class Error(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Error activated")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(error)

        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=disnake.Embed(
                title="Ошибка!",
                description=f"{ctx.author.mention}, у вас недостаточно прав для выполнения данной команды!",
                color=0xFF0000
            ),delete_after=10)
            await ctx.message.delete()
        elif isinstance(error, commands.UserInputError):
            await ctx.send(embed=disnake.Embed(
                title="Ошибка!",
                description=f"{ctx.author.mention}, у вас ошибка в команде!\nПравильное написание команды:\n!{ctx.command.name} {ctx.command.usage}",
                color=0xFF0000
            ), delete_after=10)
            await ctx.message.delete()
        else:
            await ctx.send(embed=disnake.Embed(
                title="ERROR",
                description="await ctx.send(embed=disnake.embed(\n  title=ERROR\n   description=ERROR\n collor=0xFF0000),delete after=10)",
                color=0xFF0000
            ))


def setup(bot):
    bot.add_cog(Error(bot))