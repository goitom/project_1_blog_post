# Write a Data Science Blog Post

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
For the first two questions, we focus on the 
column `HomeRemote`, which corresponds to the following question:

> How often do you work from home or remotely?

The first question looks at the relationship between `HomeRemote` and 
`Salary`, which corresponds to the question:

> What is your current annual base salary, before taxes, and excluding bonuses, grants, or other compensation?

The second question looks at the relationship between `HomeRemote` and two measures of satisfaction at work: `JobSatisfaction` and `CareerSatisfaction` which each ask the respondent to rate on a scale of 1 (least) to 10 (most) their satisfaction with their job and their career, respectively.

![HomeRemoteBarChart](/figures/HomeRemoteBarChart.png)

For the final question, we will focus on the column: `DiversityImportant`, 
which corresponds to the following question:

> Diversity in the workplace is important

### 3. Prepare Data
All three of the columns of interest require preparation, since the the columns 
of interest are categorical, and have missing data.


### 4. Data Modeling

### 5. Evaluate the Results

### 6. Deploy