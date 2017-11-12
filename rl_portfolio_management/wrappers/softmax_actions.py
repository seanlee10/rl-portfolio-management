import gym.wrappers

from ..util import softmax


class SoftmaxActions(gym.Wrapper):
    """
    Environment wrapper to softmax actions.

    Usage:
        env = gym.make('Pong-v0')
        env = SoftmaxActions(env)

    Ref: https://github.com/openai/gym/blob/master/gym/wrappers/README.md

    """

    def step(self, action):
                # also it puts it in a list
        if isinstance(action, list):
            action = action[0]

        if isinstance(action, dict):
            action = list(action[k] for k in sorted(action.keys()))

        action = softmax(action, t=1)

        observation, reward, done, info = self.env.step(action)

        return observation, reward, done, info
