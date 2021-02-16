from django.shortcuts import render
from .forms import newMovie
import tensorflow_datasets as tfds
#from keras.preprocessing import image
import tensorflow as tf
from tensorflow.keras.models import load_model
import json
from tensorflow import Graph, Session
import numpy as np
from django.core.files.storage import FileSystemStorage


def handle_uploaded_file_path(f):
    stdout = 'movierater/static/uploads'+f.name
    with open('movierater/static/uploads'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return str(stdout)

model_graph = Graph()
with model_graph.as_default():
    tf_session = Session()
    with tf_session.as_default():
        model=load_model('/home/josoga2/Documents/projects/NMDB/MovieClassifier.h5', compile=False)

encoder = tfds.deprecated.text.SubwordTextEncoder.load_from_file('/home/josoga2/Documents/projects/NMDB/encoder')
print(encoder)

# Create your views here.

def ratingPrediction(request):

    form = newMovie(request.POST, request.FILES)
    sample_text = request.POST.get('Comment')
    
    coverArt = print(request.FILES.get('coverArt'))
    
    coverArt = request.FILES.get('coverArt')
    print(coverArt)

    #sample_text = ('How wish i can stop falling in love with Nazo Ekezie')
    #predictions = sample_predict(sample_text, pad=True)*10
    #print('Predicted review based on IMDB data%.2f' %predictions)

    movieName = request.POST.get('Title')
    
    with model_graph.as_default():
        with tf_session.as_default():
            outRes = model.predict((encoder.encode(str(sample_text))))
    
    
    print(encoder)
   
    #predictedLabel=encoder[str(np.array(outRes))]
    MovieRating = round(max(outRes)[0]*10, 1)
    
    context = {'movieName':movieName, 'MovieRating': MovieRating, 'form':form, 'coverArt':coverArt}
    return render(request, 'index.html', context)