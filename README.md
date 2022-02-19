# Monthly-Traffic-Accidents-in-Munich
\
Dataset : [“Monatszahlen Verkehrsunfälle”](https://www.opengov-muenchen.de/dataset/monatszahlen-verkehrsunfaelle/resource/40094bd6-f82d-4979-949b-26c8dc00b9a7) Dataset from the München Open Data Portal.
\

## Create an AI Model
\
Five columns considered:
  1. Category (MONATSZAHL)
  2. Accident-type (insgesamt means total for all subcategories) (AUSPRAEGUNG)
  3. Year (JAHR)
  4. Month (MONAT)
  5. Value (WERT)



**Data Visualizations**
*Visualizing number of accidents by catogeries in years*
![Visualizing number of accidents by catogeries in years](https://user-images.githubusercontent.com/42963408/154789855-fbf7e14d-f606-4d6e-a224-884a93fcc9cc.png)


*Visualizing number of accidents by catogeries in months*
![image](https://user-images.githubusercontent.com/42963408/154790018-ce505c5b-330a-4c0b-9cc3-ab15270a51ca.png)

**Data Processing**
  * Removed rows with empty cells
  * Removed rows having MONAT as "Summe"
  * Converted MONAT's format from YYYYMM to MM
  * Applied Label Encoding on colums MONATZAHL and AUSPRAEGUNG so that they can be useful while training model, since their datatype was str.

\
**Training Models**

Since the dataset is an example of time series (spread over several years and months), the  ML models that could be used for forecasting were Linear Regression and Random Forest Regressor.
The dataset was split into *X = [MONATSZAHL , AUSPRAEGUNG , JAHR , MONAT] and Y=[WERT].*
Cross validation was not required to be done because random sampling on time series would have led to use of future's data to predict past, which doesn't make any sense. The model was later saved as a .joblib file for usage in deployment.
\

*Performance of RandomForestRegressor*

![image](https://user-images.githubusercontent.com/42963408/154790562-6a15e85c-49dd-4d1a-8d39-0f9ccb35db1c.png)

For more info: [Jupyter Notebook](https://github.com/Priya15073/Monthly-Traffic-Accidents-in-Munich/blob/8ef96bd012126b9e97ed4b5a607e9aeeb424143c/Mission_1.ipynb)


## Deployment of Model

The deployment of model was done via API using FastApi and Heroku.

**Using FastAPI**
FastAPI provides an API for the model earlier and shows the predicted value in JSON format.
  * FastAPI() was used to initialised the API.
  * joblib.load() enabled the loading of the model saved earlier.
  * class Traffic(BaseModal) helps in validating that the JSON received from POST is in the reaquired datatypes.
  * predict(Traffic) changes the information obtained from POST, especially MONATSZAHL , AUSPRAEGUNG to labels so that they are ready to be used by model.predict() which returns the WERT predicted value.
  * JSONResponse ensures that value returned to FastAPI is in JSON Format.
It uses unicorn to launch the API on server.


**Using Heroku**
Heroku was used to deploy the Aplication on web.
  * Procfile  is run by Heroku which provides instructions to the server
  * runtime.txt tells heroku which frameworks/tools might be needed to be preinstalled for the application to be run successfully.
  * The [application](https://num-accident-prediction.herokuapp.com/docs#/) provides an interface to input values(X) in JSON Format and displays the predicted value as well.
