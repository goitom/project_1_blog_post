# Workplace Attitudes about Diversity and Working from Home

## Overview
The motivation for this project came from the particulars of this societal 
moment. Specifically, I am interested in exploring aspects of remote work, 
and developer attitudes about diversity in the tech space. The data used in 
this analysis are a few years old. As such, they provide a baseline of the 
characteristics of these issues prior to the emergence of the COVID-19 pandemic 
and nationwide Black Lives Matter protests. The first two questions begin to 
explore the connection between remote vs. office work and salary and job 
satisfaction. The third question explores what attributes, if any, predict 
worker attitudes to diversity in the workplace.

## CRISP-DM Process

### 1. Business Understanding

This analysis is motivated by the following business questions:
* How does remote vs. office work relate to salary?
* How does remote vs. office work relate to job/career satisfaction?
* What if any factors can predict attitudes about diversity in the workplace?

### 2. Data Understanding
To answer these questions, we will look at the 2017 Stack Overflow Survey results. 

#### 2.1 How does remote vs. office work relate to salary?
For the first two questions, we focus on the 
column `HomeRemote`, which corresponds to the following question:

> How often do you work from home or remotely?

Looking at the unprepped data, we see the following distribution of responses.
![BarChartHomeRemote](/figures/BarChartHomeRemote.png)

The data preparation step below will involve making decisions about how to recode and 
collapse these eight responses into a binary independent variable. In particular, we
need to handle the 15% of respondents for which the value is missing.

The first question looks at the relationship between `HomeRemote` and 
`Salary`, which corresponds to the question:

> What is your current annual base salary, before taxes, and excluding bonuses, grants, or other compensation?

Looking at the unprepped data, we see the following distribution:
![HistogramOfReportedSalary](/figures/HistogramOfReportedSalary.png)

#### 2.2 How does remote vs. office work relate to job/career satisfaction?
The second question looks at the relationship between `HomeRemote` and two measures of satisfaction at work: `JobSatisfaction` and `CareerSatisfaction` which each ask the respondent to rate on a scale of 1 (least) to 10 (most) their satisfaction with their job and their career, respectively.

Looking at the unprepped data, we see the following distributions:
![HistogramOfJobSatis](/figures/HistogramOfJobSatis.png)
![HistogramOfCareerSatis](/figures/HistogramOfCareerSatis.png)

#### 2.3 What if any factors can predict attitudes about diversity in the workplace?
For the final question, we will focus on the column: `DiversityImportant`, 
which corresponds to the following question:

> Diversity in the workplace is important

Looking at the unprepped data, we see the following distribution of responses.
![BarChartDiversity](/figures/BarChartDiversity.png)

