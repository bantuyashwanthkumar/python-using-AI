                                                                               # (Deep Learning with TensorFlow )
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.datasets import mnist

# Load the MNIST dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Preprocess the data: Normalize pixel values to range [0, 1]
X_train, X_test = X_train / 255.0, X_test / 255.0

# Create a simple neural network model
model = Sequential([
    Flatten(input_shape=(28, 28)),  # Flatten the 28x28 images
    Dense(128, activation='relu'),  # Fully connected layer with 128 neurons
    Dense(10, activation='softmax')  # Output layer with 10 neurons (for 10 digits)
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])




# import numpy as np                                                                         (PYTHON USING AI)
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split

# # Sample Data: Number of rooms vs house price
# X = np.array([[1], [2], [3], [4], [5]])  # Number of rooms
# y = np.array([1, 2, 1.5, 3.5, 5])  # Price in $1000s

# # Split data into training and test sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Initialize the Linear Regression Model
# model = LinearRegression()

# # Train the model
# model.fit(X_train, y_train)

# # Predictions
# y_pred = model.predict(X_test)

# # Plotting the results
# plt.scatter(X, y, color='blue')
# plt.plot(X, model.predict(X), color='red')
# plt.title("House Price Prediction")
# plt.xlabel("Number of Rooms")
# plt.ylabel("Price in $1000")
# plt.show()

# # Output predictions
# print("Predicted house prices: ", y_pred)

# # Train the model
# model.fit(X_train, y_train, epochs=5)

# # Evaluate the model on test data
# test_loss, test_acc = model.evaluate(X_test, y_test)

# print(f"Test accuracy: {test_acc * 100:.2f}%")




# from sklearn.datasets import load_iris                                                     ( SKITIK.LEARNING)
# from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.metrics import accuracy_score

# # Load the Iris dataset
# data = load_iris()
# X = data.data
# y = data.target

# # Split data into training and test sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# # Initialize the Decision Tree Classifier
# clf = DecisionTreeClassifier()

# # Train the classifier
# clf.fit(X_train, y_train)

# # Predict on the test set
# y_pred = clf.predict(X_test)

# # Evaluate accuracy
# accuracy = accuracy_score(y_test, y_pred)
# print(f"Accuracy of Decision Tree Classifier: {accuracy * 100:.2f}%")








# import nltk                                                                               (NATURAL LANGUAGE PROCESSING)USING AI
# from nltk.sentiment import SentimentIntensityAnalyzer

# # Ensure that necessary NLTK resources are downloaded
# nltk.download('vader_lexicon')

# # Initialize the SentimentIntensityAnalyzer
# sia = SentimentIntensityAnalyzer()

# # Sample text for sentiment analysis
# text = "I love machine learning, it's amazing!"

# # Get sentiment scores
# sentiment_scores = sia.polarity_scores(text)

# print("Sentiment Scores:", sentiment_scores)

# # Analyze sentiment
# if sentiment_scores['compound'] >= 0.05:
#     print("The sentiment of the text is Positive.")
# elif sentiment_scores['compound'] <= -0.05:
#     print("The sentiment of the text is Negative.")
# else:
#     print("The sentiment of the text is Neutral.")




# import gym                                                          (Reinforcement Learning Example with gym USING PYTHON +AI)

# # Create the environment (CartPole)
# env = gym.make('CartPole-v1')

# # Initialize variables
# state = env.reset()
# done = False

# # Run the environment
# for _ in range(1000):
#     env.render()  # Visualize the environment
#     action = env.action_space.sample()  # Random action
#     state, reward, done, info = env.step(action)  # Take the action

#     if done:
#         break

# env.close()


