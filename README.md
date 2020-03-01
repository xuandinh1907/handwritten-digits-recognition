# Overview
![](images/MnistExamples.png)

MNIST (Modified National Institute of Standards and Technology) is the de facto *"hello world"* dataset of computer vision.Since its release in 1999,this classic dataset of handwritten images has served as the basis for benchmarking classification algorithms. As new machine learning techniques emerge,MNIST remains a reliable resource for researchers and learners alike

In this project,my goal is to correctly identify digits from a dataset of tens of thousands of handwritten images

# Data
The data files train.csv and test.csv contain gray-scale images of hand-drawn digits,from zero through nine

Donwload dataset [here](https://www.kaggle.com/c/digit-recognizer/data)

# Modeling
Random Forest
- max_depth = 21
- n_estimators = 258

Accuracy on train 96% , on test 89%

# Flask app
- create virtual env and activate env
- install necessary packages by command `pip install -r requirements.txt`
- run app by command `python main.py`