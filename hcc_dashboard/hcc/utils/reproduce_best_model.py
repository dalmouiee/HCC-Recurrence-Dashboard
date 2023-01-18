"""
Script to reproduce a Neural network from Matlab into a Keras version
"""
import numpy as np
import tensorflow as tf
import pandas as pd

mystery_weights_32 = np.array(
    [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
    ]
)

mystery_weights_2 = np.array(
    [
        0.0,
        0.0,
    ]
)


def create_model_arch():
    model = tf.keras.Sequential()

    model.add(tf.keras.Input(shape=(20,)))
    model.add(tf.keras.layers.Dense(32, activation=tf.nn.tanh))
    model.add(tf.keras.layers.Dense(32, activation=tf.nn.tanh))
    model.add(tf.keras.layers.Dense(32, activation=tf.nn.tanh))
    model.add(tf.keras.layers.Dense(32, activation=tf.nn.tanh))
    model.add(tf.keras.layers.Dense(32, activation=tf.nn.tanh))
    model.add(tf.keras.layers.Dense(32, activation=tf.nn.tanh))
    model.add(tf.keras.layers.Dense(32, activation=tf.nn.tanh))
    model.add(tf.keras.layers.Dense(32, activation=tf.nn.tanh))
    model.add(tf.keras.layers.Dense(32, activation=tf.nn.tanh))
    model.add(tf.keras.layers.Dense(32, activation=tf.nn.tanh))
    model.add(tf.keras.layers.Dense(32, activation=tf.nn.tanh))
    model.add(tf.keras.layers.Dense(2, activation=tf.nn.sigmoid))

    return model


def set_model_weights(model):

    df_1_weights = pd.read_csv(
        "../data/input_layer_weights_1.csv", header=None
    ).T.to_numpy()
    df_2_weights = pd.read_csv(
        "../data/input_layer_weights_2.csv", header=None
    ).T.to_numpy()
    df_3_weights = pd.read_csv(
        "../data/input_layer_weights_3.csv", header=None
    ).T.to_numpy()
    df_4_weights = pd.read_csv(
        "../data/input_layer_weights_4.csv", header=None
    ).T.to_numpy()
    df_5_weights = pd.read_csv(
        "../data/input_layer_weights_5.csv", header=None
    ).T.to_numpy()
    df_6_weights = pd.read_csv(
        "../data/input_layer_weights_6.csv", header=None
    ).T.to_numpy()
    df_7_weights = pd.read_csv(
        "../data/input_layer_weights_7.csv", header=None
    ).T.to_numpy()
    df_8_weights = pd.read_csv(
        "../data/input_layer_weights_8.csv", header=None
    ).T.to_numpy()
    df_9_weights = pd.read_csv(
        "../data/input_layer_weights_9.csv", header=None
    ).T.to_numpy()
    df_10_weights = pd.read_csv(
        "../data/input_layer_weights_10.csv", header=None
    ).T.to_numpy()
    df_11_weights = pd.read_csv(
        "../data/input_layer_weights_11.csv", header=None
    ).T.to_numpy()
    df_12_weights = pd.read_csv(
        "../data/input_layer_weights_12.csv", header=None
    ).T.to_numpy()

    model.layers[0].set_weights([df_1_weights, mystery_weights_32])
    model.layers[1].set_weights([df_2_weights, mystery_weights_32])
    model.layers[2].set_weights([df_3_weights, mystery_weights_32])
    model.layers[3].set_weights([df_4_weights, mystery_weights_32])
    model.layers[4].set_weights([df_5_weights, mystery_weights_32])
    model.layers[5].set_weights([df_6_weights, mystery_weights_32])
    model.layers[6].set_weights([df_7_weights, mystery_weights_32])
    model.layers[7].set_weights([df_8_weights, mystery_weights_32])
    model.layers[8].set_weights([df_9_weights, mystery_weights_32])
    model.layers[9].set_weights([df_10_weights, mystery_weights_32])
    model.layers[10].set_weights([df_11_weights, mystery_weights_32])
    model.layers[11].set_weights([df_12_weights, mystery_weights_2])

    return model


def predict(model):
    result = model.predict(
        [[0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0]]
    )
    return result.tolist()


def pipeline():
    model = create_model_arch()
    model = set_model_weights(model)
    return predict(model)
