import discord
from discord.ext import commands


class OnReactionRemove(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        if user.bot:
            return

        log_channel = discord.utils.get(user.guild.text_channels, name="log")
        if log_channel is None:
            return

        message = reaction.message
        channel = message.channel

        embed = discord.Embed(
            title="Reaction Removed",
            description=f"{user.mention} removed {reaction.emoji} in {channel.mention}",
            color=discord.Color.red(),
            timestamp=discord.utils.utcnow()
        )
        embed.add_field(name="Message", value=f"[Jump to message]({message.jump_url})", inline=True)
        embed.set_thumbnail(url=user.display_avatar.url)

        try:
            await log_channel.send(embed=embed)
        except discord.Forbidden:
            pass


async def setup(bot):
    await bot.add_cog(OnReactionRemove(bot))
