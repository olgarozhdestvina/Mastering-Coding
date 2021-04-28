# https://github.com/OlafenwaMoses/ImageAI/blob/master/imageai/Classification/README.md

from imageai.Prediction import ImagePrediction
import os

execution_path = os.getcwd()

# Model
prediction = ImagePrediction()
# Choosing MobileNetV2 as it is the lightest model
# (though it has a lower accuracy)
prediction.setModelTypeAsMobileNetV2()

# Set and load the model
prediction.setModelPath(os.path.join(execution_path, "mobilenet_v2.h5"))
prediction.loadModel()

# Make 5 predictions and probability of each prediction
predictions, probabilities = prediction.classifyImage(os.path.join(execution_path, "hippo.jpg"), result_count=5 )
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , eachProbability)