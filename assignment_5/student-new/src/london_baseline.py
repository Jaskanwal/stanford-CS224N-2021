# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
import utils

eval_corpus_path = "birth_dev.tsv"
with open(eval_corpus_path, "r") as fopen:
    num_lines = sum(1 for line in fopen)

predictions = ["London"] * num_lines

total, correct = utils.evaluate_places(eval_corpus_path, predictions)
print('Correct: {} out of {}: {}%'.format(correct, total, correct/total*100))
