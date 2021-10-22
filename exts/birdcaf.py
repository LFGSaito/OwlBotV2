import discord.ext.commands as commands
import datetime
import common as cmn
import time

datetimeFormat = '%Y %m %d %H:%M:%S'
date2 = '2021 10 20 7:44:36'
date1 = time.strftime("%Y %m %d %H:%M:%S", time.gmtime())
diff = datetime.datetime.strptime(date1, datetimeFormat) - datetime.datetime.strptime(date2, datetimeFormat)


class BridCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="birdinthekitchen", aliases=["bird"], category=cmn.Cats.FUN)
    async def _bird(self, ctx: commands.Context):
        """Checks for birds"""
        bird = f"No bird spotted in the caf as of today, if this changes DM Saito, time since last seen {diff}"
        await ctx.send(str(bird))
        return


def setup(bot: commands.Bot):
    bot.add_cog(BridCog(bot))
