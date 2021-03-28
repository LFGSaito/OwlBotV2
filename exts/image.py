"""
Image extension for qrm
---
Copyright (C) 2019-2021 Abigail Gold, 0x5c

This file is part of qrm2 and is released under the terms of
the GNU General Public License, version 2.
"""


import aiohttp
from datetime import datetime

import discord.ext.commands as commands

import common as cmn

import data.options as opt


class ImageCog(commands.Cog):
    gl_baseurl = "https://www.fourmilab.ch/cgi-bin/uncgi/Earth?img=ETOPO1_day-m.evif&dynimg=y&opt=-p"

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.bandcharts = cmn.ImagesGroup(cmn.paths.resources / "bandcharts.1.json")
        self.maps = cmn.ImagesGroup(cmn.paths.resources / "maps.1.json")
        self.session = aiohttp.ClientSession(connector=bot.qrm.connector)

    @commands.command(name="bandchart", aliases=["bandplan", "plan", "bands"], category=cmn.Cats.REF)
    async def _bandcharts(self, ctx: commands.Context, chart_id: str = ""):
        """Gets the frequency allocations chart for a given country."""
        await ctx.send(embed=create_embed(ctx, "Bandchart", self.bandcharts, chart_id))

    @commands.command(name="map", category=cmn.Cats.MAPS)
    async def _map(self, ctx: commands.Context, map_id: str = ""):
        """Posts a ham-relevant map."""
        await ctx.send(embed=create_embed(ctx, "Map", self.maps, map_id))

    @commands.command(name="grayline", aliases=["greyline", "grey", "gray", "gl"], category=cmn.Cats.MAPS)
    async def _grayline(self, ctx: commands.Context):
        """Gets a map of the current greyline, where HF propagation is the best."""
        embed = cmn.embed_factory(ctx)
        embed.title = "Current Greyline Conditions"
        embed.colour = cmn.colours.good
        date_params = f"&date=1&utc={datetime.utcnow():%Y-%m-%d+%H:%M:%S}"
        embed.set_image(url=self.gl_baseurl + date_params)
        await ctx.send(embed=embed)


def create_embed(ctx: commands.Context, not_found_name: str, db: cmn.ImagesGroup, img_id: str):
    """Creates an embed for the image and its metadata, or list available images in the group."""
    img_id = img_id.lower()
    embed = cmn.embed_factory(ctx)
    if img_id not in db:
        desc = "Possible arguments are:\n"
        for key, img in db.items():
            desc += f"`{key}`: {img.name}{('  ' + img.emoji if img.emoji else '')}\n"
        embed.title = f"{not_found_name} Not Found!"
        embed.description = desc
        embed.colour = cmn.colours.bad
        return embed
    metadata = db[img_id]
    if metadata.description:
        embed.description = metadata.description
    if metadata.source:
        embed.add_field(name="Source", value=metadata.source)
    embed.title = metadata.long_name + ("  " + metadata.emoji if metadata.emoji else "")
    embed.colour = cmn.colours.good
    embed.set_image(url=opt.resources_url + metadata.filename)
    return embed


def setup(bot: commands.Bot):
    bot.add_cog(ImageCog(bot))
