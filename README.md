# similarity_scores
# finding similarity scores of corpus extracted from  urls  against lists of security keywords
required libraries were imported.
urls were collected from location stored in the disk and  passed to the code in loop.
lists were called from INI file and iterated with corpus from url to get the similarity scores between them.
defined few functions to ge urls from file,clean the corpus extracted from url and find cosine similaities and calling pretrined model.
scores were saved to a csv file
