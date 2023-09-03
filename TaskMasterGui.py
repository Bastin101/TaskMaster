import nextcord
import datetime
from nextcord.ext import commands, tasks
from nextcord.ui import Button, View
import os, json
import random
import DataHandler
import GlobalFunctions
from nextcord import File
number = 1
user_data = {}
name = ""
level = ""
xp = ""
xp_to_next_lvl = ""
Slayer_status = ""
master_task = ""
folder_name = "SkillMasters"
amount_arr = [1,5,10,50,100]
counter = 0


async def get_player_info(user_id):
    global name, level, xp, xp_to_next_lvl, Slayer_status, master_task
    json_file = f"{folder_name}/Database.json"
    with open(json_file, "r") as file:
        data = json.load(file)
        user_data = data[user_id]
        name = user_data["user_name"]
        level = user_data["level"]
        xp = user_data["xp"]
        xp_to_next_lvl = user_data["xp_to_next_lvl"]
        Slayer_status = user_data["slayer_status"]
        master_task = user_data["current_task"]
        task_progress = user_data["task_progress"]
        return name, level, xp, xp_to_next_lvl, Slayer_status, master_task, task_progress


async def increase_Fluw_timeout():
    file_path = "fluw_timeout.txt"
    timeout = 1

    # Check if the file exists
    if os.path.exists(file_path):
        # Read the timeout value from the file
        with open(file_path, "r") as file:
            timeout = int(file.read())

        # Increase the timeout by 1
        timeout += 1

    # Write the updated timeout value to the file
    with open(file_path, "w") as file:
        file.write(str(timeout))

    return timeout





