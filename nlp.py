import tensorflow as tf
import numpy as np

task_descriptions = []

task_list = [("Check mailbox", 0)]
task_list.append(("Retrieve mail", 0))
task_list.append(("Pick up package", 0))
task_list.append(("Dispose of cardboards", 0))
task_list.append(("Call professor back", 1))
task_list.append(("Depart for airport", 1))
task_list.append(("Reply to professor's email within a day", 1))
task_list.append(("Call customer service by Friday", 1))
task_list.append(("Shop groceries", 0))
task_list.append(("Shop jacket on Amazon", 0))
task_list.append(("Return book to library by next week", 1))
task_list.append(("Book doctor's appointment within a day", 1))
task_list.append(("Drop off prescription at pharmacy by tomorrow", 1))
task_list.append(("Pick up prescription at pharmacy by Tuesday", 1))
task_list.append(("Deposit check at bank", 0))
task_list.append(("Order cartridge on Amazon", 0))

task_labels = []

for (t, l) in task_list:
    task_descriptions.append(t)
    task_labels.append(l)

task_labels_np = np.array(task_labels)

vocab_size = 50
embedding_dim = 16
max_length = 20
trunc_type = 'post'
oov_tok = "<OOV>"

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

tokenizer = Tokenizer(num_words = vocab_size, oov_token = oov_tok)
tokenizer.fit_on_texts(task_descriptions)
word_index = tokenizer.word_index
sequences = tokenizer.texts_to_sequences(task_descriptions)
padded = pad_sequences(sequences, maxlen = max_length, truncating = trunc_type)

model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length = max_length),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(6, activation = 'relu'),
    tf.keras.layers.Dense(1, activation = 'sigmoid')
])

model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics = ['accuracy'])
model.summary()

num_epochs = 10
model.fit(padded, task_labels_np, epochs = num_epochs)