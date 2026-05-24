# Real Estate Agent State Management
STATE = {
    # User preferences: neighborhoods/zip codes they research frequently
    "user_preferences": {
        "favorite_zip_codes": [],
        "preferred_neighborhoods": []
    },
    
    # Session search history: properties appraised in this session for comparison
    "session_history": [],
    
    # Budget constraints: maximum price limit
    "budget_constraint": None,
    
    # Current property context: the last property discussed
    "current_property": None,
    
    # Market data cache: cached market trends to avoid redundant API calls
    "market_data_cache": {}
}