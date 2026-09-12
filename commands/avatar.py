import discord
from discord.ext import commands


class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="avatar")
    async def avatar(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        embed = discord.Embed(title=f"{member.display_name}'s Avatar", color=member.color)
        embed.set_image(url=member.display_avatar.url)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.display_avatar.url)
        view = discord.ui.View()
        view.add_item(discord.ui.Button(label="Open in Browser", url=member.display_avatar.url))
        await ctx.send(embed=embed, view=view)


async def setup(bot):
    await bot.add_cog(Avatar(bot))
