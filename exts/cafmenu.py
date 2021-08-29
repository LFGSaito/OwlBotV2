import discord.ext.commands as commands
import common as cmn
import json


class MenuCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="cafbreakfast", aliases=["cafb"], category=cmn.Cats.LOOKUP)
    async def _CafB(self, ctx: commands.Context):
        """Looks up the Caf's Breakfast menu"""
        breakfast = open('data/Breakfast.json')
        json.load(breakfast)
        menu0 = breakfast['periods']['categories'][0]['items'][0]['name']
        await ctx.send(menu0)
        return

    @commands.command(name="caflunch", aliases=["cafl"], category=cmn.Cats.LOOKUP)
    async def _CafL(self, ctx: commands.Context):
        """Looks up the Caf's Lunch menu"""
        Lunch = open('data/Lunch.json')
        json.load(Lunch)
        menu0 = Lunch['periods']['categories'][0]['items'][0]['name']
        await ctx.send(menu0)
        return

    @commands.command(name="cafmenudinner", aliases=["cafd"], category=cmn.Cats.LOOKUP)
    async def _CafD(self, ctx: commands.Context):
        """Looks up the Caf's Dinner menu"""
        Dinner = open('data/Dinner.json')
        json.load(Dinner)
        menu0 = Dinner['periods']['categories'][0]['items'][0]['name']
        await ctx.send(menu0)
        return


def setup(bot: commands.Bot):
    bot.add_cog(MenuCog(bot))
