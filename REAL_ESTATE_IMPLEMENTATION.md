# Smart Real Estate Price Predictor - Implementation Guide

**Project Title:** Smart Real Estate Price Predictor  
**Student Name:** Brandon Pian  
**Due Date:** May 30, 2026

## Project Overview

This AI agent acts as a virtual real estate analyst that helps homebuyers, sellers, and agents quickly calculate property valuations and analyze market data without manual spreadsheet work or complex regression math.

## Architecture

### Core Components

#### 1. **State Management** (`core/state.py`)
Maintains agent memory across conversations:
- **User Preferences**: Tracked neighborhoods and zip codes
- **Session History**: Properties appraised in current session for comparison
- **Budget Constraints**: Maximum price limits set by user
- **Current Property Context**: Last property discussed for follow-up questions
- **Market Data Cache**: Cached market trends to avoid redundant calls

#### 2. **Tools System** (`tools/tools.py`)

##### Tool 1: `valuation_calculator`
Predicts home market prices using ML-backed simulation.

**Inputs:**
- `location` (str): Zip code or neighborhood
- `sq_ft` (int): Square footage
- `bedrooms` (int): Number of bedrooms
- `bathrooms` (float): Number of bathrooms

**Outputs:**
```json
{
  "predicted_price": 2150000.00,
  "location": "90210",
  "sq_ft": 1800,
  "bedrooms": 3,
  "bathrooms": 2,
  "price_per_sqft": 1194.44
}
```

**Behavior:**
- Stores property in state for context awareness
- Tracks user's interested zip codes automatically
- Adds property to session history for comparisons
- Realistic price calculation based on location multipliers, bedroom/bathroom adjustments, and variance

##### Tool 2: `market_trend_analyzer`
Analyzes market trends for specific zip codes.

**Inputs:**
- `zip_code` (str): Target zip code

**Outputs:**
```json
{
  "zip_code": "90210",
  "avg_price_per_sqft": 1194,
  "growth_pct": 4.2,
  "market_status": "stable growth"
}
```

**Behavior:**
- Caches results to avoid redundant analysis
- Provides year-over-year growth percentage
- Market status classification (stable, rapid, slow growth)

##### Tool 3: `set_budget_constraint`
Sets a maximum budget for the user.

**Inputs:**
- `max_price` (float): Maximum budget in USD

**Returns:** Confirmation message

##### Tool 4: `check_budget`
Verifies if a property price is within user's budget.

**Inputs:**
- `price` (float): Property price to check

**Returns:** Budget compliance status with variance information

##### Tool 5: `get_session_history`
Retrieves all properties appraised in the current session.

**Inputs:** None

**Returns:** List of all properties with their details

#### 3. **System Prompt** (`prompts/system_prompt.py`)

The system prompt includes:
- **Personality**: Professional, analytical, encouraging
- **Context Awareness**: Last property discussed, user budget
- **System Rules**:
  - **Rule 1 (Mandatory Tool Use)**: Never guess prices—always use valuation_calculator
  - **Rule 2 (Scope Guardrail)**: Stay on real estate topics
  - **Rule 3 (Context Awareness)**: Remember property details for follow-up questions

## Usage Examples

### Example Conversation 1: Initial Property Valuation

```
User: "Hi, I'm looking at a house in 90210. It's a 3-bed, 2-bath place with about 1,800 square feet. What do you think it's worth?"

Agent: [Calls valuation_calculator with location="90210", sq_ft=1800, bedrooms=3, bathrooms=2]

Agent: "Based on current market analysis, this 3-bedroom, 2-bathroom home in the 90210 area is estimated at approximately **$2,150,000**. This breaks down to about **$1,194 per square foot**, which is in line with the current market rates for this affluent neighborhood."
```

### Example Conversation 2: Market Analysis Follow-up

```
User: "Is that neighborhood still growing, or is it cooling down?"

Agent: [Calls market_trend_analyzer with zip_code="90210"]

Agent: "The 90210 market is showing **steady, stable growth** at **4.2% year-over-year**. With an average price-per-square-foot of **$1,194**, this is a high-cost area but not in a rapid spike phase. It's a mature, stable market—good for long-term investment."
```

### Example Conversation 3: Budget Setting & Comparison

```
User: "That's a bit high. I have a budget of $1.8M. Can you help me find something within that?"

Agent: [Calls set_budget_constraint with max_price=1800000]

Agent: "Budget constraint set to **$1,800,000**. I'll alert you if properties exceed this limit. Let me know about any properties you'd like me to evaluate!"

User: "What about a 2-bed, 2-bath, 1,500 sq ft place in the same area?"

Agent: [Calls valuation_calculator with location="90210", sq_ft=1500, bedrooms=2, bathrooms=2]
[Calls check_budget with price=1792500]

Agent: "This property would be valued at approximately **$1,792,500**. ✓ **Great news!** This is just **$7,500 below your budget limit**, so it falls within your range. You'd be saving about $357,500 compared to the 3-bed option!"
```

