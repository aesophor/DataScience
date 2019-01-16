from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
import re
import pandas as pd
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer 
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import os

def read_text(file):
	with open(file, 'r', encoding = 'utf-8') as myfile:
		return myfile.read().replace('\n', '')

def read_text_folder(folder = r'./Text_Folder/', return_names=False):
	file_names = os.listdir(folder)
	text_list = [read_text(folder + f) for f in file_names]
	if return_names:
		return (text_list, file_names)
	else:
		return text_list


def read_word_dict(file):
	with open(file, 'r',  encoding = 'utf-8') as myfile:
		word_list = myfile.read().split('\n')
	
	for i in word_list:
		jieba.add_word(i)

def read_words(file, sep='\n'):
	with open(file, 'r',  encoding = 'utf-8') as myfile:
		word_list = myfile.read().split(sep)
		return word_list

def tokenize_text(text, cut_all=False):
	return [i for i in jieba.cut(text, cut_all=cut_all)]

def count_words(seg_list, stopwords=[], puncs='', stop_pattern='[0-9]+'):
	unnecessary_words = stopwords + list(puncs)
	count_dict = {}
	for w in seg_list:
		if (w not in unnecessary_words) and (re.match(stop_pattern, w) is None):
			if w in count_dict.keys():
				count_dict[w] = count_dict[w] + 1
			else:
				count_dict[w] = 1
	return count_dict

def count_words_in_documents(doc_list, doc_names, stopwords=[], puncs='', stop_pattern='[0-9]+'):
	documents_words_count = {}
	for i in range(len(doc_list)):
		tokenized_doc = tokenize_text(doc_list[i])
		documents_words_count[doc_names[i]] = count_words(tokenized_doc, stopwords, puncs, stop_pattern)
	return documents_words_count



def plot_wordcloud(word_dict, 
				   ax = None,
				   font_path = r'example/font/path/LoremIpsum.ttc',
				   background_color = "white",
				   width = 1000,
				   height = 860,
				   margin = 2):
	wordcloud = WordCloud(font_path=font_path, background_color=background_color, width=width, height=height, margin=margin)
	wordcloud.fit_words(word_dict)
	if ax is None:
		plt.imshow(wordcloud)
	else:
		ax.imshow(wordcloud)


def plot_tf_bar(word_dict,
				ax = None,
				font_path = r'example/font/path/LoremIpsum.ttc',
				bin = 20,
				figsize = (10, 6),
				title = None,
				xticks_fontsize = 10,
				title_fontsize = 20,
				**kwargs):

	sorted_word_dict = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
	index = range(bin)
	label = [i[0] for i in sorted_word_dict[:bin]]
	value = [i[1] for i in sorted_word_dict[:bin]]
	font = FontProperties(fname=font_path)
	if ax is None:
		plt.figure(figsize=figsize)
		plt.bar(index, value, **kwargs)
		plt.xticks(index, label, fontsize=xticks_fontsize, fontproperties=font)
		if not title is None:
			plt.title(title, fontsize=title_fontsize)
	else:
		ax.bar(index, value, **kwargs)
		ax.set_xticks(index)
		ax.set_xticklabels(label, fontsize=xticks_fontsize, fontproperties=font)
		if not title is None:
			ax.set_title(title, fontsize=title_fontsize, fontproperties=font)

def get_sentences(text, sep=' '):
	sentences = text.split(sep)
	return sentences

def tokenize_sentences(sentences):
	tokenized_sentences = {}
	for i in sentences:
		tokenized_sentences[i] = tokenize_text(i)
	return tokenized_sentences


def count_words_in_sentences(tokenized_sentence, stopwords=[], puncs='', stop_pattern='[0-9]+'):
	sentences_words_count = {}
	for key, value in tokenized_sentence.items():
		sentences_words_count[key] = count_words(value, stopwords=stopwords, puncs=puncs,  stop_pattern=stop_pattern)
	return sentences_words_count

def create_word_frequency_matrix(documents_words_count, text_index=None):
	total_words = [word for count in documents_words_count.values() for word in count] 
	unique_word_set = set(total_words)
	for doc, count in documents_words_count.items():
		for zero_word in unique_word_set - set(count.keys()):
			documents_words_count[doc][zero_word] = 0
	
	word_frequency = pd.DataFrame(documents_words_count).T
	if text_index is None:
		word_frequency.index = range(len(word_frequency.index))
	else:
		word_frequency.index = text_index
	return word_frequency

