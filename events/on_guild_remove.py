import discord
from discord.ext import commands


class OnGuildRemove(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        print(f"Removed from guild: {guild.name} (ID: {guild.id}) | Members: {guild.member_count}")


async def setup(bot):
    await bot.add_cog(OnGuildRemove(bot))
