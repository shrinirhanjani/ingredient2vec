import os


# Building Training Set Paramter
FILTERING = 5					# Ingredient-Compounds Pair / Threshold for Least Compounds
RANDOM_SAMPLING = False			# Whether to Random Sample or not
NUM_SAMPLING = 50				# Number of Random Sampling


# Doc2Vec Model Parameter
PRE_TRAIN = False				# Use pre-trained character-level embeddings


# Data Path
path_data = '..' + os.sep + 'data'
path_ingr_info = path_data + os.sep + 'scientific_report' + os.sep + 'ingr_info.tsv'
path_comp_info = path_data + os.sep + 'scientific_report' + os.sep + 'comp_info.tsv'
path_ingr_comp = path_data + os.sep + 'scientific_report' + os.sep +'ingr_comp.tsv'
path_ingr_sentence = path_data + os.sep + 'scientific_report' + os.sep +'ingredient_with_compounds_sentence_level'

# Result Path
path_results = ".." + os.sep + "results"

# Embeddings
path_embeddings_compounds = path_results + os.sep + 'embeddings' + os.sep + 'embeddings_compounds_50.bin'
path_embeddings_ingredients = path_results + os.sep + 'embeddings' + os.sep + 'embeddings_ingredients_f' + str(FILTERING) + '_s' + str(NUM_SAMPLING) +'_dim50.bin'

# Plottings
path_plottings_ingredients_category = path_results + os.sep + 'plot_ingredient_embeddings_category_f' + str(FILTERING) + '_rs' + str(RANDOM_SAMPLING) + '_ns' + str(NUM_SAMPLING)
path_plottings_ingredients_clustering = path_results + os.sep + 'Plot_ingredient_embeddings_cluster_f' + str(FILTERING) + '_rs' + str(RANDOM_SAMPLING) + '_ns' + str(NUM_SAMPLING)


# Pre-Trained Embedding Path
path_embeddings_compounds = path_results + os.sep + 'embeddings' + os.sep + 'embeddings_compounds_50.bin'
path_embeddings_ingredients = path_results + os.sep + 'embeddings' + os.sep + 'embeddings_ingredients_f' + str(FILTERING) + '_rs' + str(RANDOM_SAMPLING) + '_ns' + str(NUM_SAMPLING) +'_dim50.bin'

