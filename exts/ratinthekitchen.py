import discord.ext.commands as commands
import datetime
import common as cmn
import time

difference = "TBD"

class RatCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="ratinthekitchen", aliases=["rat"], category=cmn.Cats.FUN)
    async def _rat(self, ctx: commands.Context):
        """Checks for Rats"""
        rats = f"No rats spotted in the caf as of today, if this changes DM Saito, time since last seen {difference}"
        await ctx.send(str(rats))
        return


def setup(bot: commands.Bot):
    bot.add_cog(RatCog(bot))
