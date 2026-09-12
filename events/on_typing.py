import discord
from discord.ext import commands


class OnTyping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_typing(self, channel, user, when):
        if user.bot:
            return
        if not isinstance(channel, discord.TextChannel):
            return

        log_channel = discord.utils.get(channel.guild.text_channels, name="log")
        if log_channel is None:
            return

        if channel.id == log_channel.id:
            return

        embed = discord.Embed(
            description=f"{user.mention} is typing in {channel.mention}",
            color=discord.Color.light_gray(),
            timestamp=when
        )
        embed.set_thumbnail(url=user.display_avatar.url)

        try:
            await log_channel.send(embed=embed, delete_after=30)
        except discord.Forbidden:
            pass


async def setup(bot):
    await bot.add_cog(OnTyping(bot))
