# neural-network-matlab-to-python
A package to facilitate the conversion of Matlab Neural Network models to Python using the ONNX model.

# How to run
1. Export the weights from the matlab model into CSV files and lace them into the data directory, with each file labelled appropriately according to the code
2. Install the python dependencies in `reqs.txt`, using the command `pip install -r reqs.txt`. (Note: this was developed using python 3.10.4 and using a virtual environment).
3. To run the script: `python reproduce_best_model.py`
