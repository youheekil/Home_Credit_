
# Home Credit Default Risk
**Can you predict how capable each applicant is of repaying a loan?**

**Home Credit** trying to broaden financial inclusions for the unbanked
population who are actually trustworthy lenders by using statistical and machine
learning methods to predict capable
applicant of repaying a loan. Doing so will ensure that clients capable of
replayment are not rejected and that loans are given with a principal, muturity,
and repayment calenedar that will empower their clients to be successful.

Eventually, in this project, we will answer first question of `5 Questions Data Scientist Answers` will be
investigated.

Check [Explainable AI](https://www.cc.gatech.edu/~alanwags/DLAI2016/(Gunning)%20IJCAI-16%20DLAI%20WS.pdf)

* **Is this A or B? (two-class classification)**  
> Is this applicant capable of repaying a loan or no?

These case, categorical dependent variable is only with two categories, yes (1) or no (0). 

For approaching cateogorical variables, we can classify categorical variables/features into two major types :
- Nominal variables: have two or more categoreis which do not associated with order. 
- Ordinal variables: have "levels" or categories with a particular order associated such as low, medium, high. 
When the target is **skewed**, Area Under the ROC Curve (AUC) or ROC curve will the best metric for this skewed binary classification problem. 

To answer the question *Is this A or B*, in this case, problems can be defined as
following:
1. Which factors will have a big impact on repaying the loan?
2. How would those factors affect the repayment ?

We are going to apply `Explainable Artificial Intelligence (XAI)` which refers to methods and techniques in the application of artificial intelligence such that the results of the solution can be understood by humans to answer the defined problems above [(wikipedia)](https://en.wikipedia.org/wiki/Explainable_artificial_intelligence)

----
1. Feature Engineering (Pre-processing)
2. Create Machine Learning Model
3. Find out which variable has the greatest impact through `shap value`
4. The relationship between the most influential five variables and whether to repay the loan.
----

### 1. Feature Engineering
### 2. Modelling
### 3. `shap value`
### 4. Check the relationship with the most influential five variables

----
This dataset has the following collumns:
* SK_ID_CURR
* TARGET
* CODE_GENDER
* FLAG_OWN_CAR
* FLAG_OWN_REALTY
* CNT_CHILDREN
* AMT_INCOME_TOTAL
* AMT_CREDIT
* AMT_ANNUITY
* NAME_TYPE_SUITE
* NAME_INCOME_TYPE
* NAME_EDUCATION_TYPE
* NAME_HOUSING_TYPE
* REGION_POPULATION_RELATIVE
* DAYS_BIRTH
* DAYS_EMPLOYED
* DAYS_ID_PUBLISH
* OWN_CAR_AGE
* CNT_FAM_MEMBERS
* HOUR_APPR_PROCESS_START
* ORGANIZATION_TYPE
* EXT_SOURCE_1
* EXT_SOURCE_2
* EXT_SOURCE_3
* DAYS_LAST_PHONE_CHANGE
* AMT_REQ_CREDIT_BUREAU_YEAR
