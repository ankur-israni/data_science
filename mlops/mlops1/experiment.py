import warnings
import argparse
import logging
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet

from pathlib import Path
import mlflow

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)

# Get arguments from the command line. These are hyper-parameters (alpha & l1_ratio) being passed from the command line.
# *************** MAIN ********************************************
# This is the ENTRY POINT for this Python file.
parser = argparse.ArgumentParser()
parser.add_argument("--alpha", type=float, required=False, default=0.9)
parser.add_argument("--l1_ratio", type=float, required=False, default=0.8)
args = parser.parse_args()

#evaluation function
def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2


if __name__ == "__main__":

    warnings.filterwarnings("ignore")
    np.random.seed(40)

    # Read the wine-quality csv file from local machine
    complete_dataset = pd.read_csv(r"./resources/wineqt.csv")

    # Split the data into training and test sets. (0.75, 0.25) split.
    # data (100%) = By default the split is 75% and 25%
    # train(75% of 'data') = model is trained with this data
    # test(25%) = model is tested with this data
    training_dataset_75, test_dataset_25 = train_test_split(complete_dataset)

    # The predicted column is "quality" which is a scalar from [3, 9]
    # axis=1 = drop the column called 'quality' from the dataframe
    # train_x = entire dataset without the 'quality' column
    train_x = training_dataset_75.drop(["quality"], axis=1)
    test_x = test_dataset_25.drop(["quality"], axis=1)

    # train_y = only the quality column from the 75% training dataset (training_dataset_75)
    train_y = training_dataset_75[["quality"]]

    # test_y = only the quality column from the 25% test dataset (test_dataset_25)
    test_y = test_dataset_25[["quality"]]


    print("******************************************")
    print("train_x")
    print(train_x.head());
    print("******************************************")
    print("test_x")
    print(test_x.head());
    print("******************************************")
    print("train_y")
    print(train_y.head());
    print("******************************************")
    print("test_y")
    print(test_y.head());
    print("******************************************")



    # Read arguements from the command line.
    # alpha and l1_ratio are the hyperparameters.
    # We want to try different hyperparameters by passing them from the command line and seeing which provides for a better model.
    alpha = args.alpha
    l1_ratio = args.l1_ratio

    #mlflow.set_tracking_uri(uri='file:/mlflow_files/artifacts')

    # Set the EXPERIMENT name
    exp = mlflow.set_experiment(experiment_name='wine_data_experiment')

    '''exp_id = mlflow.create_experiment(name='wine_data', tags={'algo':'multi layered perceptron', 'library':'tensorflow'}, 
                                      artifact_location='./artifacts')'''

    # Start the experiment RUN
    # ElasticNet function is the implementation is the Linear Regression. In Linear Regression we will use the 'XGboost' algorithm
    # TODO: random_state = 42 ?
    # TODO: Comments for lr.fit()
    # TODO: predicted_qualities ?
    with mlflow.start_run(experiment_id=exp.experiment_id, tags={'algo':'XGboost'}):
        lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)

        # Train the alrorithm (Linear Regression > XGBoost) with
        # input = train_x (75% of complete dataset without the 'quality' column)
        # expected output = train_y (75% of complete dataset - only the 'quality' column)
        lr.fit(train_x, train_y)

        # predicted_qualities = Predict the 'quality' based on 75% training data(test_x). This only has the 'quality' column predicted for 25% of complete dataset without the 'quality' column (test_x)
        actual_output_quality = lr.predict(test_x)


        (rmse, mae, r2) = eval_metrics(test_y, actual_output_quality)

        print("Elasticnet model (alpha={:f}, l1_ratio={:f}):".format(alpha, l1_ratio))
        print("  predicted_qualities: %s" % actual_output_quality)
        print("  RMSE: %s" % rmse)
        print("  MAE: %s" % mae)
        print("  R2: %s" % r2)

        params = {
            "alpha":alpha,
            "l1_ratio":l1_ratio
        }

        mlflow.log_params(params)

        metric_params = {
            "rmse":rmse,
            "mae":mae,
            "r2":r2
        }

        mlflow.log_metrics(metric_params)

        mlflow.log_artifact(r'./resources/wineqt.csv')

        mlflow.sklearn.log_model(lr, "linear_regression")  ## linear_regression is directory in which model is stored


##python experiment.py --alpha 0.8 --l1_ratio 0.5