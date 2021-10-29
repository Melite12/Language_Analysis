from util import sort_count_pairs
import math

def count_tokens(tokens):
    counter = {}
    for letter in tokens:
        counter[letter] = counter.get(letter, 0) + 1

    return counter

def sorted_token_list(tokens):
    token_dict = count_tokens(tokens)

    token_list = []
    for value in token_dict.items():
        token_list.append(value)
    token_list = sort_count_pairs(token_list)
    return token_list

def find_top_k(tokens, k):
    token_list = sorted_token_list(tokens)

    top_k = token_list[:k]
    ans_list = []
    for items in top_k:
        ans_list.append(items[0])

    return ans_list

def find_min_count(tokens, min_count):
    token_dict = count_tokens(tokens)

    ans_set = set()
    for value in token_dict.items():
        if value[1] >= min_count:
            ans_set.add(value[0])

    return ans_set

def tf(t, d, TD, TL):
    F_td = TD[t]
    max_term = TL[0][1]

    ans = 0.5 + (0.5 * (F_td / max_term))
    return ans

def idf(t, D):
    num_documents = len(D)

    total = 0
    for value in D:
        if t in value:
            total +=1

    ans = math.log(num_documents / total)
    return ans

def tf_idf(t,d,D, TD, TL):
    tf_val = tf(t,d, TD, TL)
    idf_val = idf(t, D)

    return tf_val*idf_val

def find_salient(docs, threshold):
    ans_list = []

    for doc in docs:
        s = set()
        token_dict = count_tokens(doc)
        token_list = sorted_token_list(doc)
        for value in token_dict:
            tf_idf_val = tf_idf(value, doc, docs, token_dict, token_list)
            if tf_idf_val > threshold:
                s.add(value)
        ans_list.append(s)

    return ans_list


def find_text_in_entities(tweets, entity_desc):
    key, data_in_key = entity_desc[0], entity_desc[1]
    data_list = []
    for tweet in tweets:
        entity = tweet['entities'][key]
        for data in entity:
            entity_text = data[data_in_key]
            data_list.append(entity_text)

    return data_list

def find_top_k_entities(tweets, entity_desc, k):

    data_list = find_text_in_entities(tweets, entity_desc)
    top_k = find_top_k(data_list, k)

    return top_k

def find_min_count_entities(tweets, entity_desc, min_count):

    data_list = find_text_in_entities(tweets, entity_desc)
    data_list_min_count = find_min_count(data_list, min_count)

    return data_list_min_count

def clean_text(text, case_sensitive, stop_words):
    if case_sensitive:
        text = text.lower()

    split_text = text.split()
    clean_text = []
    for word in split_text:
        #word = word.strip(PUNCTUATION)
        clean = True
        if stop_words and word in STOP_WORDS:
        #    clean = False
        #if word in STOP_PREFIXES or word.startswith(STOP_PREFIXES): (still have to code the input for this)
        #    clean = False
        if clean and len(word) > 0:
            clean_text.append(word)

    return clean_text

def return_ngrams(text, n, case_sensitive, stop_words):
    text = clean_text(text, case_sensitive, stop_words)

    n_grams = []
    for p in range(0, len(text) - (n - 1)):
        n_gram = []
        for i in range(0, n):
            n_gram.append(text[(i + p)])
        n_grams.append(tuple(n_gram))

    return n_grams

def return_all_ngrams(tweets, n, case_sensitive, stop_words):
    all_ngrams = []
    for tweet in tweets:
        new_ngram = return_ngrams(tweet["abridged_text"], n, case_sensitive, stop_words)
        # may need to be extend instead of append
        all_ngrams.append(new_ngram)
    return all_ngrams

def find_top_k_ngrams(tweets, n, case_sensitive, k):
    stop_words = True
    all_ngrams = return_all_ngrams(tweets, n, case_sensitive, stop_words)
    return find_top_k(all_ngrams, k)

def find_min_count_ngrams(tweets, n, case_sensitive, min_count):
    stop_words = True
    all_ngrams = return_all_ngrams(tweets, n, case_sensitive, stop_words)
    min_count = find_min_count(all_ngrams, min_count)

    return min_count

def find_salient_ngrams(tweets, n, case_sensitive, threshold):
    stop_words = False
    all_ngrams = return_all_ngrams(tweets, n, case_sensitive, stop_words)
    salient_n = find_salient(all_ngrams, threshold)

    return salient_n

PUNCTUATION = ['#']
STOP_PREFIXES
STOP_WORDS

tweets = [ {"abridged_text": "the cat in the hat" },
           {"abridged_text": "don't let the cat on the hat" },
           {"abridged_text": "the cat's hat" },
           {"abridged_text": "the hat cat" }]

ans = find_salient_ngrams(tweets, 2, False, 1.33)
print(ans)

