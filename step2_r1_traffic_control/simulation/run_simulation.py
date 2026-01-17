from env.traffic_env import TrafficEnv
from agent.q_learning_agent import QLearningAgent

env = TrafficEnv()
agent = QLearningAgent()

episodes = 50

for episode in range(episodes):
    state = env.reset()
    total_reward = 0

    for step in range(20):
        action = agent.choose_action(state)
        next_state, reward = env.step(action)
        agent.update(state, action, reward, next_state)

        state = next_state
        total_reward += reward

    print(f"Episode {episode+1}, Total Reward: {total_reward}")
