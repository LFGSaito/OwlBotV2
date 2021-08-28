import discord.ext.commands as commands
import common as cmn




class MenuCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="cafmenu breakfast", aliases=["caf b"], category=cmn.Cats.LOOKUP)
    async def _Caf(self, ctx: commands.Context):
        
        await ctx.send(str(rats))
        return

    @commands.command(name="cafmenu lunch", aliases=["caf l"], category=cmn.Cats.LOOKUP)
    async def _Caf(self, ctx: commands.Context):
        
        await ctx.send(str(rats))
        return

    @commands.command(name="cafmenu dinner", aliases=["caf d"], category=cmn.Cats.LOOKUP)
    async def _Caf(self, ctx: commands.Context):
        
        await ctx.send(str(rats))
        return


def setup(bot: commands.Bot):
    bot.add_cog(MenuCog(bot))
