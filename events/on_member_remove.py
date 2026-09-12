import discord
from discord.ext import commands


class OnMemberRemove(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = member.guild.system_channel
        if channel is None:
            for ch in member.guild.text_channels:
                if "goodbye" in ch.name.lower() or "general" in ch.name.lower():
                    channel = ch
                    break
        if channel is None:
            return

        roles = [role.name for role in member.roles[1:]]
        roles_text = ", ".join(roles) if roles else "None"

        embed = discord.Embed(
            title="Goodbye!",
            description=f"**{member.display_name}** has left **{member.guild.name}**.",
            color=discord.Color.red()
        )
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.add_field(name="Member Count", value=member.guild.member_count, inline=True)
        embed.add_field(name="Roles", value=roles_text[:1024], inline=False)
        embed.set_footer(text=f"ID: {member.id}")

        try:
            await channel.send(embed=embed)
        except discord.Forbidden:
            pass


async def setup(bot):
    await bot.add_cog(OnMemberRemove(bot))
