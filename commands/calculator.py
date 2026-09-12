import discord
import ast
import operator
from discord.ext import commands


SAFE_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}


def safe_calc(node):
    if isinstance(node, ast.Expression):
        return safe_calc(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in SAFE_OPS:
        left = safe_calc(node.left)
        right = safe_calc(node.right)
        return SAFE_OPS[type(node.op)](left, right)
    if isinstance(node, ast.UnaryOp) and type(node.op) in SAFE_OPS:
        return SAFE_OPS[type(node.op)](safe_calc(node.operand))
    raise ValueError("Unsupported expression")


class Calculator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="calc")
    async def calc(self, ctx, *, expression: str = None):
        if not expression:
            await ctx.send("Usage: `.calc <expression>`\nExample: `.calc 2 + 2 * 3`")
            return

        try:
            tree = ast.parse(expression, mode="eval")
            result = safe_calc(tree)
            embed = discord.Embed(title="Calculator", color=discord.Color.green())
            embed.add_field(name="Input", value=f"```{expression}```", inline=False)
            embed.add_field(name="Output", value=f"```{result}```", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.display_name}", icon_url=ctx.author.display_avatar.url)
            await ctx.send(embed=embed)
        except ZeroDivisionError:
            await ctx.send("Error: Division by zero!")
        except (ValueError, SyntaxError, TypeError) as e:
            await ctx.send(f"Error: Invalid expression. `{e}`")


async def setup(bot):
    await bot.add_cog(Calculator(bot))
