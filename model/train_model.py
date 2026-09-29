import pandas as pd
import pickle

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

# Load dataset
df = pd.read_csv("../data/incidents.csv")

texts = df["description"]
labels = df["category"]

# Encode labels
encoder = LabelEncoder()
y = encoder.fit_transform(labels)

# Tokenizer
tokenizer = Tokenizer(num_words=1000)
tokenizer.fit_on_texts(texts)

X = tokenizer.texts_to_sequences(texts)
X = pad_sequences(X, maxlen=10)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Deep Learning Model
model = Sequential([
    Embedding(1000, 32, input_length=10),
    LSTM(32),
    Dense(16, activation="relu"),
    Dense(len(encoder.classes_), activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

model.fit(X_train, y_train, epochs=20, validation_data=(X_test, y_test))

model.save("incident_model.h5")

pickle.dump(tokenizer, open("tokenizer.pkl","wb"))
pickle.dump(encoder, open("label_encoder.pkl","wb"))

print("Model Saved")