# Introduction to Exploratory Data Analysis in python

<br>   

## What is the Exploratory Data Analysis (EDA)?

Exploratory Data Analysis (EDA) is an important first step in data science projects. It involves understanding the data sets by summarizing their main characteristics often plotting them visually. This step is very important especially when we arrive at modeling the data in order to apply Machine learning.   
Plotting in EDA consists of Histograms, Box plot, Scatter plot and many more. It often takes much time to explore the data.   

<br> 

## Why Exploratory Data Analysis is important?  
Exploratory Data Analysis (EDA) is important for several reasons, especially in the context of data science and statistical modeling.   


-   Helps to understand the dataset, showing how many features there are, the type of data in each feature, and how the data is spread out, which helps in choosing the right methods for analysis.     
- EDA helps to identify hidden patterns and relationships between different data points, which help us in and model building.
Allows to spot errors or unusual data points (outliers) that could affect your results.      
- Insights that you obtain from EDA help you decide which features are most important for building models and how to prepare them to improve performance.   
- By understanding the data, EDA helps us in choosing the best modeling techniques and adjusting them for better results.

## Steps for Performing Exploratory Data Analysis
Performing Exploratory Data Analysis (EDA) involves a series of steps designed to help you understand the data you’re working with, uncover underlying patterns, identify anomalies, test hypotheses, and ensure the data is clean and suitable for further analysis.

### Step 1: Importing Required Libraries
Below are the libraries that are used in order to perform EDA (Exploratory data analysis).
``` python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings as wr
wr.filterwarnings('ignore')
```

### Step 2: Reading Dataset
Loading the data into the pandas data frame is certainly one of the most important steps in EDA, as we can see that the value from the data set is comma-separated. So all we have to do is to just read the CSV into a data frame and pandas data frame does the job for us. 
``` python
df = pd.read_csv('/content/sample_data/california_housing_test.csv')

# To display the top 5 rows
df.head()
```
Output
|index|longitude|latitude|housing\_median\_age|total\_rooms|total\_bedrooms|population|households|median\_income|median\_house\_value|
|---|---|---|---|---|---|---|---|---|---|
|0|-122\.05|37\.37|27\.0|3885\.0|661\.0|1537\.0|606\.0|6\.6085|344700\.0|
|1|-118\.3|34\.26|43\.0|1510\.0|310\.0|809\.0|277\.0|3\.599|176500\.0|
|2|-117\.81|33\.78|27\.0|3589\.0|507\.0|1484\.0|495\.0|5\.7934|270500\.0|
|3|-118\.36|33\.82|28\.0|67\.0|15\.0|49\.0|11\.0|6\.1359|330000\.0|
|4|-119\.67|36\.33|19\.0|1241\.0|244\.0|850\.0|237\.0|2\.9375|81700\.0|

``` python
df.tail()                        # To display the botton 5 rows
```

Output  
|index|longitude|latitude|housing\_median\_age|total\_rooms|total\_bedrooms|population|households|median\_income|median\_house\_value|
|---|---|---|---|---|---|---|---|---|---|
|2995|-119\.86|34\.42|23\.0|1450\.0|642\.0|1258\.0|607\.0|1\.179|225000\.0|
|2996|-118\.14|34\.06|27\.0|5257\.0|1082\.0|3496\.0|1036\.0|3\.3906|237200\.0|
|2997|-119\.7|36\.3|10\.0|956\.0|201\.0|693\.0|220\.0|2\.2895|62000\.0|
|2998|-117\.12|34\.1|40\.0|96\.0|14\.0|46\.0|14\.0|3\.2708|162500\.0|
|2999|-119\.63|34\.42|42\.0|1765\.0|263\.0|753\.0|260\.0|8\.5608|500001\.0|

### Step 3: Analyzing the Data
Gaining general knowledge about the data—including its values, kinds, number of rows and columns, and missing values—is the primary objective of data understanding.

