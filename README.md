# crypto-historical-patterns

Thought dump:
- these agents do a phenomenal job of processing sequences of textual, audio, and/or visual information, but don't inherently understand temporal relationships between events in a way that mirrors human cognition
- therefore it is a good idea to equip agents with the capability to understand and compare events through time
- "when and where has this happened before?" -> identifying past events that mirror current situations allows us to uncover hidden patterns, anticipate outcomes and make informed trading decisions

Things to achieve:
1. collect bitcoin dataset
2. map bitcoin based on halving cycle
3. collect key events within each halving period and map it to the graph (here!)
4. pattern recognition -> market repeat behaviors, but context matters
5. enhance existing data with social sentiment
6. use AI agents for real-time analysis and predictions
7. validate and iterate models for accuracy

Notes: 
- lag effects - how long after an event doees the market react?
- backtesting model against historical data to see if the patterns hold. 
- potential challenge in noise in social sentiment data, different events having varying impacts


4. pattern recognition
- use halving dates as anchors
- run statistical models such as ARIMA to identify cyclical trends or fourier transforms to detect recurring seasonal patterns
- calculate average drawdowns after events like the Mt. Gox collapse or China bans

5. Enhance existing data with social sentiment
- get data from data sources
- sentiment index - create a composite score
- correlation with market data

6. use AI agents for predictive analysis
- autonomous data synthesis
- scans news, regulatory filings to flag events
- monitors social platforms in real-time and updates sentiment scores