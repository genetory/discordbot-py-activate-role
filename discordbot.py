from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
from discord.ext import commands
from discord.ui import Button, View, Modal, TextInput
from discord.enums import ButtonStyle
from discord import Interaction, ui, app_commands

load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

class my_modal(ui.Modal, title="🔒 Enter the code"):
    answer = ui.TextInput(label="Role Code (8자리)", 
                          style=discord.TextStyle.short,
                          placeholder="Role Code (8자리)", 
                          required=True)
    
    async def on_submit(self, interaction: Interaction, /) -> None:
        member = interaction.user
        
        value = self.answer.value
        if value == "l902yqds": #선미야 홀더
            role = discord.utils.get(interaction.guild.roles, id=1083199181839143102)
        elif value == "xkvcx5yq": #메토드 홀더
            role = discord.utils.get(interaction.guild.roles, id=1084807036635721808)
        elif value == "c77yznku": #팔라 홀더
            role = discord.utils.get(interaction.guild.roles, id=1084807187773259817)
        elif value == "jbj2m5aj": #슈퍼위크 홀더
            role = discord.utils.get(interaction.guild.roles, id=1084807391599673394)
        elif value == "ti5o3jbj": #스니커즈 홀더
            role = discord.utils.get(interaction.guild.roles, id=1084806863863951431)
        elif value == "pl0w3zdw": #시티즌 홀더
            role = discord.utils.get(interaction.guild.roles, id=1084808172079960115)
        elif value == "vjyvgv6t": #알파크루즈 홀더
            role = discord.utils.get(interaction.guild.roles, id=1084808080094670929)
        elif value == "pey4szow": #LN 홀더
            role = discord.utils.get(interaction.guild.roles, id=1085086336857423962)
        elif value == "xo2ekz93": #GGLabs
            role = discord.utils.get(interaction.guild.roles, id=1084791050670977126)
        else:
            await interaction.response.send_message(f"전달 받으신 코드를 다시 한번 확인해주세요!", ephemeral=True)
            return

        if role:
            await member.add_roles(role)
            await interaction.response.send_message(f"{member.mention}님에게 {role.mention} 역할을 추가했습니다.", ephemeral=True)
        else:
            await interaction.response.send_message(f"전달 받으신 코드를 다시 한번 확인해주세요!", ephemeral=True)

    
bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())


@bot.event
async def on_ready():
    print('Bot is ready')

@bot.command()
async def activate_role(ctx):
    codeButton = Button(style=ButtonStyle.green, label="🍻 Enter Code!")

    async def on_button_click(interaction):
        await interaction.response.send_modal(my_modal())
        
    codeButton.callback = on_button_click
    
    view = View()
    view.add_item(codeButton)

    await ctx.send('>>> 굳갱랩스에 오신 것을 환영합니다. 👋\n전달받으신 **Actviate Code**를 입력하세요!', view=view)

async def keep_alive():
    await client.wait_until_ready()
    while True:
        await client.ping() # Discord 서버에 ping을 보냄
        await asyncio.sleep(60) # 60초마다 실행

bot.loop.create_task(keep_alive())

        
try:
    bot.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
