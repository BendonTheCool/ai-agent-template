#!/usr/bin/env python3
"""
Test script for the Smart Real Estate Price Predictor Agent
Demonstrates the agent handling various real estate queries
"""

from agent import run_agent
from core.state import STATE
import json

def print_state():
    """Pretty print the agent state"""
    print("\n" + "="*60)
    print("AGENT STATE SNAPSHOT")
    print("="*60)
    print(json.dumps(STATE, indent=2, default=str))
    print("="*60 + "\n")

def test_conversation():
    """Run through example conversations"""
    
    print("\n" + "="*80)
    print("SMART REAL ESTATE PRICE PREDICTOR - TEST SUITE")
    print("="*80)
    
    # Test 1: Initial valuation
    print("\n[TEST 1] Initial Property Valuation")
    print("-" * 60)
    query1 = "Hi, I'm looking at a house in 90210. It's a 3-bed, 2-bath place with about 1,800 square feet. What do you think it's worth?"
    print(f"User: {query1}")
    result1 = run_agent(query1)
    print(f"Agent: {result1}")
    print_state()
    
    # Test 2: Market analysis follow-up
    print("\n[TEST 2] Market Trend Analysis")
    print("-" * 60)
    query2 = "Is that neighborhood still growing, or is it cooling down?"
    print(f"User: {query2}")
    result2 = run_agent(query2)
    print(f"Agent: {result2}")
    print_state()
    
    # Test 3: Budget constraint
    print("\n[TEST 3] Budget Setting")
    print("-" * 60)
    query3 = "That's a bit high. My budget is $1.8 million. Can you help me find something within that?"
    print(f"User: {query3}")
    result3 = run_agent(query3)
    print(f"Agent: {result3}")
    print_state()
    
    # Test 4: Alternative property within budget
    print("\n[TEST 4] Alternative Property with Budget Check")
    print("-" * 60)
    query4 = "What about a 2-bed, 2-bath place with 1,500 square feet in the same area?"
    print(f"User: {query4}")
    result4 = run_agent(query4)
    print(f"Agent: {result4}")
    print_state()
    
    # Test 5: Session comparison
    print("\n[TEST 5] Session Comparison")
    print("-" * 60)
    query5 = "How do the properties we've looked at compare?"
    print(f"User: {query5}")
    result5 = run_agent(query5)
    print(f"Agent: {result5}")
    print_state()
    
    # Test 6: Scope guardrail
    print("\n[TEST 6] Off-Topic Query (Scope Guardrail)")
    print("-" * 60)
    query6 = "What's a good recipe for lasagna?"
    print(f"User: {query6}")
    result6 = run_agent(query6)
    print(f"Agent: {result6}")
    print_state()

if __name__ == "__main__":
    print("\n" + "🏠 "*20)
    print("Real Estate Price Predictor Agent - Interactive Test")
    print("🏠 "*20)
    
    # Option 1: Run test suite
    print("\nOptions:")
    print("1. Run full test suite")
    print("2. Interactive mode (single query)")
    print("3. Exit")
    
    choice = input("\nSelect option (1-3): ").strip()
    
    if choice == "1":
        test_conversation()
        print("\n✅ Test suite completed!")
        
    elif choice == "2":
        print("\nEnter your real estate question (or 'exit' to quit):")
        print("Examples:")
        print("  - 'What's a 3-bed, 2-bath, 1800 sq ft house worth in 90210?'")
        print("  - 'Show me market trends for zip code 90210'")
        print("  - 'Set my budget to $2,000,000'")
        
        while True:
            query = input("\n> ").strip()
            if query.lower() == 'exit':
                break
            
            result = run_agent(query)
            print(f"\nAgent Response:\n{result}")
            
            show_state = input("\nShow state? (y/n): ").strip().lower()
            if show_state == 'y':
                print_state()
    
    elif choice == "3":
        print("Goodbye!")
    
    else:
        print("Invalid choice")
