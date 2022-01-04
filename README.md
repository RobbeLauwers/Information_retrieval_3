# Information retrieval 3: Plagiarism Detection

Make sure that the [requirements](requirements.txt) are installed.

The datasets provided in the assignment are placed in [./data](data).

To remove punctuation marks from the datasets, we made [alphanumerical.py](alphanumerical.py). This
generates [news_articles_small_alphanumerical.csv](data/news_articles_small_alphanumerical.csv)
and [news_articles_larg_alphanumerical.csv](data/news_articles_large_alphanumerical.csv). This has already been done,
you do not need to run the script again.

To calculate the Jaccard index for each article pair in the small dataset, we made [jaccard.py](jaccard.py). This
generates the
files [news_articles_small_alphanumerical_jaccard.csv](data/news_articles_small_alphanumerical_jaccard.csv). This has
already been done, you do not need to run the script again.

LSH can be used on the data using [main.py](main.py). There are several hardcoded parameters at the top of the file that
can be changed. If not changed, this will
generate [news_articles_small_alphanumerical_estimated_jaccard.csv](data/news_articles_small_alphanumerical_estimated_jaccard.csv)
. This file has already been generated. It contains all article pairs that LSH thinks are duplicates, and their Jaccard
distance.

To compare the file generated above to the full list of Jaccard indexes,
use [compare_jaccard_files.py](compare_jaccard_files.py). This will print to the terminal which article pairs are false
negatives or positives.

