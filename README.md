# Project B***AI***ch

B**_AI_**ch is a project that generates songs using LSTM Neural Networks in Python using the Keras library.

The name is inspired on the great classical composer _Johann Sebastian Bach_.

All the songs used in the dataset are from [VGMusic](https://www.vgmusic.com/) and are creative common or public domain. It includes 100 songs used for training and validation.

## Contribute

If you want to contribute to our project, it's simple! We have a [Contribution Guide](docs/CONTRIBUTING.md) where all the steps to contribute are explained.
Don't forget to also read our [Code of Conduct](docs/CODE_OF_CONDUCT.md).
If you have any questions you can also contact us by creating an issue.

## Project Members

| Name | Registry |
| --- | --- |
| Isaque Alves | 14/0144544 |
| Mariana Mendes | 14/0154027 |
| João Pedro Sconetto | 14/0145940 |

## Requirements

* Python 3.x (Python 3.8 is recommended)
* Installing the following packages using pip:
	* Music21
	* Keras
	* Tensorflow
	* h5py

## External Dependencies

Some libraries are required for the base requirements to work properly. To install them run the following command (command for Debian based distro/linux):

```shell
sudo apt-get install portaudio19-dev python3-pyaudio
```

## Usage

### Training Model

To train the network you need to run the **lstm.py** file (make sure to have dependencies and your environment set as shown on `Development`).

```shell
python src/lstm.py
```

The network will use every MIDI file in `assets/songs` to train the network. The MIDI files should only contain a single instrument to get the most out of the training.

**NOTE**: You can stop the process at any point in time and the weights from the latest completed epoch will be available.

When you're satisfied with the loss of the AI select the weight you want to be use to predict and generate songs and rename it to `weights.hdf5` and leave it at `assets/weights`.

### Generating Music

Once you have trained the network you can generate text using **predict.py** file. Run the following command (make sure to have dependencies and your environment set as shown on `Development`).

```shell
python src/predict.py
```

### Known Errors

- music21 while reading mid files getting an decode error:

Check this correction: https://github.com/cuthbertLab/music21/pull/607/files

(intended for the next version but on version 6.1.0 this corrections is not present)

## Development

### Installing VirtualEnvWrapper

We recommend using a virtual environment created by the __virtualenvwrapper__ module. There is a virtual site with English instructions for installation that can be accessed [here](https://virtualenvwrapper.readthedocs.io/en/latest/install.html). But you can also follow these steps below for installing the environment:

```shell
sudo python3 -m pip install -U pip             # Update pip
sudo python3 -m pip install virtualenvwrapper  # Install virtualenvwrapper module
```

**Observation**: If you do not have administrator access on the machine remove `sudo` from the beginning of the command and add the flag `--user` to the end of the command.

Now configure your shell to use **virtualenvwrapper** by adding these two lines to your shell initialization file (e.g. `.bashrc`, `.profile`, etc.)

```shell
export WORKON_HOME=\$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
```

If you want to add a specific project location (will automatically go to the project folder when the virtual environment is activated) just add a third line with the following `export`:

```shell
export PROJECT_HOME=/path/to/project
```

Run the shell startup file for the changes to take effect, for example:

```shell
source ~/.bashrc
```

Now create a virtual environment with the following command (entering the name you want for the environment), in this example I will use the name **baich**:

```shell
mkvirtualenv -p $(which python3) baich
```

To use it:

```shell
workon baich
sudo python3 -m pip install pipenv
pipenv install # Will install all of the project dependencies
# or
pip install -r requirements.txt
```

**Observaion**: Again, if necessary, add the flag `--user` to make the pipenv package installation for the local user.

### Local Execution

For local system execution, run the following command in the project root folder (assuming virtualenv is already active):

```shell
python src/lstm.py
```

This will train and run the system on your machine. This way you can test new implementations or new optmizations. Also you can create songs for testing.

### Test

#### Lint

To lint your code follow the script bellow:

1. Enable virtualenv _baich_;

2. Ensure that the dependencies are installed, especially:

```code
black
flake8
```

3. Run the command below:

```shell
black src/*
flake8 --ignore E501 src
```

During the lint process the terminal will report a code errors and warnings from the PEP8 style guide, for more configurations and additional documentation go to [flake8](http://flake8.pycqa.org/en/latest/) and [PEP8](https://www.python.org/dev/peps/pep-0008/).
The rule `E501` (Line too long) is ignored because the base linter is black and not PEP8.

## Build

### Generate Changelog

To generate changelog we use the `standard version` tool, it will auto generate a new changelog for every new release by using the commit messages. To generate a new release and generate the updated changelog just do the following steps:

1. Install all dependencies

```shell
yarn install
```

2. Run standard version:

```shell
yarn run release
```

If the release is a pre-release you should add the `--prerelease` to the command:

```shell
yarn run release -- --prerelease alpha
```

For further instructions or other options check the full documentation of `standard version` project in the [CLI Usage](https://github.com/conventional-changelog/standard-version#cli-usage) section.

## References

Skúli, Sigurður (Dec, 2017). How to Generate Music using a LSTM Neural Network in Keras. Towards Data Science. Access date: 10 Nov 2020. Available at <https://towardsdatascience.com/how-to-generate-music-using-a-lstm-neural-network-in-keras-68786834d4c5>
