import tensorflow as tf

a_1 = tf.constant(2)
b_1 = tf.constant(3)
c_1 = tf.constant(4)
a_2 = tf.placeholder(tf.int32, [3])
b_2 = tf.constant(2)
a_3 = tf.placeholder(tf.int32, [None])
b_3 = tf.constant(10)

add_op = a_1 + b_1
clac1_op = a_1 + b_1 + c_1
clac2_op = (a_1 + b_1) * c_1
x2_op = a_2 * b_2
x10_op = a_3 * b_3
d2_op = a_3 / b_3

sess = tf.Session()
res1_1 = sess.run(clac1_op)
res2_1 = sess.run(clac2_op)
res1_2 = sess.run(x2_op, feed_dict = {a_2 : [1, 2, 3]})
res2_2 = sess.run(x2_op, feed_dict = {a_2 : [10, 20, 10]})
res1_3 = sess.run(x10_op, feed_dict = {a_3 : [1, 2, 3, 4, 5]})
res2_3 = sess.run(x10_op, feed_dict = {a_3 : [10, 20]})
res3_3 = sess.run(d2_op, feed_dict = {a_3 : [1, 2, 3, 4, 5]})
# print(res1_1)
# print(res2_1)
# print(res1_2)
# print(res2_2)
print(res1_3)
print(res2_3)
print(res3_3)