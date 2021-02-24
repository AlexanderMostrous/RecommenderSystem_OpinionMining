import loadFile as lf
import data_sanitizer as ds
import create_sets as cs

filePath = 'C:/Development/Thesis/RecommenderSystem_OpinionMining/Appliances_5.json'

# Read File
my_data_frame = lf.load_file(filePath)

# Sanitize Data
my_data_frame = ds.sanitize_data(my_data_frame)

# Create Sets - (optional: Second argument as float - Ratio of data that will be used as testing set - Default 0.2)
training_set, testing_set = cs.create_sets(my_data_frame)

