
import tensorflow as tf
from config import CLUSTER, JOB_NAME

server = tf.train.Server(CLUSTER, job_name=JOB_NAME, task_index=1)
server.start()
server.join()