def evaluate_tfidf(word_frequency, drop_freq=0):
	transformer = TfidfTransformer()
	tfidf = transformer.fit_transform(word_frequency.values)  
	df_tfidf = pd.DataFrame(tfidf.toarray(), columns = word_frequency.columns.tolist())
	return df_tfidf

def plot_tfidf_wordcloud(df_tfidf, text_index=0, ax=None, font_path=r'example/font/path/LoremIpsum.ttc', background_color="white", width=1000, height=860, margin=2):
	tfidf_dict = df_tfidf.to_dict(orient='records')
	if ax is None:
		plot_wordcloud(tfidf_dict[text_index], font_path=font_path, background_color=background_color, width=width, height=height, margin=margin)
	else:
		plot_wordcloud(tfidf_dict[text_index], ax=ax, font_path=font_path, background_color=background_color, width=width, height=height, margin=margin)

def plot_tfidf_bar(df_tfidf,
				   text_index=0,
				   ax=None,
				   font_path=r'example/font/path/LoremIpsum.ttc',
				   bin=20,
				   figsize=(10, 6),
				   xticks_fontsize = 10,
				   title_fontsize = 26,
				   **kwargs):
	tfidf_dict = df_tfidf.to_dict(orient='records')
	plot_tf_bar(tfidf_dict[text_index], ax=ax, font_path=font_path, bin=bin, figsize=figsize, xticks_fontsize = 10, title_fontsize = 20, **kwargs)


def set_puncs(add_puncs=''):
	full_space_puncs = '！？｡＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｢｣､、〃》「」『』【】〔〕〝〞〰–—‘’‛“”„‟…‧﹏.。'
	half_space_puncs = """!?." #$%&' ()*+,-/:;<=>[\]@^_{|}~"""
	return full_space_puncs + half_space_puncs +  add_puncs

def PCA_tfidf(df_tfidf, n_components=2, index=None):
	pca = PCA(n_components=n_components)
	pca_df_tfidf = pca.fit_transform(df_tfidf)
	pca_df_tfidf = pd.DataFrame(pca_df_tfidf)
	if index is None:
		pca_df_tfidf.index = df_tfidf.index
	else:
		pca_df_tfidf.index = index
	return pca_df_tfidf



def KMeans_tfidf(pca_df_tfidf, KMeans_object, only_label=True):
	kmeans = KMeans_object
	clustered = kmeans.fit(pca_df_tfidf.values)
	labels = pd.Series(clustered.labels_, name='Label', index=pca_df_tfidf.index)
	if only_label == True:
		return labels
	else:
		tfidf_clustered = pd.concat([pca_df_tfidf, labels], axis=1)
		return tfidf_clustered

def plot_kmeans_scatter(tfidf_clustered,
						ax = None, 
						kmeans_label = None,
						figsize = (8,8),
						label_color_map = None,
						alpha = None,
						title = None,
						title_fontsize = 36,
						font_path = r'example/font/path/LoremIpsum.ttc',
						annotate = True,
						annotate_fontsize = 12):

	font = FontProperties(fname=font_path)
	tag = tfidf_clustered.index

	if kmeans_label is None:
		label = tfidf_clustered['Label'].values
	else:
		label = kmeans_label

	if label_color_map is None:
		label_color = label
	else:
		label_color = [label_color_map[i] for i in label]

	if ax is None:
		plt.figure(figsize = figsize)
		plt.scatter(tfidf_clustered.iloc[:,0], tfidf_clustered.iloc[:,1], c=label_color, alpha=alpha)
		if not title is None:
			params = {'axes.titlesize':title_fontsize}
			plt.rcParams.update(params)
			plt.title(title, fontproperties=font)
		if annotate == True:
			for i in range(len(tag)):
				plt.annotate(tag[i], xy=(tfidf_clustered.iloc[i,0], tfidf_clustered.iloc[i,1]), fontsize=annotate_fontsize, fontproperties=font)
		plt.show()
	else:
		ax.scatter(tfidf_clustered.iloc[:,0], tfidf_clustered.iloc[:,1], c=label_color, alpha=alpha)
		if not title is None:
			params = {'axes.titlesize':title_fontsize}
			plt.rcParams.update(params)
			ax.set_title(title, fontproperties=font)
		if annotate == True:
			for i in range(len(tag)):
				ax.annotate(tag[i], xy=(tfidf_clustered.iloc[i,0], tfidf_clustered.iloc[i,1]), fontsize=annotate_fontsize, fontproperties=font)

