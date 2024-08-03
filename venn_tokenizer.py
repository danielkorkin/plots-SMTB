import json

from templates_charts.venn_diagram import venn_to_plotly

type_of_token = ["bpe", "wordpiece", "unigram"]
json_directory = "data/output/"

bpe_set = set()
wordpiece_set = set()
unigram_set = set()

# Load the sets from the respective JSON files
for token_type in type_of_token:
    with open(f"{json_directory}{token_type}.json", "r") as files:
        data_dict = json.loads(files.read())
        set_ = data_dict["model"]["vocab"]
        vocab = set(set_)
        if token_type == "bpe":
            bpe_set = vocab
        elif token_type == "wordpiece":
            wordpiece_set = vocab
        elif token_type == "unigram":
            unigram_set = vocab

s = [bpe_set, wordpiece_set, unigram_set]
venn_to_plotly(s, ("BPE", "Wordpiece", "Unigram"), renderer="iframe")
