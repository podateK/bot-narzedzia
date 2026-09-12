import discord
from discord.ext import commands


class OnReady(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Logged in as {self.bot.user} (ID: {self.bot.user.id})")
        print(f"Connected to {len(self.bot.guilds)} server(s)")
        print(f"Total users: {sum(g.member_count for g in self.bot.guilds)}")
        await self.bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name=f"{len(self.bot.guilds)} servers | .help"
            )
        )


async def setup(bot):
    await bot.add_cog(OnReady(bot))
