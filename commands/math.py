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


def safe_eval(node):
    if isinstance(node, ast.Expression):
        return safe_eval(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in SAFE_OPS:
        left = safe_eval(node.left)
        right = safe_eval(node.right)
        return SAFE_OPS[type(node.op)](left, right)
    if isinstance(node, ast.UnaryOp) and type(node.op) in SAFE_OPS:
        return SAFE_OPS[type(node.op)](safe_eval(node.operand))
    raise ValueError("Unsupported expression")


class Math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="math")
    async def math_cmd(self, ctx, *, expression: str):
        try:
            tree = ast.parse(expression, mode="eval")
            result = safe_eval(tree)
            embed = discord.Embed(title="Math Result", color=discord.Color.green())
            embed.add_field(name="Expression", value=f"```{expression}```", inline=False)
            embed.add_field(name="Result", value=f"```{result}```", inline=False)
            await ctx.send(embed=embed)
        except (ValueError, ZeroDivisionError, SyntaxError, TypeError) as e:
            await ctx.send(f"Error evaluating expression: {e}")


async def setup(bot):
    await bot.add_cog(Math(bot))
