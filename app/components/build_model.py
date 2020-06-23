from components.build_post_list import build_post_list
from components.tweet_cleaning import emoji_free_text, url_free_text

# Base and Cleaning
import pandas as pd
import re
import string

# Natural Language Processing (NLP)
import spacy
from spacy.tokenizer import Tokenizer
from gensim.corpora import Dictionary
from gensim.models import LdaModel
from gensim.parsing.preprocessing import STOPWORDS as gensim_stopwords
from wordcloud import STOPWORDS as wordcloud_stopwords

wordcloud_stopwords = set(wordcloud_stopwords)


def build_model(twitter_handle, num_followers_to_scan, max_tweet_age=7, user_stopwords=None):
    # Creating the dataframe from tweets pulled from Twitter API
    if user_stopwords is None:
        user_stopwords = []
    data = build_post_list(twitter_handle, num_followers_to_scan=num_followers_to_scan, max_tweet_age=max_tweet_age)

    df = pd.DataFrame.from_dict(data, orient='index')
    df = df.rename(columns={0: 'tweets'})
    df['tweets'] = df['tweets'].apply(emoji_free_text)
    df['tweets'] = df['tweets'].apply(url_free_text)

    # Tokenizing the tweets
    nlp = spacy.load('en_core_web_sm')

    tokenizer = Tokenizer(nlp.vocab)
    custom_stopwords = ['&amp;', '&', '⠀', '|', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    # Customize stop words by adding to the default list. Add other stop words for good measure.
    stopwords = nlp.Defaults.stop_words.union(custom_stopwords).union(wordcloud_stopwords).union(gensim_stopwords)
    stopwords = stopwords.union(user_stopwords)

    tokens = []
    for doc in tokenizer.pipe(df['tweets'], batch_size=500):
        doc_tokens = []
        for token in doc:
            if token.text.lower() not in stopwords:
                doc_tokens.append(token.text.lower())
        tokens.append(doc_tokens)
    # Makes tokens column
    df['tokens'] = tokens
    # Make tokens a string again

    # Reference 4 : https://stackoverflow.com/questions/45306988/column-of-lists-convert-list-to-string-as-a-new-column
    df['tokens_back_to_text'] = [' '.join(map(str, l)) for l in df['tokens']]

    # Lemmitization
    def get_lemmas(text):
        """
        Used to lemmatize the processed tweets
        """
        lemmas = []

        doc = nlp(text)

        # Something goes here :P
        for token in doc:

            if ((token.is_stop is False) and (token.is_punct is False)) and (token.pos_ != 'PRON'):
                lemmas.append(token.lemma_)

        return lemmas

    df['lemmas'] = df['tokens_back_to_text'].apply(get_lemmas)

    # Make lemmas a string again
    df['lemmas_back_to_text'] = [' '.join(map(str, lemma)) for lemma in df['lemmas']]

    # Tokenizing lemmas and cleaning tokens
    def tokenize(text):
        """
        Parses a string into a list of semantic units (words)
        Args:
            text (str): The string that the function will tokenize.
        Returns:
            list: tokens parsed out
        """
        # Removing url's
        pattern = r"http\S+"

        text = re.sub(pattern, "", text)  # https://www.youtube.com/watch?v=O2onA4r5UaY
        text = re.sub('[^a-zA-Z 0-9]', '', text)
        text = re.sub('[%s]' % re.escape(string.punctuation), '', text)  # Remove punctuation
        text = re.sub('\w*\d\w*', '', text)  # Remove words containing numbers
        text = re.sub('@*!*\$*', '', text)  # Remove @ ! $
        text = text.replace(',', '')  # TESTING THIS LINE
        text = text.replace('?', '')  # TESTING THIS LINE
        text = text.replace('!', '')  # TESTING THIS LINE
        text = text.replace("'", '')  # TESTING THIS LINE
        text = text.replace(".", '')  # TESTING THIS LINE

        text_tokens = text.lower().split()  # Make text lowercase and split it

        return text_tokens

    # Apply tokenizer
    df['lemma_tokens'] = df['lemmas_back_to_text'].apply(tokenize)

    # Create a id2word dictionary
    id2word = Dictionary(df['lemma_tokens'])

    # Filtering Extremes
    id2word.filter_extremes(no_below=2, no_above=.99)

    # Creating a corpus object 
    corpus = [id2word.doc2bow(d) for d in df['lemma_tokens']]

    # Instantiating a LDA model
    # model = LdaModel(corpus=corpus, num_topics=5, id2word=id2word, passes=5)
    model = LdaModel(
        corpus=corpus,
        id2word=id2word,
        num_topics=68,
        random_state=42,
        chunksize=2000,
        passes=25,
        decay=0.5,
        iterations=70)

    # Filtering for words 
    words = [re.findall(r'"([^"]*)"', t[1]) for t in model.print_topics()]

    # Create Topics
    topics = [' '.join(t[0:10]) for t in words]

    # Load up dictionary for return value
    topics_dict = {"topics": {}}
    for topic_number, topic in enumerate(topics):
        if topic_number + 1 <= 5:
            topics_dict['topics'][topic_number + 1] = topic.split(" ")

    return topics_dict


if __name__ == "__main__":
    print(build_model('DutchBros', 5))
