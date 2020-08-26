import aiohttp
import asyncio
import json
import datetime


# Step 1 - update the user credentials
# main account
howard = {
    "HG_TOKEN": "k7e0InS5x4Jwz05LlZVW2s35u1y10POHOj3WeRfPo55BfC4SoDVqpGjfSJR8fD0y",
    "uh": "RdQtaaE8"
}



def filterResponse(response):
    if response['jsDialog']['tokens']['content']['value'] != None:
        return response['jsDialog']['tokens']['content']['value']
    return response

def processResponse(response):
    if response == "The right parts are used but the quantities aren't correct.":
        return False
    return True


# Update the output of the print crafting combinations, I'm too lazy to generalize it.
def print_craftingCombination(body):
    i_crystal_crucible = body['parts[crystal_crucible_crafting_item]']
    i_dragon_ember = body['parts[dragon_ember]']
    i_glass_shard = body['parts[glass_shard_crafting_item]']
    i_essence_prism = body['parts[essence_prism_crafting_item]']
    i_gold_leaf = body['parts[gold_leaf_crafting_item]']
    print(f'CrystalCrucible: {i_crystal_crucible}, DragonEmber: {i_dragon_ember}, GlassShard: {i_glass_shard}, EssencePrism: {i_essence_prism}, Gold_leaf: {i_gold_leaf}')


async def callAPI(url, body, headers, cookies):
    async with aiohttp.ClientSession() as session:

        URL = 'https://www.mousehuntgame.com/managers/ajax/users/crafting.php'
        headers = {
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Sec-Fetch-Dest": "empty",
                "X-Requested-With": "XMLHttpRequest",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-Mode": "cors"
                }
                
        async with session.post(url, data = body, headers = headers, cookies = cookies) as resp:

            # Retriving the content
            byte_array = await resp.content.read()
            my_json = json.loads(byte_array)

            if processResponse(filterResponse(my_json)):
                print("This is the right recipe")
                print_craftingCombination(body)

            return resp



# Update the generation coroutines
def generator_coroutines():
    """
    This method generates the necessary corountines to run the various combinations
    """

    coroutines = []
    count = 0
                       
    crystal_crucible = [1, 5] # 20 inventory
    dragon_ember = [1, 10] # 10 inventory
    glass_shard = [1, 20] # 103 inventory
    essence_prism = [1, 20] # 39 inventory
    gold_leaf = [1, 20] # 51 inventory
                        
    for i_crystal_crucible in range(crystal_crucible[0], crystal_crucible[1]):
        for i_dragon_ember in range(dragon_ember[0], dragon_ember[1]):
            for i_glass_shard in range(glass_shard[0], glass_shard[1]):
                for i_essence_prism in range(essence_prism[0], essence_prism[1]):
                    for i_gold_leaf in range (gold_leaf[0], gold_leaf[1]):
                        body = {
                            "uh": 'RdQtaaE8',
                            'parts[damaged_oculus_crafting_item]': 1,
                            'parts[gold_leaf_crafting_item]': i_gold_leaf,
                            'parts[essence_prism_crafting_item]': i_essence_prism,
                            'parts[crystal_crucible_crafting_item]': i_crystal_crucible,
                            'parts[dragon_ember]': i_dragon_ember,
                            'parts[glass_shard_crafting_item]': i_glass_shard,
                            'craftQty': 1
                        }
                        coroutines.append(callAPI(URL, body, headers, howard))
                        
    for coroutine in coroutines:
        count += 1
        yield coroutine, count


def main_iteration():
    print(f'[{datetime.datetime.now()}] Start Execution')

    # Definitions
    start_from = 163000
    batch_size = 300

    execute_routines = []
    for api_call, count in generator_coroutines():
        if count < start_from:
            continue

        execute_routines.append(api_call)

        # Execute in batches of 400 calls.
        if len(execute_routines) == batch_size:
            print(f"Executed {batch_size} calls, count={count}")

            loop = asyncio.get_event_loop()
            results = loop.run_until_complete(asyncio.gather(*execute_routines))
            execute_routines = []

    # Execute the last bit
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(asyncio.gather(*execute_routines))

    print(f'[{datetime.datetime.now()}] End Execution')


if __name__ == "__main__":
    main_iteration()