### Example Conversation 4: Session Comparison

```
User: "How do these two properties compare that we've looked at?"

Agent: [Calls get_session_history]

Agent: "You've appraised 2 properties in this session:

1. **3-bed, 2-bath, 1,800 sq ft** → $2,150,000 ($1,194/sq ft)
2. **2-bed, 2-bath, 1,500 sq ft** → $1,792,500 ($1,195/sq ft)

The price-per-square-foot is nearly identical, but the 3-bed is larger and commands more total value. The 2-bed keeps you within budget with good savings!"
```

## Key Features

### ✅ Context Awareness (Rule 3)
- Automatically remembers the last property discussed
- Allows follow-up questions like "What if it had an extra bathroom?" without re-entering details
- Tracks all properties in current session for easy comparison

### ✅ Mandatory Tool Use (Rule 1)
- Agent refuses to estimate prices without using valuation_calculator
- Ensures all predictions are based on consistent ML model logic
- Provides detailed breakdown (price, price-per-sqft, property details)

### ✅ Scope Guardrail (Rule 2)
- Agent politely redirects non-real-estate topics
- Stays focused on property valuations, market analysis, and budget tracking

### ✅ Memory System
- **User Preferences**: Tracks favorite zip codes automatically
- **Session History**: All properties appraised in this session
- **Budget Constraints**: Maximum price limit with automatic compliance checks
- **Market Data Cache**: Avoids redundant API calls

### ✅ Professional Tone
- Encourages informed decision-making
- Data-driven analysis with citations
- Clear, accessible explanations of complex market concepts

## Optional Features Implemented

### Budget Tracking & Alerts
- Users can set a maximum budget
- Agent automatically checks properties against budget
- Proactive notifications when properties exceed limits
- Shows variance (over/under budget) in dollars

### Market Status Classification
- "Stable growth": Moderate, predictable appreciation
- "Rapid growth": High appreciation potential
- "Slow growth": Conservative, stable market
- Helps users assess investment potential

### Session Comparison
- Agent maintains full history of appraised properties
- Enables side-by-side comparisons
- Helps users track their search process

## Technical Stack

- **Language Model**: Llama 3.1 (via Ollama)
- **Framework**: Python with FastAPI
- **State Management**: In-memory dictionary (easily upgradeable to database)
- **Tool System**: JSON-based tool interface with structured I/O

## Running the Agent

### Setup
1. Ensure Ollama is installed and running: `ollama serve`
2. Pull the model: `ollama pull llama3.1:8b`
3. Install dependencies: `pip install -r requirements.txt`

### Interactive Testing
```bash
python main.py  # Starts FastAPI server
# Then POST to /chat with {"query": "your question"}
```

### Example API Request
```bash
curl -X POST "http://localhost:8000/chat" -H "Content-Type: application/json" -d '{"query": "I am looking at a 3 bed, 2 bath, 1800 sq ft house in 90210. What is it worth?"}'
```

## State Example

```json
{
  "user_preferences": {
    "favorite_zip_codes": ["90210", "94301"],
    "preferred_neighborhoods": []
  },
  "session_history": [
    {
      "location": "90210",
      "sq_ft": 1800,
      "bedrooms": 3,
      "bathrooms": 2,
      "timestamp": "2026-05-24T10:30:00"
    }
  ],
  "budget_constraint": 1800000,
  "current_property": {
    "location": "90210",
    "sq_ft": 1500,
    "bedrooms": 2,
    "bathrooms": 2,
    "timestamp": "2026-05-24T10:35:00"
  },
  "market_data_cache": {
    "90210": {
      "zip_code": "90210",
      "avg_price_per_sqft": 1194,
      "growth_pct": 4.2,
      "market_status": "stable growth"
    }
  }
}
```

## How This Meets Project Requirements

✅ **Purpose**: Helps with property valuations and market analysis (productivity tool)  
✅ **Tool List**: Valuation_Calculator and Market_Trend_Analyzer implemented  
✅ **Memory System**: Tracks preferences, history, and budget constraints  
✅ **System Rules**: All three rules enforced in system prompt  
✅ **Example Conversations**: Fully supported by tool implementations  
✅ **Optional Features**: Budget tracking and session comparison included  
✅ **Professional Tone**: Realistic, encouraging, data-driven communication  

## Future Enhancements

- Persist state to database for multi-session memory
- Add real MLS API integration for actual property data
- Implement neural network with real training data
- Add neighborhood demographics and school ratings
- Support for investment ROI calculations
- Property comparison scoring system
- Historical price trend visualization
