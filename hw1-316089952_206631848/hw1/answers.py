r"""
Use this module to write your answers to the questions in the notebook.

Note: Inside the answer strings you can use Markdown format and also LaTeX
math (delimited with $$).
"""

# ==============
# Part 1 answers

part1_q1 = r"""

1. False - The in-sample error is the error in our train set.
          The test set allows us to estimate the error on real world data.

2. False - For example, taking a set of pictures of oranges and sheep and putting
            all the oranges in the train and the sheep in the test.
            It would give horrible results (the trained model will likely give a contact result)
            
3. True - Because if we used the test, we would specialise the hyperparameters chosen towards the training data.

4. True - In each fold, the validation set is used to estimate the out of sample error the current fold is getting
          and by that we fit our hyper parameters. Therefore, our validation score is a proxy to our test score.

"""

part1_q2 = r"""

You should probably lose touch with this friend and he will likely not get very far in life.
This method is exactly what you shouldn't do. This so called friend, is fitting the hyperparameters to the test-set which
means that the test set's result will not be representative the generalised problem.

"""

# ==============
# Part 2 answers

part2_q1 = r"""
As we saw in the wet part, increasing `k` will improve results only up to a certain point. After, it would harm the result.

Let's look at `k=len(train_set)`. A model trained with such a `k` would simply give the most common result with no regard
to how close the data is to its neighbors.

In the case of `k=1`, the result would be the class of the neighbor closest to the data.
This might even give good results in case of clear separation between classes.

"""

part2_q2 = r"""
1. Training using k-fold CV is better because instead of fitting our model to a specific train-set as a whole 
  (which doesn't give us a good estimation of out of sample error), we use different folds to vary our validation sets
  and thus we can adjust the hyperparameters with less over-fitting to our train-set.
2. Like before. This option is horrible because we fit the model to the test-set which renders the test-set useless.
    Kinda like finding a bug in the code, and instead of fixing it, we amend the unittest that found it.

"""

# ==============

# ==============
# Part 3 answers

part3_q1 = r"""
Because the choice of different $\Delta>0$ would yield weights with similar to identical performance.
This is because the regularization would compensate and provide us with weights that work well for the given $\Delta$.
"""

part3_q2 = r"""
1. According to the visualisation, it seems that the model adjusts the weights like a heatmap.
In the sense that where there are "usually" white pixels in a certain image, its weight would reflect this.
Thus, shifted or stretched images in a certain way, might "better" fit to the wrong class.

2. The key difference compared to KNN, is that in KNN we only look at a relatively small set of data 
    (the `k` nearest neighbors) while in SVM all of the data is taken into account (with "far away" sample, less than
    "similar" ones).

"""

part3_q3 = r"""
1. I'd say that the learning rate is good. We can see in the graph that the accuracy rise quickly with a relatively
    steady rise, compared with the test-set accuracy. This can also be seen in the loss graph, where the loss drops
    quickly and steadily improves along with the epochs. 

2. The model is slightly overfitted. The loss graph shows that while the train-set's loss improves, the valid-set's loss
    doesn't improve much. Meaning, that we fit the model for the training set without improving generalisation by much.

"""

# ==============

# ==============
# Part 4 answers

part4_q1 = r"""
We would like our residual graph's mean to be as close to 0 as possible, with a low variance.
By looking at the residual plot, we can see that the trained model improves because the mean stays close to 0 while the
  variance gets lower. Thus our error decreases.
We can see this by comparing the top 5 features' plot with the final plot after the CV, where the variance got lower.
"""

part4_q2 = r"""
1. This model is still considered linear, because linearity is not measured against the features, but against the weight matrix.
 in our model, we are applying a non linear transformation to still use a nice, easy, linear model.
2. Yes, we can apply any non-linear function on our original features, and generate new features from them, on which, we will apply the linear model.
3. By applying non linear transformation on our model, we are able to move our data to another hyperplane, in which, we are able to better separate 
 our data by a linear model.

"""

part4_q3 = r"""
1. np.logspace returns numbers evenly spaced out in the log scale, meaning, for base 2, we get (for 5 numbers) 1, 2, 4, 8,16.
    this would help us in our CV, as usually we would like to do a cross validation on values of lambda that differ greatly, as its effect diverges with both 
    exponentially bigger and smaller lambdas.
2.  in our cross validation, we have 3 different degrees we would like to search over, and 20 different lambdas. in total, the amount of 
    combinations together is `3*20=60`. in addition, each combination, is fitted over 3 times, one for each fold in our 3-fold CV.
    therefore, in total, `fit=3*20*3=180` fits.
```
"""

# ==============
