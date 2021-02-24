import numpy as np
import math


def create_sets(df, test_set_ratio=0.20):

    # print("Initial set is: ", df)

    # Implement type checking for test_set_ratio
    if not isinstance(test_set_ratio, float):  # Need to test if it's working correctly
        test_set_ratio = 0.20

    index = math.floor(len(df.index) - (test_set_ratio * len(df.index)))

    training_set = df.iloc[np.arange(index)]
    # print("Training set is: ", training_set)

    testing_set = df.iloc[np.arange(index + 1, len(df.index))]
    # print("Testing set is: ", testing_set)

    # print("Training set rows = ", len(training_set.index), "Testing set rows = ")
    return training_set, testing_set
