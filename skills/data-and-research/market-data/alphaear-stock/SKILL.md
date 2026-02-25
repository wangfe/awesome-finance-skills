---
name: AlphaEar Stock
description: Search A-Share and HK stock tickers by name or code and retrieve OHLCV historical price data
category: data-and-research/market-data
tags: [a-shares, stock-data, ohlcv, chinese-markets]
---

# AlphaEar Stock Skill

## Overview

Search A-Share/HK stock tickers and retrieve historical price data (OHLCV).

## Capabilities

### 1. Stock Search & Data

Use `scripts/stock_tools.py` via `StockTools`.

-   **Search**: `search_ticker(query)`
    -   Fuzzy search by code or name (e.g., "Moutai", "600519").
    -   Returns: List of `{code, name}`.
-   **Get Price**: `get_stock_price(ticker, start_date, end_date)`
    -   Returns DataFrame with OHLCV data.
    -   Dates format: "YYYY-MM-DD".

## Dependencies

-   `pandas`, `requests`
-   `scripts/database_manager.py` (stock tables)
