import discord
from discord.ext import commands


class OnMemberUpdate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if before.bot:
            return

        log_channel = discord.utils.get(before.guild.text_channels, name="log")
        if log_channel is None:
            return

        embed = discord.Embed(color=discord.Color.blurple(), timestamp=discord.utils.utcnow())
        embed.set_thumbnail(url=after.display_avatar.url)
        embed.set_author(name=str(after), icon_url=after.display_avatar.url)

        if before.nick != after.nick:
            embed.title = "Nickname Changed"
            embed.add_field(name="Before", value=before.nick or before.name, inline=True)
            embed.add_field(name="After", value=after.nick or after.name, inline=True)

        elif before.roles != after.roles:
            added = set(after.roles) - set(before.roles)
            removed = set(before.roles) - set(after.roles)
            if added:
                embed.title = "Role Added"
                embed.description = ", ".join(r.mention for r in added)
            if removed:
                embed.title = "Role Removed"
                embed.description = ", ".join(r.mention for r in removed)
            if not added and not removed:
                return

        elif before.avatar != after.avatar:
            embed.title = "Avatar Changed"
            embed.set_image(url=after.display_avatar.url)

        else:
            return

        try:
            await log_channel.send(embed=embed)
        except discord.Forbidden:
            pass


async def setup(bot):
    await bot.add_cog(OnMemberUpdate(bot))
