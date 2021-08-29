import discord.ext.commands as commands
import common as cmn
import json


class MenuCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="cafbreakfast", aliases=["cafb"], category=cmn.Cats.LOOKUP)
    async def _CafB(self, ctx: commands.Context):
        """Looks up the Caf's Breakfast menu"""
        Breakfastj = open('data/Breakfast.json')
        Breakfastd = json.load(Breakfastj)
        print(Breakfastd)
        menu0 = Breakfastd['periods']['categories'][0]['items'][0]['name']
        await ctx.send(menu0)
        return

    @commands.command(name="caflunch", aliases=["cafl"], category=cmn.Cats.LOOKUP)
    async def _CafL(self, ctx: commands.Context):
        """Looks up the Caf's Lunch menu"""
        Lunchj = open('data/Lunch.json')
        Lunchd = json.load(Lunchj)
        menu0 = Lunchd['periods']['categories'][0]['items'][0]['name']
        await ctx.send(menu0)
        return

    @commands.command(name="cafmenudinner", aliases=["cafd"], category=cmn.Cats.LOOKUP)
    async def _CafD(self, ctx: commands.Context):
        """Looks up the Caf's Dinner menu"""
        Dinnerj = open('data/Dinner.json')
        Dinnerd = json.load(Dinnerj)
        menu0 = Dinnerd['periods']['categories'][0]['items'][0]['name']
        await ctx.send(menu0)
        return


def setup(bot: commands.Bot):
    bot.add_cog(MenuCog(bot))
