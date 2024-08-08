import sparknlp
from sparknlp.base import *
spark = sparknlp.start()
document = sparknlpץDocumentAssembler().setInputCol("text").setOutputCol("document")
sentence = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "xx").setInputCols(["document"]).setOutputCol("sentence")
tokenizer = Tokenizer().setInputCols(["sentence"]).setOutputCol("token") 
lemma = LemmatizerModel.pretrained("lemma_htb", "he").setInputCols(["token"]).setOutputCol("lemma")

pipeline = Pipeline(stages=[document, sentence, tokenizer, lemma])

data = spark.createDataFrame([["I love Spark NLP"]]).toDF("text")

result = pipeline.fit(data).transform(data)
print(result)