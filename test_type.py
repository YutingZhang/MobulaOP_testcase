import mobula
mobula.op.load('./some_op')

import mxnet as mx
a = mx.nd.array([1,2,3], dtype='float32')
b = mx.nd.array([2,3,4], dtype='int32')
c = mx.nd.array([0,0,0], dtype='float32')

@mobula.op.register
class SomeOP:
    def forward(self, x, y):
        mobula.func.some_op(x.size, x, y, self.y)
    def backward(self, dy):
        return [0, 0]
    def infer_shape(self, in_shape):
        return in_shape, [in_shape[0]]

# mobula.func.some_op(a.size, a, b, c)
c = SomeOP(a, b)
print (c)