As a next step in the exploration of the data, we would like to look which variables are associated with `DiversityImportant`. Since many of the variables of interest are nominal, we use the [Cramér's V statistic](https://en.wikipedia.org/wiki/Cram%C3%A9r%27s_V) to describe the strength of association. The statistic yields a value in the range [-1,1] and can be interpreted similarly to the [Pearson's Chi-Squared Test](https://en.wikipedia.org/wiki/Pearson%27s_chi-squared_test#Calculating_the_test-statistic).

The top ten variables associated with `DiversityImportant` are:

| Column               | Cramer's V |
| -------------------- | ---------- |
| `AssessJobDiversity` | 0.401460   |
| `ChangeWorld`	       | 0.111006   |
| `AssessJobProduct`   | 0.106984   |
| `KinshipDevelopers`  | 0.106110   |
| `Country`	           | 0.105216   |
| `ExCoderBelonged`	   | 0.104378   |
| `SeriousWork`	       | 0.103858   |
| `ChallengeMyself`	   | 0.103548   |
| `Gender`	           | 0.103246   |
| `LearningNewTech`	   | 0.099870   |

Let's focus on the columns above. Below are the column names and the corresponding question text: 

| Column | Question |
| ------ | ------ |
| `AssessJobDiversity` | When you're assessing potential jobs to apply to, how important are each of the following to you? The diversity of the company or organization. |
| `ChangeWorld` | I want to change the world. |
| `AssessJobProduct` | When you're assessing potential jobs to apply to, how important are each of the following to you? How widely used or impactful the product or service I'd be working on is. |
| `KinshipDevelopers` | I feel a sense of kinship to other developers. |
| `Country` | In which country do you currently live? |
| `ExCoderBelonged` | You said before that you used to code as part of your job, but no longer do. To what extent do you agree or disagree with the following statements? When I was a developer, I didn't feel like I belonged with my colleagues. |
| `SeriousWork` | I take my work very seriously. |
| `ChallengeMyself` | I like to challenge myself. |
| `Gender` | Which of the following do you currently identify as? |
| `LearningNewTech` | Learning new technologies is fun. |

It looks like feelings about the importance of diversity are associated with other mission-driven sentiments and concientiousness. In the following section, we walk through how we prepared the data for further analysis.

### 3. Prepare Data
All three of the columns of interest may require preparation, since the columns 
of interest are categorical, and have missing data.

#### 3.1 Dropping Rows Where Dependent Variable is Missing
One of the cases where dropping observations is acceptable is when the dependent variable is missing. Let's look at how dropping these rows affects the distribution of values for our explanatory variable, `HomeRemote`:

##### Dropping Rows Where `Salary` is Missing
![BarChartHomeRemote_non_miss_salary](/figures/BarChartHomeRemote_non_miss_salary.png)

##### Dropping Rows Where `JobSatisfaction` is Missing
![BarChartHomeRemote_non_miss_job](/figures/BarChartHomeRemote_non_miss_job.png)

##### Dropping Rows Where `CareerSatisfaction` is Missing
![BarChartHomeRemote_non_miss_career](/figures/BarChartHomeRemote_non_miss_career.png)

##### Dropping Rows Where `DiversityImportant` is Missing
![BarChartDiversity_non_miss](/figures/BarChartDiversity_non_miss.png)

#### 3.2 Collapsing Categories

##### Collapsing `HomeRemote`
Let's collapse the responses into broader categories. In the case of `HomeRemote` it might be helpful to group the responses into a binary classification. We can do this a few ways, and two definitions ('Strict' and 'Lax') are presented here.

>**Strict**: A remote worker is one that is full-time remote

>**Lax**: A remote worker is one that spends at least one day a week working remotely. 

In either case, if are implicitly imputing missing values by treating them as if they were the modal response ("A few days each month").

##### Collapsing Categorical Variables in Diversity Classification
For the columns of interest in the diversity question, I collapsed according to the following critera:

**Ordinal Variables**
>**Strict**: "Very important", "Important"/"Strongly agree", "Agree"

>**Lax**: "Very important", "Important", "Somewhat important"/"Strongly agree", "Agree", "Somewhat agree"

**Non-Ordinal Categorical Variables**
>**Gender**: Self-identified Males as 1, all other categories as 0
>**Country**: Dummy variable indicating if the respondent resides in the United States

### 4. Data Modeling

#### 4.1 Descriptive Statistics for HomeRemote Questions
To assess the association between remote work and other aspects of the job, I generate a variety of plots that describe the relationships between the variables of interest.

#### 4.2 Classification Models for Diversity Question
To predict attitudes about the importance of diversity in the workplace, I compared the performance of four classifiers: Naive Bayes (GNB), Random Forest, Logistic Regression, AdaBoost. Each of these models were applied two models: one that used the 'Strict' recoding of variables, and one that used the 'Lax' recoding of variables.


### 5. Evaluate the Results

#### 5.1 How `Salary` Varies across categories of `HomeRemote`
First, let's look at a boxplot of salary across all response categories for `HomeRemote`:

![BoxPlotHomeRemote](/figures/BoxPlotHomeRemote.png)

The number of categories makes comparison difficult. Looking at the lax definition of remote work
![BoxPlotHomeRemoteLax](/figures/BoxPlotHomeRemoteSalaryLax.png)

we see that the salary floors for both types of workers (remote and non-remote) are similar. However, the medians and the upper quartile range is larger for remote workers.

#### 5.2 Performance of Classifiers 
Turning to attitudes of diversity, predictors of attitudes about the importance of workplace  diversity, we see that the accuracy of the predictors increases markedly across all classifiers if we use the 'Lax' definition of the predictors. The table below summarizes the results.
 
| Classifier           | Accuracy (Strict Model) | Accuracy (Lax Model) |
| -------------------- | ----------------------- | -------------------- |
| GNB                  | 0.6008                  | 0.8379               |
| Random Forest        | 0.6554                  | 0.8847               |
| Logistic Regression  | 0.6598                  | 0.8859               |
| AdaBoost             | 0.6603                  | 0.8861               |


## Acknowledgements
* [Collapsing Cagegorical Variables](https://stats.stackexchange.com/questions/146907/principled-way-of-collapsing-categorical-variables-with-many-levels)
* [Correlation Measures](https://medium.com/@outside2SDs/an-overview-of-correlation-measures-between-categorical-and-continuous-variables-4c7f85610365)
* [Cramér's V statistic](https://en.wikipedia.org/wiki/Cram%C3%A9r%27s_V)
* [Pearson's Chi-Squared Test](https://en.wikipedia.org/wiki/Pearson%27s_chi-squared_test#Calculating_the_test-statistic)
