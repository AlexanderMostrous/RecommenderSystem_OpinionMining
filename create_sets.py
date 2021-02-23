import numpy as np


def create_sets(df, test_set_ratio=0.20):

    # Implement type checking for test_set_ratio
    index = test_set_ratio * len(df.index)
    training_set = np.arrange(index)
    testing_set = np.arrange(index + 1, df.index)

    return training_set, testing_set