async def show_embed_gui(ctx, bot):
    # Declare the variables as global
    global name, level, xp, xp_to_next_lvl, Slayer_status, master_task

    # Get user information from the JSON file
    user_id = str(ctx.author.id)
    json_file = f"{folder_name}/Database.json"

    with open(json_file, "r") as file:
        data = json.load(file)

    # Check if the user exists in the JSON data
    if user_id in data:
        user_data = data[user_id]
        slayer_points = user_data["slayer_points"]
        name, level, xp, xp_to_next_lvl, Slayer_status, master_task, task_progress = await get_player_info(user_id)

        # FIRST Embed
        embed1 = nextcord.Embed(title=name, description='User Infomation:')
        # Set the user's profile picture as the embed's thumbnail
        user = bot.get_user(ctx.author.id)
        if ctx.author.avatar:
            embed1.set_thumbnail(url=ctx.author.avatar.url)
        else:
            # Set a default thumbnail URL or leave it empty
            embed1.set_thumbnail(url='https://www.pngmart.com/files/11/Grumpy-Cat-PNG-Pic.png')

        # Add fields for level, xp, and xp to next level
        embed1.add_field(name="Level", value=level, inline=False)
        embed1.add_field(name="XP", value=xp, inline=False)
        embed1.add_field(name="Tasker points", value=slayer_points, inline=False)
        embed1.add_field(name="XP until Next Level", value=xp_to_next_lvl, inline=False)




        # 2. Embed 
        embed2 = nextcord.Embed(title='Taskmasters', description='Level Requirements.')
        logo_filename = "Logos/SillyHat.png"
        file = File(logo_filename, filename="logo.png")
        embed2.set_thumbnail(url="attachment://logo.png")
        # Add taskmasters with their level requirements
        taskmasters = {
            "Bastin": 1,
            "Liet": 10,
            "Swaggy": 25,
            "Blemma": 30,
            "Becs": 50,
            "Qridan": 70,
                }

        for taskmaster, level_requirement in taskmasters.items():
            embed2.add_field(
            name=taskmaster, value=f"Level Requirement: {level_requirement}", inline=False
            )


        

    #Embed3
        description = "```md\n"
        description += "| Item            | Price |\n"
        description += "|-----------------|-------|\n"
        description += "| Skip task       | 3     |\n"
        """description += "| Tasker Staff    | 600   |\n"""
        """description += "| Double Trouble  | 9999  |\n"""
        description += "| Timeout Flurraw | 2     |\n"
        description += "| Timeout Liet    | 10    |\n"
        """description += "| Magebit boots   | 2000  |\n"""
        description += "| Tasker hat      | 20    |\n"
        """description += "| Luck potion     | 2500  |\n"""
        description += "|-----------------|-------|\n"
        description += "```"
        embed3 = nextcord.Embed(title='Reward Shop', description=description)





        # Embed 4
        embed4 = nextcord.Embed(title=name, description='')
        master_task = ""
        task_progress = ""
        await get_player_info(user_id)
        embed4.add_field(name="Your task: ", value=master_task, inline=False)
        embed4.add_field(name="Current amount: ", value=task_progress, inline=False)









        async def switch_to_embed1(interaction):
            view = nextcord.ui.View(timeout=None)
            view.add_item(button1)
            view.add_item(button2)
            view.add_item(button3)
            view.add_item(button4)
        
            if interaction.user.id == ctx.author.id:
                user_id = str(ctx.author.id)
                json_file = f"{folder_name}/Database.json"

                with open(json_file, "r") as file:
                    data = json.load(file)
        
                if user_id in data:
                    user_data = data[user_id]
                    name = user_data["user_name"]
                    level = user_data["level"]
                    xp = user_data["xp"]
                    xp_to_next_lvl = user_data["xp_to_next_lvl"]
                    slayer_points = user_data["slayer_points"]

                    embed1 = nextcord.Embed(title=name, description='User Infomation:')
                    user = bot.get_user(ctx.author.id)
                    if ctx.author.avatar:
                        embed1.set_thumbnail(url=ctx.author.avatar.url)
                    else:
                        embed1.set_thumbnail(url='https://www.pngmart.com/files/11/Grumpy-Cat-PNG-Pic.png')

                    embed1.add_field(name="Level", value=level, inline=False)
                    embed1.add_field(name="XP", value=xp, inline=False)
                    embed1.add_field(name="Tasker points", value = slayer_points, inline=False)
                    embed1.add_field(name="XP until Next Level", value=xp_to_next_lvl, inline=False)

                    await interaction.message.edit(view=view, embed=embed1)
                else:
                    await interaction.response.send_message("You are not in the game!")




        async def switch_to_embed2(interaction):
            view = nextcord.ui.View(timeout=None)
            if interaction.user.id == ctx.author.id:
                if await DataHandler.is_silly(user_id):
                    embed2.set_thumbnail(url='https://oldschool.runescape.wiki/images/Silly_jester_hat_detail.png?d100a')
                # Remove the thumbnail by setting url to None
                await interaction.message.edit(embed=embed2)

                # Update the message view
                view = MyView(ctx)
                if user_id in data:
                    name, level, xp, xp_to_next_lvl, Slayer_status, master_task, task_progress = await get_player_info(user_id)
                    if Slayer_status:
                        view = nextcord.ui.View(timeout=None)  # Create a new empty View object
                    view.add_item(button1)
                    view.add_item(button2)
                    view.add_item(button3)
                    view.add_item(button4)
                    await interaction.message.edit(view=view)

        async def switch_to_embed3(interaction):

            view = nextcord.ui.View(timeout=None)  # Create a new empty View object
            view = MyShop(ctx)
            view.add_item(button1)
            view.add_item(button2)
            view.add_item(button3)
            view.add_item(button4)
            if interaction.user.id == ctx.author.id:
                if await DataHandler.is_silly(user_id):
                    embed3.set_thumbnail(url='https://oldschool.runescape.wiki/images/Silly_jester_hat_detail.png?d100a')
                await interaction.message.edit(view=view, embed=embed3)
        


        async def switch_to_embed4(interaction):
            user_id = str(ctx.author.id)
            view = nextcord.ui.View(timeout=None)
            view.add_item(button1)
            view.add_item(button2)
            view.add_item(button3)
            view.add_item(button4)
            if await DataHandler.is_task(user_id):
                view.add_item(button5)
                view.add_item(button6)
                view.add_item(button7)
                view.add_item(button8)
                view.add_item(button9)
            # Get user information from the interaction object
            user_id = str(interaction.user.id)
            json_file = f"{folder_name}/Database.json"

            with open(json_file, "r") as file:
                data = json.load(file)

            # Check if the user exists in the JSON data
            if user_id in data:
                name, level, xp, xp_to_next_lvl, Slayer_status, master_task, task_progress = await get_player_info(user_id)

                # Update the embed4 object with the current task
                embed4 = nextcord.Embed(title=name, description='')
                embed4.add_field(name="Your task:", value=master_task, inline=False)
                embed4.add_field(name="Current progress:", value=task_progress, inline=False)
                # Send the updated embed4 as a response to the interaction
                if await DataHandler.is_silly(user_id):
                    embed4.set_thumbnail(url='https://oldschool.runescape.wiki/images/Silly_jester_hat_detail.png?d100a')

                await interaction.message.edit(embed=embed4,view=view)
            else:
                await interaction.response.send_message("You are not in the game!")

        async def edit_num(interaction):
            if interaction.user.id == ctx.author.id:
                global counter
                global amount_arr
                await DataHandler.update_user_amount(user_id, amount_arr[counter])
                embed4 = nextcord.Embed()
                name, level, xp, xp_to_next_lvl, Slayer_status, master_task, task_progress = await get_player_info(user_id)
                embed4 = nextcord.Embed(title=name, description='')
                embed4.add_field(name="Your task:", value=master_task, inline=False)
                embed4.add_field(name="Current progress:", value=task_progress, inline=False)
                if await DataHandler.is_silly(user_id):
                    embed4.set_thumbnail(url='https://oldschool.runescape.wiki/images/Silly_jester_hat_detail.png?d100a')
                await interaction.message.edit(embed=embed4)






        async def amount_add(interaction):
            global counter
            global number
            if interaction.user.id == ctx.author.id:
                if counter < len(amount_arr) - 1:
                    counter += 1
                else:
                    counter = 0

                number = amount_arr[counter]
                button5.label = str(number)
                view = nextcord.ui.View(timeout=None)
                view.add_item(button1)
                view.add_item(button2)
                view.add_item(button3)
                view.add_item(button4)
                view.add_item(button5)
                view.add_item(button6)
                view.add_item(button7)
                view.add_item(button8)
                view.add_item(button9)
                await interaction.message.edit(view=view)




        async def Reset_number(interaction):
            if interaction.user.id == ctx.author.id:
                name, level, xp, xp_to_next_lvl, Slayer_status, master_task, task_progress = await get_player_info(user_id)

                await DataHandler.update_user_amount(user_id, -task_progress)
                embed4 = nextcord.Embed()
                embed4 = nextcord.Embed(title=name, description='')
                embed4.add_field(name="Your task:", value=master_task, inline=False)
                embed4.add_field(name="Current progress:", value=0, inline=False)
                if await DataHandler.is_silly(user_id):
                    embed4.set_thumbnail(url='https://oldschool.runescape.wiki/images/Silly_jester_hat_detail.png?d100a')
                await interaction.message.edit(embed=embed4)
        async def Skip_task(interaction):
            if interaction.user.id == ctx.author.id:
                json_file = f"{folder_name}/Database.json"
                with open(json_file, "r") as file:
                    data = json.load(file)
                    user_data = data[user_id]
                    xp_to_give = user_data["potentiel_points"]
                    Users_xp = user_data["xp"]
                    Users_for_lvl = user_data["xp_to_next_lvl"]
                    user_lvl = user_data["level"]
                    new_xp = Users_xp - (int(xp_to_give)*2)
                    Users_for_lvl = await DataHandler.xp_calc_next_lvl(1, user_lvl+1)
                    while Users_for_lvl <= new_xp:
                        user_lvl += 1  # Increment level when condition is true
                        user_lvl_to = user_lvl + 1
                        Users_for_lvl = await DataHandler.xp_calc_next_lvl(1, user_lvl_to)

                    if user_id in data:
                        user_data = data[user_id]
                        user_data["xp"] = new_xp
                        user_data["level"] = user_lvl  # Assign updated level value to user_data["level"]
                        user_data["xp_to_next_lvl"] = int(Users_for_lvl)
                        user_data["slayer_status"] = False
                        user_data["current_task"] = ""
                        user_data["potentiel_points"] = ""
                        # Write the updated data back to the JSON file
                        await GlobalFunctions.Audiolog(ctx, name, "Skipped their task...", "noob")
                        with open(json_file, "w") as file:
                            json.dump(data, file, indent=4)
                        await switch_to_embed1(interaction)


            await switch_to_embed1(interaction)


        async def Finish_task(interaction):
            if interaction.user.id == ctx.author.id:
                json_file = f"{folder_name}/Database.json"
                with open(json_file, "r") as file:
                    data = json.load(file)
                    user_data = data[user_id]
                    xp_to_give = user_data["potentiel_points"]
                    Users_xp = user_data["xp"]
                    Users_for_lvl = user_data["xp_to_next_lvl"]
                    user_lvl = user_data["level"]
                    user_points = user_data["slayer_points"]
                    user_unlocks = user_data["unlocks"]
                    user_task_streak = user_data["task_streak"]
                    current_task = user_data["current_task"]
                    new_xp = int(xp_to_give) + Users_xp
                    await GlobalFunctions.Audiolog(ctx, name, "finished their task \n", current_task)
                    Users_for_lvl = await DataHandler.xp_calc_next_lvl(1, user_lvl+1)
                    while Users_for_lvl <= new_xp:
                        user_lvl += 1  # Increment level when condition is true
                        await GlobalFunctions.Audiolog(ctx, name, "Gained level", user_lvl)
                        user_lvl_to = user_lvl + 1
                        Users_for_lvl = await DataHandler.xp_calc_next_lvl(1, user_lvl_to)

                        


                    user_lvl_to = user_lvl + 1
                    Users_for_lvl = await DataHandler.xp_calc_next_lvl(user_lvl, user_lvl_to)
                    if user_id in data:
                        user_data = data[user_id]
                        user_data["xp"] = new_xp
                        user_data["level"] = user_lvl  # Assign updated level value to user_data["level"]
                        user_data["xp_to_next_lvl"] = int(Users_for_lvl)
                        user_data["slayer_status"] = False
                        user_data["current_task"] = ""
                        user_data["potentiel_points"] = ""
                        if user_unlocks == "Tasker Hat":
                            user_task_streak = user_task_streak +1
                            if user_task_streak >= 5:
                                user_data["slayer_points"] = int(user_points) + 5
                                user_task_streak = 0
                            else:
                                user_data["slayer_points"] = int(user_points) + 1
                            user_data["task_streak"] = user_task_streak
                        else:
                            user_data["slayer_points"] = int(user_points) + 1

                        # Write the updated data back to the JSON file
                        with open(json_file, "w") as file:
                            json.dump(data, file, indent=4)
                        await switch_to_embed1(interaction)



        view = View()
        button1 = Button(label='User Info', custom_id='embed1', style=nextcord.ButtonStyle.secondary)
        button1.callback = switch_to_embed1

        button2 = Button(label='Slayer Masters', custom_id='embed2', style=nextcord.ButtonStyle.secondary)
        button2.callback = switch_to_embed2

        button3 = Button(label='Reward Shop', custom_id='embed3', style=nextcord.ButtonStyle.secondary)
        button3.callback = switch_to_embed3

        button4 = Button(label='Task', custom_id='embed4', style=nextcord.ButtonStyle.secondary)
        button4.callback = switch_to_embed4


        button5 = Button(label=number, custom_id='amount', style=nextcord.ButtonStyle.secondary, row=2)
        button5.callback = amount_add

        button6 = Button(label='Add', custom_id='add_number', style=nextcord.ButtonStyle.secondary, row=2)
        button6.callback = edit_num

        button7 = Button(label='Reset', custom_id='Reset_num', style=nextcord.ButtonStyle.secondary, row=2)
        button7.callback = Reset_number

        button8 = Button(label='Finish Task', custom_id='Finish_task', style=nextcord.ButtonStyle.blurple, row=2)
        button8.callback = Finish_task

        button9 = Button(label='Skip Task', custom_id='Skip_task', style=nextcord.ButtonStyle.red, row=2)
        button9.callback = Skip_task

        view.add_item(button1)
        view.add_item(button2)
        view.add_item(button3)
        view.add_item(button4)







        class MyShop(nextcord.ui.View):
            def __init__(self, ctx):
                super().__init__()

                self.ctx = ctx
            @nextcord.ui.select(# the decorator that lets you specify the properties of the select menu
                placeholder = "Select reward", # the placeholder text that will be displayed if nothing is selected
                min_values = 1, # the minimum number of values that must be selected by the users
                max_values = 1, # the maximum number of values that can be selected by the users
                options = [ # the list of options from which users can choose, a required field
                    nextcord.SelectOption(
                        label="Skip Task",
                        description="3 gp: Read the label, duh"
                    ),
                    nextcord.SelectOption(
                        label="Timeout Liet",
                        description="15 gp: need a 5 min break?"
                    ),
                    nextcord.SelectOption(
                        label="Timeout Flurraw",
                        description="2 gp: For 1 sec?? it increses with 1 sec everytime"
                    ),
                    nextcord.SelectOption(
                        label="Tasker Hat",
                        description="20 gp: every 5 tasks gives bonus GP"
                    ),
                    nextcord.SelectOption(
                        label="Option 5?",
                        description="Type suggestions in the suggestion chat"

                    )
                ]

            )
            async def select_callback(self, select, interaction):
                selected_option = select.values[0]
                user_id = str(interaction.user.id)

                # Dictionary to store "gp" values for each option
                gp_values = {
                    "Skip Task": 3,
                    "Timeout Liet": 15,
                    "Timeout Flurraw": 2,
                    "Tasker Hat": 20,
                    "Option 5?": 0,  # This option doesn't require any "gp" points
                }

                # Check if the selected option exists in the gp_values dictionary
                if selected_option in gp_values:
                    required_gp = gp_values[selected_option]

                    # Get user information from the JSON file
                    json_file = f"{folder_name}/Database.json"

                    with open(json_file, "r") as file:
                        data = json.load(file)

                    # Check if the user exists in the JSON data
                    if user_id in data:
                        user_data = data[user_id]
                        user_gp = user_data.get("slayer_points", 0)

                        if user_gp >= required_gp:
                            # Deduct the required "gp" points from the user
                            user_data["slayer_points"] = user_gp - required_gp

                            # Write the updated data back to the JSON file
                            with open(json_file, "w") as file:
                                json.dump(data, file, indent=4)

                            # Execute the action for the selected option
                            if selected_option == "Skip Task":
                                await GlobalFunctions.Audiolog(ctx, name, "bought", "Skip Task")
                                if user_id in data:
                                    user_data = data[user_id]
                                    user_data["slayer_status"] = False
                                    user_data["current_task"] = ""
                                    user_data["potentiel_points"] = ""
                                    user_data["task_streak"] = 0
                                    # Write the updated data back to the JSON file
                                    with open(json_file, "w") as file:
                                        json.dump(data, file, indent=4)

                            elif selected_option == "Timeout Liet":
                                member_id = 302235821367361536
                                time = 300
                                member = ctx.guild.get_member(member_id)
                                if member is not None:
                                    await member.edit(timeout=nextcord.utils.utcnow() + datetime.timedelta(seconds=time))
                                    channel = self.ctx.bot.get_channel(1134533312359174144)
                                    await channel.send(f"Liet got a timeout")

                            elif selected_option == "Timeout Flurraw":
                                # Get the increased timeout value
                                liet_timeout = await increase_Fluw_timeout()
                                member_id = 145345772995477504
                                member = ctx.guild.get_member(member_id)
                                if member is not None:
                                    await member.edit(timeout=nextcord.utils.utcnow() + datetime.timedelta(seconds=liet_timeout))
                                channel = self.ctx.bot.get_channel(1134533312359174144)
                                await channel.send(f"Flurraw got a {liet_timeout} sec timeout!")


                            elif selected_option == "Tasker Hat":
                                json_file = f"{folder_name}/Database.json"
                                with open(json_file, "r") as file:
                                    data = json.load(file)
            
                                if user_id in data:
                                    user_data = data[user_id]
                                    user_data["unlocks"] = "Tasker Hat"

                                        # Write the updated data back to the JSON file
                                    with open(json_file, "w") as file:
                                        json.dump(data, file, indent=4)



                            # Option 5? doesn't require any action

                            elif selected_option == "Option 5?":
                                json_file = f"{folder_name}/Database.json"
                                if user_id in data:
                                    user_data = data[user_id]
                                    gp = user_data["slayer_points"]
                                    if gp < 200:
                                        await interaction.response.send_message("You do not have enough gp for the Hat-DLC", ephemeral=True)

                                    else:
                                        await interaction.response.send_message("200 gp lost? Gz? here is your hat.. i guess", ephemeral=True)
                                        user_data["slayer_points"] = gp - 200
                                        user_data["silly"] = True
                                        # Write the updated data back to the JSON file
                                        with open(json_file, "w") as file:
                                            json.dump(data, file, indent=4)


                        else:
                            await self.ctx.send(f"You don't have enough gp to select {selected_option}.")

                    else:
                        await self.ctx.send("You are not in the game!")

                else:
                    await self.ctx.send("Invalid option selected.")


























        class MyView(nextcord.ui.View):
            def __init__(self, ctx):
                super().__init__()

                self.ctx = ctx
            @nextcord.ui.select(# the decorator that lets you specify the properties of the select menu
                placeholder = "Select TaskerMaster to get task from", # the placeholder text that will be displayed if nothing is selected
                min_values = 1, # the minimum number of values that must be selected by the users
                max_values = 1, # the maximum number of values that can be selected by the users
                options = [ # the list of options from which users can choose, a required field
                    nextcord.SelectOption(
                        label="Bastin",
                        description="Lvl 1 Bastin: Afk"
                    ),
                    nextcord.SelectOption(
                        label="Liet",
                        description="Lvl 10 Liet: Pvm"
                    ),
                    nextcord.SelectOption(
                        label="Swaggy",
                        description="Lvl 25 Swaggy: trolling"
                    ),
                    nextcord.SelectOption(
                        label="Blemma",
                        description="Lvl 30 Blemma: Skilling"
                    ),
                    nextcord.SelectOption(
                        label="Becs",
                        description="Lvl 50 Becs: PvP/wild"
                    ),
                    nextcord.SelectOption(
                        label="Qridan",
                        description="Lvl 70 Qridan: Items/clues (winner of OsrsGames V1)"
                    )
                ]

            )
            async def select_callback(self, select, interaction):
                if interaction.user.id == self.ctx.author.id:
                    selected_person = select.values[0]

                    # Get user information from the JSON file
                    user_id = str(self.ctx.author.id)
                    json_file = f"{folder_name}/Database.json"

                    with open(json_file, "r") as file:
                        data = json.load(file)

                    # Check if the user exists in the JSON data
                    if user_id in data:
                        user_data = data[user_id]
                        level = user_data["level"]

                        # Check if the user has the required level for the selected person
                        taskmasters = {
                            "Bastin": 1,
                            "Liet": 10,
                            "Swaggy": 25,
                            "Blemma": 30,
                            "Becs": 50,
                            "Qridan": 70,
                        }
                        if os.path.exists(f"/home/pi/Desktop/SkillMaster/SkillMasters/{selected_person}.json"):
                            with open(f"/home/pi/Desktop/SkillMaster/SkillMasters/{selected_person}.json", "r") as file:
                        #if os.path.exists(f"C:/Users/jacob/Desktop/github/SkillMaster/SkillMasters/{selected_person}.json"):
                        #    with open(f"C:/Users/jacob/Desktop/github/SkillMaster/SkillMasters/{selected_person}.json", "r") as file:
                                data = json.load(file)
                                tasks = data["tasks"]
                        else:
                            print("error file not found")

                        if level < 96:
                            if selected_person in taskmasters:
                                required_level = taskmasters[selected_person]
                                if level >= required_level:
                                    accessible_tasks = []

                                    if level < (required_level+10):
                                        accessible_tasks = random.sample(tasks[:min(10, len(tasks))], 1)
                                    else:
                                        accessible_tasks = tasks[:level - required_level]
                                        accessible_tasks = random.sample(accessible_tasks, 1)
                                        

                                    task_text = "\n".join([f"{task['index']}. {task['task']} - {task['points']} xp" for task in accessible_tasks])
                                    amount = ', '.join(str(task['points']) for task in accessible_tasks)
                                    DataHandler.update_user_data(user_id, task_text)
                                    await DataHandler.update_user_P_point(user_id, amount)
                                    name, level, xp, xp_to_next_lvl, Slayer_status, master_task, task_progress = await get_player_info(user_id)
                                    await GlobalFunctions.Audiolog(ctx, name, f"Got the task from {selected_person} \n", task_text)
                                    embed4 = nextcord.Embed(title=name, description='')
                                    embed4.add_field(name="Your task:", value=master_task, inline=False)
                                    embed4.add_field(name="Current progress:", value=task_progress, inline=False)
                                    view = nextcord.ui.View(timeout=None)  # Create a new empty View object
                                    view.add_item(button1)
                                    view.add_item(button2)
                                    view.add_item(button3)
                                    view.add_item(button4)
                                    view.add_item(button5)
                                    view.add_item(button6)
                                    view.add_item(button7)
                                    view.add_item(button8)
                                    view.add_item(button9)
                                    if await DataHandler.is_silly(user_id):
                                        embed4.set_thumbnail(url='https://oldschool.runescape.wiki/images/Silly_jester_hat_detail.png?d100a')
                                    await interaction.response.edit_message(embed=embed4, view=view)


                                else:
                                    await interaction.response.send_message(f"You don't have the required level to select {selected_person}.")

                        else:
                            if selected_person in taskmasters:
                                required_level = taskmasters[selected_person]
                                if level >= required_level:
                                    accessible_tasks = []


                                    accessible_tasks = random.sample(tasks[:min(60, len(tasks))],1)
                                        

                                    task_text = "\n".join([f"{task['index']}. {task['task']} - {task['points']} xp" for task in accessible_tasks])
                                    amount = ', '.join(str(task['points']) for task in accessible_tasks)
                                    DataHandler.update_user_data(user_id, task_text)
                                    await DataHandler.update_user_P_point(user_id, amount)
                                    name, level, xp, xp_to_next_lvl, Slayer_status, master_task, task_progress = await get_player_info(user_id)
                                    await GlobalFunctions.Audiolog(ctx, name, "got the task", task_text)
                                    embed4 = nextcord.Embed(title=name, description='')
                                    embed4.add_field(name="Your task:", value=master_task, inline=False)
                                    embed4.add_field(name="Current progress:", value=task_progress, inline=False)
                                    view = nextcord.ui.View(timeout=None)  # Create a new empty View object
                                    view.add_item(button1)
                                    view.add_item(button2)
                                    view.add_item(button3)
                                    view.add_item(button4)
                                    view.add_item(button5)
                                    view.add_item(button6)
                                    view.add_item(button7)
                                    view.add_item(button8)
                                    view.add_item(button9)
                                    if await DataHandler.is_silly(user_id):
                                        embed4.set_thumbnail(url='https://oldschool.runescape.wiki/images/Silly_jester_hat_detail.png?d100a')
                                    await interaction.response.edit_message(embed=embed4, view=view)


                                else:
                                    await interaction.response.send_message(f"You don't have the required level to select {selected_person}.")


    message = await ctx.send(embed=embed1, view=view)














