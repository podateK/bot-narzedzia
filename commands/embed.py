import discord
from discord.ext import commands


class Embed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="embed")
    async def embed_cmd(self, ctx, title: str = None, *, description: str = None):
        if not title or not description:
            await ctx.send("Usage: `.embed <title> | <description>`\nOptional: add `| color=#hex` at the end")
            return

        color = discord.Color.blurple()
        if "| color=" in description.lower():
            parts = description.rsplit("| color=", 1)
            description = parts[0].strip()
            color_str = parts[1].strip()
            try:
                color = discord.Color(int(color_str.replace("#", ""), 16))
            except ValueError:
                color = discord.Color.blurple()

        embed = discord.Embed(title=title, description=description, color=color)
        embed.set_footer(text=f"Created by {ctx.author.display_name}", icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed=embed)

    @commands.command(name="emtitle")
    async def emtitle(self, ctx, title: str = None):
        if not title:
            await ctx.send("Usage: `.emtitle <title>`")
            return
        embed = discord.Embed(title=title, color=discord.Color.blurple())
        await ctx.send(embed=embed)

    @commands.command(name="emdsc")
    async def emdsc(self, ctx, *, description: str = None):
        if not description:
            await ctx.send("Usage: `.emdsc <description>`")
            return
        embed = discord.Embed(description=description, color=discord.Color.blurple())
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Embed(bot))
