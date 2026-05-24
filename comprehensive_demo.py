#!/usr/bin/env python3
"""
Comprehensive demo of the Real Estate Agent
Shows key features: tool use, context awareness, budget tracking
"""

from agent import run_agent
from core.state import STATE
import json

def demo_query(num, question):
    """Run a query and display results"""
    print(f"\n{'='*70}")
    print(f"QUERY {num}: {question}")
    print('='*70)
    result = run_agent(question)
    print(f"Agent: {result}")
    return result

def show_state():
    """Display current agent state"""
    print(f"\n{'-'*70}")
    print("AGENT STATE:")
    print(f"  Budget: ${STATE['budget_constraint']:,.0f}" if STATE['budget_constraint'] else "  Budget: Not set")
    print(f"  Favorite Zip Codes: {STATE['user_preferences']['favorite_zip_codes']}")
    print(f"  Properties Appraised: {len(STATE['session_history'])}")
    if STATE['current_property']:
        prop = STATE['current_property']
        print(f"  Current Property: {prop['bedrooms']}-bed, {prop['bathrooms']}-bath, {prop['sq_ft']} sq ft in {prop['location']}")
    print(f"{'-'*70}")

print("\n" + "🏠"*20)
print("REAL ESTATE PRICE PREDICTOR - COMPREHENSIVE DEMO")
print("🏠"*20)

# Demo 1: Initial valuation
demo_query(1, "Hi, I'm looking at a house in 90210. It's a 3-bed, 2-bath with 1,800 square feet. What's it worth?")
show_state()

# Demo 2: Market analysis
demo_query(2, "Is 90210 still a good investment? What are the market trends?")
show_state()

# Demo 3: Budget setting
demo_query(3, "My budget is $2 million. What should I know?")
show_state()

# Demo 4: Alternative property (within budget)
demo_query(4, "What about a 3-bed, 2-bath, 2,200 sq ft place in the same area?")
show_state()

# Demo 5: Budget compliance
demo_query(5, "Is that property within my budget?")
show_state()

# Demo 6: Session comparison
demo_query(6, "How do the properties we've looked at compare?")
show_state()

print("\n" + "✅"*20)
print("DEMO COMPLETED SUCCESSFULLY!")
print("✅"*20)
print("\n📊 Final Agent State:")
print(json.dumps(STATE, indent=2, default=str))
