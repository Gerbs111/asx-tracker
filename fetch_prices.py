name: Fetch ASX Prices

on:
schedule:
- cron: ‘0 * * * *’
workflow_dispatch:

permissions:
contents: write

jobs:
fetch:
runs-on: ubuntu-latest
steps:
- uses: actions/checkout@v4

```
  - uses: actions/setup-python@v5
    with:
      python-version: '3.11'

  - name: Install dependencies
    run: pip install yfinance pandas

  - name: Fetch prices
    run: python fetch_prices.py

  - name: Commit prices.json
    run: |
      git config user.email "action@github.com"
      git config user.name "GitHub Action"
      git add prices.json
      git diff --staged --quiet || git commit -m "Update prices"
      git push
```
