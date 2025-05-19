## Optimization of Wheel of Fortune Bonus Round
*Axyl Fredrick* | *Math 37700* | *Spring 2025*
=========================

### Project Overview

### Problem Area

 In the final bonus round of the game show *Wheel of Fortune*, a contestant has to pick a category and solve a Hangman-esque puzzle. The letters R, S, T, L, N, and E are all chosen already, and the contestant has to pick between three additional consonants and one vowel, and then solve the puzzle. For this project, we will look for the best letter combination in general case scenarios and across different categories. We also intend to build a regression model that provides the best combination to maximize the letters in a given puzzle also based on the preexisting placement of the letters R, S, T, L, N, and E.

 Key takeaways include:
 * Prediction of what letters are most frequent
 * Prediction of what letters are best in certain contexts
 * Maximizing the number of letters that are covered on the board.

### Affected People
* Those who decide to enter *Wheel*. 
* People at home or school playing *Wheel*-like games.
* The production companies behind *Wheel*, as they can tailor the show to make easier or more difficult puzzles based on these metrics.

### Impact
* By finding the optimal combination of letters by category and in a general case scenario, a skilled contestant who applies these findings is closer to winning tens of thousands of dollars per contestant.

### Proposed Solution

* We intend to build a regression model using SciKit Learn to find which letters should be guessed in different puzzles, and find a general case guess based on what works for each word. We will evaluate whether linear or logistic works better.

* We proxied earlier based on frequencies that G, H, D, A are the best combination in terms of frequency, but we want to take into account the individual words that make up each puzzle. 

### Data Dictionary

* For the *Wheel* dataset:

| Variable | Type | Description |
| -------- | ------- | --------- |
| Puzzle  | String    | An individual puzzle from an episode.
| Category | String | The category to which a puzzle belongs. 
| Date    | String/Date Object if possible to convert | The date that an episode aired.


* For the Word Frequency dataset:

| Variable | Type | Description |
| -------- | ------- | --------- |
| Word  | String | A word that is found in an online corpus of English text.
| Count | Integer | The frequency of a word. 

### Organization

## Notebooks  
| Path | Purpose |
|------|---------|
| `notebooks/1_data_prep.ipynb` | Data ingestion, cleaning, and saving processed files |
| `notebooks/2_eda.ipynb` | Visual and statistical exploration of cleaned data |
| `notebooks/3_pre-processing.ipynb` | Preprocessing and testing with basic models |
| `notebooks/4_modeling.ipynb` | Advanced modeling, optimization, and final evaluation |

---

## Installation & Setup (OPTIONAL)
1. **Clone the repo**  
    git clone https://github.com/YourUsername/CapstoneProject.git  
    cd CapstoneProject  

2. **Create environment & install dependencies**  
    python3 -m venv .venv  
    source .venv/bin/activate   # macOS / Linux  
    .venv\Scripts\activate      # Windows  
    pip install -r requirements.txt  

3. **Directory permissions**  
    Ensure `data/` and `outputs/` are writable.

---

## Project Structure  
    CapstoneProject/
    ├── README.md
    ├── .gitignore
    ├── requirements.txt
    │
    ├── data/
    │   ├── raw/                # Immutable source data
    │   └── processed/          # Cleaned, feature‑engineered data
    │
    ├── notebooks/              # Jupyter notebooks
    │   ├── 1_data_prep.ipynb
    │   ├── 2_eda.ipynb
    │   ├── 3_baseline_models.ipynb
    │   └── 4_final_modeling.ipynb
    │
    ├── src/ (OPTIONAL)         #  Reusable Python modules
    │   ├── __init__.py
    │   ├── preprocessing.py
    │   ├── features.py
    │   ├── modeling.py
    │   └── evaluation.py
    │
    ├── slides/                 # Slide deck PDF & source
    │   ├── Capstone_Final_Presentation.pdf
    │
    ├── outputs/                # Model artifacts & figures
    │   ├── models/
    │   └── figures/
    │
    └── tests/                  # (Optional) unit tests for src/

---

## Project Flow  

    Raw Data Ingestion  →  Data Cleaning  
    Data Cleaning       →  Feature Engineering  
    Feature Engineering →  Exploratory Data Analysis  
    EDA                 →  Baseline Modeling  
    Baseline Modeling   →  Advanced Modeling & Optimization  
    Advanced Modeling   →  Model Evaluation & Interpretation
    Evaluation          →  Deployment & Reporting  

1. **Raw Data Ingestion** – load source files and validate schema.  
2. **Data Cleaning** – handle missing values, remove duplicates, standardize formats.  
3. **Feature Engineering** – create new variables, encode categoricals, scale numerics.  
4. **Exploratory Data Analysis** – generate summary statistics and key visualizations (e.g. histograms, boxplots, scatterplots).  
5. **Baseline Modeling** – simple models (e.g., linear regression, logistic regression, decision tree, ARIMA) to set performance benchmarks.  
6. **Advanced Modeling & Optimization** – hyperparameter tuning, ensembles, or complex architectures (e.g. Random Forests, SARIMAX, Simple Neural Networks, LSTM, CNN, XGBoost etc.).  
7. **Model Evaluation & Interpretation** – compare metrics (e.g. MSE, MAE, Accuracy), confusion matrix, plot ROC / precision‑recall.  
8. **Deployment & Reporting**

---

#### Repository 

* `data` 
    - contains link to copy of the dataset (stored in a publicly accessible cloud storage)
    - saved copy of aggregated / processed data as long as those are not too large (> 10 MB)

* `model`
    - `joblib` dump of final model(s)

* `notebooks`
    - contains all final notebooks involved in the project

* `docs`
    - contains final report, presentations which summarize the project

* `references`
    - contains papers / tutorials used in the project

* `src`
    - Contains the project source code (refactored from the notebooks)

* `.gitignore`
    - Part of Git, includes files and folders to be ignored by Git version control

* `conda.yml`
    - Conda environment specification

* `scrape_wheeldata.py`
    - Program to scrape necessary episode data from HTML pages of *Wheel of Fortune* Compendium

* `README.md`
    - Project landing page (this page)

* `LICENSE`
    - Project license

---

## License  
This project is licensed under the **MIT License** – see `LICENSE` for details.

#### Dataset

- **Source:** Wheel of Fortune Compendium
- **Raw File:** Located under `data/raw/` 

| File name | Description |
|-----------|-------------|
| `data/obtained/wheeldata.csv` | full dataset scraped |

### Credits & References

https://www.kaggle.com/code/chrisloop89/english-words-and-letters-frequency

https://saturncloud.io/blog/how-to-iterate-through-specific-columns-and-rows-in-pandas-dataframe-to-perform-a-check/

Dataset Source:
https://buyavowel.boards.net/page/compendium