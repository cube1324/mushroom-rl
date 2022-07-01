try:
    from mushroom_rl.environments.pybullet_envs.air_hockey import AirHockeyDefend
    import numpy as np
    obs = []
    mdp = AirHockeyDefend()
    mdp.reset()
    action = np.array([1] * 3)

    for _ in range(20):
        observation, _, _, _ = mdp.step(action)
        assert len(observation) == len(mdp._mdp_info.observation_space.low)
        assert len(observation) == len(mdp._mdp_info.observation_space.high)
        obs.append(observation)

    obs_test = np.load("defend_data.npy")

    assert np.allclose(obs, obs_test)

except ImportError:
    pass
