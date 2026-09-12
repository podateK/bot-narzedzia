import discord
from discord.ext import commands


class OnMemberJoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is None:
            for ch in member.guild.text_channels:
                if "welcome" in ch.name.lower() or "general" in ch.name.lower():
                    channel = ch
                    break
        if channel is None:
            return

        embed = discord.Embed(
            title="Welcome!",
            description=f"Welcome to **{member.guild.name}**, {member.mention}!",
            color=discord.Color.green()
        )
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.add_field(name="Account Created", value=f"<t:{int(member.created_at.timestamp())}:R>", inline=True)
        embed.add_field(name="Member Count", value=member.guild.member_count, inline=True)
        embed.add_field(name="ID", value=member.id, inline=True)
        embed.set_footer(text=f"Member joined {member.guild.name}")

        if member.guild.icon:
            embed.set_author(name=member.guild.name, icon_url=member.guild.icon.url)

        try:
            await channel.send(embed=embed)
        except discord.Forbidden:
            pass


async def setup(bot):
    await bot.add_cog(OnMemberJoin(bot))
