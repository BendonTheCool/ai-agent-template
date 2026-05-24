from tools.tools import *

TOOLS = {
    "valuation_calculator": valuation_calculator,
    "market_trend_analyzer": market_trend_analyzer,
    "set_budget_constraint": set_budget_constraint,
    "check_budget": check_budget,
    "get_session_history": get_session_history,
}

TOOL_DESCRIPTIONS = {
    "valuation_calculator": "Predicts home market price. Args: location (str: zip/neighborhood), sq_ft (int), bedrooms (int), bathrooms (float)",
    "market_trend_analyzer": "Gets market trends for a zip code. Args: zip_code (str)",
    "set_budget_constraint": "Sets maximum budget limit. Args: max_price (float)",
    "check_budget": "Checks if a property price is within budget. Args: price (float)",
    "get_session_history": "Returns all properties appraised in this session. Args: none",
}
