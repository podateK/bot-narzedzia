import discord
from discord.ext import commands


class OnVoiceStateUpdate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if member.bot:
            return

        log_channel = discord.utils.get(member.guild.text_channels, name="log")
        if log_channel is None:
            return

        embed = discord.Embed(color=discord.Color.blurple())
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.timestamp = discord.utils.utcnow()

        if before.channel is None and after.channel is not None:
            embed.title = "Voice Channel Joined"
            embed.description = f"{member.mention} joined **{after.channel.name}**"
            embed.color = discord.Color.green()
        elif before.channel is not None and after.channel is None:
            embed.title = "Voice Channel Left"
            embed.description = f"{member.mention} left **{before.channel.name}**"
            embed.color = discord.Color.red()
        elif before.channel != after.channel:
            embed.title = "Voice Channel Moved"
            embed.description = f"{member.mention} moved from **{before.channel.name}** to **{after.channel.name}**"
            embed.color = discord.Color.orange()
        else:
            changes = []
            if before.self_mute != after.self_mute:
                changes.append(f"Self Mute: {after.self_mute}")
            if before.self_deaf != after.self_deaf:
                changes.append(f"Self Deaf: {after.self_deaf}")
            if before.mute != after.mute:
                changes.append(f"Muted: {after.mute}")
            if before.deaf != after.deaf:
                changes.append(f"Deafened: {after.deaf}")
            if changes:
                embed.title = "Voice State Updated"
                embed.description = f"{member.mention} in **{after.channel.name}**"
                embed.add_field(name="Changes", value="\n".join(changes), inline=False)
            else:
                return

        try:
            await log_channel.send(embed=embed)
        except discord.Forbidden:
            pass


async def setup(bot):
    await bot.add_cog(OnVoiceStateUpdate(bot))
