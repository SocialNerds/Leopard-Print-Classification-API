import includes.train_data as train_data
import includes.prediction_model as prediction_model
import includes.modelarg as modelarg
import tensorflow as tf

# Disable warnings.
tf.logging.set_verbosity(tf.logging.ERROR)

# Load specific model weigths.
model = prediction_model.PredictionModel(modelarg.get_argument())

# Train model multiple times with different cuts and shufflings.
for i in range(1, 16):
    print('Running', i, 'out of 15 times.')
    values, labels = train_data.Data().get_training_photos()
    model.train(values, labels)

    model.save()
    print('Model saved to disk')
