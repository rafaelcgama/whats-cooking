# What's Cooking?

In this project, I analyzed data from the [What's Cooking](https://www.kaggle.com/c/whats-cooking) dataset. The goal of this project is to train a model to predict the type of cuisine of a particular recipe given its ingredients list. 

The dataset is composed of 39,774 recipes from 20 cuisines and using 6714 different ingredients. The recipes are unevenly distributed across the cuisines as it is shown below:

![](/images/recipes_per_cuisine.png)

Having so many ingredients creates a problem when building a classification model because it generates too many features for this amount of data. Therefore, the first step before trying to train a model, should be to reduce its dimensionality. To achieve that, I first went about identifying all the common ingredients among all the cuisines and removing them as they wouldn't be relevant predictors. In total, 107 common ingredients were found. Here are the 10 most common ones:

![](/images/common_ingredients.png)

Unfortunately, removing 107 out of 6714 ingredients barely scratches the surface of the dimensionality problem so I decided to do a completely different approach and applied the PCA technique to reduce all ingredients into latent space of only 1000 dimensions.

After the dimensionality issue was addressed, the dataset was properly prepped, trained and tested and yielded the following accuracy results:


<table border="1" 
       class="dataframe">  
    <thead>    
        <tr style="text-align: right;">      
            <th></th>      
            <th>Logistic Regression</th>     
            <th>SVM Classifier</th>      
            <th>Random Forest Classifier</th>      
            <th>KNN</th>      
            <th>Decision Tree Classifier</th>    
        </tr>  
    </thead>  
    <tbody>    
        <tr>      
            <th>Accuracy</th>     
            <td>0.740038</td>      
            <td>0.674796</td>     
            <td>0.583030</td>     
            <td>0.556128</td>      
            <td>0.376116</td>   
        </tr>  
    </tbody>
</table>


You can follow the exploratory data analysis in the `DataPresentation.ipynb` and `DataWrangling.ipynb` notebooks and the PCA modeling in the `PCAModeling.ipynb` notebook above. 