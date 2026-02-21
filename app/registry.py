PARAMETER_REGISTRY = [
    {
        "name": "coal_consumption",
        "display_name": "Coal Consumption",
        "unit": "MT",
        "category": "input",
        "section": "COGEN BOILER",
        "applicable_assets": ["boiler"]
    },
    {
        "name": "steam_generation",
        "display_name": "Steam Generation",
        "unit": "T/hr",
        "category": "output",
        "section": "COGEN BOILER",
        "applicable_assets": ["boiler"]
    },
    {
        "name": "power_generation",
        "display_name": "Power Generation",
        "unit": "MWh",
        "category": "output",
        "section": "POWER PLANT",
        "applicable_assets": ["turbine"]
    },
    {
        "name": "efficiency",
        "display_name": "Boiler Efficiency",
        "unit": "%",
        "category": "calculated",
        "section": "COGEN BOILER",
        "applicable_assets": ["boiler"]
    }
]

ASSET_REGISTRY = [
    {"name": "AFBC-1", "display_name": "AFBC Boiler 1", "type": "boiler"},
    {"name": "AFBC-2", "display_name": "AFBC Boiler 2", "type": "boiler"},
    {"name": "TG-1", "display_name": "Turbo Generator 1", "type": "turbine"},
    {"name": "TG-2", "display_name": "Turbo Generator 2", "type": "turbine"}
]