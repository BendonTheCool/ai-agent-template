from core.state import STATE
import json
from datetime import datetime

# ==================== REAL ESTATE TOOLS ====================

def valuation_calculator(location: str, sq_ft: int, bedrooms: int, bathrooms: float):
    """
    Uses a trained ML model to predict the market price of a home.
    
    Args:
        location: Zip code or neighborhood string
        sq_ft: Square footage (integer)
        bedrooms: Number of bedrooms (integer)
        bathrooms: Number of bathrooms (float)
    
    Returns:
        Dictionary with predicted_price (float in USD)
    """
    # Input validation - handle cases where LLM sends lists instead of single values
    if isinstance(bedrooms, list):
        bedrooms = bedrooms[0] if bedrooms else 3
    if isinstance(bathrooms, list):
        bathrooms = bathrooms[0] if bathrooms else 2.0
    if isinstance(sq_ft, list):
        sq_ft = sq_ft[0] if sq_ft else 1500
    if isinstance(location, list):
        location = location[0] if location else "90210"
    
    # Convert to proper types
    bedrooms = int(bedrooms)
    bathrooms = float(bathrooms)
    sq_ft = int(sq_ft)
    location = str(location)
    
    # Store current property in state for context awareness
    property_data = {
        "location": location,
        "sq_ft": sq_ft,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "timestamp": datetime.now().isoformat()
    }
    STATE["current_property"] = property_data
    STATE["session_history"].append(property_data)
    
    # Add zip code to user preferences if not already there
    if location not in STATE["user_preferences"]["favorite_zip_codes"]:
        STATE["user_preferences"]["favorite_zip_codes"].append(location)
    
    # Realistic price calculation based on features
    # Base price varies by location
    location_multiplier = {
        "90210": 1400,  # Beverly Hills, high-end
        "90001": 400,   # South LA, lower
        "94301": 1800,  # Palo Alto, tech hub
        "10001": 1200,  # NYC, moderate
    }
    
    base_price_per_sqft = location_multiplier.get(str(location), 800)
    
    # Calculate base price
    base_price = sq_ft * base_price_per_sqft
    
    # Adjust for bedrooms and bathrooms
    bedroom_adjustment = (bedrooms - 3) * 50000  # $50k per bedroom difference from 3-bed
    bathroom_adjustment = (bathrooms - 2) * 30000  # $30k per bathroom difference from 2-bath
    
    predicted_price = base_price + bedroom_adjustment + bathroom_adjustment
    
    # Add some randomness for realism (~+/- 5%)
    import random
    variance = predicted_price * random.uniform(-0.05, 0.05)
    predicted_price += variance
    
    return {
        "predicted_price": round(predicted_price, 2),
        "location": location,
        "sq_ft": sq_ft,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "price_per_sqft": round(predicted_price / sq_ft, 2)
    }


def market_trend_analyzer(zip_code: str):
    """
    Fetches average price-per-square-foot and historical appreciation rate.
    
    Args:
        zip_code: String zip code
    
    Returns:
        Dictionary with avg_price_per_sqft and year_over_year_growth_pct
    """
    # Input validation - handle lists
    if isinstance(zip_code, list):
        zip_code = zip_code[0] if zip_code else "90210"
    zip_code = str(zip_code)
    
    # Check cache first
    if zip_code in STATE["market_data_cache"]:
        return STATE["market_data_cache"][zip_code]
    
    # Market data simulation based on zip code
    market_data_db = {
        "90210": {"avg_price_per_sqft": 1194, "growth_pct": 4.2, "market_status": "stable growth"},
        "90001": {"avg_price_per_sqft": 425, "growth_pct": 2.1, "market_status": "slow growth"},
        "94301": {"avg_price_per_sqft": 1850, "growth_pct": 6.5, "market_status": "rapid growth"},
        "10001": {"avg_price_per_sqft": 1400, "growth_pct": 3.8, "market_status": "steady growth"},
    }
    
    # Default if zip code not in database
    default_data = {
        "avg_price_per_sqft": 850,
        "growth_pct": 3.0,
        "market_status": "moderate growth"
    }
    
    result = market_data_db.get(str(zip_code), default_data)
    result["zip_code"] = zip_code
    
    # Cache the result
    STATE["market_data_cache"][zip_code] = result
    
    return result


def set_budget_constraint(max_price: float):
    """
    Sets a maximum budget constraint for the user.
    
    Args:
        max_price: Maximum budget in USD
    
    Returns:
        Confirmation message
    """
    # Input validation - handle lists
    if isinstance(max_price, list):
        max_price = max_price[0] if max_price else 2000000
    max_price = float(max_price)
    
    STATE["budget_constraint"] = max_price
    return f"Budget constraint set to ${max_price:,.2f}. I'll alert you if properties exceed this limit."


def check_budget(price: float):
    """
    Checks if a given price exceeds the user's budget.
    
    Args:
        price: Property price to check
    
    Returns:
        Dictionary with budget_check result
    """
    # Input validation - handle lists
    if isinstance(price, list):
        price = price[0] if price else 0
    price = float(price)
    
    if STATE["budget_constraint"] is None:
        return {"within_budget": True, "message": "No budget constraint set"}
    
    within_budget = price <= STATE["budget_constraint"]
    difference = abs(price - STATE["budget_constraint"])
    
    if within_budget:
        return {
            "within_budget": True,
            "message": f"✓ Within budget! ${difference:,.2f} below your limit."
        }
    else:
        return {
            "within_budget": False,
            "message": f"⚠ Exceeds budget by ${difference:,.2f}"
        }


def get_session_history():
    """
    Returns all properties appraised in this session for comparison.
    
    Returns:
        List of property records
    """
    return {
        "session_count": len(STATE["session_history"]),
        "properties": STATE["session_history"]
    }

