import gensim
import pyemd
from gensim import models
#from gensim.models import Word2Vec, WordEmbeddingSimilarityIndex
#from gensim.similarities import WmdSimilarity, SoftCosineSimilarity, SparseTermSimilarityMatrix
import gensim.downloader as api

from gensim.models import KeyedVectors

path = get_tmpfile("wordvectors.kv")

model.wv.save(path)
wv = KeyedVectors.load("model.wv", mmap='r')
w2v_model_300 = api.load("glove-wiki-gigaword-300")
