# Credit-Card-Default-Prediction-Project-Pwskills
"In this repository, you'll find my end-to-end machine learning project focused on predicting credit card defaults. The project includes data preprocessing, model training, evaluation, and deployment using Streamlit. Feel free to explore the code, contribute, and use the project for your own analysis and learning purposes."

- [Project_Link] (https://credit-card-default-prediction-project-govindkv-3qodijdls3wyth.streamlit.app/)

- [LinkedIn] (https://www.linkedin.com/in/govind-kumar-97aa07235)
  
## About The Project

The Credit Card Default Prediction project is an end-to-end machine learning initiative designed to predict whether credit card holders will default on their payments in the next month. Financial threats are displaying a trend about the credit risk of commercial banks as the incredible improvement in the financial industry has arisen. In this way, one of the  biggest threats faces by commercial banks is the risk prediction of credit clients. The goal is to predict the probability of credit default based on credit card owner's characteristics and payment history.

## About the Data

This dataset contains information on default payments, demographic factors, credit data, history of payment, and bill statements of credit card clients in Taiwan from April 2005 to September 2005.

There are 24 independent variables (including id):

 - ID: ID of each client
 - LIMIT_BAL: Amount of given credit in NT dollars (includes individual and family/supplementary credit)
 - SEX: Gender (1=male, 2=female)
 - EDUCATION: (1=graduate school, 2=university, 3=high school, 4=others, 5=unknown, 6=unknown)
 - MARRIAGE: Marital status (1=married, 2=single, 3=others)
 - AGE: Age in years
 - PAY_0: Repayment status in September, 2005 (-1=pay duly, 1=payment delay for one month, 2=payment delay for two months,...8=payment delay for eight months, 9=payment delay for nine months and above)
 - PAY_2: Repayment status in August, 2005 (scale same as above)
 - PAY_3: Repayment status in July, 2005 (scale same as above)
 - PAY_4: Repayment status in June, 2005 (scale same as above)
 - PAY_5: Repayment status in May, 2005 (scale same as above)
 - PAY_6: Repayment status in April, 2005 (scale same as above)
 - BILL_AMT1: Amount of bill statement in September, 2005 (NT dollar)
 - BILL_AMT2: Amount of bill statement in August, 2005 (NT dollar)
 - BILL_AMT3: Amount of bill statement in July, 2005 (NT dollar)
 - BILL_AMT4: Amount of bill statement in June, 2005 (NT dollar)
 - BILL_AMT5: Amount of bill statement in May, 2005 (NT dollar)
 - BILL_AMT6: Amount of bill statement in April, 2005 (NT dollar)
 - PAY_AMT1: Amount of previous payment in September, 2005 (NT dollar)
 - PAY_AMT2: Amount of previous payment in August, 2005 (NT dollar)
 - PAY_AMT3: Amount of previous payment in July, 2005 (NT dollar)
 - PAY_AMT4: Amount of previous payment in June, 2005 (NT dollar)
 - PAY_AMT5: Amount of previous payment in May, 2005 (NT dollar)
 - PAY_AMT6: Amount of previous payment in April, 2005 (NT dollar)

### Target variable: 
- default.payment.next.month: Default payment (1=yes, 0=no)
  

Dataset Source Link : ```https://www.kaggle.com/datasets/uciml/default-of-credit-card-clients-dataset/data```

## Built With

 - Pandas
 - Numpy
 - Scikit-learn
 - Flask
 - Seaborn
 - Matplotlib
 - streamlit

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.


## Contact

Govind Vishwakarma - Govind26663355@gmail.com


## Acknowledgements

We'd like to extend our gratitude to all individuals and organizations who have played a role in the development and success of this project. Your support, whether through contributions, inspiration, or encouragement, has been invaluable. Thank you for being a part of our journey.
