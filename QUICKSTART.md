# Quick Start Guide - Real Estate Agent

## 🏠 Smart Real Estate Price Predictor

### Prerequisites
- Python 3.8+
- Ollama installed ([download here](https://ollama.ai/))
- 8GB+ RAM

### Setup (5 minutes)

```bash
# 1. Start Ollama (in background terminal)
ollama serve

# 2. In a new terminal, pull the model
ollama pull llama3.1:8b

# 3. Install dependencies
pip install -r requirements.txt
```

### Run the Agent

#### Option A: Interactive Mode (Recommended for Testing)
```bash
python test_real_estate.py
```
Then select option 2 for interactive mode or option 1 for test suite.

#### Option B: API Server
```bash
python main.py
```
Then in another terminal:
```bash
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"query": "What is a 3 bed, 2 bath, 1800 sq ft house worth in 90210?"}'
```

### Example Queries to Try

**Valuation:**
```
"What's a 3-bed, 2-bath, 1800 sq ft house worth in 90210?"
```

**Market Analysis:**
```
"What are the market trends for 90210?"
```

**Budget Setting:**
```
"Set my budget to $1,800,000"
```

**Context Awareness:**
```
"What if it had an extra bathroom?" 
(Agent remembers previous property)
```

**Session Comparison:**
```
"How do the properties we've looked at compare?"
```

## What the Agent Does

✅ **Never guesses prices** - Always uses ML-backed valuation tool  
✅ **Remembers context** - Tracks properties and preferences  
✅ **Tracks budget** - Alerts if properties exceed your limit  
✅ **Analyzes markets** - Provides growth rates and trends  
✅ **Compares properties** - Maintains full session history  
✅ **Stays on topic** - Redirects non-real estate questions  

## Documentation

- **Full Implementation**: `REAL_ESTATE_IMPLEMENTATION.md`
- **Project Requirements**: `PROJECT_REQUIREMENTS_MET.md`
- **Test Suite**: `test_real_estate.py`

## Troubleshooting

### Issue: "Cannot connect to Ollama"
```bash
# Make sure Ollama server is running
ollama serve
```

### Issue: "Model not found"
```bash
# Pull the model
ollama pull llama3.1:8b
```

### Issue: "Out of memory"
Use a smaller model:
```bash
# In config.py, change to:
MODEL_NAME = "llama2:7b"
# Then: ollama pull llama2:7b
```

## API Endpoint Reference

### POST /chat
```bash
Request:
{
  "query": "What is a 2-bed, 1-bath, 1200 sq ft property in 90210 worth?"
}

Response:
{
  "response": "Based on market analysis, this property would be valued at approximately $1,600,000..."
}
```

---

**Ready to go!** 🚀 Start with `python test_real_estate.py`
