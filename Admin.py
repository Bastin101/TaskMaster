import GlobalFunctions
import os, json

async def CheckIfOwner(ctx):
    member = ctx.author 
    role_name = "owner" 

    has_role = any(role.name == role_name for role in member.roles)

    if has_role:
        return 

    else:
        await ctx.send("You are not allowed to use Owner commands :)")
        raise Exception("You do not have the required permission to use this command.")


import os
import json

async def startgame(ctx):
    folder_name = "SkillMasters"
    Jsonfile = f"{folder_name}/Database.json"

    if os.path.exists(Jsonfile):
        text = "Game already started"
        await GlobalFunctions.simple_embed(ctx, text)
        return


async def startgame(ctx):
    folder_name = "SkillMasters"
    Jsonfile = f"{folder_name}/Database.json"

    if os.path.exists(Jsonfile):
        text = "Game already started"
        await GlobalFunctions.simple_embed(ctx, text)
        return

   
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    with open(Jsonfile, "w") as file:
        json.dump({}, file, indent=4)


    text = "Startup done"
    await GlobalFunctions.simple_embed(ctx, text)
