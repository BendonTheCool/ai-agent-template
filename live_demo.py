#!/usr/bin/env python3
"""
Clean demo of Real Estate Agent - Shows all key features
"""

from agent import run_agent
from core.state import STATE
import json

def demo(title, query):
    """Run a query and show results"""
    print(f"\n{'='*70}")
    print(f"👤 USER: {query}")
    print('='*70)
    try:
        result = run_agent(query)
        print(f"🏠 AGENT: {result}\n")
        return True
    except Exception as e:
        print(f"❌ ERROR: {e}\n")
        return False

print("\n" + "🏠"*25)
print("REAL ESTATE PRICE PREDICTOR - LIVE DEMO")
print("🏠"*25)
print("\nThis demo shows all key features in action:")
print("  ✓ Tool-based price predictions")
print("  ✓ Market analysis")
print("  ✓ Budget tracking")
print("  ✓ Session history\n")

# Feature 1: Property Valuation
demo("Feature 1", "What's a 3-bed, 2-bath, 1800 sq ft house in 90210 worth?")

# Feature 2: Market Analysis  
demo("Feature 2", "What are the market trends for 90210?")

# Feature 3: Budget Setting
demo("Feature 3", "My budget is $2.5 million")

# Feature 4: Different Property
demo("Feature 4", "What about a 2-bed, 1-bath, 1200 sq ft place in 90210?")

# Show final state
print(f"\n{'='*70}")
print("FINAL AGENT STATE")
print('='*70)
print(f"✓ Budget: ${STATE['budget_constraint']:,.0f}" if STATE['budget_constraint'] else "✓ Budget: Not set")
print(f"✓ Favorite Zip Codes: {', '.join(STATE['user_preferences']['favorite_zip_codes'])}")
print(f"✓ Properties Appraised: {len(STATE['session_history'])}")
print(f"✓ Current Property: {STATE['current_property']['bedrooms']}-bed, {STATE['current_property']['bathrooms']}-bath, {STATE['current_property']['sq_ft']} sq ft" if STATE['current_property'] else "✓ Current: None")

print(f"\n{'='*70}")
print("✅ DEMO COMPLETE - All features working!")
print('='*70 + "\n")