``` python
df.shape           # shape will show how many features (columns) and observations (rows) there are in the dataset.
```
Output
``` text
(3000, 9)
```
**`info()`** facilitates comprehension of the data type and related information, such as the quantity of records in each column, whether the data is null or not, the type of data, and the dataset’s memory use.
``` python
df.info()          # info() facilitates comprehension of the data type and related informatio.
```
Output
``` <class 'pandas.core.frame.DataFrame'>
RangeIndex: 3000 entries, 0 to 2999
Data columns (total 9 columns):
 #   Column              Non-Null Count  Dtype  
---  ------              --------------  -----  
 0   longitude           3000 non-null   float64
 1   latitude            3000 non-null   float64
 2   housing_median_age  3000 non-null   float64
 3   total_rooms         3000 non-null   float64
 4   total_bedrooms      3000 non-null   float64
 5   population          3000 non-null   float64
 6   households          3000 non-null   float64
 7   median_income       3000 non-null   float64
 8   median_house_value  3000 non-null   float64
dtypes: float64(9)
memory usage: 211.1 KB
```

**`Description of the data`**    
The DataFrame “df” is statistically summarized by the code df.describe(), which gives the count, mean, standard deviation, minimum, and quartiles for each numerical column. The dataset’s central tendencies and spread are briefly summarized.

``` pyhton
df.describe()
```
Output
|index|longitude|latitude|housing\_median\_age|total\_rooms|total\_bedrooms|population|households|median\_income|median\_house\_value|
|---|---|---|---|---|---|---|---|---|---|
|count|3000\.0|3000\.0|3000\.0|3000\.0|3000\.0|3000\.0|3000\.0|3000\.0|3000\.0|
|mean|-119\.58919999999999|35\.635389999999994|28\.845333333333333|2599\.578666666667|529\.9506666666666|1402\.7986666666666|489\.912|3\.8072717999999997|205846\.275|
|std|1\.9949362939550161|2\.1296695233438325|12\.555395554955755|2155\.59333162558|415\.6543681363232|1030\.5430124122422|365\.42270980552604|1\.854511729691481|113119\.68746964433|
|min|-124\.18|32\.56|1\.0|6\.0|2\.0|5\.0|2\.0|0\.4999|22500\.0|
|25%|-121\.81|33\.93|18\.0|1401\.0|291\.0|780\.0|273\.0|2\.5439999999999996|121200\.0|
|50%|-118\.485|34\.27|29\.0|2106\.0|437\.0|1155\.0|409\.5|3\.4871499999999997|177650\.0|
|75%|-118\.02|37\.69|37\.0|3129\.0|636\.0|1742\.75|597\.25|4\.6564749999999995|263975\.0|
|max|-114\.49|41\.92|52\.0|30450\.0|5419\.0|11935\.0|4930\.0|15\.0001|500001\.0|

<br>

**`Checking Columns`**
The code df.columns.tolist() converts the column names of the DataFrame ‘df’ into a Python list, providing a convenient way to access and manipulate column names.

``` python
df.columns.tolist()
```
Output
```
['longitude',
 'latitude',
 'housing_median_age',
 'total_rooms',
 'total_bedrooms',
 'population',
 'households',
 'median_income',
 'median_house_value']
```

### Step 4: Checking Missing Values
The code df.isnull().sum() checks for missing values in each column of the DataFrame ‘df’ and returns the sum of null values for each column

``` pyhton
df.isnull().sum()
```

Output
```
                   0
longitude	0
latitude	0
housing_median_age	0
total_rooms	0
total_bedrooms	0
population	0
households	0
median_income	0
median_house_value	0

dtype: int64
```


### Step 5:  Checking for the duplicate values
The function df.nunique() determines how many unique values there are in each column of the DataFrame “df,” offering information about the variety of data that makes up each feature.

``` python
# checking duplicate values
df.nunique()
```
Output
```
	              0
longitude	        607
latitude	       587
housing_median_age	52
total_rooms	    2215
total_bedrooms	1055
population	  1802
households  	1026
median_income	2578
median_house_value	1784

dtype: int64
```
