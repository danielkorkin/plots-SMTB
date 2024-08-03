import json

import plotly.graph_objects as go

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

# Calculate token lengths
bpe_lengths = [len(token) for token in bpe_set]
wordpiece_lengths = [len(token) for token in wordpiece_set]
unigram_lengths = [len(token) for token in unigram_set]

# Create distribution plot with Plotly
fig = go.Figure()

fig.add_trace(go.Histogram(x=bpe_lengths, histnorm="percent", name="BPE", opacity=0.6))

fig.add_trace(
    go.Histogram(x=wordpiece_lengths, histnorm="percent", name="WordPiece", opacity=0.6)
)

fig.add_trace(
    go.Histogram(x=unigram_lengths, histnorm="percent", name="Unigram", opacity=0.6)
)

# Overlay both histograms
fig.update_layout(barmode="overlay")
fig.update_traces(opacity=0.6)

# Update layout for better visualization
fig.update_layout(
    title="Token Length Distributions for BPE, WordPiece, and Unigram",
    xaxis=dict(title="Token Length"),
    yaxis=dict(title="Percentage"),
    bargap=0.2,
    bargroupgap=0.1,
)

fig.show()
