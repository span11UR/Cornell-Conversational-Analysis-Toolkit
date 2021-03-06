# This example extracts question types from the Wimbledon Winner Interviews Dataset explained TODO
#   using the methods in the asking too much paper (http://www.cs.cornell.edu/~cristian/Asking_too_much.html) to extract question types.
#   (since there is a seed provided, multiple executions of this script will always produce the same clusters)

import os
import pkg_resources
import numpy as np

from convokit import Corpus, QuestionTypology, download

#Initialize QuestionTypology class

num_clusters = 8

# Get precomputed motifs. data_dir contains the downloaded data.
data_dir = os.path.join(pkg_resources.resource_filename("convokit", ""),
    'downloads')

#Load the corpus
corpus = Corpus(filename=download("tennis-corpus"))

#Extract clusters of the motifs and assign questions to these clusters
questionTypology = QuestionTypology(corpus, data_dir, dataset_name='tennis', num_dims=25,
  num_clusters=num_clusters, verbose=False, random_seed=125)

# questionTypology.types_to_data contains the necessary data that is computed in the step above
# its keys are the indices of the clusters (here 0-7). The values are dictionaries with the following keys:
# "motifs": the motifs, as a list of tuples of the motif terms
# "motif_dists": the corresponding distances of each motif from the centroid of the cluster this motif is in
# "fragments": the answer fragments, as a list of tuples of answer terms
# "fragment_dists": the corresponding distances of each fragment from the centroid of the cluster this
# fragment is in
# "questions": the IDs of the questions in this cluster. You can get the corresponding question text by using the
# get_question_text_from_pair_idx(pair_idx) method.
# "question_dists": the corresponding distances of each question from the centroid of the cluster
# this question is in

# #Output required data representations

questionTypology.display_totals()
print('10 examples for types 1-8:')
for i in range(num_clusters):
    questionTypology.display_motifs_for_type(i, num_egs=10)
    questionTypology.display_answer_fragments_for_type(i, num_egs=10)
    questionTypology.display_question_answer_pairs_for_type(i, num_egs=10)
