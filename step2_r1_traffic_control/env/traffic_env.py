import random

class TrafficEnv:
    def __init__(self):
        self.max_cars = 20
        self.state = self.reset()

    def reset(self):
        self.state = {
            "road_A": random.randint(0, self.max_cars),
            "road_B": random.randint(0, self.max_cars)
        }
        return self.state

    def step(self, action):
        """
        action: 0 -> Green for road A
                1 -> Green for road B
        """
        if action == 0:
            self.state["road_A"] = max(0, self.state["road_A"] - random.randint(1, 5))
            self.state["road_B"] += random.randint(0, 2)
        else:
            self.state["road_B"] = max(0, self.state["road_B"] - random.randint(1, 5))
            self.state["road_A"] += random.randint(0, 2)

        waiting_time = self.state["road_A"] + self.state["road_B"]
        reward = -waiting_time  # minimize waiting time

        return self.state, reward
