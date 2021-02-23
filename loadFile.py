import pandas as pd
import json

def load_file(path):
    # Opening file
    file1 = open(path, 'r')

    df = pd.DataFrame({})
    counter = 0
    for line in file1:
        if counter == 9:
            break  # For testing purposes
        s = pd.Series(json.loads(line))
        df = df.append(s, ignore_index=True)
        counter += 1

    file1.close()

    return df
