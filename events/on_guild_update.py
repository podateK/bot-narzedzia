import discord
from discord.ext import commands


class OnGuildUpdate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_update(self, before, after):
        log_channel = discord.utils.get(after.text_channels, name="log")
        if log_channel is None:
            return

        changes = []

        if before.name != after.name:
            changes.append(f"**Name:** `{before.name}` -> `{after.name}`")
        if before.icon != after.icon:
            changes.append("**Icon** was changed")
        if before.banner != after.banner:
            changes.append("**Banner** was changed")
        if before.owner != after.owner:
            changes.append(f"**Owner:** {before.owner} -> {after.owner}")
        if before.verification_level != after.verification_level:
            changes.append(f"**Verification Level:** {before.verification_level} -> {after.verification_level}")
        if before.description != after.description:
            changes.append("**Description** was changed")

        if not changes:
            return

        embed = discord.Embed(
            title="Server Updated",
            description="\n".join(changes),
            color=discord.Color.orange(),
            timestamp=discord.utils.utcnow()
        )
        if after.icon:
            embed.set_thumbnail(url=after.icon.url)

        try:
            await log_channel.send(embed=embed)
        except discord.Forbidden:
            pass


async def setup(bot):
    await bot.add_cog(OnGuildUpdate(bot))
