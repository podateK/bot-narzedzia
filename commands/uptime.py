import discord
from datetime import datetime, timezone
from discord.ext import commands


class Uptime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = datetime.now(timezone.utc)

    @commands.command(name="uptime")
    async def uptime(self, ctx):
        delta = datetime.now(timezone.utc) - self.start_time
        days = delta.days
        hours, remainder = divmod(delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        parts = []
        if days:
            parts.append(f"{days}d")
        if hours:
            parts.append(f"{hours}h")
        if minutes:
            parts.append(f"{minutes}m")
        parts.append(f"{seconds}s")

        embed = discord.Embed(
            title="Bot Uptime",
            description=f"Running for **{' '.join(parts)}**",
            color=discord.Color.green()
        )
        embed.set_footer(text=f"Started at {self.start_time.strftime('%Y-%m-%d %H:%M:%S UTC')}")
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Uptime(bot))
