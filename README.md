# Lichess Analyzer

This is a project to enable you to analyze your chess games on lichess.

The easiest way is to use the [analyze notebook](./lichess_analyzer/notebook/analyze.ipynb)

## Usage

### Set Up poetry environment

To set up the poetry environment, follow these steps:

1. **Install Python**: If you haven't installed python 3.12 or later, you can do so by following the instructions on the [Download Python page](https://www.python.org/downloads/).

2. **Install Poetry**: If you haven't installed Poetry yet, you can do so by following the instructions on the [Poetry installation page](https://python-poetry.org/docs/#installation). e.g.

  ```sh
  pip install poetry
  ```

3. **Install Dependencies**: Navigate to the project directory and run the following command to install the dependencies:

  ```sh
  poetry install
  ```

4. **Using the Environment in Jupyter Notebook**: Ensure that your Jupyter Notebook is using the Poetry environment's kernel. You can do this by selecting the appropriate kernel from the Jupyter interface.

Now you are ready to use the Lichess Analyzer in your Jupyter Notebook.

### API Token

In order to use the lichess API, you need a token.

You can generate your own one on [https://lichess.org/account/oauth/token](https://lichess.org/account/oauth/token).  
The token does not need any write access, the default token configuration is enough.

You can enter your token in in a file called `api_token.txt` so that is less likely to be shared involuntarily as txt files are in `.gitignore`.

### Run the notebook

1. Enter your personal data in the settings segment
2. Run the notebook to get a number of analyzes. Each analyze will be provided as file next to the notebook.

### Costumizations

If you got your own opening preferences you can define them yourself and use the available functionalities to get your personal analyzis.

Check out the notebook for further information.

## Pre Commit Hooks

This project tries to prevent you from sharing your token by using pre-commit.

In order for this mechanism to be effective you need to:

- Install pre-commit on your system, e.g. `pip install pre-commit`
- Run `pre-commit install` within this project
