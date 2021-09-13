import discord.ext.commands as commands
import datetime
import common as cmn
import time

datetimeFormat = '%Y-%m-%d %H:%M:%S'
date2 = '2019-11-18 12:25:34'
date1 = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
diff = datetime.datetime.strptime(date1, datetimeFormat) - datetime.datetime.strptime(date2, datetimeFormat)


class RatCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="ratinthekitchen", aliases=["rat"], category=cmn.Cats.FUN)
    async def _rat(self, ctx: commands.Context):
        """Checks for Rats"""
        rats = f"No rats spotted in the caf as of today, if this changes DM Saito, time since last seen {diff}"
        await ctx.send("DateTime Format is" + datetimeFormat + "Date2 is" + date2 + "date 1 is" + date1 + "and Diff is" + diff + rats)
        return


def setup(bot: commands.Bot):
    bot.add_cog(RatCog(bot))
