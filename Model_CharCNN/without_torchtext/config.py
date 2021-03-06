# config.py

class Config(object):
    num_channels = 256
    linear_size = 256
    output_size = 4
    max_epochs = 10
    lr = 0.001
    batch_size = 128
    vocab_size = 68
    max_len = 300 # 1014 in original paper
    dropout_keep = 0.5