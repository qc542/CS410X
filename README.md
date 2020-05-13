# CS410X
Updates on CS410X project

## May 13
### Web tutorials
#### [_pdb - Interactive Debugger_ by pymotw.com](https://pymotw.com/2/pdb/)
* The command "condition \<breakpoint\_number\> \<condition\>" makes pdb break at the specified point only when the specified condition is met
* The command "interact" makes pdb start an interactive interpreter; enter Ctrl-D in the interpreter to exit to pdb's regular interface
* The command "break \<module\_name\>:\<line\_number\>" sets a breakpoint in the specified module

## May 12
### Web tutorials
#### [_git-reset Documentation_ by git-scm.com](https://git-scm.com/docs/git-reset)
* The command "git reset --hard" reverses any changes made to tracked files since the last commit
* "git log" makes Git list a few of the most recent commits made to the repo
* "git log -p" makes Git display the differences before and after each commit in addition to recent commits

## Apr. 29
### Web tutorials
#### [_Pull Request Tutorial - A Visual Guide to Pull Requests_ by Yang Su](https://yangsu.github.io/pull-request-tutorial/)
* Pull request is a feature of GitHub that allows a user to notify others of changes pushed to a repo
* Stakeholders can review a pull request, suggest changes and eventually merge it into the main branch
* If there are no conflicts between the two branches, the pull request can be merged automatically by Git
* In case where a large number of conflicts emerge because of a long standing main branch, it would be helpful to squash all commits into one, rebase, and cherry-pick the changes to merge

## Apr. 24
### Web tutorials
#### [_Git - Branches in a Nutshell_ by git-scm.com](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)
* Explains the fundamentals of branching operations on Git
* Branches on Git are pointers to individual commits
* The command "git branch <branch\_name>" creates a new branch
* "git checkout <branch\_name>" makes Git switch to the specified branch

#### [_Git - Basic Branching and Merging_ by git-scm.com](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
* To merge two branches, check out the target branch and enter "git merge <previous\_branch>"
* If the later commit is directly ahead, Git simply moves the pointer forward
* If commit history diverged, Git does a three-way merge
* Merge conflicts arise when the same part of a file is modified on both branches
* Conflicts have to be resolved manually

## Apr. 19
### Web tutorials
#### [_How To Use the Python Debugger_ by Lisa Tagliaferri on _DigitalOcean_](https://www.digitalocean.com/community/tutorials/how-to-use-the-python-debugger)
* Covers the common commands of debugging Python programs with the pdb module
* "step" executes the current line and stops immediately afterward, like in GUI debuggers
* "next" makes the program continue until the next line of the function returns
* "pp" prints the value of the given expression
* "continue" makes the program run until the next breakpoint
* "break <filename>:<line#>" sets a breakpoint at the given line

## Apr. 17
### Meeting via Zoom
* Made a forty-minute conference call with Prof. Musco via Zoom
* Reviewed latest progress and discussed next steps
* Planning to develop algorithm that compares task descriptions to each other
* Discussed potential approaches to derive task similarity by comparing the dot products of vectors

## Apr. 4
### word\_vector.py
* Implemented load\_vector function, which calls Python's IO function to load a local vector file in a text stream and assemble all word entries and vector components into a Python dictionary object
* Implemented lookup\_vector function, which looks up a given string in the previously-generated dictionary and returns the corresponding Vector object
* Implemented construct\_word function, which calls lookup\_vector to obtain the Vector object of the given string and then calls the constructor of the Word class to create an instance
* Implemented construct\_word\_list function, which takes a list of strings and verifies whether each string is a single word. Once the string is verified, the function passes it to construct\_word and appends the Word object returned to a list
* Implemented show\_similarity\_ranking function, which passes a list of Word objects and a base Vector object to sorted\_by\_similarity to obtain a sorted list of tuples. The function then prints the outcome in an easy-to-read format
* Fixed several runtime issues found when running word\_vector\_test.py for testing

### word\_vector\_test.py
* Implemented a few test cases for word\_vector.py
* Calls the show\_similarity\_ranking function in word\_vector.py to print the given list of words, ranked from most to least similar to the base word

## Mar. 29
### word\_vector.py
* Implemented sorted\_by\_similarity function, which returns the given target list of words ranked from most to least similar to the given base word
* Contains Python 3's built-in sorted() function, which takes a lambda function as the key for sorting
* Return variable is a list of tuples in the form of the output word's cosine similarity value to the based word, followed by the output word itself

### Web tutorials
#### [_Python — List Sorting, Keys & Lambdas_ by John Grant](https://medium.com/@johngrant/python-list-sorting-keys-lambdas-1903b2a4c949)
* Introduces the two sorting functions built into Python 3
* sort() modifies the original list in-place, whereas sorted() takes an iterable and returns a newly-created list upon sorting
* The paramter "key" is declared as a function that takes a single argument and returns a key for sorting
* The key can be declared as lambda, an anonymous function, followed by a parameter. The return variable is entered following a colon
* Enabling the "reverse" option makes the list sorted in descending order. The option is disabled by default.

## Mar. 28
### word\_vector.py 
* Wrote a Python script to evaluate cosine similarity between two vectors
* Defined a Word class to import word vectors
* Defined three functions: vector\_len(v), dot\_product(v1, v2) and cosine\_similarity(v1, v2)
* vector\_len(v) calculates the Euclidean norm of a word vector
  * The Euclidean norm equals the square root of the sum of each component of the vector squared
* dot\_product(v1, v2) returns the sum of each component in v1 multiplied by the corresponding component in v2 at the same index
* cosine\_similarity(v1, v2) returns the cosine of the angle between v1 and v2
  * The cosine of the angle equals the dot product of v1 and v2 divided by the product of their lengths (as in Euclidean norm) 


### Web tutorials
#### [_A Beginner's Guide to Word2Vec and Neural Word Embeddings_ by Chris Nicholson](https://pathmind.com/wiki/word2vec)
* The Word2Vec nerual net outputs a collection of words with a vector attached to each
* Similarity between the vectors is measured by cosine distance: cos(0) = 1 represents total similarity, whereas cos(1) = 0 represents no similarity 
* To train words against others located closely in the text, skip-gram works more accurately on large datasets than Continuous Bag of Words does
* One shortcoming of Word2Vec is its inability to address the different definitions of the same word; newer models such as ELMo and BERT do better in this aspect

#### [_Playing with word vectors_ by Martin Konicek](https://medium.com/swlh/playing-with-word-vectors-308ab2faa519)
* Introduces the methodology of measuring word similarity by calculating cosine similarity 

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
