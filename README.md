# CS 224N: Natural Language Processing with Deep Learning
This repo summarizes Assignments of [CS 224N (Stanford class on NLP - 2021)](http://web.stanford.edu/class/cs224n/). A brief summary of key concepts covered in 
different assignments is summarized below.

## Assignment 1: [Exploring Word Vectors](assignment_1/exploring_word_vectors.ipynb)
This assignment focuses in two fundamental concepts in NLP:
1. Generating count-based word vectors: Many word vector implementations are driven by the idea that similar words, i.e., (near) synonyms, will be used in similar contexts. As a result, similar words will often be spoken or written along with a shared subset of words, i.e., contexts. By examining these contexts, we can try to develop embeddings for our words. With this intuition in mind, many "old school" approaches to constructing word vectors relied on word counts. Goal of this assignment to generate word embeddings based on co-occurance
counts of words in a given corpus and reducing its dimension by performing Singular Value Decomposition (SVD).

2. Prediction-Based Word Vectors: Prediction-based word vectors have demonstrated better performance, such as word2vec and GloVe (which also utilizes the benefit of counts). This assignment explore the embeddings produced by GloVe. 200 dimensional GloVe
word vectors are imported by using Gensim library and they are reduced to 2 dimensional vectors by performing SVD for ease of visualization. Different similarity tasks are performed in order to develop an understanding of the word embedding. 

## Assignment 2: [word2vec](assignment_2/a2.pdf)
This assignment focuses on understanding and implementing the word2vec-skip gram algorithm.
<p align="center">
<img src="figures/a2/word2vec_skip_gram.png" alt="Word2Vec skip gram algorithm" width="450"/> 
</p>

![](figures/a2/word2vec_skip_gram.png)
