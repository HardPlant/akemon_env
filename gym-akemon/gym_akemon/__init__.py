from gym.envs.registration import register

register(
    id='akemon-v1',
    entry_point='gym_akemon.envs:AkemonEnv',
)
