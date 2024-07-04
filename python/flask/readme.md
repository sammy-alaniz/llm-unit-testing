# Flask:

When writing tests in python it usually requires a suite of other files to support the test. In order to have reporduceable results we've created a fork of the flask repo, named `test-flask`. The branch is named `llm-research`. Link is below,

Link : `https://github.com/sammy-alaniz/test-flask`

The original tests are located in the `test` directory. Our new tests will be written in the `llm-research` directory. This will allow us to compare our results vs the current standard of testing available.


### How to run original tests:

1. Run `python3 -m venv env`
2. Run `source env/bin/activate`
3. Run `pip install -e .`
4. Run `pip install pytest`
5. Run `pytest test/`


### How to run llm-research tests:

1. Run `python3 -m venv env`
2. Run `source env/bin/activate`
3. Run `pip install -e .`
4. Run `pip install pytest`
5. Run `pytest llm-research/`