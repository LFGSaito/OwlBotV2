"""
TeX extension for qrm
---
Copyright (C) 2021 thxo

This file is part of qrm2 and is released under the terms of
the GNU General Public License, version 2.
"""

import aiohttp
from io import BytesIO
from urllib.parse import urljoin

import discord
import discord.ext.commands as commands

import common as cmn
import data.options as opt


class TexCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(connector=bot.qrm.connector)
        self.rtex_instance = getattr(opt, "rtex_instance", "https://rtex.probablyaweb.site/")
        with open(cmn.paths.resources / "template.1.tex") as latex_template:
            self.template = latex_template.read()

    @commands.command(name="tex", aliases=["latex"], category=cmn.cat.fun)
    async def tex(self, ctx: commands.Context, *, expr: str):
        """Renders a LaTeX expression."""
        payload = {
            "format": "png",
            "code": self.template.replace("#CONTENT#", expr),
            "quality": 50
        }

        with ctx.typing():
            # ask rTeX to render our expression
            async with self.session.post(urljoin(self.rtex_instance, "api/v2"), json=payload) as r:
                if r.status != 200:
                    raise cmn.BotHTTPError(r)

                render_result = await r.json()
                if render_result["status"] != "success":
                    embed = cmn.embed_factory(ctx)
                    embed.title = "LaTeX Rendering Failed!"
                    embed.description = render_result.get("description", "Unknown error")
                    embed.colour = cmn.colours.bad
                    await ctx.send(embed=embed)
                    return

            # if rendering went well, download the file given in the response
            async with self.session.get(urljoin(self.rtex_instance, "api/v2/" + render_result["filename"])) as r:
                png_buffer = BytesIO(await r.read())

            embed = cmn.embed_factory(ctx)
            embed.title = "LaTeX Expression"
            embed.description = "Rendered by [rTeX](https://rtex.probablyaweb.site/)."
            embed.set_image(url="attachment://tex.png")
            await ctx.send(file=discord.File(png_buffer, "tex.png"), embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(TexCog(bot))
