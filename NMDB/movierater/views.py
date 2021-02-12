from django.shortcuts import render
from .forms import newMovie
from keras.models import load_model
from keras.preprocessing import image
import tensorflow as tf
import json
from tensorflow import Graph, Session



model_graph = Graph()
with model_graph.as_default():
    tf_session = Session()
    with tf_session.as_default():
        model=load_model('/home/josoga2/Documents/projects/NMDB/MovieClassifier.h5')

# Create your views here.

def ratingPrediction(request):

    form = newMovie(request.POST)
    
    def pad_to_size(vec, size):
        zeros = [0]*(size-len(vec))
        vec.extend(zeros)
        return vec

    def sample_predict(sentence, pad):
        encoded_sample_pred_text = encoder.encode(sentence)
        if pad:
            encoded_sample_pred_text = pad_to_size(encoded_sample_pred_text, 64)
            encoded_sample_pred_text = tf.cast(encoded_sample_pred_text, tf.float32)
            predictions = model.predict(tf.expand_dims(encoded_sample_pred_text, 0))
            return predictions
    
    sample_text = ('How wish i can stop falling in love with Nazo Ekezie')
    sample_text = request.POST.get('Comment')
    predictions = sample_predict(sample_text, pad=True)*10
    print('Predicted review based on IMDB data%.2f' %predictions)

    movieName = request.POST.get('Title')
    MovieRating = predictions
    
    context = {'movieName':movieName, 'MovieRating': MovieRating, 'form':form}
    return render(request, 'index.html', context)
