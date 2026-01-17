import random

class QLearningAgent:
    def __init__(self):
        self.q_table = {}
        self.alpha = 0.1     # learning rate
        self.gamma = 0.9     # discount factor
        self.epsilon = 0.2   # exploration rate

    def get_state_key(self, state):
        return (state["road_A"], state["road_B"])

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.choice([0, 1])

        state_key = self.get_state_key(state)
        self.q_table.setdefault(state_key, [0, 0])
        return self.q_table[state_key].index(max(self.q_table[state_key]))

    def update(self, state, action, reward, next_state):
        state_key = self.get_state_key(state)
        next_key = self.get_state_key(next_state)

        self.q_table.setdefault(state_key, [0, 0])
        self.q_table.setdefault(next_key, [0, 0])

        self.q_table[state_key][action] += self.alpha * (
            reward + self.gamma * max(self.q_table[next_key])
            - self.q_table[state_key][action]
        )
