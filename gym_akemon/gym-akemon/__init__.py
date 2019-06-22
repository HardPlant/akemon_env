from gym.envs.registration import register

register(
    id='akemon-v0',
    entry_point='gym_akemon.envs:AkemonEnv',
)
