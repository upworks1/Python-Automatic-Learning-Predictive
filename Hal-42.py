import pandas as pd
import numpy as np 
import matplotlib as plt
import tensorflow as tf


AMD_TRAIN_DATA = 'Training-data/AMD_train_year.csv'
AMD_TEST_DATA = 'AMD-realtime.csv'

current_train_data = AMD_TRAIN_DATA
current_test_data = AMD_TEST_DATA 

NUM_TRAIN_DATA_POINTS = 125
NUM_TEST_DATA_POINTS = 50

def load_stock_data(stock_name, num_data_points):
    data = pd.read_csv(stock_name, skiprows=0,nrows=num_data_points,usecols=['Price','Open', 'Vol.'])

 final_prices = data['Price'].astype(str).str.replace(',','').astype(np.float)
    # Prices of stock at the beginning of each day
    opening_prices = data['Open'].astype(str).str.replace(',', '').astype(np.float)
    # Volume of stock exchanged throughout the day
    volumes = data['Vol.'].str.strip('MK').astype(np.float)
    return final_prices, opening_prices, volumes


# Training data sets
train_final_prices, train_opening_prices, train_volumes = load_stock_data(current_train_data, NUM_TRAIN_DATA_POINTS)
train_price_differences = calculate_price_differences(train_final_prices, train_opening_prices)
train_volumes = train_volumes[:-1]

# Testing data sets
test_final_prices, test_opening_prices, test_volumes = load_stock_data(current_test_data, NUM_TEST_DATA_POINTS)
test_price_differences = calculate_price_differences(test_final_prices, test_opening_prices)
test_volumes = test_volumes[:-1]

# Building computational graph after y = Wx + b

# Used to input volumes
x = tf.placeholder(tf.float32, name='x')
# Variables that our model will change to get actual output as close to expected output as possible
W = tf.Variable([.1], name='W')
b = tf.Variable([.1], name='b')
# How our model outputs the actual values
y = W * x + b
# Used to input expected values for training purposes (shows the model what a "good" outcome is)
y_predicted = tf.placeholder(tf.float32, name='y_predicted')

# Loss function based on the difference between actual and expected outputs
loss = tf.reduce_sum(tf.square(y - y_predicted))
# Optimizer aimed at minimizing loss by changing W and b
optimizer = tf.train.AdamOptimizer(LEARNING_RATE).minimize(loss)

# Session is used to actually run the nodes
session = tf.Session()
# Need to initialize global variables
session.run(tf.global_variables_initializer())
for _ in range(NUM_EPOCHS):
    # Run the optimizer which will allow it to change the values of W and b to minimize loss
    session.run(optimizer, feed_dict={x: train_volumes, y_predicted: train_price_differences})

results = session.run(y, feed_dict={x: test_volumes})
accuracy = calculate_accuracy(test_price_differences, results)
print("Accuracy of model: {0:.2f}%".format(accuracy))

# # Plotting purposes only, not necessary
# plt.figure(1)
# plt.plot(train_volumes, train_price_differences, 'bo')
# plt.title('Price Differences for Given Volumes for the Past Year')
# plt.xlabel('Volumes')
# plt.ylabel('Price differences')
# plt.show()