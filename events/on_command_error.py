import discord
from discord.ext import commands


class OnCommandError(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(
                title="Command Not Found",
                description=f"Unknown command. Use `.help` to see available commands.",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed, delete_after=10)

        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title="Missing Argument",
                description=f"Missing required argument: `{error.param.name}`\nUsage: `.{ctx.command.qualified_name} {ctx.command.signature}`",
                color=discord.Color.orange()
            )
            await ctx.send(embed=embed, delete_after=15)

        elif isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                title="Bad Argument",
                description=f"Invalid argument provided.\nUsage: `.{ctx.command.qualified_name} {ctx.command.signature}`",
                color=discord.Color.orange()
            )
            await ctx.send(embed=embed, delete_after=15)

        elif isinstance(error, commands.MissingPermissions):
            missing = ", ".join(error.missing_permissions)
            embed = discord.Embed(
                title="Missing Permissions",
                description=f"You need the following permissions to use this command:\n`{missing}`",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed, delete_after=15)

        elif isinstance(error, commands.BotMissingPermissions):
            missing = ", ".join(error.missing_permissions)
            embed = discord.Embed(
                title="Bot Missing Permissions",
                description=f"I need the following permissions:\n`{missing}`",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed, delete_after=15)

        elif isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(
                title="Cooldown",
                description=f"This command is on cooldown. Try again in **{error.retry_after:.1f}s**.",
                color=discord.Color.orange()
            )
            await ctx.send(embed=embed, delete_after=15)

        elif isinstance(error, commands.NotOwner):
            embed = discord.Embed(
                title="Owner Only",
                description="This command can only be used by the bot owner.",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed, delete_after=15)

        elif isinstance(error, commands.NoPrivateMessage):
            embed = discord.Embed(
                title="DM Only",
                description="This command can only be used in a server.",
                color=discord.Color.red()
            )
            await ctx.author.send(embed=embed)

        else:
            embed = discord.Embed(
                title="Error",
                description=f"An unexpected error occurred:\n```{error}```",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed, delete_after=15)
            raise error


async def setup(bot):
    await bot.add_cog(OnCommandError(bot))
