import discord.ext.commands as commands
import common as cmn
import json

class MenuCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="cafmenu breakfast", aliases=["caf b"], category=cmn.Cats.LOOKUP)
    async def _CafB(self, ctx: commands.Context):
        breakfast = open('data/Breakfast.json')
        json.load(breakfast)
        menu0 = breakfast['periods']['categories'][0]['items'][0]['name']
        await ctx.send(menu0)
        return
   
    @commands.command(name="cafmenu lunch", aliases=["caf l"], category=cmn.Cats.LOOKUP)
    async def _CafL(self, ctx: commands.Context):
        await ctx.send(str(rats))
        return

    @commands.command(name="cafmenu dinner", aliases=["caf d"], category=cmn.Cats.LOOKUP)
    async def _CafD(self, ctx: commands.Context):
        await ctx.send(str(rats))
        return

def setup(bot: commands.Bot):
    bot.add_cog(MenuCog(bot))
