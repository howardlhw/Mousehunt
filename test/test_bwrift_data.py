
# Defining test cases for chamber selection
portal_test_cases = {
	'case1': {
		'portals': ['entrance_chamber','entrance_chamber','entrance_chamber'],
		'runic_string_cheese': 70,
		'rift_hourglass_sand_stat_item': 20,
		'selection': 'basic_chamber'
	},
	'case2': {
		'portals': ['lucky_tower','magic_chamber','timewarp_chamber'],
		'runic_string_cheese': 70,
		'rift_hourglass_sand_stat_item': 200,
		'selection': 'lucky_tower'
	},
	'case3': {
		'portals': ['hidden_treasury','magic_chamber','timewarp_chamber'],
		'runic_string_cheese': 70,
		'rift_hourglass_sand_stat_item': 200,
		'selection': 'hidden_treasury'
	},
	'case4': {
		'portals': ['lucky_tower','magic_chamber','timewarp_chamber'],
		'runic_string_cheese': 70,
		'rift_hourglass_sand_stat_item': 200,
		'selection': 'lucky_tower'
	},
	'case5': {
		'portals': ['acolyte_chamber','magic_chamber','timewarp_chamber'],
		'runic_string_cheese': 70,
		'rift_hourglass_sand_stat_item': 70,
		'selection': 'acolyte_chamber'
	},
	'case6': {
		'portals': ['acolyte_chamber','magic_chamber','timewarp_chamber'],
		'runic_string_cheese': 70,
		'rift_hourglass_sand_stat_item': 30,
		'selection': 'timewarp_chamber'
	},
	'case7': {
		'portals': ['acolyte_chamber','magic_chamber','timewarp_chamber'],
		'runic_string_cheese': 40,
		'rift_hourglass_sand_stat_item': 70,
		'selection': 'magic_chamber'
	},
	'case8': {
		'portals': ['acolyte_chamber','magic_chamber','timewarp_chamber'],
		'runic_string_cheese': 20,
		'rift_hourglass_sand_stat_item': 30,
		'selection': 'magic_chamber'
	},
	'case9': {
		'portals': ['ancient_chamber','ancient_chamber','timewarp_chamber'],
		'runic_string_cheese': 20,
		'rift_hourglass_sand_stat_item': 30,
		'selection': 'ancient_chamber'
	},
	'case10': {
		'portals': ['security_chamber','ancient_chamber','timewarp_chamber'],
		'runic_string_cheese': 20,
		'rift_hourglass_sand_stat_item': 30,
		'selection': 'security_chamber'
	},
	'case11': {
		'portals': ['ancient_chamber','guard_barracks','timewarp_chamber'],
		'runic_string_cheese': 20,
		'rift_hourglass_sand_stat_item': 30,
		'selection': 'ancient_chamber'
	},
	'case12': {
		'portals': ['guard_barracks','guard_barracks','guard_barracks'],
		'runic_string_cheese': 20,
		'rift_hourglass_sand_stat_item': 30,
		'selection': 'guard_barracks'
	}

}

