""" This module prepares midi file data and feeds it to the neural
    network for training """
import glob
import pickle
import numpy
import logging
from music21 import converter, instrument, note, chord
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM, Activation
from keras.layers import BatchNormalization as BatchNorm
from keras.utils import np_utils
from keras.callbacks import ModelCheckpoint


logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s [%(levelname)s] - %(message)s"
)
_logger = logging.getLogger(__name__)


def train_network():
    """ Train a Neural Network to generate music """
    logging.info('Start Train Network')
    notes = get_notes()

    # get amount of pitch names
    n_vocab = len(set(notes))
    logging.info(f'Amount of pitches:{n_vocab}')

    network_input, network_output = prepare_sequences(notes, n_vocab)

    model = create_network(network_input, n_vocab)

    train(model, network_input, network_output)


def get_notes():
    """ Get all the notes and chords from the midi files in the ./assets/songs directory """
    logging.info('Start get all notes and chords')
    notes = []

    for file in glob.glob("assets/songs/*.mid"):
        midi = converter.parse(file)

        _logger.info(f"Parsing song: {file}")

        notes_to_parse = None

        # file has instrument parts
        try:
            s2 = instrument.partitionByInstrument(midi)
            notes_to_parse = s2.parts[0].recurse()
        # file has notes in a flat structure
        except:
            notes_to_parse = midi.flat.notes
            logging.error("Exception occurred", exc_info=True)

        for element in notes_to_parse:
            if isinstance(element, note.Note):
                notes.append(str(element.pitch))
            elif isinstance(element, chord.Chord):
                notes.append(".".join(str(n) for n in element.normalOrder))

    with open("data/notes", "wb") as filepath:
        pickle.dump(notes, filepath)
        logging.info('written notes in data/notes')
    return notes


def prepare_sequences(notes, n_vocab):
    """ Prepare the sequences used by the Neural Network """
    logging.info('Starting to prepar the sequence')
    sequence_length = 100

    # get all pitch names
    pitchnames = sorted(set(item for item in notes))

    # create a dictionary to map pitches to integers
    note_to_int = dict((note, number) for number, note in enumerate(pitchnames))
    logging.info('Dictionary created')

    network_input = []
    network_output = []

    # create input sequences and the corresponding outputs
    for i in range(0, len(notes) - sequence_length, 1):
        sequence_in = notes[i : i + sequence_length]
        sequence_out = notes[i + sequence_length]
        network_input.append([note_to_int[char] for char in sequence_in])
        network_output.append(note_to_int[sequence_out])
    
    loggin.info('Network input and output created')
    n_patterns = len(network_input)
    logging.info('Number of patterns:%s', n_patterns)

    # reshape the input into a format compatible with LSTM layers
    network_input = numpy.reshape(network_input, (n_patterns, sequence_length, 1))
    # normalize input
    network_input = network_input / float(n_vocab)
    loggin.info('Network input reshaped and normalized')

    network_output = np_utils.to_categorical(network_output)
    logging.info('Sequences Prepared')
    return (network_input, network_output)


def create_network(network_input, n_vocab):
    """ create the structure of the neural network """
    logging.info('Starting to create network')
    model = Sequential()
    model.add(
        LSTM(
            512,
            input_shape=(network_input.shape[1], network_input.shape[2]),
            recurrent_dropout=0.3,
            return_sequences=True,
        )
    )
    model.add(
        LSTM(
            512,
            return_sequences=True,
            recurrent_dropout=0.3,
        )
    )
    model.add(LSTM(512))
    model.add(BatchNorm())
    model.add(Dropout(0.3))
    model.add(Dense(256))
    model.add(Activation("relu"))
    model.add(BatchNorm())
    model.add(Dropout(0.3))
    model.add(Dense(n_vocab))
    model.add(Activation("softmax"))
    model.compile(loss="categorical_crossentropy", optimizer="rmsprop")

    logging.info('Neural Network created')
    return model


def train(model, network_input, network_output):
    """ train the neural network """
    logging.info('Starting model training')
    filepath = "assets/weights/weights-improvement-{epoch:02d}-{loss:.4f}-bigger.hdf5"
    checkpoint = ModelCheckpoint(
        filepath, monitor="loss", verbose=0, save_best_only=True, mode="min"
    )
    callbacks_list = [checkpoint]

    model.fit(
        network_input,
        network_output,
        epochs=200,
        batch_size=128,
        callbacks=callbacks_list,
    )
    logging.info('Model Trained')


if __name__ == "__main__":
    train_network()
