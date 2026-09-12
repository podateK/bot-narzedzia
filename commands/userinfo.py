import discord
from discord.ext import commands


class UserInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="userinfo")
    async def userinfo(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        roles = [role.mention for role in member.roles[1:]]
        roles.reverse()

        embed = discord.Embed(title=f"User Info: {member}", color=member.color)
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.add_field(name="ID", value=member.id, inline=True)
        embed.add_field(name="Nickname", value=member.nick or "None", inline=True)
        embed.add_field(name="Bot", value="Yes" if member.bot else "No", inline=True)
        embed.add_field(name="Account Created", value=f"<t:{int(member.created_at.timestamp())}:R>", inline=True)
        embed.add_field(name="Joined Server", value=f"<t:{int(member.joined_at.timestamp())}:R>" if member.joined_at else "Unknown", inline=True)
        embed.add_field(name="Top Role", value=member.top_role.mention if member.top_role != ctx.guild.default_role else "None", inline=True)

        if member.premium_since:
            embed.add_field(name="Boosting Since", value=f"<t:{int(member.premium_since.timestamp())}:R>", inline=True)

        embed.add_field(
            name=f"Roles ({len(roles)})",
            value=", ".join(roles) if roles else "None",
            inline=False
        )
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(UserInfo(bot))
