hyperparams = {
    "seals/HalfCheetah-v0": dict(
        n_timesteps=1000000.0,
        policy="MlpPolicy",
        learning_starts=10000,
        noise_type="normal",
        noise_std=0.1,
    ),
    "seals/Ant-v0": dict(
        n_timesteps=1000000.0,
        policy="MlpPolicy",
        learning_starts=10000,
        noise_type="normal",
        noise_std=0.1,
    ),
    "seals/Hopper-v0": dict(
        n_timesteps=1000000.0,
        policy="MlpPolicy",
        learning_starts=10000,
        noise_type="normal",
        noise_std=0.1,
    ),
    "seals/Walker2d-v0": dict(
        n_timesteps=1000000.0,
        policy="MlpPolicy",
        learning_starts=10000,
        noise_type="normal",
        noise_std=0.1,
    ),
    "seals/Humanoid-v0": dict(
        n_timesteps=2000000.0,
        policy="MlpPolicy",
        learning_starts=10000,
        noise_type="normal",
        noise_std=0.1,
    ),
    "seals/Swimmer-v0": dict(
        n_timesteps=1000000.0,
        policy="MlpPolicy",
        learning_starts=10000,
        noise_type="normal",
        noise_std=0.1,
        gamma=0.9999,
        train_freq=1,
        gradient_steps=1,
    ),
}
