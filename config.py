# training set-up
train_config = {
    'url_file_path': '/home/joe/Research/generalized_filtering/data/youtube_8m_urls/Science.txt',
    'save_dir': '/media/joe/SSD/datasets/temp',
    'encoder_learning_rate': 0.0002,
    'decoder_learning_rate': 0.0002,
    'kl_min': 0,
    'cuda_device': 1,
    'display_iter': 10,
    'resume_experiment_dir': None
}

# model architecture
model_config = {
    'encoding_form': ['posterior'],
    'concat_levels': True,
    'transform_input': False,
    'constant_prior_variances': True,
    'learn_top_prior': False,

    'output_distribution': 'gaussian',

    'normalizing_flows': True,

    'n_latent': [128],

    'n_det_enc': [0],
    'n_det_dec': [0],

    'n_layers_enc': [2, 0],
    'n_layers_dec': [2, 1],

    'n_units_enc': [1024, 0],
    'n_units_dec': [1024, 1],

    'non_linearity_enc': 'elu',
    'non_linearity_dec': 'elu',

    'connection_type_enc': 'sequential',
    'connection_type_dec': 'sequential',

    'batch_norm_enc': False,
    'batch_norm_dec': False,

    'weight_norm_enc': False,
    'weight_norm_dec': False,

    'dropout_enc': 0.0,
    'dropout_dec': 0.0
}
