trapSetup = {
    'physical': {
        'weapon': 'geyser_physical_weapon',
    },
    'tactical': {
        'weapon': 'geyser_tactical_weapon',
        # 'trinket': 'rift_vacuum_trinket'
    },
    'hydro': {
        'weapon': 'geyser_hydro_weapon',
    },
    'arcane': {
        'weapon': 'event_horizon_weapon',
    },
    'shadow': {
        'weapon': 'chrome_temporal_turbine_weapon',
    },
    'forgotten': {
        'weapon': 'infinite_labyrinth_weapon',
    },
    'draconic': {
        'weapon': 'geyser_draconic_weapon',
    },
    'law': {
        'weapon': 'ember_prison_core_weapon',
    },
    'rift': {
        'weapon': 'temporal_dissonance_weapon',
    }

}

# Input options
## Bait
# gouda_cheese
# medium_queso_cheese
# mild_queso_cheese
# grilled_cheese
# duskshade_camembert_cheese
# brie_cheese

## Destinations
# mousoleum
# pinnacle_chamber
# 
# 
# 
# 
# 
# 
# 

mouseCatchSequence = [
    {
        'name': 'Archer',
        'bait': 'super_brie_cheese',
        'destination': 'training_grounds',
        'setup': trapSetup['tactical']
    },
    {
        'name': 'Captain Croissant',
        'bait': 'grilled_cheese',
        'destination': 'windmill',
        'setup': trapSetup['physical']
    },
    {
        'name': 'Bat',
        'bait': 'radioactive_blue_cheese',
        'destination': 'mousoleum',
        'setup': trapSetup['shadow']
    },
    {
        'name': 'Meteorite Snacker',
        'bait': 'moon_cheese',
        'destination': 'fort_rox',
        'setup': trapSetup['law']
    },
    {
        'name': 'Gladiator',
        'bait': 'crunchy_cheese',
        'destination': 'derr_dunes',
        'setup': trapSetup['physical']
    }
]