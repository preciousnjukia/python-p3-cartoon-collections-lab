def roll_call_dwarves(names):
     for i, name in enumerate(names, start=1):
        print(f"{i}. {name}")

def summon_captain_planet(planeeter_calls):
    modified_calls = []

    for call in planeeter_calls:
        modified_call = call.capitalize() + "!"
        modified_calls.append(modified_call)

    return modified_calls

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
         return True
        
    return False

def find_the_cheese(ingredients):
    cheese_types = ["cheddar", "gouda", "camembert"]
    for ingredient in ingredients:
        if ingredient in cheese_types:
            return ingredient
    return None
