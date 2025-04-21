## Optimization of Wheel of Fortune Bonus Round
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

#### Dataset

TBA

### Credits & References

https://www.kaggle.com/code/chrisloop89/english-words-and-letters-frequency

https://saturncloud.io/blog/how-to-iterate-through-specific-columns-and-rows-in-pandas-dataframe-to-perform-a-check/

Dataset Source:
https://buyavowel.boards.net/page/compendium