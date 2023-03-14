import discord
from discord.ext import commands
from discord.ui import Button, View, Modal, TextInput
from discord.enums import ButtonStyle
import asyncio
from discord import Interaction, ui, app_commands

class my_modal(ui.Modal, title="🔒 Enter the code"):
    answer = ui.TextInput(label="Role Code (8자리)", 
                          style=discord.TextStyle.short,
                          placeholder="Role Code (8자리)", 
                          required=True)
    
    async def on_submit(self, interaction: Interaction, /) -> None:
        member = interaction.user
        
        value = self.answer.value
        if value == "코드":
            role = discord.utils.get(interaction.guild.roles, id=역할ID)
        elif value == "코드":
            role = discord.utils.get(interaction.guild.roles, id=역할ID)
        elif value == "코드": 
            role = discord.utils.get(interaction.guild.roles, id=역할ID)
        elif value == "코드": 
            role = discord.utils.get(interaction.guild.roles, id=역할ID)
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


bot.run('TOKEN')



