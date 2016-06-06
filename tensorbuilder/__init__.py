# Init code
import tensorflow as tf
from tensorbuilder import *
import nn
import builder_nn
from decorator import decorator

#version
__version__ = "0.0.1"


# Monkey Patch TensorFlow
tf.python.framework.ops.Tensor.builder = builder


import tensorbuilder
__all__ = ["tensorbuilder", "nn", "builder_nn"]
