import asyncio
import discord
from discord.ext import commands


class Reminder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="remind")
    async def remind(self, ctx, time: int = None, *, message: str = None):
        if time is None or message is None:
            await ctx.send("Usage: `.remind <seconds> <message>`")
            return

        embed = discord.Embed(
            title="Reminder Set",
            description=f"I will remind you in **{time} seconds** about:\n{message}",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)

        await asyncio.sleep(time)

        remind_embed = discord.Embed(
            title="Reminder!",
            description=f"You asked me to remind you about:\n**{message}**",
            color=discord.Color.gold(),
            timestamp=discord.utils.utcnow()
        )
        remind_embed.set_footer(text=f"Requested in {ctx.guild.name}" if ctx.guild else "DM")
        try:
            await ctx.author.send(embed=remind_embed)
            await ctx.send(f"{ctx.author.mention}, I sent you a DM with your reminder!")
        except discord.Forbidden:
            await ctx.send(f"{ctx.author.mention}, here is your reminder: **{message}**")


async def setup(bot):
    await bot.add_cog(Reminder(bot))
