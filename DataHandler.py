import nextcord
import json


async def xp_calc_next_lvl(level_from, level_to):
    points = 0
    output = 0  # Assign an initial value to 'output'
    level_from = int(level_from)
    level_to = int(level_to)
    while level_from <= level_to:
        points += level_from + 300.0 * (2.0 ** (level_from / 7.0))
        if level_from >= level_to:
            break  # Exit the loop when the condition is met
        level_from += 1
        output = points // 4
    
    return output


async def getpoints(user_id):
    # Specify the path to the JSON file
    json_file = "SkillMasters/Database.json"

    with open(json_file, "r") as file:
        data = json.load(file)

        if user_id in data:
            user_data = data[user_id]
            tasker_points = user_data["slayer_points"]
            streak = user_data["task_streak"]

            if streak % 5:
                tasker_points = tasker_points +5
            else:
                tasker_points = tasker_points +1
            # Update the JSON data with the modified user data
            with open(json_file, "w") as file:
                json.dump(data, file, indent=4)

            






def update_user_data(user_id, task_text):
    # Specify the path to the JSON file
    json_file = "SkillMasters/Database.json"

    with open(json_file, "r") as file:
        data = json.load(file)

    # Check if the user exists in the JSON data
    if user_id in data:
        user_data = data[user_id]
        user_data["slayer_status"] = True
        user_data["current_task"] = task_text
        user_data["task_progress"] = 0

        # Update the JSON data with the modified user data
        with open(json_file, "w") as file:
            json.dump(data, file, indent=4)




async def update_user_amount(user_id, amount):
    # Specify the path to the JSON file
    json_file = "SkillMasters/Database.json"

    with open(json_file, "r") as file:
        data = json.load(file)

    # Check if the user exists in the JSON data
    if user_id in data:
        user_data = data[user_id]
        task_progress = user_data["task_progress"]
        user_data["task_progress"] = task_progress + amount
        # Update the JSON data with the modified user data
        with open(json_file, "w") as file:
            json.dump(data, file, indent=4)



async def update_user_P_point(user_id, amount):
    # Specify the path to the JSON file
    json_file = "SkillMasters/Database.json"

    with open(json_file, "r") as file:
        data = json.load(file)

    # Check if the user exists in the JSON data
    if user_id in data:
        user_data = data[user_id]
        user_data["potentiel_points"] = amount
        # Update the JSON data with the modified user data
        with open(json_file, "w") as file:
            json.dump(data, file, indent=4)



async def is_silly(user_id):
    # Specify the path to the JSON file
    json_file = "SkillMasters/Database.json"

    with open(json_file, "r") as file:
        data = json.load(file)

    # Check if the user exists in the JSON data
    if user_id in data:
        user_data = data[user_id]
        silly =  user_data["silly"]
        return silly 


async def is_task(user_id):
    # Specify the path to the JSON file
    json_file = "SkillMasters/Database.json"

    with open(json_file, "r") as file:
        data = json.load(file)

    # Check if the user exists in the JSON data
    if user_id in data:
        user_data = data[user_id]
        slayer_status =  user_data["slayer_status"]
        return slayer_status 






def generate_leaderboard_embed(data):
    # Sort the user data based on "xp" in descending order (highest first)
    sorted_users = sorted(data.values(), key=lambda x: x["xp"], reverse=True)

    # Create an embed to display the leaderboard
    embed = nextcord.Embed(title="Leaderboard", description="Top Users by XP", color=0x00FF00)

    # Add each user to the embed with their rank, name, xp, and level
    for rank, user in enumerate(sorted_users, start=1):
        if user["xp"] > 9999 or user["xp"] < 0:
            user_name = user["user_name"]
            xp = user["xp"]
            level = user["level"]
            level_size = len(str(level))
            embed.add_field(name=f"Rank {rank}", value=f"{user_name}\nLvL: {level} {'-'*(4-level_size)}--------XP: {xp}", inline=False)

    return embed




