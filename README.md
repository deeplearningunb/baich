# Project B***AI***ch

B**_AI_**ch is a project that generates songs using LSTM Neural Networks in Python using the Keras library.

It's inspired on the great classical composer _Johan Sebastina Bach_.

## Contribute

If you want to contribute to our project, it's simple! We have a [Contribution Guide](docs/CONTRIBUTING.md) where all the steps to contribute are explained.
Don't forget to also read our [Code of Conduct](docs/CODE_OF_CONDUCT.md).
If you have any questions you can also contact us by creating an issue.

## Project Members

Isaque Alves  
Mariana Mendes  
João Pedro Sconetto  

## Requirements

* Python 3.x
* Installing the following packages using pip:
	* Music21
	* Keras
	* Tensorflow
	* h5py

## Dependencies

```shell
sudo apt-get install portaudio19-dev python3-pyaudio
```

## Training

To train the network you run **lstm.py**.

E.g.

```
python lstm.py
```

The network will use every midi file in ./assets/songs to train the network. The midi files should only contain a single instrument to get the most out of the training.

**NOTE**: You can stop the process at any point in time and the weights from the latest completed epoch will be available for text generation purposes.

## Generating music

Once you have trained the network you can generate text using **predict.py**

E.g.

```
python predict.py
```

## Known Errors

- music21 while reading mid files getting an decode error:

Check this correction: https://github.com/cuthbertLab/music21/pull/607/files

(intended for the next version but on version 6.1.0 this corrections is not present)
