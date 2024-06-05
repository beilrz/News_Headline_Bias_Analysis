# News Headline Analysis

## Research Question:

For this project, I analyzed the news headlines from popular news media in the US. I am interested in exploring whether political bias or national bias affect the news coverage. The research questions I aim to answer are: 1. What are the trends of news topics? Does the media cover news topics or political figures selectively, based on their political leaning?  2. Does the tone of news headlines affect the political leaning of the news media?

## Data:

To answer the research question, I have collected headlines from news media frontpages of 45 sites, based on the featured media list from allsides.com. Each frontpage is scraped every two hours since 1/1/24. This project is still ongoing, and the initial analysis is based on the headlines from January and February. Each month, I collected around 1 million headlines, with around 150,000 unique ones, all sites combined.

## Method:
To analyze the headlines, I primarily conducted two types of analysis so far: word space analysis and word embedding space analysis. (Word space analysis)[./ Word Space Analysis.ipynb] primarily concerns with the frequency of reported political figures (first-order agenda setting). (Word embedding space analysis)[./ Word Embedding Analysis.ipynb] primarily concerns with the framing and sentiment of reported political figures (second-order agenda setting).

## Preliminary Finding:
There are two noticeable preliminary finding:
1.	News media tend to report the political figure with opposite leaning more (left-leaning media report Trump more; right-leaning media report Biden more).
2.  The political bias against Democratic-affiliated figures is well-aligned with positive-negative dimension, where right-leaning media consistently associated Democratic figures with negative terms and Republican figures with positive terms and left-leaning media consistently associated Republican figures with negative terms and Democratic figures with positive terms. However, the (potential) bias against Republican-affiliated figures is more complex and can be less explained by a simplistic positive vs negative dimension.