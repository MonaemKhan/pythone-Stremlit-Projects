import numpy as np
import re, pickle
import tensorflow as tf

stopword_list = open('bangla_stopwords.pkl', 'rb')
stp = pickle.load(stopword_list)

def process_news(articles):
		news = articles.replace('\n', ' ')
		news = re.sub('[^\u0980-\u09FF]', ' ', str(news))  # removing unnecessary punctuation
		# stopwords removal
		result = news.split()
		news = [word.strip() for word in result if word not in stp]
		news = " ".join(news)
		return news

with open('tokenizer.pickle', 'rb') as handle:
		loaded_tokenizer = pickle.load(handle)

model = tf.keras.models.load_model('Document_Categorization.h5')

class_names = ['দুর্ঘটনা', 'শিল্প', 'অপরাধ', 'অর্থনীতি', 'শিক্ষা', 'বিনোদন',
				   'পরিবেশ', 'আন্তর্জাতিক', 'মতামত', 'রাজনীতি', 'বিজ্ঞান', 'খেলাধুলা']

def process(file):
    article = file
    cleaned_news = process_news(article)
    seq = loaded_tokenizer.texts_to_sequences([cleaned_news])
    padded = tf.keras.utils.pad_sequences(seq, value=0.0, padding='post',maxlen=300)
    pred = model.predict(padded)
    category_name = class_names[np.argmax(pred)]
    return category_name


