import discord
from discord.ext import commands


class VerifyUI(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Verify", emoji="<a:Yes_DLC:833322133648179201>", style=discord.ButtonStyle.blurple)
    async def verify(self, ctx: discord.Interaction, button: discord.ui.Button):
        if ctx.guild.get_role(825355424836354066) in ctx.user.roles:
            await ctx.response.send_message(
                embed=discord.Embed(
                    title="",
                    description="<a:No_DLC:833322134050177024> Unable to verify | You are currently muted in the server"
                ),
                ephemeral=False
            )
        if not ctx.guild.get_role(825355424827310090) in ctx.user.roles:
            await ctx.response.send_message(
                embed=discord.Embed(
                    title="",
                    description="<a:Yes_DLC:833322133648179201> Added the role `Verified`",
                    color=discord.Color.green(),
                )
                ,ephemeral=True
            )
            await ctx.user.add_roles(ctx.guild.get_role(825355424827310090))
            return
        else:
            await ctx.response.send_message(
                embed=discord.Embed(
                    title="",
                    description="<:Info_DLC:859281354519478302> No changes has been made | You have already been verified.",
                ),
                ephemeral=True
            )
            return


class verify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        guild = self.bot
    
    @commands.command()
    async def verifymessage(self, ctx: commands.Context, channel: discord.TextChannel = None):
        if channel is None:
            channel = ctx.channel
        embed = discord.Embed(
            title="Verification",
            description="By pressing the button below this message, You agree to be pinged by anyone in this server and you agree to abide by ALL of the laws above. Additionally, You also agree to be sent a friend request by Fasty when you leave the server and a DM If you accept it.\n\nhttps://discord.gg/8bedEJyaCu = Our Invite Link\n\nPlease DM DLC ModMail For any inquires, questions or if you would like to gain your roles back from the old DLC.\n\nPlease enjoy your stay in the DLC. \n- Moderation Team",
            color=0x00FFFF,
        ) 
        
        embed.set_author(name="Discord Leisure Centre")
        embed.set_footer(text="Formality Is Professionality")
        view = VerifyUI()
        await channel.send(embed=embed, view=view)

    @commands.command()
    @commands.has_role(825355424836354058)
    async def verify(self, ctx, member:discord.Member):
        verify = discord.utils.get(ctx.guild.roles, name = "Verified")
        await member.add_roles(verify)
        await ctx.send(f"Sucessfully verified the user: `{member.name}#{member.discriminator}`")


async def setup(bot):
    await bot.add_cog(verify(bot))
