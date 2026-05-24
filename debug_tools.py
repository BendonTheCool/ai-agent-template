#!/usr/bin/env python3
"""
Debug script to test Real Estate Agent tools directly
Bypasses the LLM to verify tool functionality
"""

from tools.tools import (
    valuation_calculator, 
    market_trend_analyzer,
    set_budget_constraint,
    check_budget,
    get_session_history
)
from core.state import STATE
import json

print("\n" + "="*60)
print("REAL ESTATE AGENT - TOOL TESTING")
print("="*60)

# Test 1: Valuation Calculator
print("\n[TEST 1] Valuation Calculator")
print("-" * 60)
result1 = valuation_calculator(location="90210", sq_ft=1800, bedrooms=3, bathrooms=2)
print(f"Input: 3-bed, 2-bath, 1800 sq ft in 90210")
print(f"Result: {json.dumps(result1, indent=2)}")

# Test 2: Market Trend Analyzer
print("\n[TEST 2] Market Trend Analyzer")
print("-" * 60)
result2 = market_trend_analyzer(zip_code="90210")
print(f"Input: zip_code=90210")
print(f"Result: {json.dumps(result2, indent=2)}")

# Test 3: Set Budget Constraint
print("\n[TEST 3] Set Budget Constraint")
print("-" * 60)
result3 = set_budget_constraint(max_price=1800000)
print(f"Input: max_price=1800000")
print(f"Result: {result3}")

# Test 4: Check Budget
print("\n[TEST 4] Check Budget")
print("-" * 60)
result4 = check_budget(price=1792500)
print(f"Input: price=1792500")
print(f"Result: {json.dumps(result4, indent=2)}")

# Test 5: Alternative property
print("\n[TEST 5] Valuation Calculator (Alternative)")
print("-" * 60)
result5 = valuation_calculator(location="90210", sq_ft=1500, bedrooms=2, bathrooms=2)
print(f"Input: 2-bed, 2-bath, 1500 sq ft in 90210")
print(f"Result: {json.dumps(result5, indent=2)}")

# Test 6: Budget check for second property
print("\n[TEST 6] Check Budget (Second Property)")
print("-" * 60)
result6 = check_budget(price=result5['predicted_price'])
print(f"Input: price={result5['predicted_price']}")
print(f"Result: {json.dumps(result6, indent=2)}")

# Test 7: Get Session History
print("\n[TEST 7] Get Session History")
print("-" * 60)
result7 = get_session_history()
print(f"Result: {json.dumps(result7, indent=2, default=str)}")

# Display final state
print("\n[FINAL STATE]")
print("-" * 60)
print(json.dumps(STATE, indent=2, default=str))

print("\n✅ All tool tests completed successfully!")
