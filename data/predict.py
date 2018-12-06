import numpy as np
import includes.train_data as train_data
import includes.prediction_model as prediction_model
import includes.modelarg as modelarg
import tensorflow as tf
import pandas as pd

# Disable warnings.
tf.logging.set_verbosity(tf.logging.ERROR)

# Load model.
model = prediction_model.PredictionModel(modelarg.get_argument())

# Load test data.
values = np.array(train_data.Data().get_test_photos())

len_values = len(values)
predictions = []
for w in range(len_values):
    # predictions.append([values[w][1], np.round(model.predict(np.asarray([values[w][0]])) * 100, 2)[0][0]])
    predictions.append([values[w][1], np.round(model.predict(np.asarray([values[w][0]])) * 100, 2)[0]])

df = pd.DataFrame([i[1] for i in predictions], columns=[""], index=[i[0] for i in predictions])
print("Percentage (%) of Good Leopardism,")
print(df.groupby(df.index).mean().round(1))