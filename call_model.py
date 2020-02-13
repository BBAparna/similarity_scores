from gensim.test.utils import datapath

from gensim.models import KeyedVectors


w2v_model_300= KeyedVectors.load_word2vec_format("model300.bin", binary=True)
print("Model 300 loaded")
w2v_model_100= KeyedVectors.load_word2vec_format("model100.bin", binary=True)
print("Model 100 loaded")