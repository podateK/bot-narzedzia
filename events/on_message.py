import re
import discord
from discord.ext import commands


INVITE_PATTERN = re.compile(
    r"(discord\.gg|discordapp\.com/invite|discord\.com/invite)/[a-zA-Z0-9]+",
    re.IGNORECASE
)


class OnMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if message.guild is None:
            return
        if message.author.guild_permissions.administrator:
            return

        if INVITE_PATTERN.search(message.content):
            try:
                await message.delete()
                embed = discord.Embed(
                    title="Invite Link Removed",
                    description=f"{message.author.mention}, posting invite links is not allowed here.",
                    color=discord.Color.red()
                )
                await message.channel.send(embed=embed, delete_after=10)
            except discord.Forbidden:
                pass


async def setup(bot):
    await bot.add_cog(OnMessage(bot))
