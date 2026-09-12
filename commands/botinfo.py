import discord
import platform
from datetime import datetime, timezone
from discord.ext import commands


class BotInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = datetime.now(timezone.utc)

    @commands.command(name="botinfo")
    async def botinfo(self, ctx):
        uptime_dt = datetime.now(timezone.utc) - self.start_time
        hours, remainder = divmod(int(uptime_dt.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        uptime_str = f"{hours}h {minutes}m {seconds}s"

        embed = discord.Embed(title="Bot Info", color=discord.Color.blurple())
        embed.set_thumbnail(url=self.bot.user.display_avatar.url)
        embed.add_field(name="Name", value=self.bot.user.name, inline=True)
        embed.add_field(name="ID", value=self.bot.user.id, inline=True)
        embed.add_field(name="Servers", value=len(self.bot.guilds), inline=True)
        embed.add_field(name="Users", value=sum(g.member_count for g in self.bot.guilds), inline=True)
        embed.add_field(name="Uptime", value=uptime_str, inline=True)
        embed.add_field(name="Latency", value=f"{round(self.bot.latency * 1000)}ms", inline=True)
        embed.add_field(name="Python", value=platform.python_version(), inline=True)
        embed.add_field(name="discord.py", value=discord.__version__, inline=True)
        embed.add_field(name="Platform", value=platform.system(), inline=True)
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(BotInfo(bot))
