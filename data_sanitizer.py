def sanitize_data(df):

    # Columns that are not useful and should be omitted
    omit_list = ["verified", "reviewTime", "style", "unixReviewTime"]

    for columnName in omit_list:
        del df[columnName]

    return df
