import pandas as pd
import gensim
#from gensim.test.utils import common_texts
#from gensim.models.doc2vec import Doc2Vec, TaggedDocument

patentData = pd.read_csv('patentData.csv')

df = patentData[['patent_abstract','patent_date','patent_number','patent_title']].copy()

pTitle = df['patent_title']
pAbstract = df['patent_abstract']

for i in pAbstract :
  print(i)
  print('\n')
