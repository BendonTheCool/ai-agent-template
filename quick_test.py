#!/usr/bin/env python3
"""
Quick test of the agent with one simple query
"""

from agent import run_agent

print("\n" + "="*60)
print("TESTING AGENT WITH LLM")
print("="*60 + "\n")

print("Testing simple property valuation query...")
print("User: What is a 3-bed, 2-bath, 1800 sq ft house in 90210 worth?\n")

try:
    result = run_agent("What is a 3-bed, 2-bath, 1800 sq ft house in 90210 worth?")
    print(f"Agent Response:\n{result}")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
