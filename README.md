# Twitter Scraping and News Distribution Data Pipeline

This repository contains Python code and notebooks for collecting, preprocessing, and analyzing
large-scale Twitter/X data for socio-digital discourse research.

It was developed to support research on algorithmic content distribution, engagement patterns,
sentiment dynamics, and informational representativeness — directly aligned with AI-driven
analysis of online news and social media.

---

## 📂 Repository Contents

### `src/`
Contains data collection, preprocessing, and analysis scripts.

- `collect_data.py`: Twitter/X API scraping with rate-limit handling
- `preprocess.py`: Cleaning and normalization of text data
- `analysis.py`: Exploratory analysis and basic sentiment extraction
- `utils.py`: Helper functions

### `notebooks/`
Interactive Jupyter notebooks showcasing data pipelines and results:

- `EDA.ipynb`: Exploratory Data Analysis
- `Sentiment_Analysis.ipynb`: Sentiment classification
- `Topic_Modeling.ipynb`: Topic detection and discourse patterns

### `data/`
Directory for intermediate data (not uploaded on GitHub for privacy/size). Includes:
- sample JSON / CSV subsets for reproducibility

---

## 🧠 Purpose & Research Context

This project demonstrates:

- Large-scale social media data collection
- NLP preprocessing (tokenization, cleaning, normalization)
- Sentiment classification
- Engagement and distribution pattern analysis
- Data pipelines suitable for machine learning

It reflects my ability to develop research-oriented computational workflows, a key skill
for PhD research in AI, NLP, and news distribution modelling.

---

## 📊 Example Code Snippet

```python
from src.collect_data import collect_tweets

query = "#election2025"
tweets = collect_tweets(query, max_tweets=10000)
print(tweets.head())
