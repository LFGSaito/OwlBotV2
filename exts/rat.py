import discord
import discord.ext.commands as commands
import datetime
from time import gmtime, strftime
import common as cmn

datetimeFormat = '%Y-%m-%d %H:%M:%S'
date2 = '2019-11-18 12:25:34'
date1 = strftime("%Y-%m-%d %H:%M:%S", gmtime())
diff = datetime.datetime.strptime(date1, datetimeFormat) - datetime.datetime.strptime(date2, datetimeFormat)


class RatCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


@commands.command(name="rat", aliases=["r"], category=cmn.Cats.FUN)
async def rat(command: str, message: discord.Message):
    rats = f"No rats spotted in the caf as of today, if this changes DM Saito, time since last seen {diff}"
    await message.channel.send(rats)
    return


def setup(bot: commands.Bot):
    bot.add_cog(RatCog(bot))
