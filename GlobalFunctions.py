import os, json
import nextcord




async def simple_embed(ctx, text):

        # Create an embed with a single field and no title
        embed = nextcord.Embed(color=nextcord.Color.orange())
        embed.add_field(name="**Bot**", value=text, inline=False)
        await ctx.send(embed=embed)


async def joingame(ctx):
    folder_name = "SkillMasters"
    json_file = f"{folder_name}/Database.json"
    user_id = str(ctx.author.id)
    user_name = ctx.author.name

    if not os.path.exists(json_file):
        # File doesn't exist, create it
         await ctx.send("The game has not started yet.")
         return

    # Read the existing data from the JSON file
    with open(json_file, "r") as file:
        data = json.load(file)

    if user_id in data:
        text = "You are already in the game!"
        await simple_embed(ctx, text)
        return

    # Add the user to the data with initial values
    data[user_id] = {
        "user_name": user_name,
        "user_id": user_id,
        "level": 1,
        "xp": 0,
        "xp_to_next_lvl": 98,
        "slayer_status": False,
        "current_task": "Idle",
        "potentiel_points": 0,
        "task_progress": "",
        "slayer_points": 0,
        "unlocks": "",
        "task_streak": 0,
        "silly": False
    }

    # Write the updated data back to the JSON file
    with open(json_file, "w") as file:
        json.dump(data, file, indent=4)

    text = "You have joined the game!"
    await   simple_embed(ctx, text)




      

async def Audiolog(ctx, person, action, task):
    channel = ctx.bot.get_channel(1147478916110483509)
    embed = nextcord.Embed(color=nextcord.Color.orange())
    text = (f"{action} {task}")
    embed.add_field(name=f"**{person}**", value=text, inline=False)

    await channel.send(embed=embed)
