# CS410X
Updates on CS410X project

## Mar. 19
### Web tutorials
#### [_Introduction to Word Vectors_ by Jayesh Bapu Ahire](https://medium.com/@jayeshbahire/introduction-to-word-vectors-ea1d4e4b84bf)
* NLP models rely on word vectors to predict the contextual probabilities of a word given as input
* Word vectors are of enormous dimensions, and the vectors of closely-related words point toward each other
* Word vectors are trained by marking a word as related to the others within a window in the same sentence
* Each node in the hidden layer of the neural network optimizes the parameter to minimize error; the parameters of the output layer make up a word vector

#### [_A Beginner’s Git and GitHub Tutorial_ by Matthew Setter](https://blog.udacity.com/2015/06/a-beginners-git-github-tutorial.html)
* Covered elementary Git operations such as cloning repo from GitHub, commiting, pulling and branching
* Practiced by cloning the current repo into local directory, making changes and pushing changes onto GitHub

## Mar. 17
### Meeting via Zoom
* Made a forty-minute conference call with Prof. Musco via Zoom
* Discussed next steps to use pre-trained word vectors to identify closely-related words
* Dicussed approaches to write functions to compare word vectors and identify similar task descriptions

## Mar. 8
### Web tutorials
#### [A Gentle Introduction to Scikit-Learn: A Python Machine Learning Library](https://machinelearningmastery.com/a-gentle-introduction-to-scikit-learn-a-python-machine-learning-library/)
* Covered the origin of the scikit-learn library, its primary features, some sample code and links to resources for further learning

#### [An introduction to machine learning with scikit-learn](https://scikit-learn.org/stable/tutorial/basic/tutorial.html)
* Official tutorial written by scikit-learn
* Covered loading a dataset, learning and predicting, updating paramaters and multiclass/multilabel fitting
* Wrote a Python file with elementary scikit-learn functions by following the tutorial--uploaded to repo as sk_learn_tutorial.py

#### [Scikit-learn Official User Guide: Nearest Neighbors](https://scikit-learn.org/stable/modules/neighbors.html)
* Covered the differences between neighbors-based classification and neighbors-based regression
* Covered the pros and cons of both k-neighbors classification and radius-based neighbors classification
* Covered factors that influence the time complexity of nearest neighbor algorithms, including a comparison of how brute force, ball tree and KD tree each perform with regards to each factor
* Explained that Neighborhood Component Analysis (NCA) is ideal for handling multi-class problems without increasing model size or introducing extra parameters
* Covered reducing dimensionality of datasets with NCA


## Mar. 6
### _Natural Language Processing in TensorFlow_ by deeplearning.ai on _Coursera_
* Watched lesson videos of Week 4
* Passed Week 4 quiz
* Covered training model with an LSTM layer to predict next word in a text
* Finished the entire course and earned the certificate: https://coursera.org/share/17d6740d911360cb28bdc25867589eaa

## Mar. 4
### _Natural Language Processing in TensorFlow_ by deeplearning.ai on _Coursera_
* Watched lesson videos of Week 3
* Passed Week 3 quiz
* Covered long short term memory (LSTM) and the issue of overfitting in NLP

## Feb. 26
### YouTube tutorials
#### [Tensorflow 2.0 Tutorial - What is an Embedding Layer? Text Classification P2](https://youtu.be/qpb_39IjZA0)
* Covered the components of an Embedding layer, the average layer and the Dense layers

## Feb. 23
### nlp.py
* Implemented a rough draft of the NLP model
* Created model by Keras's Tokenizer class
* Trained model with a short list of manually-written tasks and labels
* Tasks are divided into urgent and non-urgent ones, labeled 1 and 0 respectively
* Achieved 75% accuracy on training data after 10 epochs
* Testing data to be added to further assess model accuracy

## Feb. 18
### _Natural Language Processing in TensorFlow_ by deeplearning.ai on _Coursera_
* Watched lesson videos of Week 2
* Passed Week 2 quiz
* Covered training tokenizer with IMDB dataset, building model with the embedding method, loss function and subword encoder

## Feb. 17
### _Natural Language Processing in TensorFlow_ by deeplearning.ai on _Coursera_
* Watched lesson videos of Week 1
* Passed Week 1 quiz
* Covered word-based encodings, tokenizer and padding

## Feb. 12
### _Introduction to TensorFlow_ by deeplearning.ai on _Coursera_
* Watched lesson videos of Week 4
* Completed coding assignment of Week 4 in Python
* Passed Week 4 quiz
* Covered TensorFlow's Image Generator module and adding automatic validation
* Finished the entire course and earned the certificate: https://coursera.org/share/a8c73293650d30e144a8ad0c261e6a28

## Feb. 10
### _Introduction to TensorFlow_ by deeplearning.ai on _Coursera_
* Watched lesson videos of Week 3
* Completed coding assignment of Week 3 in Python
* Passed Week 3 quiz
* Covered convolutional layer, pooling and applying image filters

## Prior to Feb. 8
### _Machine Learning_ by Stanford University on _Coursera_
* Watched lesson videos of Week 1-4
* Completed coding assignments of Week 1-4 in MATLAB language
* Topics studied:
  * Linear regression with multiple variables
  * Gradient descent
  * Normal equation
  * Logistic regression
  * Neural networks
  * Forward propagation

&nbsp;  
### _Introduction to TensorFlow_ by deeplearning.ai on _Coursera_
* Watched lesson videos of Week 1-2
* Completed coding assignments of Week 1-2 in Python
* Topics studied:
    * Implementing neural network with TensorFlow
    * Intro to Computer Vision
    * Training a neural network with Fashion MNIST database
    * Training a neural network to recognize handwritten digits
