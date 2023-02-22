# HCC-Recurrence-Dashboard
A package to deploy a dashboard to utilise the model described in the [publication](https://github.com/VafaeeLab/HCC-Recurrence) *"Artificial intelligence reliably identifies patients at risk of HCC recurrence one-year post-surgical resection"*.

You can access the official dashboard here: https://vafaeelab.pythonanywhere.com/hcc/

[![HCC dashboard Pylint and tests Validation](https://github.com/dalmouiee/HCC-Recurrence-Dashboard/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/dalmouiee/HCC-Recurrence-Dashboard/actions/workflows/tests.yml)
# How to run
1. Export the weights from the matlab model into CSV files and lace them into the data directory, with each file labelled appropriately according to the code
2. Install the python dependencies in `reqs.txt`, using the command `pip install -r reqs.txt`. (Note: this was developed using python 3.10.4 and using a virtual environment).
3. The install the database tables used to run the app, run `python manage.py migrate`
4. To run a local version of the dashboard (Eg. for development/testing purposes), run `python manage.py runserver`

# Authors:
 - ## [Daniel Al Mouiee](https://github.com/dalmouiee)
 - ## [Sasha Barisic](https://github.com/Sasha-Barisic)
