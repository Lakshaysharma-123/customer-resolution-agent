CUSTOMERS = {
    "SK4821X": {
        "name": "Priya Nair",
        "tier": "Gold",
        "flight": "SK-204",
        "route": "Delhi → Goa",
        "status": "Cancelled"
    },
    "TR1190B": {
        "name": "Arvind Kulkarni",
        "tier": "Silver",
        "flight": "SK-118",
        "route": "Mumbai → Bengaluru",
        "status": "Delayed4"
    },
    "WL7742": {
        "name": "Meher Kaur",
        "tier": "Platinum",
        "flight": "SK-305",
        "route": "Delhi → Hyderabad",
        "status": "Delayed6"
    }
}

POLICIES = {
    "Cancelled": {
        "refund": True,
        "rebooking": True
    },
    "Delayed4": {
        "meal": True,
        "lounge": True,
        "hotel": False
    },
    "Delayed6": {
        "meal": True,
        "lounge": True,
        "hotel": True
    }
}