test_data = {
  "user": {
    "user_id": 8056376,
    "sn_user_id": "2328945374090567",
    "firstname": "Sashimi",
    "lastname": "Donburi",
    "username": "Sashimi Donburi",
    "gender": "male",
    "unique_hash": "LeA1Z1B4",
    "base_item_id": "2120",
    "base_name": "Attuned Enerchi Induction Base",
    "weapon_item_id": "2956",
    "weapon_name": "Rift Glacier Gatler",
    "trinket_item_id": "1430",
    "trinket_name": "Rift Charm",
    "gold": 15029560,
    "points": 501447513,
    "title_id": 6,
    "title_icon": "https://www.mousehuntgame.com/images/titles/065e8bbd86d10304736db6e306d0aa95.gif?cv=246",
    "title_name": "Grand Duke",
    "title_percent": 34,
    "title_wisdom": 75625813,
    "title_order": 0,
    "num_active_turns": 28343,
    "last_active_turn_timestamp": 1598453399,
    "is_online": True,
    "environment_id": 55,
    "environment_name": "Bristle Woods Rift",
    "environment_type": "rift_bristle_woods",
    "environment_header": "https://www.mousehuntgame.com/images/environments/f96ec205e6d305a8ceb62a9ffc7042c4.jpg?cv=246",
    "environment_icon": "https://www.mousehuntgame.com/images/environments/2b8f8498d46eb6a83376fd2bbe8969c1.jpg?cv=246",
    "has_shield": True,
    "shield_expiry": "2020-08-28 03:46:31",
    "trinket_slot_level": 1,
    "access_granted": True,
    "bait_item_id": 2343,
    "bait_name": "Ancient String Cheese",
    "bait_pedestal_image": "https://www.mousehuntgame.com/images/items/bait/f90dfbc62c21b1ef24fa1b9c11f38f86.png?cv=246",
    "bait_quantity": 89,
    "trinket_quantity": 1157,
    "skin_item_id": None,
    "trap_power_type_name": "Rift",
    "trap_power": 2609,
    "trap_power_bonus": 0.41000000000000003,
    "trap_luck": 25,
    "trap_attraction_bonus": 0.2,
    "trap_cheese_effect": "No Effect",
    "title_percent_accurate": 34.02,
    "activeturn_wait_seconds": 900,
    "next_activeturn_seconds": 738,
    "has_puzzle": False,
    "last_active": "2 minutes 42 seconds",
    "shield_seconds": 132830,
    "quests": {
      "QuestRiftBristleWoods": {
        "chamber_type": "magic_chamber",
        "chamber_name": "Runic Laboratory",
        "chamber_description": "Equip <b>Ancient String Cheese</b> and collect <b>Runic String Potions</b> to create <b>Runic String Cheese</b> which will help you find even better loot.",
        "is_bonus": None,
        "is_normal": True,
        "no_debuff": "",
        "cleaver_status": "available",
        "progress_percent": 60,
        "progress_goal": 30,
        "progress_remaining": 18,
        "portals": [
          {
            "type": "closed",
            "name": "",
            "status": "disabled"
          },
          {
            "type": "closed",
            "name": "",
            "status": "disabled"
          },
          {
            "type": "closed",
            "name": "",
            "status": "disabled"
          }
        ],
        "chamber_status": "closed",
        "equipment_warning": "",
        "acolyte_catches": 1,
        "acolyte_crown": "default",
        "acolyte_sand": 0,
        "obelisk_percent": 0,
        "has_obelisk_charge": "",
        "status_effects": {
          "ng": "default",
          "ac": "default",
          "ex": "default",
          "fr": "default",
          "st": "default",
          "un": "default"
        },
        "items": {
          "marble_string_cheese": {
            "quantity": "0",
            "status": "disabled hidden"
          },
          "swiss_string_cheese": {
            "quantity": "0",
            "status": "disabled hidden"
          },
          "brie_string_cheese": {
            "quantity": "371",
            "status": "hidden"
          },
          "magical_string_cheese": {
            "quantity": "33",
            "status": ""
          },
          "ancient_string_cheese": {
            "quantity": "89",
            "status": "active highlight"
          },
          "runic_string_cheese": {
            "quantity": "86",
            "status": ""
          },
          "rift_anti_skele_trinket": {
            "quantity": "11",
            "status": ""
          },
          "rift_scramble_portals_stat_item": {
            "quantity": "0",
            "status": "disabled noPortals"
          },
          "rift_quantum_quartz_stat_item": {
            "quantity": "73",
            "status": ""
          },
          "rift_hourglass_stat_item": {
            "quantity": "0",
            "status": "disabled"
          },
          "rift_hourglass_sand_stat_item": {
            "quantity": "0",
            "status": "disabled noHourglass"
          },
          "rift_portal_warmer_stat_item": {
            "quantity": "1",
            "status": "disabled"
          },
          "ancient_string_cheese_potion": {
            "quantity": "0",
            "status": "disabled"
          },
          "runic_string_cheese_potion": {
            "quantity": "5",
            "status": "highlight"
          }
        },
        "minigame": {
          "magic_chamber": {
            "ancient_string_cheese": "active",
            "runic_string_cheese_potion": "active"
          }
        }
      },
      "QuestZurrealTrapResearch": {
        "is_assignment": True,
        "type": "zurreal_trap_research_quest_item"
      },
      "QuestTheme": {
        "active": "theme_halloween_2019"
      },
      "QuestAdventureBook": {
        "hash": "b1161a2a59ba81a26df888bde2d8d46b",
        "adventure": {
          "name": "Capture the Absolute Acolyte",
          "can_claim": True,
          "is_claimed": None,
          "type": "catch_rift_acolyte_adv",
          "header_image": "https://www.mousehuntgame.com/images/environments/f96ec205e6d305a8ceb62a9ffc7042c4.jpg?cv=246",
          "header_type": False,
          "goal": False,
          "has_goal": None
        }
      },
      "MiniEventRonzaChromeBit": {
        "num_chrome_bits_found": 200,
        "num_chrome_bits": 287,
        "num_chrome_bit_first_voucher": 100,
        "num_chrome_bit_second_voucher": 200,
        "percent": 100,
        "state": "complete",
        "claimed_first_voucher": True,
        "claimed_second_voucher": True,
        "is_shutdown": None,
        "is_ronza": True
      },
      "QuestRelicHunter": {
        "invites_hash": "e9f4ad8f7d5f0b58d41814ca3c356a4b",
        "inventory_hash": "6c9822c663974ae61bf2455058011877",
        "notifications": 0,
        "num_invites": 0,
        "new_chat": False,
        "mice_warning": True,
        "label": "Lightning Treasure Map",
        "value": "23 remaining",
        "image": "https://www.mousehuntgame.com/images/ui/treasure_maps/default_common.jpg",
        "maps": [
          {
            "map_id": 2706312,
            "name": "Lightning Treasure Map",
            "hash": "baa8979f5cf4ea07ae6f2d7e7089c657",
            "thumb": "https://www.mousehuntgame.com/images/ui/treasure_maps/default_common.jpg",
            "remaining": 23,
            "is_rare": None,
            "is_complete": None,
            "is_favourite": None,
            "has_message": None
          }
        ],
        "favourite_map_sn_user_ids": [
          "hg_23563e649ec48226883147901a10ce2c",
          "10157732359895016"
        ],
        "num_maps_dusted": 4,
        "default_map_id": 2706312,
        "items": {
          "rare_map_dust_stat_item": "0",
          "map_clue_stat_item": "1,455",
          "ancient_relic_collectible": "51"
        }
      }
    },
    "team": {
      "team_id": "112974",
      "name": "TEAM 7TEEN",
      "new_chat": False
    },
    "viewing_atts": {
      "trap_effectiveness": "Medium",
      "reset_effectiveness": False
    },
    "enviroment_atts": {
      "profile_pic": "https://www.gravatar.com/avatar/e442abb0c39b7dc766abce56310d397f?r=g&size=200&d=https://www.mousehuntgame.com/images/mice/square/f066ee3e7173523edc5db147b92291aa.jpg",
      "gold": 15029560,
      "gold_formatted": "15,029,560",
      "points": 501447513,
      "points_formatted": "501,447,513",
      "base_name": "Attuned Enerchi Induction Base",
      "base_thumb": "https://www.mousehuntgame.com/images/items/bases/4013d40ad9cea2d53b55fcc1b5d20851.jpg?cv=246",
      "base_item_id": "2120",
      "weapon_name": "Rift Glacier Gatler",
      "weapon_thumb": "https://www.mousehuntgame.com/images/items/weapons/a1b6c88f8ed3e8598b088852a8d3db1b.jpg?cv=246",
      "weapon_item_id": "2956",
      "trinket_name": "Rift Charm",
      "trinket_thumb": "https://www.mousehuntgame.com/images/items/trinkets/78dc60695a186f1496f69f0dc699c627.gif?cv=246",
      "trinket_item_id": "1430",
      "team_id": "112974",
      "team_name": "TEAM 7TEEN",
      "title_name": "Grand Duke",
      "title_percent": 34,
      "environment_name": "Bristle Woods Rift",
      "bait_item_id": 2343,
      "bait_name": "Ancient String Cheese",
      "bait_pedestal_image": "https://www.mousehuntgame.com/images/items/bait/f90dfbc62c21b1ef24fa1b9c11f38f86.png?cv=246",
      "bait_quantity": 89,
      "bait_thumb": "https://www.mousehuntgame.com/images/items/bait/5cb84d2e781edafc6419b8cab67f92ce.gif?cv=246",
      "bait_quantity_formatted": "89",
      "trinket_quantity_formatted": "1,157",
      "shield_image": "https://www.mousehuntgame.com/images/titles/87937fa96bbb3b2dd3225df883002642.png?cv=246",
      "title_percent_accurate": 34.02,
      "has_trinket_slot": True,
      "user_at_max_title": None,
      "has_map": True,
      "map_image": "https://www.mousehuntgame.com/images/ui/treasure_maps/default_common.jpg",
      "map_label": "Lightning Treasure Map",
      "map_value": "23 remaining",
      "num_map_notifications": 0,
      "has_map_corkboard_message": None,
      "has_map_warning": True,
      "team_emblem": {
        "layers": [
          {
            "category": "background",
            "type": "19",
            "colour": "19",
            "image": "https://www.mousehuntgame.com/images/teams/background/_19.png"
          },
          {
            "category": "middle",
            "type": "right_slant_stripes",
            "colour": 9,
            "image": "https://www.mousehuntgame.com/images/teams/middle/right_slant_stripes/_9.png"
          },
          {
            "category": "sigil",
            "type": "drill",
            "colour": 3,
            "image": "https://www.mousehuntgame.com/images/teams/sigil/drill/_3.png"
          }
        ]
      },
      "has_team_corkboard_message": None,
      "power": 2609,
      "power_formatted": "2,609",
      "environment_hud": "<div class=\"riftBristleWoodsHUD magic_chamber closed\"><div class=\"riftBristleWoodsHUD-chamberTitle\" title=\"Runic Laboratory\"></div><div class=\"riftBristleWoodsHUD-chamberProgressBar\"><span style=\"width: 60%;\"></span></div><div class=\"riftBristleWoodsHUD-chamberProgressQuantity\">18/30</div><div class=\"riftBristleWoodsHUD-chamberCleaver mousehuntTooltipParent available\"><div class=\"mousehuntTooltip right tight hasBuffer\">Catch a <b>Chamber Cleaver Mouse</b> to open portals early.<span class=\"riftBristleWoodsHUD-chamberCleaver-status found\">Portals are open and the Chamber Cleaver Mouse is nowhere to be found!</span><span class=\"riftBristleWoodsHUD-chamberCleaver-status available\">The Chamber Cleaver Mouse is available to catch with Runic String Cheese!</span><span class=\"riftBristleWoodsHUD-chamberCleaver-status unavailable\">The chamber is too cramped with loot for the Chamber Cleaver Mouse to come around.</span><span class=\"riftBristleWoodsHUD-chamberCleaver-status bonus\">The Chamber Cleaver Mouse doesn't know how to reach this Chamber.</span><div class=\"mousehuntTooltip-arrow\"></div></div></div><div class=\"riftBristleWoodsHUD-acolyteStats  default mousehuntTooltipParent\"><div class=\"mousehuntTooltip bottom tight\"><div class=\"riftBristleWoodsHUD-acolyteStats-block\"><div class=\"riftBristleWoodsHUD-acolyteStats-block-title\"><span>Obelisk<br />Charge</span></div><div class=\"riftBristleWoodsHUD-acolyteStats-block-value\"><span class=\"riftBristleWoodsHUD-acolyteStats-obeliskCharge\">0</span>%</div></div><div class=\"riftBristleWoodsHUD-acolyteStats-block\"><div class=\"riftBristleWoodsHUD-acolyteStats-block-title\"><span>Acolyte<br />Sand</span></div><div class=\"riftBristleWoodsHUD-acolyteStats-block-value\"><span class=\"riftBristleWoodsHUD-acolyteStats-acolyteSand\">0</span></div></div><div class=\"riftBristleWoodsHUD-acolyteStats-block\"><div class=\"riftBristleWoodsHUD-acolyteStats-block-title\"><span>Acolyte<br />Catches</span></div><div class=\"riftBristleWoodsHUD-acolyteStats-block-value\"><span class=\"riftBristleWoodsHUD-acolyteStats-acolyteCatches\">1</span></div></div><div class=\"riftBristleWoodsHUD-acolyteStats-block\"><div class=\"riftBristleWoodsHUD-acolyteStats-block-title\"><span>Mysterious<br />Box Quality</span></div><div class=\"riftBristleWoodsHUD-acolyteStats-block-value\"><span class=\"riftBristleWoodsHUD-acolyteStats-acolyteBoxLevel default\">Normal</span><span class=\"riftBristleWoodsHUD-acolyteStats-acolyteBoxLevel bronze\">Bronze</span><span class=\"riftBristleWoodsHUD-acolyteStats-acolyteBoxLevel silver\">Silver</span><span class=\"riftBristleWoodsHUD-acolyteStats-acolyteBoxLevel gold\">Gold</span></div></div><div class=\"riftBristleWoodsHUD-acolyteStats-description\">Crown the Acolyte to upgrade the Mysterious Rift Box!</div><div class=\"mousehuntTooltip-arrow\"></div></div></div><div class=\"riftBristleWoodsHUD-portalEquipment acolyteHourglass disabled noHourglass mousehuntTooltipParent\"><div class=\"riftBristleWoodsHUD-portalEquipment-image\"></div><div class=\"riftBristleWoodsHUD-footer-item-quantity quantity\" data-item-type=\"rift_hourglass_sand_stat_item\">0</div><div class=\"mousehuntTooltip tight top noEvents\"><div class=\"riftBristleWoodsHUD-acolyteHourglass-title\">Store <b>Time Sand</b> in your <b>Ancient Hourglass</b>!</div>The more sand you possess, the greater chance of finding the <b>Acolyte Chamber</b>.<span class=\"riftBristleWoodsHUD-acolyteHourglass-status noHourglass\">Catch a Chronomaster Mouse in the Timewarp Chamber to find an Ancient Hourglass.</span><span class=\"riftBristleWoodsHUD-acolyteHourglass-status empty\">You're all out of Time Sand.</span><div class=\"mousehuntTooltip-arrow\"></div></div></div><div class=\"riftBristleWoodsHUD-portalEquipment portalScrambler mousehuntTooltipParent disabled noPortals\"><div class=\"riftBristleWoodsHUD-portalEquipment-image\"></div><div class=\"riftBristleWoodsHUD-footer-item-quantity quantity\" data-item-type=\"rift_scramble_portals_stat_item\">0</div><a href=\"#\" class=\"riftBristleWoodsHUD-portalEquipment-action\" onclick=\"hg.views.HeadsUpDisplayRiftBristleWoodsView.showConfirm(this); return false;\" data-confirm-type=\"scramblePortals\"></a><div class=\"mousehuntTooltip tight top\"><div class=\"riftBristleWoodsHUD-footer-item-tooltip-content\"><b>Portal Scramblers</b> can generate new portals!<span class=\"riftBristleWoodsHUD-portalScrambler-status empty\">You have no Portal Scramblers.</span><span class=\"riftBristleWoodsHUD-portalScrambler-status noPortals\">The portals are not yet open.</span><span class=\"riftBristleWoodsHUD-portalScrambler-status entrance\">Only one portal is available here.</span></div><div class=\"riftBristleWoodsHUD-footer-item-tooltip-actions\"><a href=\"#\" class=\"mousehuntActionButton tiny\" onclick=\"MHCheckout.quickAddToCart('5portal_scrambler'); return false;\"><span>Buy in<br />Shoppe</span></a></div><div class=\"mousehuntTooltip-arrow\"></div></div></div><div class=\"riftBristleWoodsHUD-portalEquipment lootBooster mousehuntTooltipParent \"><div class=\"riftBristleWoodsHUD-portalEquipment-image\"></div><div class=\"riftBristleWoodsHUD-footer-item-quantity quantity\" data-item-type=\"rift_quantum_quartz_stat_item\">73</div><a href=\"#\" class=\"riftBristleWoodsHUD-portalEquipment-action\" onclick=\"hg.views.HeadsUpDisplayRiftBristleWoodsView.toggleLootBoost(this); return false;\"></a><div class=\"mousehuntTooltip tight right\"><div class=\"riftBristleWoodsHUD-footer-item-tooltip-content\">Power the <b>Quantum Pocketwatch</b> with <b>Quantum Quartz</b> to add +1 loot drops for certain Rift items and clear chambers faster!<span class=\"riftBristleWoodsHUD-lootBooster-status empty\">You've run out of Quantum Quartz.</span><span class=\"riftBristleWoodsHUD-lootBooster-status chamberEmpty\">This chamber has no more loot.</span></div><div class=\"riftBristleWoodsHUD-footer-item-tooltip-actions\"><a href=\"#\" class=\"mousehuntActionButton tiny\" onclick=\"MHCheckout.quickAddToCart('25rift_quantum_quartz'); return false;\"><span>Buy in<br />Shoppe</span></a></div><div class=\"mousehuntTooltip-arrow\"></div></div></div><div class=\"riftBristleWoodsHUD-portalEquipment portalWarmer mousehuntTooltipParent disabled\"><div class=\"riftBristleWoodsHUD-portalEquipment-image\"></div><div class=\"riftBristleWoodsHUD-footer-item-quantity quantity\" data-item-type=\"rift_portal_warmer_stat_item\">1</div><div class=\"mousehuntTooltip tight top\"><div class=\"riftBristleWoodsHUD-footer-item-tooltip-content\">Use a <b>Portal Rekindling Key</b> to unfreeze a frozen portal!</div><div class=\"riftBristleWoodsHUD-footer-item-tooltip-actions\"><a href=\"#\" class=\"mousehuntActionButton tiny\" onclick=\"MHCheckout.quickAddToCart('5portalwarmers'); return false;\"><span>Buy in<br />Shoppe</span></a></div><div class=\"mousehuntTooltip-arrow\"></div></div></div><div class=\"riftBristleWoodsHUD-chamberDetails\"><div class=\"riftBristleWoodsHUD-chamberDetails-description riftBristleWoodsHUD-chamberSpecificTextContainer magic_chamber \"><div class=\"riftBristleWoodsHUD-chamberDetails-description-padding\"><div class=\"riftBristleWoodsHUD-chamberSpecificText acolyte_chamber\">Beyond this portal lies the dangerous Acolyte Chamber. Time is broken in this place and plenty of <b>Time Sand</b> is required to remain safely inside.<br />\n<br />\nIf you run out of sand, you run out of time...</div><div class=\"riftBristleWoodsHUD-chamberSpecificText basic_chamber\">Each chamber has a finite amount of loot! When the chamber is emptied, or when you catch a Chamber Cleaver Mouse, new portals will open to strange new chambers.</div><div class=\"riftBristleWoodsHUD-chamberSpecificText entrance_chamber\">You stand at the entrance of the <b>Rift Acolyte Tower</b>. Enter to seek out the <b>Absolute Acolyte Mouse</b> and restore the timeline!</div><div class=\"riftBristleWoodsHUD-chamberSpecificText guard_chamber\"><div class=\"riftBristleWoodsHUD-chamberDetails-buffContainer\">Loot the chamber to seal away the <b>Portal Paladin mice</b>. Every hunt raises the alert, but catching a Portal Paladin Mouse will reset it!</div><div class=\"riftBristleWoodsHUD-guardChamber \"></div></div><div class=\"riftBristleWoodsHUD-chamberSpecificText icebreak_chamber\"><div class=\"riftBristleWoodsHUD-chamberDetails-buffContainer\">Fix the broken furnace by capturing mice that have tampered with it to bring the temperature up and unfreeze the portals.</div></div><div class=\"riftBristleWoodsHUD-chamberSpecificText icy_chamber\"><div class=\"riftBristleWoodsHUD-chamberDetails-buffContainer\">Complete this chamber in order to gain a magical <b>Acolyte Influence</b> spell.</div><div class=\"riftBristleWoodsHUD-chamberDetails-debuffContainer clear-block\"><div class=\"riftBristleWoodsHUD-icyChamber\"><div class=\"riftBristleWoodsHUD-icyChamber-progressBar\"><span style=\"height:%;\"><div class=\"riftBristleWoodsHUD-icyChamber-temperature\"><b></b>&deg;</div></span></div></div>The room temperature decreases every hunt. Escape before it hits -30&deg; to prevent frozen portals!</div></div><div class=\"riftBristleWoodsHUD-chamberSpecificText ingress_chamber\">Failing to capture a <b>Portal Pursuer Mouse</b> will break one of the containment seals.<div class=\"riftBristleWoodsHUD-ingressChamber \"></div></div><div class=\"riftBristleWoodsHUD-chamberSpecificText lucky_chamber\">Aww, lucky! This chamber is loaded with luck charms and some extra Quantum Quartz! Loot it up before the luck runs dry!</div><div class=\"riftBristleWoodsHUD-chamberSpecificText magic_chamber\"><div class=\"riftBristleWoodsHUD-chamberDetails-buffContainer\"><div class=\"riftBristleWoodsHUD-chamberDetails-imageContainer floatl\"><div class=\"riftBristleWoodsHUD-chamberDetails-image active ancient_string_cheese\" title=\"Ancient String Cheese\"><div class=\"riftBristleWoodsHUD-chamberDetails-image-padding\" style=\"background-image:url(https://www.mousehuntgame.com/images/items/bait/5cb84d2e781edafc6419b8cab67f92ce.gif?cv=246);\"></div></div><div class=\"riftBristleWoodsHUD-chamberDetails-image active runic_string_cheese_potion\" title=\"Runic String Cheese Potion\"><div class=\"riftBristleWoodsHUD-chamberDetails-image-padding\" style=\"background-image:url(https://www.mousehuntgame.com/images/items/potions/d22e1e50ae80c4f1318106659ee6440a.jpg?cv=246);\"></div></div></div>Use Ancient String Cheese to gather Runic String Potions from the strange mice in this chamber!</div></div><div class=\"riftBristleWoodsHUD-chamberSpecificText potion_chamber\">The chamber walls hum with dusty magic! Mice are scurrying about, bottling the dust bunnies into Ancient String Potions for nefarious reasons. Get some of your own!</div><div class=\"riftBristleWoodsHUD-chamberSpecificText silence_chamber\"><div class=\"riftBristleWoodsHUD-chamberDetails-buffContainer\">Disable the security system by capturing mice in this chamber to silence the alarm and bring luck back to your trap.</div></div><div class=\"riftBristleWoodsHUD-chamberSpecificText stalker_chamber\"><div class=\"riftBristleWoodsHUD-chamberDetails-buffContainer\">Hunt through this accursed place to bring the <b>Portal Pursuer Mouse</b> to rest and end her tireless pursuit.</div></div><div class=\"riftBristleWoodsHUD-chamberSpecificText timewarp_chamber\"><div class=\"riftBristleWoodsHUD-chamberDetails-buffContainer\"><div class=\"riftBristleWoodsHUD-chamberDetails-imageContainer\"><div class=\"riftBristleWoodsHUD-chamberDetails-image  runic_string_cheese\" title=\"Runic String Cheese\"><div class=\"riftBristleWoodsHUD-chamberDetails-image-padding\" style=\"background-image:url(https://www.mousehuntgame.com/images/items/bait/8b5b3dd636cc701bd4c714e0d50d67c6.gif?cv=246);\"></div></div><div class=\"riftBristleWoodsHUD-chamberDetails-image  rift_hourglass_stat_item\" title=\"Ancient Hourglass\"><div class=\"riftBristleWoodsHUD-chamberDetails-image-padding\" style=\"background-image:url(https://www.mousehuntgame.com/images/items/stats/e01d6a35913e049fc1406e3993d2e106.gif?cv=246);\"></div></div><div class=\"riftBristleWoodsHUD-chamberDetails-image  rift_hourglass_sand_stat_item\" title=\"Time Sand\"><div class=\"riftBristleWoodsHUD-chamberDetails-image-padding\" style=\"background-image:url(https://www.mousehuntgame.com/images/items/stats/51517ccbc695147cb6f19c067f14d493.gif?cv=246);\"></div></div></div>Use Runic String Cheese to attract the Chronomaster Mouse and loot the Ancient Hourglass!</div></div><div class=\"riftBristleWoodsHUD-chamberSpecificText treasury_chamber\">A hidden chamber of wealth, full of gold! Grab as many satchels as you can before the other mice do!</div></div></div><div class=\"riftBristleWoodsHUD-equipmentWarningContainer \"><div class=\"riftBristleWoodsHUD-equipmentWarningContainer-padding\"><span class=\"riftBristleWoodsHUD-equipmentWarning baitWarning\" onclick=\"hg.views.HeadsUpDisplayRiftBristleWoodsView.showTrapSelector(this); return false;\">Only Ancient, Runic, and basic String baits attract mice in this strange place.</span><span class=\"riftBristleWoodsHUD-equipmentWarning runicWarning\" onclick=\"hg.views.HeadsUpDisplayRiftBristleWoodsView.showTrapSelector(this); return false;\">Only Runic String Cheese can attract the mice here!</span><span class=\"riftBristleWoodsHUD-equipmentWarning powerTypeWarning\" onclick=\"hg.views.HeadsUpDisplayRiftBristleWoodsView.showTrapSelector(this); return false;\">Only weapons powered by the Rift have any strength here!</span></div></div></div><div class=\"riftBristleWoodsHUD-chamberImage\"><div class=\"riftBristleWoodsHUD-portalContainer\"><a href=\"#\" onclick=\"hg.views.HeadsUpDisplayRiftBristleWoodsView.showConfirm(this); return false;\" data-confirm-type=\"enterPortal\" data-portal-type=\"closed\" class=\"riftBristleWoodsHUD-portal riftBristleWoodsHUD-chamberSpecificTextContainer closed disabled\"><div class=\"riftBristleWoodsHUD-portal-padding\"><div class=\"riftBristleWoodsHUD-portal-image\"></div><div class=\"riftBristleWoodsHUD-portal-name\"><span></span></div><div class=\"riftBristleWoodsHUD-portal-lock\"></div><div class=\"riftBristleWoodsHUD-portal-tooltip\"><div class=\"riftBristleWoodsHUD-portal-tooltip-padding\"><div class=\"riftBristleWoodsHUD-chamberSpecificText closed\"><span>Portal is sealed.</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText acolyte_chamber\"><span>Challenge the Absolute Acolyte</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText basic_chamber\"><span>Find Tiny Sprockets</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText entrance_chamber\"><span>Enter the Tower</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText guard_chamber\"><span>Seal away Portal Paladins</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText icebreak_chamber\"><span>Thaw the frozen portals</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText icy_chamber\"><span>Earn a magical spell</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText ingress_chamber\"><span>Unlock an extra portal</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText lucky_chamber\"><span>Lucky Loot!</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText magic_chamber\"><span>Find Runic String Potions</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText potion_chamber\"><span>Find Ancient String Potions</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText silence_chamber\"><span>Silence the Unlucky Alarm</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText stalker_chamber\"><span>Escape your pursuer</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText timewarp_chamber\"><span>Find Ancient Hourglass and Time Sand</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText treasury_chamber\"><span>Golden Hoard!</span></div></div></div></div></a><a href=\"#\" onclick=\"hg.views.HeadsUpDisplayRiftBristleWoodsView.showConfirm(this); return false;\" data-confirm-type=\"enterPortal\" data-portal-type=\"closed\" class=\"riftBristleWoodsHUD-portal riftBristleWoodsHUD-chamberSpecificTextContainer closed disabled\"><div class=\"riftBristleWoodsHUD-portal-padding\"><div class=\"riftBristleWoodsHUD-portal-image\"></div><div class=\"riftBristleWoodsHUD-portal-name\"><span></span></div><div class=\"riftBristleWoodsHUD-portal-lock\"></div><div class=\"riftBristleWoodsHUD-portal-tooltip\"><div class=\"riftBristleWoodsHUD-portal-tooltip-padding\"><div class=\"riftBristleWoodsHUD-chamberSpecificText closed\"><span>Portal is sealed.</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText acolyte_chamber\"><span>Challenge the Absolute Acolyte</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText basic_chamber\"><span>Find Tiny Sprockets</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText entrance_chamber\"><span>Enter the Tower</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText guard_chamber\"><span>Seal away Portal Paladins</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText icebreak_chamber\"><span>Thaw the frozen portals</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText icy_chamber\"><span>Earn a magical spell</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText ingress_chamber\"><span>Unlock an extra portal</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText lucky_chamber\"><span>Lucky Loot!</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText magic_chamber\"><span>Find Runic String Potions</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText potion_chamber\"><span>Find Ancient String Potions</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText silence_chamber\"><span>Silence the Unlucky Alarm</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText stalker_chamber\"><span>Escape your pursuer</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText timewarp_chamber\"><span>Find Ancient Hourglass and Time Sand</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText treasury_chamber\"><span>Golden Hoard!</span></div></div></div></div></a><a href=\"#\" onclick=\"hg.views.HeadsUpDisplayRiftBristleWoodsView.showConfirm(this); return false;\" data-confirm-type=\"enterPortal\" data-portal-type=\"closed\" class=\"riftBristleWoodsHUD-portal riftBristleWoodsHUD-chamberSpecificTextContainer closed disabled\"><div class=\"riftBristleWoodsHUD-portal-padding\"><div class=\"riftBristleWoodsHUD-portal-image\"></div><div class=\"riftBristleWoodsHUD-portal-name\"><span></span></div><div class=\"riftBristleWoodsHUD-portal-lock\"></div><div class=\"riftBristleWoodsHUD-portal-tooltip\"><div class=\"riftBristleWoodsHUD-portal-tooltip-padding\"><div class=\"riftBristleWoodsHUD-chamberSpecificText closed\"><span>Portal is sealed.</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText acolyte_chamber\"><span>Challenge the Absolute Acolyte</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText basic_chamber\"><span>Find Tiny Sprockets</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText entrance_chamber\"><span>Enter the Tower</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText guard_chamber\"><span>Seal away Portal Paladins</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText icebreak_chamber\"><span>Thaw the frozen portals</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText icy_chamber\"><span>Earn a magical spell</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText ingress_chamber\"><span>Unlock an extra portal</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText lucky_chamber\"><span>Lucky Loot!</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText magic_chamber\"><span>Find Runic String Potions</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText potion_chamber\"><span>Find Ancient String Potions</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText silence_chamber\"><span>Silence the Unlucky Alarm</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText stalker_chamber\"><span>Escape your pursuer</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText timewarp_chamber\"><span>Find Ancient Hourglass and Time Sand</span></div><div class=\"riftBristleWoodsHUD-chamberSpecificText treasury_chamber\"><span>Golden Hoard!</span></div></div></div></div></a></div></div><div class=\"riftBristleWoodsHUD-chamberEffects\"><div class=\"riftBristleWoodsHUD-statusEffectContainer\"><div class=\"riftBristleWoodsHUD-statusEffect\"><div class=\"riftBristleWoodsHUD-statusEffect-iconContainer\"><div class=\"riftBristleWoodsHUD-statusEffect-icon ng default\" title=\"Paladin's Bane\"></div><div class=\"riftBristleWoodsHUD-statusEffect-icon un default\" title=\"Unlucky Alarm\"></div></div><div class=\"riftBristleWoodsHUD-statusEffect-info\"><div class=\"riftBristleWoodsHUD-statusEffect-info-padding\"><div class=\"riftBristleWoodsHUD-statusEffect-info-column ng default\"><div class=\"riftBristleWoodsHUD-statusEffect-icon ng default\"></div><div class=\"riftBristleWoodsHUD-statusEffect-info-column-content\"><b>Paladin's Bane<i class=\"riftBristleWoodsHUD-statusEffect-tooltip-status active\"> - Active</i><i class=\"riftBristleWoodsHUD-statusEffect-tooltip-status removed\"> - Blocked</i></b><br />Seal away all Portal Paladins!</div></div><div class=\"riftBristleWoodsHUD-statusEffect-info-column un default\"><div class=\"riftBristleWoodsHUD-statusEffect-icon un default\"></div><div class=\"riftBristleWoodsHUD-statusEffect-info-column-content\"><b>Unlucky Alarm<i class=\"riftBristleWoodsHUD-statusEffect-tooltip-status active\"> - Active</i><i class=\"riftBristleWoodsHUD-statusEffect-tooltip-status removed\"> - Blocked</i></b><br /><div class=\"riftBristleWoodsHUD-statusEffect-tooltip-status default\">Lose the trap luck from your weapon and base.</div><div class=\"riftBristleWoodsHUD-statusEffect-tooltip-status active\">The blaring alarms have weakened your trap! There has to be a Security Chamber somewhere...</div><div class=\"riftBristleWoodsHUD-statusEffect-tooltip-status removed\">With the alarm silenced, your trap's luck will once again have an effect.</div></div></div><div class=\"riftBristleWoodsHUD-statusEffect-location\"><div class=\"riftBristleWoodsHUD-portal guard_chamber \"><div class=\"riftBristleWoodsHUD-portal-padding\"><div class=\"riftBristleWoodsHUD-portal-image\"></div><div class=\"riftBristleWoodsHUD-portal-name\"><span>Guard Barracks</span></div><div class=\"riftBristleWoodsHUD-portal-lock\"></div></div></div></div></div></div></div><div class=\"riftBristleWoodsHUD-statusEffect\"><div class=\"riftBristleWoodsHUD-statusEffect-iconContainer\"><div class=\"riftBristleWoodsHUD-statusEffect-icon ac default\" title=\"Acolyte Influence\"></div><div class=\"riftBristleWoodsHUD-statusEffect-icon fr default\" title=\"Frozen Portals\"></div></div><div class=\"riftBristleWoodsHUD-statusEffect-info\"><div class=\"riftBristleWoodsHUD-statusEffect-info-padding\"><div class=\"riftBristleWoodsHUD-statusEffect-info-column ac default\"><div class=\"riftBristleWoodsHUD-statusEffect-icon ac default\"></div><div class=\"riftBristleWoodsHUD-statusEffect-info-column-content\"><b>Acolyte Influence<i class=\"riftBristleWoodsHUD-statusEffect-tooltip-status active\"> - Active</i><i class=\"riftBristleWoodsHUD-statusEffect-tooltip-status removed\"> - Blocked</i></b><br />Prevent the Absolute Acolyte from pillaging your trap and find extra loot when caught!</div></div><div class=\"riftBristleWoodsHUD-statusEffect-info-column fr default\"><div class=\"riftBristleWoodsHUD-statusEffect-icon fr default\"></div><div class=\"riftBristleWoodsHUD-statusEffect-info-column-content\"><b>Frozen Portals<i class=\"riftBristleWoodsHUD-statusEffect-tooltip-status active\"> - Active</i><i class=\"riftBristleWoodsHUD-statusEffect-tooltip-status removed\"> - Blocked</i></b><br /><div class=\"riftBristleWoodsHUD-statusEffect-tooltip-status default\">A random portal will be frozen in ice!</div><div class=\"riftBristleWoodsHUD-statusEffect-tooltip-status active\">Oh no! Every time portals open, one will be frozen. Find a Furnace Room to warm up!</div><div class=\"riftBristleWoodsHUD-statusEffect-tooltip-status removed\">The air is warm and calm again.</div></div></div><div class=\"riftBristleWoodsHUD-statusEffect-location\"><div class=\"riftBristleWoodsHUD-portal icy_chamber \"><div class=\"riftBristleWoodsHUD-portal-padding\"><div class=\"riftBristleWoodsHUD-portal-image\"></div><div class=\"riftBristleWoodsHUD-portal-name\"><span>Frozen Alcove</span></div><div class=\"riftBristleWoodsHUD-portal-lock\"></div></div></div></div></div></div></div><div class=\"riftBristleWoodsHUD-statusEffect\"><div class=\"riftBristleWoodsHUD-statusEffect-iconContainer\"><div class=\"riftBristleWoodsHUD-statusEffect-icon ex default\" title=\"Fourth Portal\"></div><div class=\"riftBristleWoodsHUD-statusEffect-icon st default\" title=\"Pursued\"></div></div><div class=\"riftBristleWoodsHUD-statusEffect-info\"><div class=\"riftBristleWoodsHUD-statusEffect-info-padding\"><div class=\"riftBristleWoodsHUD-statusEffect-info-column ex default\"><div class=\"riftBristleWoodsHUD-statusEffect-icon ex default\"></div><div class=\"riftBristleWoodsHUD-statusEffect-info-column-content\"><b>Fourth Portal<i class=\"riftBristleWoodsHUD-statusEffect-tooltip-status active\"> - Active</i><i class=\"riftBristleWoodsHUD-statusEffect-tooltip-status removed\"> - Blocked</i></b><br />Unlock an extra portal!</div></div><div class=\"riftBristleWoodsHUD-statusEffect-info-column st default\"><div class=\"riftBristleWoodsHUD-statusEffect-icon st default\"></div><div class=\"riftBristleWoodsHUD-statusEffect-info-column-content\"><b>Pursued<i class=\"riftBristleWoodsHUD-statusEffect-tooltip-status active\"> - Active</i><i class=\"riftBristleWoodsHUD-statusEffect-tooltip-status removed\"> - Blocked</i></b><br /><div class=\"riftBristleWoodsHUD-statusEffect-tooltip-status default\">An unkind stranger follows your footsteps...</div><div class=\"riftBristleWoodsHUD-statusEffect-tooltip-status active\">The Portal Pursuer Mouse has your scent! Find the Pursuer Mousoleum to bring her to rest.</div><div class=\"riftBristleWoodsHUD-statusEffect-tooltip-status removed\">The old bones of the Portal Pursuer Mouse now lie undisturbed.</div></div></div><div class=\"riftBristleWoodsHUD-statusEffect-location\"><div class=\"riftBristleWoodsHUD-portal ingress_chamber \"><div class=\"riftBristleWoodsHUD-portal-padding\"><div class=\"riftBristleWoodsHUD-portal-image\"></div><div class=\"riftBristleWoodsHUD-portal-name\"><span>Ingress Chamber</span></div><div class=\"riftBristleWoodsHUD-portal-lock\"></div></div></div></div></div></div></div></div></div><div class=\"riftBristleWoodsHUD-itemContainer\"><div class=\"riftBristleWoodsHUD-footer-itemContainer\"><div class=\"riftBristleWoodsHUD-footer-itemGroup  mousehuntTooltipParent\"><div class=\"footer-item-imageContainer\"><div class=\"riftBristleWoodsHUD-footer-item-image marble_string_cheese disabled hidden\" data-item-type=\"marble_string_cheese\" style=\"background-image:url(https://www.mousehuntgame.com/images/items/bait/515221197c0e6cc7fb5a8fc971f28159.gif?cv=246);\"><div class=\"riftBristleWoodsHUD-footer-item-border\"></div><div class=\"riftBristleWoodsHUD-footer-item-quantity quantity\" data-item-type=\"marble_string_cheese\">0</div><div class=\"riftBristleWoodsHUD-footer-item-boundingBox disabled hidden\" data-item-type=\"marble_string_cheese\" data-item-classification=\"bait\" onclick=\"hg.utils.TrapControl.toggleItem(this); return false;\" title=\"Marble String Cheese\"></div></div><div class=\"riftBristleWoodsHUD-footer-item-image swiss_string_cheese disabled hidden\" data-item-type=\"swiss_string_cheese\" style=\"background-image:url(https://www.mousehuntgame.com/images/items/bait/476fb908748757f976715c3d40722654.gif?cv=246);\"><div class=\"riftBristleWoodsHUD-footer-item-border\"></div><div class=\"riftBristleWoodsHUD-footer-item-quantity quantity\" data-item-type=\"swiss_string_cheese\">0</div><div class=\"riftBristleWoodsHUD-footer-item-boundingBox disabled hidden\" data-item-type=\"swiss_string_cheese\" data-item-classification=\"bait\" onclick=\"hg.utils.TrapControl.toggleItem(this); return false;\" title=\"Swiss String Cheese\"></div></div><div class=\"riftBristleWoodsHUD-footer-item-image brie_string_cheese hidden\" data-item-type=\"brie_string_cheese\" style=\"background-image:url(https://www.mousehuntgame.com/images/items/bait/5e3e6973e0f640538ff5c33fe0275c0e.gif?cv=246);\"><div class=\"riftBristleWoodsHUD-footer-item-border\"></div><div class=\"riftBristleWoodsHUD-footer-item-quantity quantity\" data-item-type=\"brie_string_cheese\">371</div><div class=\"riftBristleWoodsHUD-footer-item-boundingBox hidden\" data-item-type=\"brie_string_cheese\" data-item-classification=\"bait\" onclick=\"hg.utils.TrapControl.toggleItem(this); return false;\" title=\"Brie String Cheese\"></div></div><div class=\"riftBristleWoodsHUD-footer-item-image magical_string_cheese \" data-item-type=\"magical_string_cheese\" style=\"background-image:url(https://www.mousehuntgame.com/images/items/bait/e513ef0cbeec29c9c5e44e4db39df7d1.gif?cv=246);\"><div class=\"riftBristleWoodsHUD-footer-item-border\"></div><div class=\"riftBristleWoodsHUD-footer-item-quantity quantity\" data-item-type=\"magical_string_cheese\">33</div><div class=\"riftBristleWoodsHUD-footer-item-boundingBox \" data-item-type=\"magical_string_cheese\" data-item-classification=\"bait\" onclick=\"hg.utils.TrapControl.toggleItem(this); return false;\" title=\"Magical String Cheese\"></div></div></div><div class=\"mousehuntTooltip tight top hasBuffer\"><div class=\"riftBristleWoodsHUD-footer-item-tooltip-baitRow\"><div class=\"riftBristleWoodsHUD-footer-item-tooltip-baitRow-image\" style=\"background-image:url(https://www.mousehuntgame.com/images/items/bait/515221197c0e6cc7fb5a8fc971f28159.gif?cv=246);\"><div class=\"riftBristleWoodsHUD-footer-item-quantity quantity\" data-item-type=\"marble_string_cheese\">0</div></div><div class=\"riftBristleWoodsHUD-footer-item-tooltip-baitRow-name\">Marble String</div><a href=\"#\" class=\"mousehuntArmNowButton disabled hidden\" data-item-type=\"marble_string_cheese\" data-item-classification=\"bait\" onclick=\"hg.utils.TrapControl.toggleItem(this); return false;\"></a></div><div class=\"riftBristleWoodsHUD-footer-item-tooltip-baitRow\"><div class=\"riftBristleWoodsHUD-footer-item-tooltip-baitRow-image\" style=\"background-image:url(https://www.mousehuntgame.com/images/items/bait/476fb908748757f976715c3d40722654.gif?cv=246);\"><div class=\"riftBristleWoodsHUD-footer-item-quantity quantity\" data-item-type=\"swiss_string_cheese\">0</div></div><div class=\"riftBristleWoodsHUD-footer-item-tooltip-baitRow-name\">Swiss String</div><a href=\"#\" class=\"mousehuntArmNowButton disabled hidden\" data-item-type=\"swiss_string_cheese\" data-item-classification=\"bait\" onclick=\"hg.utils.TrapControl.toggleItem(this); return false;\"></a></div><div class=\"riftBristleWoodsHUD-footer-item-tooltip-baitRow\"><div class=\"riftBristleWoodsHUD-footer-item-tooltip-baitRow-image\" style=\"background-image:url(https://www.mousehuntgame.com/images/items/bait/5e3e6973e0f640538ff5c33fe0275c0e.gif?cv=246);\"><div class=\"riftBristleWoodsHUD-footer-item-quantity quantity\" data-item-type=\"brie_string_cheese\">371</div></div><div class=\"riftBristleWoodsHUD-footer-item-tooltip-baitRow-name\">Brie String</div><a href=\"#\" class=\"mousehuntArmNowButton hidden\" data-item-type=\"brie_string_cheese\" data-item-classification=\"bait\" onclick=\"hg.utils.TrapControl.toggleItem(this); return false;\"></a></div><div class=\"riftBristleWoodsHUD-footer-item-tooltip-baitRow\"><div class=\"riftBristleWoodsHUD-footer-item-tooltip-baitRow-image\" style=\"background-image:url(https://www.mousehuntgame.com/images/items/bait/e513ef0cbeec29c9c5e44e4db39df7d1.gif?cv=246);\"><div class=\"riftBristleWoodsHUD-footer-item-quantity quantity\" data-item-type=\"magical_string_cheese\">33</div></div><div class=\"riftBristleWoodsHUD-footer-item-tooltip-baitRow-name\">Magical String</div><a href=\"#\" class=\"mousehuntArmNowButton \" data-item-type=\"magical_string_cheese\" data-item-classification=\"bait\" onclick=\"hg.utils.TrapControl.toggleItem(this); return false;\"></a></div><div class=\"mousehuntTooltip-arrow\"></div></div></div><div class=\"riftBristleWoodsHUD-footer-itemGroup wide mousehuntTooltipParent\"><div class=\"footer-item-imageContainer\"><div class=\"riftBristleWoodsHUD-footer-item-image ancient_string_cheese_potion disabled\" data-item-type=\"ancient_string_cheese_potion\" style=\"background-image:url(https://www.mousehuntgame.com/images/items/potions/27067eb2fbcf9e3f124c572563c0ac21.jpg?cv=246);\"><div class=\"riftBristleWoodsHUD-footer-item-border\"></div><div class=\"riftBristleWoodsHUD-footer-item-quantity quantity\" data-item-type=\"ancient_string_cheese_potion\">0</div><div class=\"riftBristleWoodsHUD-footer-item-boundingBox\" onclick=\"hg.views.ItemView.show('ancient_string_cheese_potion', True); return false;\"></div></div><div class=\"riftBristleWoodsHUD-footer-item-image ancient_string_cheese active highlight\" data-item-type=\"ancient_string_cheese\" style=\"background-image:url(https://www.mousehuntgame.com/images/items/bait/5cb84d2e781edafc6419b8cab67f92ce.gif?cv=246);\"><div class=\"riftBristleWoodsHUD-footer-item-border\"></div><div class=\"riftBristleWoodsHUD-footer-item-quantity quantity\" data-item-type=\"ancient_string_cheese\">89</div><div class=\"riftBristleWoodsHUD-footer-item-boundingBox active highlight\" data-item-type=\"ancient_string_cheese\" data-item-classification=\"bait\" onclick=\"hg.utils.TrapControl.toggleItem(this); return false;\" title=\"Ancient String Cheese\"></div></div></div><div class=\"mousehuntTooltip tight top hasBuffer\"><div class=\"riftBristleWoodsHUD-footer-item-tooltip-content\"><b>Ancient String</b> attracts more mice with loot.</div><div class=\"riftBristleWoodsHUD-footer-item-tooltip-actions\"><a href=\"#\" class=\"mousehuntActionButton riftBristleWoodsHUD-footer-item-tooltip-action-brew tiny disabled\" data-item-type=\"ancient_string_cheese_potion\" onclick=\"hg.views.ItemView.show('ancient_string_cheese_potion', true); return false;\"><span>Brew</span></a><a href=\"#\" class=\"mousehuntBuyButton\" onclick=\"MHCheckout.quickAddToCart('15ancient_string'); return false;\"></a><a href=\"#\" class=\"mousehuntArmNowButton active highlight\" data-item-type=\"ancient_string_cheese\" data-item-classification=\"bait\" onclick=\"hg.utils.TrapControl.toggleItem(this); return false;\"></a></div><div class=\"mousehuntTooltip-arrow\"></div></div></div><div class=\"riftBristleWoodsHUD-footer-itemGroup wide mousehuntTooltipParent\"><div class=\"footer-item-imageContainer\"><div class=\"riftBristleWoodsHUD-footer-item-image runic_string_cheese_potion highlight\" data-item-type=\"runic_string_cheese_potion\" style=\"background-image:url(https://www.mousehuntgame.com/images/items/potions/d22e1e50ae80c4f1318106659ee6440a.jpg?cv=246);\"><div class=\"riftBristleWoodsHUD-footer-item-border\"></div><div class=\"riftBristleWoodsHUD-footer-item-quantity quantity\" data-item-type=\"runic_string_cheese_potion\">5</div><div class=\"riftBristleWoodsHUD-footer-item-boundingBox\" onclick=\"hg.views.HeadsUpDisplayRiftBristleWoodsView.brewRunicStringPotion(); return false;\"></div></div><div class=\"riftBristleWoodsHUD-footer-item-image runic_string_cheese \" data-item-type=\"runic_string_cheese\" style=\"background-image:url(https://www.mousehuntgame.com/images/items/bait/8b5b3dd636cc701bd4c714e0d50d67c6.gif?cv=246);\"><div class=\"riftBristleWoodsHUD-footer-item-border\"></div><div class=\"riftBristleWoodsHUD-footer-item-quantity quantity\" data-item-type=\"runic_string_cheese\">86</div><div class=\"riftBristleWoodsHUD-footer-item-boundingBox \" data-item-type=\"runic_string_cheese\" data-item-classification=\"bait\" onclick=\"hg.utils.TrapControl.toggleItem(this); return false;\" title=\"Runic String Cheese\"></div></div></div><div class=\"mousehuntTooltip tight top hasBuffer\"><div class=\"riftBristleWoodsHUD-footer-item-tooltip-content\"><b>Runic String</b> attracts mice with the most loot!</div><div class=\"riftBristleWoodsHUD-footer-item-tooltip-actions\"><a href=\"#\" class=\"mousehuntActionButton riftBristleWoodsHUD-footer-item-tooltip-action-brew tiny highlight\" data-item-type=\"runic_string_cheese_potion\" onclick=\"hg.views.HeadsUpDisplayRiftBristleWoodsView.brewRunicStringPotion(); return false;\"><span>Brew</span></a><a href=\"#\" class=\"mousehuntBuyButton\" onclick=\"app.pages.ShopsPage.showItem('runic_string_cheese_potion'); return false;\"></a><a href=\"#\" class=\"mousehuntArmNowButton \" data-item-type=\"runic_string_cheese\" data-item-classification=\"bait\" onclick=\"hg.utils.TrapControl.toggleItem(this); return false;\"></a></div><div class=\"mousehuntTooltip-arrow\"></div></div></div></div></div><div class=\"riftBristleWoodsHUD-acolyteChamber \"><div class=\"riftBristleWoodsHUD-acolyteChamber-sandBar\"><span style=\"height:%;\"></span></div><div class=\"riftBristleWoodsHUD-acolyteChamber-sandDetails quantity\" data-item-type=\"rift_hourglass_sand_stat_item\">0</div><div class=\"riftBristleWoodsHUD-acolyteChamber-boundingBox sand mousehuntTooltipParent\"><div class=\"mousehuntTooltip tight noEvents right\">Each hunt drains a piece of your <b>Time Sand</b>! When it runs out, you'll find yourself back in a Gearworks Chamber.<div class=\"mousehuntTooltip-arrow\"></div></div></div><div class=\"riftBristleWoodsHUD-acolyteChamber-obeliskChargeBar\"><span style=\"height:0%;\"></span></div><div class=\"riftBristleWoodsHUD-acolyteChamber-obeliskPercent\"><span></span>%</div><div class=\"riftBristleWoodsHUD-acolyteChamber-boundingBox obelisk mousehuntTooltipParent\"><div class=\"mousehuntTooltip tight noEvents right\">The <b>Timesplit Obelisk</b> gains +1 charge for each piece of Rift loot dropped in the chamber. When fully charged, the Absolute Acolyte Mouse's sand will start to drain.<div class=\"mousehuntTooltip-arrow\"></div></div></div><div class=\"riftBristleWoodsHUD-acolyteChamber-acolyteChargeBar\"><span style=\"height:%;\"></span></div><div class=\"riftBristleWoodsHUD-acolyteChamber-acolyteChargeDetails\"></div><a href=\"#\" class=\"riftBristleWoodsHUD-acolyteChamber-retreat mousehuntActionButton tiny \" onclick=\"hg.views.HeadsUpDisplayRiftBristleWoodsView.showConfirm(this); return false;\" data-confirm-type=\"retreat\"><span>Retreat</span></a><div class=\"riftBristleWoodsHUD-acolyteChamber-boundingBox acolyte mousehuntTooltipParent\"><div class=\"mousehuntTooltip tight noEvents left\">Until the <b>Timesplit Obelisk</b> is fully charged, the Absolute Acolyte Mouse will collect Time Sand that runs from your Ancient Hourglass!<br /><br />Charge the Timesplit Obelisk as quickly as possible!<div class=\"mousehuntTooltip-arrow\"></div></div></div></div><div class=\"riftBristleWoodsHUD-overlay\"><div class=\"riftBristleWoodsHUD-dialogContainer\"><div class=\"riftBristleWoodsHUD-dialog-padding\"><div class=\"riftBristleWoodsHUD-dialog-state enterPortal\"><div class=\"riftBristleWoodsHUD-chamberSpecificTextContainer\"><div class=\"riftBristleWoodsHUD-chamberSpecificText acolyte_chamber\"><div class=\"riftBristleWoodsHUD-dialog-title\">Enter the <span class=\"riftBristleWoodsHUD-dialog-title-portalName\">Acolyte Chamber</span>?</div><div class=\"riftBristleWoodsHUD-dialog-description\">Beyond this portal lies the dangerous Acolyte Chamber. Time is broken in this place and plenty of <b>Time Sand</b> is required to remain safely inside.<br />\n<br />\nIf you run out of sand, you run out of time...</div><div class=\"riftBristleWoodsHUD-dialog-image\"><div class=\"riftBristleWoodsHUD-portal acolyte_chamber \"><div class=\"riftBristleWoodsHUD-portal-padding\"><div class=\"riftBristleWoodsHUD-portal-image\"></div><div class=\"riftBristleWoodsHUD-portal-lock\"></div></div></div></div></div><div class=\"riftBristleWoodsHUD-chamberSpecificText basic_chamber\"><div class=\"riftBristleWoodsHUD-dialog-title\">Enter the <span class=\"riftBristleWoodsHUD-dialog-title-portalName\">Gearworks</span>?</div><div class=\"riftBristleWoodsHUD-dialog-description\">Collect <b>Tiny Sprockets</b> as loot from mice to fuel your journey through the Bristle Woods Rift.</div><div class=\"riftBristleWoodsHUD-dialog-image\"><div class=\"riftBristleWoodsHUD-portal basic_chamber \"><div class=\"riftBristleWoodsHUD-portal-padding\"><div class=\"riftBristleWoodsHUD-portal-image\"></div><div class=\"riftBristleWoodsHUD-portal-lock\"></div></div></div></div></div><div class=\"riftBristleWoodsHUD-chamberSpecificText entrance_chamber\"><div class=\"riftBristleWoodsHUD-dialog-title\">Enter the <span class=\"riftBristleWoodsHUD-dialog-title-portalName\">Rift Acolyte Tower</span>?</div><div class=\"riftBristleWoodsHUD-dialog-description\">You stand at the entrance of the <b>Rift Acolyte Tower</b>. Enter to seek out the <b>Absolute Acolyte Mouse</b> and restore the timeline!</div></div><div class=\"riftBristleWoodsHUD-chamberSpecificText guard_chamber\"><div class=\"riftBristleWoodsHUD-dialog-title\">Enter the <span class=\"riftBristleWoodsHUD-dialog-title-portalName\">Guard Barracks</span>?</div><div class=\"riftBristleWoodsHUD-dialog-description\">Loot the chamber to seal away the <b>Portal Paladin mice</b>. Every hunt raises the alert, but catching a Portal Paladin Mouse will reset it!</div><div class=\"riftBristleWoodsHUD-dialog-image\"><div class=\"riftBristleWoodsHUD-portal guard_chamber \"><div class=\"riftBristleWoodsHUD-portal-padding\"><div class=\"riftBristleWoodsHUD-portal-image\"></div><div class=\"riftBristleWoodsHUD-portal-lock\"></div></div></div></div></div><div class=\"riftBristleWoodsHUD-chamberSpecificText icebreak_chamber\"><div class=\"riftBristleWoodsHUD-dialog-title\">Enter the <span class=\"riftBristleWoodsHUD-dialog-title-portalName\">Furnace Room</span>?</div><div class=\"riftBristleWoodsHUD-dialog-description\">Fix the broken furnace by capturing mice that have tampered with it to bring the temperature up and unfreeze the portals.</div><div class=\"riftBristleWoodsHUD-dialog-image\"><div class=\"riftBristleWoodsHUD-portal icebreak_chamber \"><div class=\"riftBristleWoodsHUD-portal-padding\"><div class=\"riftBristleWoodsHUD-portal-image\"></div><div class=\"riftBristleWoodsHUD-portal-lock\"></div></div></div></div></div><div class=\"riftBristleWoodsHUD-chamberSpecificText icy_chamber\"><div class=\"riftBristleWoodsHUD-dialog-title\">Enter the <span class=\"riftBristleWoodsHUD-dialog-title-portalName\">Frozen Alcove</span>?</div><div class=\"riftBristleWoodsHUD-dialog-description\">Complete this chamber in order to gain a magical <b>Acolyte Influence</b> spell.</div><div class=\"riftBristleWoodsHUD-dialog-image\"><div class=\"riftBristleWoodsHUD-portal icy_chamber \"><div class=\"riftBristleWoodsHUD-portal-padding\"><div class=\"riftBristleWoodsHUD-portal-image\"></div><div class=\"riftBristleWoodsHUD-portal-lock\"></div></div></div></div></div><div class=\"riftBristleWoodsHUD-chamberSpecificText ingress_chamber\"><div class=\"riftBristleWoodsHUD-dialog-title\">Enter the <span class=\"riftBristleWoodsHUD-dialog-title-portalName\">Ingress Chamber</span>?</div><div class=\"riftBristleWoodsHUD-dialog-description\">Loot the chamber to gain a <b>Fourth Portal</b> before the <b>Portal Pursuer Mouse</b> is released!</div><div class=\"riftBristleWoodsHUD-dialog-image\"><div class=\"riftBristleWoodsHUD-portal ingress_chamber \"><div class=\"riftBristleWoodsHUD-portal-padding\"><div class=\"riftBristleWoodsHUD-portal-image\"></div><div class=\"riftBristleWoodsHUD-portal-lock\"></div></div></div></div></div><div class=\"riftBristleWoodsHUD-chamberSpecificText lucky_chamber\"><div class=\"riftBristleWoodsHUD-dialog-title\">Enter the <span class=\"riftBristleWoodsHUD-dialog-title-portalName\">Lucky Tower</span>?</div><div class=\"riftBristleWoodsHUD-dialog-description\">Aww, lucky! This chamber is loaded with luck charms and some extra Quantum Quartz! Loot it up before the luck runs dry!</div><div class=\"riftBristleWoodsHUD-dialog-image\"><div class=\"riftBristleWoodsHUD-portal lucky_chamber \"><div class=\"riftBristleWoodsHUD-portal-padding\"><div class=\"riftBristleWoodsHUD-portal-image\"></div><div class=\"riftBristleWoodsHUD-portal-lock\"></div></div></div></div></div><div class=\"riftBristleWoodsHUD-chamberSpecificText magic_chamber\"><div class=\"riftBristleWoodsHUD-dialog-title\">Enter the <span class=\"riftBristleWoodsHUD-dialog-title-portalName\">Runic Laboratory</span>?</div><div class=\"riftBristleWoodsHUD-dialog-description\">Equip <b>Ancient String Cheese</b> and collect <b>Runic String Potions</b> to create <b>Runic String Cheese</b> which will help you find even better loot.</div><div class=\"riftBristleWoodsHUD-dialog-image\"><div class=\"riftBristleWoodsHUD-portal magic_chamber \"><div class=\"riftBristleWoodsHUD-portal-padding\"><div class=\"riftBristleWoodsHUD-portal-image\"></div><div class=\"riftBristleWoodsHUD-portal-lock\"></div></div></div></div></div><div class=\"riftBristleWoodsHUD-chamberSpecificText potion_chamber\"><div class=\"riftBristleWoodsHUD-dialog-title\">Enter the <span class=\"riftBristleWoodsHUD-dialog-title-portalName\">Ancient Lab</span>?</div><div class=\"riftBristleWoodsHUD-dialog-description\">Collect <b>Ancient String Potions</b> to create <b>Ancient String Cheese</b> which will help you find better loot.</div><div class=\"riftBristleWoodsHUD-dialog-image\"><div class=\"riftBristleWoodsHUD-portal potion_chamber \"><div class=\"riftBristleWoodsHUD-portal-padding\"><div class=\"riftBristleWoodsHUD-portal-image\"></div><div class=\"riftBristleWoodsHUD-portal-lock\"></div></div></div></div></div><div class=\"riftBristleWoodsHUD-chamberSpecificText silence_chamber\"><div class=\"riftBristleWoodsHUD-dialog-title\">Enter the <span class=\"riftBristleWoodsHUD-dialog-title-portalName\">Security Chamber</span>?</div><div class=\"riftBristleWoodsHUD-dialog-description\">Disable the security system by capturing mice in this chamber to silence the alarm and bring luck back to your trap.</div><div class=\"riftBristleWoodsHUD-dialog-image\"><div class=\"riftBristleWoodsHUD-portal silence_chamber \"><div class=\"riftBristleWoodsHUD-portal-padding\"><div class=\"riftBristleWoodsHUD-portal-image\"></div><div class=\"riftBristleWoodsHUD-portal-lock\"></div></div></div></div></div><div class=\"riftBristleWoodsHUD-chamberSpecificText stalker_chamber\"><div class=\"riftBristleWoodsHUD-dialog-title\">Enter the <span class=\"riftBristleWoodsHUD-dialog-title-portalName\">Pursuer Mousoleum</span>?</div><div class=\"riftBristleWoodsHUD-dialog-description\">Hunt through this accursed place to bring the <b>Portal Pursuer Mouse</b> to rest and end her tireless pursuit.</div><div class=\"riftBristleWoodsHUD-dialog-image\"><div class=\"riftBristleWoodsHUD-portal stalker_chamber \"><div class=\"riftBristleWoodsHUD-portal-padding\"><div class=\"riftBristleWoodsHUD-portal-image\"></div><div class=\"riftBristleWoodsHUD-portal-lock\"></div></div></div></div></div><div class=\"riftBristleWoodsHUD-chamberSpecificText timewarp_chamber\"><div class=\"riftBristleWoodsHUD-dialog-title\">Enter the <span class=\"riftBristleWoodsHUD-dialog-title-portalName\">Timewarp Chamber</span>?</div><div class=\"riftBristleWoodsHUD-dialog-description\">Catch a <b>Chronomaster Mouse</b> in this chamber using <b>Runic String Cheese</b> to find an <b>Ancient Hourglass</b> and fill it with <b>Time Sand</b>.</div><div class=\"riftBristleWoodsHUD-dialog-image\"><div class=\"riftBristleWoodsHUD-portal timewarp_chamber \"><div class=\"riftBristleWoodsHUD-portal-padding\"><div class=\"riftBristleWoodsHUD-portal-image\"></div><div class=\"riftBristleWoodsHUD-portal-lock\"></div></div></div></div></div><div class=\"riftBristleWoodsHUD-chamberSpecificText treasury_chamber\"><div class=\"riftBristleWoodsHUD-dialog-title\">Enter the <span class=\"riftBristleWoodsHUD-dialog-title-portalName\">Hidden Treasury</span>?</div><div class=\"riftBristleWoodsHUD-dialog-description\">A hidden chamber of wealth, full of gold! Grab as many satchels as you can before the other mice do!</div><div class=\"riftBristleWoodsHUD-dialog-image\"><div class=\"riftBristleWoodsHUD-portal treasury_chamber \"><div class=\"riftBristleWoodsHUD-portal-padding\"><div class=\"riftBristleWoodsHUD-portal-image\"></div><div class=\"riftBristleWoodsHUD-portal-lock\"></div></div></div></div></div></div><div class=\"riftBristleWoodsHUD-dialog-actions\"><a href=\"#\" class=\"mousehuntActionButton small cancel\" onclick=\"hg.views.HeadsUpDisplayRiftBristleWoodsView.hideConfirm(); return false;\"><span>Cancel</span></a><a href=\"#\" class=\"mousehuntActionButton small\" onclick=\"hg.views.HeadsUpDisplayRiftBristleWoodsView.submitConfirm(this); return false;\"><span>Enter Portal</span></a></div></div><div class=\"riftBristleWoodsHUD-dialog-state unfreezePortal\"><div class=\"riftBristleWoodsHUD-chamberSpecificTextContainer\"><div class=\"riftBristleWoodsHUD-chamberSpecificText acolyte_chamber\"><div class=\"riftBristleWoodsHUD-dialog-title\">This <span class=\"riftBristleWoodsHUD-dialog-title-portalName\">Acolyte Chamber</span> is completely frozen!</div><div class=\"riftBristleWoodsHUD-dialog-description\">The cold from the Frozen Alcove has frozen this portal! I'll need to use a Portal Rekindling Key if I want to open it.</div><div class=\"riftBristleWoodsHUD-dialog-image\"><div class=\"itemImage\" style=\"background-image:url(https://www.mousehuntgame.com/images/items/stats/3adb1b99b7d8afe4fc6824d3b785a51d.gif?cv=246);\"><div class=\"quantity\" data-item-type=\"rift_portal_warmer_stat_item\">1</div></div><a href=\"#\" class=\"mousehuntActionButton tiny\" onclick=\"MHCheckout.quickAddToCart('5portalwarmers'); return false;\"><span>Buy 5 Portal<br />Enkindling Keys</span></a></div></div><div class=\"riftBristleWoodsHUD-chamberSpecificText basic_chamber\"><div class=\"riftBristleWoodsHUD-dialog-title\">This <span class=\"riftBristleWoodsHUD-dialog-title-portalName\">Gearworks</span> is completely frozen!</div><div class=\"riftBristleWoodsHUD-dialog-description\">The cold from the Frozen Alcove has frozen this portal! I'll need to use a Portal Rekindling Key if I want to open it.</div><div class=\"riftBristleWoodsHUD-dialog-image\"><div class=\"itemImage\" style=\"background-image:url(https://www.mousehuntgame.com/images/items/stats/3adb1b99b7d8afe4fc6824d3b785a51d.gif?cv=246);\"><div class=\"quantity\" data-item-type=\"rift_portal_warmer_stat_item\">1</div></div><a href=\"#\" class=\"mousehuntActionButton tiny\" onclick=\"MHCheckout.quickAddToCart('5portalwarmers'); return false;\"><span>Buy 5 Portal<br />Enkindling Keys</span></a></div></div><div class=\"riftBristleWoodsHUD-chamberSpecificText entrance_chamber\"><div class=\"riftBristleWoodsHUD-dialog-title\">This <span class=\"riftBristleWoodsHUD-dialog-title-portalName\">Rift Acolyte Tower</span> is completely frozen!</div><div class=\"riftBristleWoodsHUD-dialog-description\">The cold from the Frozen Alcove has frozen this portal! I'll need to use a Portal Rekindling Key if I want to open it.</div><div class=\"riftBristleWoodsHUD-dialog-image\"><div class=\"itemImage\" style=\"background-image:url(https://www.mousehuntgame.com/images/items/stats/3adb1b99b7d8afe4fc6824d3b785a51d.gif?cv=246);\"><div class=\"quantity\" data-item-type=\"rift_portal_warmer_stat_item\">1</div></div><a href=\"#\" class=\"mousehuntActionButton tiny\" onclick=\"MHCheckout.quickAddToCart('5portalwarmers'); return false;\"><span>Buy 5 Portal<br />Enkindling Keys</span></a></div></div><div class=\"riftBristleWoodsHUD-chamberSpecificText guard_chamber\"><div class=\"riftBristleWoodsHUD-dialog-title\">This <span class=\"riftBristleWoodsHUD-dialog-title-portalName\">Guard Barracks</span> is completely frozen!</div><div class=\"riftBristleWoodsHUD-dialog-description\">The cold from the Frozen Alcove has frozen this portal! I'll need to use a Portal Rekindling Key if I want to open it.</div><div class=\"riftBristleWoodsHUD-dialog-image\"><div class=\"itemImage\" style=\"background-image:url(https://www.mousehuntgame.com/images/items/stats/3adb1b99b7d8afe4fc6824d3b785a51d.gif?cv=246);\"><div class=\"quantity\" data-item-type=\"rift_portal_warmer_stat_item\">1</div></div><a href=\"#\" class=\"mousehuntActionButton tiny\" onclick=\"MHCheckout.quickAddToCart('5portalwarmers'); return false;\"><span>Buy 5 Portal<br />Enkindling Keys</span></a></div></div><div class=\"riftBristleWoodsHUD-chamberSpecificText icebreak_chamber\"><div class=\"riftBristleWoodsHUD-dialog-title\">This <span class=\"riftBristleWoodsHUD-dialog-title-portalName\">Furnace Room</span> is completely frozen!</div><div class=\"riftBristleWoodsHUD-dialog-description\">The cold from the Frozen Alcove has frozen this portal! I'll need to use a Portal Rekindling Key if I want to open it.</div><div class=\"riftBristleWoodsHUD-dialog-image\"><div class=\"itemImage\" style=\"background-image:url(https://www.mousehuntgame.com/images/items/stats/3adb1b99b7d8afe4fc6824d3b785a51d.gif?cv=246);\"><div class=\"quantity\" data-item-type=\"rift_portal_warmer_stat_item\">1</div></div><a href=\"#\" class=\"mousehuntActionButton tiny\" onclick=\"MHCheckout.quickAddToCart('5portalwarmers'); return false;\"><span>Buy 5 Portal<br />Enkindling Keys</span></a></div></div><div class=\"riftBristleWoodsHUD-chamberSpecificText icy_chamber\"><div class=\"riftBristleWoodsHUD-dialog-title\">This <span class=\"riftBristleWoodsHUD-dialog-title-portalName\">Frozen Alcove</span> is completely frozen!</div><div class=\"riftBristleWoodsHUD-dialog-description\">The cold from the Frozen Alcove has frozen this portal! I'll need to use a Portal Rekindling Key if I want to open it.</div><div class=\"riftBristleWoodsHUD-dialog-image\"><div class=\"itemImage\" style=\"background-image:url(https://www.mousehuntgame.com/images/items/stats/3adb1b99b7d8afe4fc6824d3b785a51d.gif?cv=246);\"><div class=\"quantity\" data-item-type=\"rift_portal_warmer_stat_item\">1</div></div><a href=\"#\" class=\"mousehuntActionButton tiny\" onclick=\"MHCheckout.quickAddToCart('5portalwarmers'); return false;\"><span>Buy 5 Portal<br />Enkindling Keys</span></a></div></div><div class=\"riftBristleWoodsHUD-chamberSpecificText ingress_chamber\"><div class=\"riftBristleWoodsHUD-dialog-title\">This <span class=\"riftBristleWoodsHUD-dialog-title-portalName\">Ingress Chamber</span> is completely frozen!</div><div class=\"riftBristleWoodsHUD-dialog-description\">The cold from the Frozen Alcove has frozen this portal! I'll need to use a Portal Rekindling Key if I want to open it.</div><div class=\"riftBristleWoodsHUD-dialog-image\"><div class=\"itemImage\" style=\"background-image:url(https://www.mousehuntgame.com/images/items/stats/3adb1b99b7d8afe4fc6824d3b785a51d.gif?cv=246);\"><div class=\"quantity\" data-item-type=\"rift_portal_warmer_stat_item\">1</div></div><a href=\"#\" class=\"mousehuntActionButton tiny\" onclick=\"MHCheckout.quickAddToCart('5portalwarmers'); return false;\"><span>Buy 5 Portal<br />Enkindling Keys</span></a></div></div><div class=\"riftBristleWoodsHUD-chamberSpecificText lucky_chamber\"><div class=\"riftBristleWoodsHUD-dialog-title\">This <span class=\"riftBristleWoodsHUD-dialog-title-portalName\">Lucky Tower</span> is completely frozen!</div><div class=\"riftBristleWoodsHUD-dialog-description\">The cold from the Frozen Alcove has frozen this portal! I'll need to use a Portal Rekindling Key if I want to open it.</div><div class=\"riftBristleWoodsHUD-dialog-image\"><div class=\"itemImage\" style=\"background-image:url(https://www.mousehuntgame.com/images/items/stats/3adb1b99b7d8afe4fc6824d3b785a51d.gif?cv=246);\"><div class=\"quantity\" data-item-type=\"rift_portal_warmer_stat_item\">1</div></div><a href=\"#\" class=\"mousehuntActionButton tiny\" onclick=\"MHCheckout.quickAddToCart('5portalwarmers'); return false;\"><span>Buy 5 Portal<br />Enkindling Keys</span></a></div></div><div class=\"riftBristleWoodsHUD-chamberSpecificText magic_chamber\"><div class=\"riftBristleWoodsHUD-dialog-title\">This <span class=\"riftBristleWoodsHUD-dialog-title-portalName\">Runic Laboratory</span> is completely frozen!</div><div class=\"riftBristleWoodsHUD-dialog-description\">The cold from the Frozen Alcove has frozen this portal! I'll need to use a Portal Rekindling Key if I want to open it.</div><div class=\"riftBristleWoodsHUD-dialog-image\"><div class=\"itemImage\" style=\"background-image:url(https://www.mousehuntgame.com/images/items/stats/3adb1b99b7d8afe4fc6824d3b785a51d.gif?cv=246);\"><div class=\"quantity\" data-item-type=\"rift_portal_warmer_stat_item\">1</div></div><a href=\"#\" class=\"mousehuntActionButton tiny\" onclick=\"MHCheckout.quickAddToCart('5portalwarmers'); return false;\"><span>Buy 5 Portal<br />Enkindling Keys</span></a></div></div><div class=\"riftBristleWoodsHUD-chamberSpecificText potion_chamber\"><div class=\"riftBristleWoodsHUD-dialog-title\">This <span class=\"riftBristleWoodsHUD-dialog-title-portalName\">Ancient Lab</span> is completely frozen!</div><div class=\"riftBristleWoodsHUD-dialog-description\">The cold from the Frozen Alcove has frozen this portal! I'll need to use a Portal Rekindling Key if I want to open it.</div><div class=\"riftBristleWoodsHUD-dialog-image\"><div class=\"itemImage\" style=\"background-image:url(https://www.mousehuntgame.com/images/items/stats/3adb1b99b7d8afe4fc6824d3b785a51d.gif?cv=246);\"><div class=\"quantity\" data-item-type=\"rift_portal_warmer_stat_item\">1</div></div><a href=\"#\" class=\"mousehuntActionButton tiny\" onclick=\"MHCheckout.quickAddToCart('5portalwarmers'); return false;\"><span>Buy 5 Portal<br />Enkindling Keys</span></a></div></div><div class=\"riftBristleWoodsHUD-chamberSpecificText silence_chamber\"><div class=\"riftBristleWoodsHUD-dialog-title\">This <span class=\"riftBristleWoodsHUD-dialog-title-portalName\">Security Chamber</span> is completely frozen!</div><div class=\"riftBristleWoodsHUD-dialog-description\">The cold from the Frozen Alcove has frozen this portal! I'll need to use a Portal Rekindling Key if I want to open it.</div><div class=\"riftBristleWoodsHUD-dialog-image\"><div class=\"itemImage\" style=\"background-image:url(https://www.mousehuntgame.com/images/items/stats/3adb1b99b7d8afe4fc6824d3b785a51d.gif?cv=246);\"><div class=\"quantity\" data-item-type=\"rift_portal_warmer_stat_item\">1</div></div><a href=\"#\" class=\"mousehuntActionButton tiny\" onclick=\"MHCheckout.quickAddToCart('5portalwarmers'); return false;\"><span>Buy 5 Portal<br />Enkindling Keys</span></a></div></div><div class=\"riftBristleWoodsHUD-chamberSpecificText stalker_chamber\"><div class=\"riftBristleWoodsHUD-dialog-title\">This <span class=\"riftBristleWoodsHUD-dialog-title-portalName\">Pursuer Mousoleum</span> is completely frozen!</div><div class=\"riftBristleWoodsHUD-dialog-description\">The cold from the Frozen Alcove has frozen this portal! I'll need to use a Portal Rekindling Key if I want to open it.</div><div class=\"riftBristleWoodsHUD-dialog-image\"><div class=\"itemImage\" style=\"background-image:url(https://www.mousehuntgame.com/images/items/stats/3adb1b99b7d8afe4fc6824d3b785a51d.gif?cv=246);\"><div class=\"quantity\" data-item-type=\"rift_portal_warmer_stat_item\">1</div></div><a href=\"#\" class=\"mousehuntActionButton tiny\" onclick=\"MHCheckout.quickAddToCart('5portalwarmers'); return false;\"><span>Buy 5 Portal<br />Enkindling Keys</span></a></div></div><div class=\"riftBristleWoodsHUD-chamberSpecificText timewarp_chamber\"><div class=\"riftBristleWoodsHUD-dialog-title\">This <span class=\"riftBristleWoodsHUD-dialog-title-portalName\">Timewarp Chamber</span> is completely frozen!</div><div class=\"riftBristleWoodsHUD-dialog-description\">The cold from the Frozen Alcove has frozen this portal! I'll need to use a Portal Rekindling Key if I want to open it.</div><div class=\"riftBristleWoodsHUD-dialog-image\"><div class=\"itemImage\" style=\"background-image:url(https://www.mousehuntgame.com/images/items/stats/3adb1b99b7d8afe4fc6824d3b785a51d.gif?cv=246);\"><div class=\"quantity\" data-item-type=\"rift_portal_warmer_stat_item\">1</div></div><a href=\"#\" class=\"mousehuntActionButton tiny\" onclick=\"MHCheckout.quickAddToCart('5portalwarmers'); return false;\"><span>Buy 5 Portal<br />Enkindling Keys</span></a></div></div><div class=\"riftBristleWoodsHUD-chamberSpecificText treasury_chamber\"><div class=\"riftBristleWoodsHUD-dialog-title\">This <span class=\"riftBristleWoodsHUD-dialog-title-portalName\">Hidden Treasury</span> is completely frozen!</div><div class=\"riftBristleWoodsHUD-dialog-description\">The cold from the Frozen Alcove has frozen this portal! I'll need to use a Portal Rekindling Key if I want to open it.</div><div class=\"riftBristleWoodsHUD-dialog-image\"><div class=\"itemImage\" style=\"background-image:url(https://www.mousehuntgame.com/images/items/stats/3adb1b99b7d8afe4fc6824d3b785a51d.gif?cv=246);\"><div class=\"quantity\" data-item-type=\"rift_portal_warmer_stat_item\">1</div></div><a href=\"#\" class=\"mousehuntActionButton tiny\" onclick=\"MHCheckout.quickAddToCart('5portalwarmers'); return false;\"><span>Buy 5 Portal<br />Enkindling Keys</span></a></div></div></div><div class=\"riftBristleWoodsHUD-dialog-actions\"><a href=\"#\" class=\"mousehuntActionButton small cancel\" onclick=\"hg.views.HeadsUpDisplayRiftBristleWoodsView.hideConfirm(); return false;\"><span>Cancel</span></a><a href=\"#\" class=\"mousehuntActionButton small confirm\" onclick=\"hg.views.HeadsUpDisplayRiftBristleWoodsView.submitConfirm(this); return false;\"><span>Unfreeze Portal</span></a></div></div><div class=\"riftBristleWoodsHUD-dialog-state scramblePortals\"><div class=\"riftBristleWoodsHUD-dialog-title\">Scramble Portals?</div><div class=\"riftBristleWoodsHUD-dialog-description\">This will consume 1 Portal Scrambler and generate new portals.</div><div class=\"riftBristleWoodsHUD-dialog-image\"><div class=\"itemImage\" style=\"background-image:url(https://www.mousehuntgame.com/images/items/stats/61e4557721b07d36916048791fa23cb9.gif?cv=246);\"><div class=\"quantity\" data-item-type=\"rift_scramble_portals_stat_item\">0</div></div><a href=\"#\" class=\"mousehuntActionButton tiny\" onclick=\"MHCheckout.quickAddToCart('5portal_scrambler'); return false;\"><span>Buy 5 Portal<br />Scramblers</span></a></div><div class=\"riftBristleWoodsHUD-dialog-actions\"><a href=\"#\" class=\"mousehuntActionButton small cancel\" onclick=\"hg.views.HeadsUpDisplayRiftBristleWoodsView.hideConfirm(); return false;\"><span>Cancel</span></a><a href=\"#\" class=\"mousehuntActionButton small confirm disabled noPortals\" onclick=\"hg.views.HeadsUpDisplayRiftBristleWoodsView.submitConfirm(this); return false;\"><span>Scramble it!</span></a></div></div><div class=\"riftBristleWoodsHUD-dialog-state retreat\"><div class=\"riftBristleWoodsHUD-dialog-title\">Retreat from the Acolyte Chamber?</div><div class=\"riftBristleWoodsHUD-dialog-description\">You'll need to find another Acolyte Chamber portal to return.</div><div class=\"riftBristleWoodsHUD-dialog-actions\"><a href=\"#\" class=\"mousehuntActionButton small cancel\" onclick=\"hg.views.HeadsUpDisplayRiftBristleWoodsView.hideConfirm(); return false;\"><span>Cancel</span></a><a href=\"#\" class=\"mousehuntActionButton small confirm\" onclick=\"hg.views.HeadsUpDisplayRiftBristleWoodsView.submitConfirm(this); return false;\"><span>Retreat</span></a></div></div></div></div></div></div>",
      "global_hud": None,
      "is_legacy": None
    }
  },
  "messageData": {
    "page": {
      "newMessageCount": 0,
      "messageCount": 0,
      "messages": []
    },
    "notification": {
      "newMessageCount": 0,
      "messageCount": 28
    },
    "popup": {
      "newMessageCount": 0,
      "messageCount": 0,
      "messages": []
    },
    "arrow": {
      "newMessageCount": 0,
      "messageCount": 0,
      "messages": []
    },
    "custom": {
      "newMessageCount": 0,
      "messageCount": 0,
      "messages": []
    },
    "game_request": {
      "newMessageCount": 0,
      "messageCount": 0
    },
    "message_model": {
      "newMessageCount": 0,
      "messageCount": 0,
      "messages": []
    },
    "map_invite": {
      "newMessageCount": 0,
      "messageCount": 0
    },
    "corkboard_map": {
      "newMessageCount": 0,
      "messageCount": 0
    },
    "corkboard_team": {
      "newMessageCount": 0,
      "messageCount": 0
    },
    "social_gift_counter": {
      "newMessageCount": 0,
      "messageCount": 0
    },
    "egg_carton": {
      "newMessageCount": 0,
      "messageCount": 0
    }
  },
  "page_title": "MouseHunt | Hunter's Camp",
  "page": {
    "user_id": "8056376",
    "trap_stats": [
      {
        "type": "power",
        "label": "Power",
        "value": "2,609",
        "power_type": "Rift",
        "base": [
          {
            "value": "500",
            "thumb": "https://www.mousehuntgame.com/images/items/bases/4013d40ad9cea2d53b55fcc1b5d20851.jpg?cv=246",
            "name": "Attuned Enerchi Induction Base"
          },
          {
            "value": "1,250",
            "thumb": "https://www.mousehuntgame.com/images/items/weapons/a1b6c88f8ed3e8598b088852a8d3db1b.jpg?cv=246",
            "name": "Rift Glacier Gatler"
          },
          {
            "value": "100",
            "thumb": "https://www.mousehuntgame.com/images/items/trinkets/78dc60695a186f1496f69f0dc699c627.gif?cv=246",
            "name": "Rift Charm"
          }
        ],
        "bonus": [
          {
            "value": "10%",
            "thumb": "https://www.mousehuntgame.com/images/items/bases/4013d40ad9cea2d53b55fcc1b5d20851.jpg?cv=246",
            "name": "Attuned Enerchi Induction Base"
          },
          {
            "value": "10%",
            "thumb": "https://www.mousehuntgame.com/images/items/weapons/a1b6c88f8ed3e8598b088852a8d3db1b.jpg?cv=246",
            "name": "Rift Glacier Gatler"
          },
          {
            "value": "1%",
            "thumb": "https://www.mousehuntgame.com/images/items/trinkets/78dc60695a186f1496f69f0dc699c627.gif?cv=246",
            "name": "Rift Charm"
          }
        ],
        "has_bonus": True,
        "special": [
          {
            "value": "20%",
            "name": "Riftwalker Set Bonus (3 pieces)",
            "thumb": "https://www.mousehuntgame.com/images/items/maps/e283e8bffd84142b6469d8324df5b5bb.jpg?cv=246",
            "css_class": "special"
          }
        ],
        "has_special": True
      },
      {
        "type": "luck",
        "label": "Luck",
        "value": 25,
        "has_shield": True,
        "base": [
          {
            "value": "10",
            "thumb": "https://www.mousehuntgame.com/images/items/bases/4013d40ad9cea2d53b55fcc1b5d20851.jpg?cv=246",
            "name": "Attuned Enerchi Induction Base"
          },
          {
            "value": "3",
            "thumb": "https://www.mousehuntgame.com/images/items/weapons/a1b6c88f8ed3e8598b088852a8d3db1b.jpg?cv=246",
            "name": "Rift Glacier Gatler"
          }
        ],
        "special": [
          {
            "value": "5",
            "name": "Riftwalker Set Bonus (3 pieces)",
            "thumb": "https://www.mousehuntgame.com/images/items/maps/e283e8bffd84142b6469d8324df5b5bb.jpg?cv=246",
            "css_class": "special"
          }
        ],
        "has_special": True
      },
      {
        "type": "attraction_bonus",
        "label": "Attraction Bonus",
        "value": "20%",
        "base": [
          {
            "value": "10%",
            "thumb": "https://www.mousehuntgame.com/images/items/bases/4013d40ad9cea2d53b55fcc1b5d20851.jpg?cv=246",
            "name": "Attuned Enerchi Induction Base"
          },
          {
            "value": "10%",
            "thumb": "https://www.mousehuntgame.com/images/items/weapons/a1b6c88f8ed3e8598b088852a8d3db1b.jpg?cv=246",
            "name": "Rift Glacier Gatler"
          }
        ]
      },
      {
        "type": "cheese_effect",
        "label": "Cheese Effect",
        "value": "No Effect",
        "base": [
          {
            "name": "Your trap has no cheese effect bonus.",
            "value": ""
          }
        ]
      }
    ],
    "limited_edition": True,
    "base_item_id": "2120",
    "base_thumb": "https://www.mousehuntgame.com/images/items/bases/4013d40ad9cea2d53b55fcc1b5d20851.jpg?cv=246",
    "has_base": "",
    "weapon_item_id": "2956",
    "weapon_thumb": "https://www.mousehuntgame.com/images/items/weapons/a1b6c88f8ed3e8598b088852a8d3db1b.jpg?cv=246",
    "has_weapon": "",
    "bait_item_id": "2343",
    "bait_name": "Ancient String Cheese",
    "bait_thumb": "https://www.mousehuntgame.com/images/items/bait/5cb84d2e781edafc6419b8cab67f92ce.gif?cv=246",
    "bait_quantity": "89",
    "has_bait": "",
    "trinket_item_id": "1430",
    "trinket_thumb": "https://www.mousehuntgame.com/images/items/trinkets/78dc60695a186f1496f69f0dc699c627.gif?cv=246",
    "trinket_quantity": "1,157",
    "has_trinket": "",
    "skin_item_id": "",
    "skin_thumb": "",
    "has_skin": "hidden",
    "skin_name": "",
    "journals": [
      {
        "entry": "<div id=\"journallatestentry\" class='entry short active catchsuccessloot' data-entry-id='59207' data-mouse-type='rift_sorcerer'><div class='journalimage'><a href='https://www.mousehuntgame.com/images/mice/large/e5f1e36e5e9249774146972b89fa3f27.jpg?cv=246' onclick='showJournalPopup(\"https://www.mousehuntgame.com/images/mice/large/e5f1e36e5e9249774146972b89fa3f27.jpg?cv=246\", this); return false;'><img src='https://www.mousehuntgame.com/images/mice/thumb/852bdd9e2840461cb9189d9f5f60808a.gif?cv=246' border='0' /></a></div><div class='journalbody'><div class='journalactions'><a href=\"#\" onclick=\"SocialFramework.shareToFeedButton(this); return false;\" data-type=\"journal\" data-params-string=\"user_id=8056376&journal_id=59207\" class=\"\"></a></div><div class='journaldate'>10:49 pm - Bristle Woods Rift</div><div class='journaltext'>I sounded the Hunter's Horn and was successful in the hunt! I caught a 1 lb. 4 oz. <a href=\"https://www.mousehuntgame.com/\" onclick=\"javascript:hg.views.MouseView.show('rift_sorcerer'); return false;\">Timelost Thaumaturge Mouse</a> worth 70,000 points and 7,500 gold.<br /><br /><b>The mouse also dropped the following loot:</b><br />1 <a class=\"lucky\" title=\"The Luck from your Trap Setup caused this item to drop!\" href=\"https://www.mousehuntgame.com/item.php?item_type=rift_quantum_quartz_stat_item\" onclick=\"hg.views.ItemView.show('rift_quantum_quartz_stat_item'); return false;\">Quantum Quartz</a>, 7 <a class=\"loot\" title=\"\" href=\"https://www.mousehuntgame.com/item.php?item_type=rift_temporal_distortion_stat_item\" onclick=\"hg.views.ItemView.show('rift_temporal_distortion_stat_item'); return false;\">Rift Distortions</a>, 1 <a class=\"loot\" title=\"\" href=\"https://www.mousehuntgame.com/item.php?item_type=chrome_bit_stat_item\" onclick=\"hg.views.ItemView.show('chrome_bit_stat_item'); return false;\">Chrome Bit</a>, and 3 <a class=\"loot\" title=\"\" href=\"https://www.mousehuntgame.com/item.php?item_type=runic_string_cheese_potion\" onclick=\"hg.views.ItemView.show('runic_string_cheese_potion'); return false;\">Runic String Cheese Potions</a></div></div><div style='clear:both;'></div></div>"
      },
      {
        "entry": "<div  class='entry short passive catchsuccessloot' data-entry-id='59206' data-mouse-type='rift_gorgon'><div class='journalimage'><a href='https://www.mousehuntgame.com/images/mice/large/8a07ab1422c2786553af6a9e2ec663cb.jpg?cv=246' onclick='showJournalPopup(\"https://www.mousehuntgame.com/images/mice/large/8a07ab1422c2786553af6a9e2ec663cb.jpg?cv=246\", this); return false;'><img src='https://www.mousehuntgame.com/images/mice/thumb/35727c1f4ed537a9278fd4da23f4f153.gif?cv=246' border='0' /></a></div><div class='journalbody'><div class='journalactions'><a href=\"#\" onclick=\"SocialFramework.shareToFeedButton(this); return false;\" data-type=\"journal\" data-params-string=\"user_id=8056376&journal_id=59206\" class=\"\"></a></div><div class='journaldate'>10:45 pm - Bristle Woods Rift</div><div class='journaltext'>I checked my trap and found that I had caught a mouse! I caught a 1 lb. 7 oz. <a href=\"https://www.mousehuntgame.com/\" onclick=\"javascript:hg.views.MouseView.show('rift_gorgon'); return false;\">Timeslither Pythoness Mouse</a> worth 100,000 points and 20,000 gold.<br /><br /><b>The mouse also dropped the following loot:</b><br />10 <a class=\"loot\" title=\"\" href=\"https://www.mousehuntgame.com/item.php?item_type=rift_temporal_distortion_stat_item\" onclick=\"hg.views.ItemView.show('rift_temporal_distortion_stat_item'); return false;\">Rift Distortions</a>, and 2 <a class=\"loot\" title=\"\" href=\"https://www.mousehuntgame.com/item.php?item_type=runic_string_cheese_potion\" onclick=\"hg.views.ItemView.show('runic_string_cheese_potion'); return false;\">Runic String Cheese Potions</a></div></div><div style='clear:both;'></div></div>"
      },
      {
        "entry": "<div  class='entry short potionuse convertible_open' data-entry-id='59205' ><div class='journalimage'><img src='https://www.mousehuntgame.com/images/items/potions/d22e1e50ae80c4f1318106659ee6440a.jpg?cv=246' border='0' /></div><div class='journalbody'><div class='journalactions'><a href=\"#\" onclick=\"SocialFramework.shareToFeedButton(this); return false;\" data-type=\"journal\" data-params-string=\"user_id=8056376&journal_id=59205\" class=\"\"></a></div><div class='journaldate'>10:44 pm - Bristle Woods Rift</div><div class='journaltext'>I brewed 6 Runic String Cheese which used <span class=\"token\">6 Ancient String Cheese</span>, <span class=\"token\">3 Runic String Cheese Potions</span> and <span class=\"token\">3,000 gold</span>.</div></div><div style='clear:both;'></div></div>"
      },
      {
        "entry": "<div  class='entry short active catchsuccessloot' data-entry-id='59204' data-mouse-type='rift_sorcerer'><div class='journalimage'><a href='https://www.mousehuntgame.com/images/mice/large/e5f1e36e5e9249774146972b89fa3f27.jpg?cv=246' onclick='showJournalPopup(\"https://www.mousehuntgame.com/images/mice/large/e5f1e36e5e9249774146972b89fa3f27.jpg?cv=246\", this); return false;'><img src='https://www.mousehuntgame.com/images/mice/thumb/852bdd9e2840461cb9189d9f5f60808a.gif?cv=246' border='0' /></a></div><div class='journalbody'><div class='journalactions'><a href=\"#\" onclick=\"SocialFramework.shareToFeedButton(this); return false;\" data-type=\"journal\" data-params-string=\"user_id=8056376&journal_id=59204\" class=\"\"></a></div><div class='journaldate'>10:34 pm - Bristle Woods Rift</div><div class='journaltext'>I sounded the Hunter's Horn and was successful in the hunt! I caught a 15 oz. <a href=\"https://www.mousehuntgame.com/\" onclick=\"javascript:hg.views.MouseView.show('rift_sorcerer'); return false;\">Timelost Thaumaturge Mouse</a> worth 70,000 points and 7,500 gold.<br /><br /><b>The mouse also dropped the following loot:</b><br />1 <a class=\"loot\" title=\"\" href=\"https://www.mousehuntgame.com/item.php?item_type=rift_quantum_quartz_stat_item\" onclick=\"hg.views.ItemView.show('rift_quantum_quartz_stat_item'); return false;\">Quantum Quartz</a>, 7 <a class=\"loot\" title=\"\" href=\"https://www.mousehuntgame.com/item.php?item_type=rift_temporal_distortion_stat_item\" onclick=\"hg.views.ItemView.show('rift_temporal_distortion_stat_item'); return false;\">Rift Distortions</a>, 1 <a class=\"lucky\" title=\"The Luck from your Trap Setup caused this item to drop!\" href=\"https://www.mousehuntgame.com/item.php?item_type=chrome_bit_stat_item\" onclick=\"hg.views.ItemView.show('chrome_bit_stat_item'); return false;\">Chrome Bit</a>, and 3 <a class=\"loot\" title=\"\" href=\"https://www.mousehuntgame.com/item.php?item_type=runic_string_cheese_potion\" onclick=\"hg.views.ItemView.show('runic_string_cheese_potion'); return false;\">Runic String Cheese Potions</a></div></div><div style='clear:both;'></div></div>"
      },
      {
        "entry": "<div  class='entry short potionuse convertible_open' data-entry-id='59203' ><div class='journalimage'><img src='https://www.mousehuntgame.com/images/items/potions/d22e1e50ae80c4f1318106659ee6440a.jpg?cv=246' border='0' /></div><div class='journalbody'><div class='journalactions'><a href=\"#\" onclick=\"SocialFramework.shareToFeedButton(this); return false;\" data-type=\"journal\" data-params-string=\"user_id=8056376&journal_id=59203\" class=\"\"></a></div><div class='journaldate'>10:24 pm - Bristle Woods Rift</div><div class='journaltext'>I brewed 2 Runic String Cheese which used <span class=\"token\">2 Ancient String Cheese</span>, <span class=\"token\">1 Runic String Cheese Potion</span> and <span class=\"token\">1,000 gold</span>.</div></div><div style='clear:both;'></div></div>"
      },
      {
        "entry": "<div  class='entry short active catchsuccessloot luckycatchsuccess' data-entry-id='59202' data-mouse-type='rift_gargoyle'><div class='journalimage'><a href='https://www.mousehuntgame.com/images/mice/large/7d1a957eb8f26a989427c0c9c7e7981b.jpg?cv=246' onclick='showJournalPopup(\"https://www.mousehuntgame.com/images/mice/large/7d1a957eb8f26a989427c0c9c7e7981b.jpg?cv=246\", this); return false;'><img src='https://www.mousehuntgame.com/images/mice/thumb/f7b15a0b73dd724474750f4de68d4a95.gif?cv=246' border='0' /></a></div><div class='journalbody'><div class='journalactions'><a href=\"#\" onclick=\"SocialFramework.shareToFeedButton(this); return false;\" data-type=\"journal\" data-params-string=\"user_id=8056376&journal_id=59202\" class=\"\"></a></div><div class='journaldate'>10:19 pm - Bristle Woods Rift</div><div class='journaltext'>I sounded the Hunter's Horn and got <font class='luckyCatch'>lucky</font>!<br /><br />I caught a 1 lb. 4 oz. <a href=\"https://www.mousehuntgame.com/\" onclick=\"javascript:hg.views.MouseView.show('rift_gargoyle'); return false;\">Vigilant Ward Mouse</a> worth 42,275 points and 5,000 gold.<br /><br /><b>The mouse also dropped the following loot:</b><br />1 <a class=\"loot\" title=\"\" href=\"https://www.mousehuntgame.com/item.php?item_type=rift_sprocket_stat_item\" onclick=\"hg.views.ItemView.show('rift_sprocket_stat_item'); return false;\">Tiny Sprocket</a>, 5 <a class=\"loot\" title=\"\" href=\"https://www.mousehuntgame.com/item.php?item_type=rift_temporal_distortion_stat_item\" onclick=\"hg.views.ItemView.show('rift_temporal_distortion_stat_item'); return false;\">Rift Distortions</a>, 1 <a class=\"lucky\" title=\"The Luck from your Trap Setup caused this item to drop!\" href=\"https://www.mousehuntgame.com/item.php?item_type=chrome_bit_stat_item\" onclick=\"hg.views.ItemView.show('chrome_bit_stat_item'); return false;\">Chrome Bit</a>, and 1 <a class=\"loot\" title=\"\" href=\"https://www.mousehuntgame.com/item.php?item_type=runic_string_cheese_potion\" onclick=\"hg.views.ItemView.show('runic_string_cheese_potion'); return false;\">Runic String Cheese Potion</a></div></div><div style='clear:both;'></div></div>"
      },
      {
        "entry": "<div  class='entry short marketplace marketplace_complete_listing' data-entry-id='59201' ><div class='journalbody'><div class='journalactions'><a href=\"#\" onclick=\"SocialFramework.shareToFeedButton(this); return false;\" data-type=\"journal\" data-params-string=\"user_id=8056376&journal_id=59201\" class=\"\"></a></div><div class='journaldate'>10:18 pm - Bristle Woods Rift</div><div class='journaltext'>I completed a listing for Ancient String Cheese at the Marketplace.  I received 100 Ancient String Cheese.</div></div><div style='clear:both;'></div></div>"
      },
      {
        "entry": "<div  class='entry short marketplace marketplace_create_listing' data-entry-id='59200' ><div class='journalbody'><div class='journalactions'><a href=\"#\" onclick=\"SocialFramework.shareToFeedButton(this); return false;\" data-type=\"journal\" data-params-string=\"user_id=8056376&journal_id=59200\" class=\"\"></a></div><div class='journaldate'>10:18 pm - Bristle Woods Rift</div><div class='journaltext'>I created an offer to buy 100 Ancient String Cheese for 15,700 gold each, for a total of 1,570,000 gold.</div></div><div style='clear:both;'></div></div>"
      },
      {
        "entry": "<div  class='entry short active catchfailure' data-entry-id='59199' data-mouse-type='rift_ooze'><div class='journalbody'><div class='journalactions'><a href=\"#\" onclick=\"SocialFramework.shareToFeedButton(this); return false;\" data-type=\"journal\" data-params-string=\"user_id=8056376&journal_id=59199\" class=\"\"></a></div><div class='journaldate'>10:03 pm - Bristle Woods Rift</div><div class='journaltext'>I sounded the Hunter's Horn, but my efforts were fruitless. A <a href=\"https://www.mousehuntgame.com/\" onclick=\"javascript:hg.views.MouseView.show('rift_ooze'); return false;\">Sentient Slime Mouse</a> ate a piece of cheese without setting off my trap.</div></div><div style='clear:both;'></div></div>"
      },
      {
        "entry": "<div  class='entry short misc custom rift-bristlewoods-enterPortal' data-entry-id='59198' ><div class='journalbody'><div class='journalactions'><a href=\"#\" onclick=\"SocialFramework.shareToFeedButton(this); return false;\" data-type=\"journal\" data-params-string=\"user_id=8056376&journal_id=59198\" class=\"\"></a></div><div class='journaldate'>9:54 pm - Bristle Woods Rift</div><div class='journaltext'><b>I entered a Runic Laboratory!</b><br />Equip <b>Ancient String Cheese</b> and collect <b>Runic String Potions</b> to create <b>Runic String Cheese</b> which will help you find even better loot.</div></div><div style='clear:both;'></div></div>"
      }
    ],
    "journal_theme": "theme_halloween_2019",
    "friends": [],
    "friends_online": 24,
    "environment_name": "Bristle Woods Rift",
    "larry_tips": "The tower consists of an array of chambers separated by impenetrable walls. The only way to move throughout the tower is to pass through the various portals that present themselves within the chambers.<br />\n<br />\nEach chamber is filled with precious loot that the mice themselves are trying to collect in order to fashion a way of escape. Once a chamber has been emptied of its loot, look for a portal to be opened by the mice looking to escape into another more prosperous room.<br />\n<br />\nYou will need to find the Ancient Lab and Runic Laboratory chambers to obtain powerful potions that can be used to turn your String Cheese into a more preferred flavour to attract the obscure and powerful mice within the many special chambers of this Rift.<br />\n<br />\nOnce you have accumulated some Runic String Cheese, you can attempt to enter the Timewarp Chamber and acquire an Ancient Hourglass. Once obtained, you can then collect valuable Time Sand which will allow you to find the Acolyte Chamber and challenge the fearsome mouse itself.<br />\n<br />\nThere is also a plethora of special chambers that offer difficult challenges and unique abilities as well as powerful curses that will hinder your progress. Many great treasures await, so good luck and happy hunting!<br />\n<br />\nJust... try not to lose too much time...",
    "larry_thumb_class": "",
    "camp_banner": False,
    "has_camp_banner": "hidden",
    "has_quest": True,
    "has_daily": True,
    "trap_effectiveness": "Medium",
    "setup_effectiveness": "medium",
    "adventures": [
      {
        "name": "Capture the Absolute Acolyte",
        "can_claim": True,
        "is_claimed": None,
        "type": "catch_rift_acolyte_adv",
        "header_image": "https://www.mousehuntgame.com/images/environments/f96ec205e6d305a8ceb62a9ffc7042c4.jpg?cv=246",
        "header_type": False,
        "goal": False,
        "has_goal": None
      }
    ],
    "camp_huds": [
      "MiniEventRonzaChromeBit"
    ],
    "layers": {
      "base": {
        "type": "furoma_rift_energy_upgraded_base",
        "url": "https://www.mousehuntgame.com/images/items/bases/trap_small/2db1cf12d746f7d95b1bc2538ef48943.png?cv=246",
        "left": 0,
        "top": 0,
        "width": None
      },
      "weapon": {
        "type": "rift_glacier_gatler_weapon",
        "url": "https://www.mousehuntgame.com/images/items/weapons/trap_small/deef0e572c13244386a14fbf771dc2af.png?cv=246",
        "skin": "no_skin"
      },
      "bait": {
        "type": "ancient_string_cheese",
        "url": "https://www.mousehuntgame.com/images/items/bait/trap_small/b82baf827849bf2ef2e6707425ea1bae.png?cv=246",
        "left": 0,
        "top": 0,
        "width": None
      }
    },
    "auras": {
      "MiniEventLabyrinthLostChest": {
        "status": "hidden",
        "expiry": "Jan 1"
      },
      "MiniEventFestiveAura": {
        "status": "hidden",
        "expiry": "January 26, 2020 @ 9:42am (Local Time)"
      },
      "QuestRelicHunter": {
        "status": "hidden",
        "expiry": "Aug 26 2020 @ 10:52pm"
      },
      "MiniEventPillowcase": {
        "status": "hidden",
        "expiry": "Aug 26 2020 @ 10:52pm"
      },
      "QuestChromeAura": {
        "status": "inactive",
        "expiry": "Aug 26 2020 @ 10:52pm"
      },
      "QuestHalloween2019": {
        "status": "hidden",
        "expiry": "November 23, 2019 @ 12:31am (Local Time)"
      },
      "QuestLightningAura": {
        "status": "inactive",
        "expiry": "August 26, 2020 @ 10:52pm"
      },
      "QuestAnniversaryAura": {
        "status": "hidden",
        "expiry": "April 2, 2020 @ 2:56pm"
      }
    }
  },
  "body_css_class": "PageCamp hasSidebar",
  "page_banner": {
    "title": "Dominate the Rift! Arm yourself with the Bristle Woods Rift Supply Kit",
    "image": "https://www.mousehuntgame.com/images/promo/page_banners/rift_bristle_woods/bwr_supply_kit.jpg",
    "onclick": "MHCheckout.show(); return false;",
    "weight": 5
  },
  "asset_package_hash": "246e289300ac7",
  "server_info": "10.208.225.236 - web-def-as52d6e9fb",
  "success": 1,
  "inventory": [],
  "trap_image": {
    "user_id": "8056376",
    "layers": {
      "base": {
        "type": "furoma_rift_energy_upgraded_base",
        "url": "https://www.mousehuntgame.com/images/items/bases/trap_small/2db1cf12d746f7d95b1bc2538ef48943.png?cv=246",
        "left": 0,
        "top": 0,
        "width": None
      },
      "weapon": {
        "type": "rift_glacier_gatler_weapon",
        "url": "https://www.mousehuntgame.com/images/items/weapons/trap_small/deef0e572c13244386a14fbf771dc2af.png?cv=246",
        "skin": "no_skin"
      },
      "bait": {
        "type": "ancient_string_cheese",
        "url": "https://www.mousehuntgame.com/images/items/bait/trap_small/b82baf827849bf2ef2e6707425ea1bae.png?cv=246",
        "left": 0,
        "top": 0,
        "width": None
      }
    },
    "limited_edition": True,
    "auras": {
      "MiniEventLabyrinthLostChest": {
        "status": "hidden",
        "expiry": "Jan 1"
      },
      "MiniEventFestiveAura": {
        "status": "hidden",
        "expiry": "January 26, 2020 @ 9:42am (Local Time)"
      },
      "QuestRelicHunter": {
        "status": "hidden",
        "expiry": "Aug 26 2020 @ 10:52pm"
      },
      "MiniEventPillowcase": {
        "status": "hidden",
        "expiry": "Aug 26 2020 @ 10:52pm"
      },
      "QuestChromeAura": {
        "status": "inactive",
        "expiry": "Aug 26 2020 @ 10:52pm"
      },
      "QuestHalloween2019": {
        "status": "hidden",
        "expiry": "November 23, 2019 @ 12:31am (Local Time)"
      },
      "QuestLightningAura": {
        "status": "inactive",
        "expiry": "August 26, 2020 @ 10:52pm"
      },
      "QuestAnniversaryAura": {
        "status": "hidden",
        "expiry": "April 2, 2020 @ 2:56pm"
      }
    }
  }
}