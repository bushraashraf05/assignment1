import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from collections import deque

# ---------------------------
# Environment
# ---------------------------
class Environment:
    def _init_(self, size=5, dirt_prob=0.3):
        self.size = size
        self.grid = [[1 if random.random() < dirt_prob else 0 for _ in range(size)] for _ in range(size)]
        self.agent_pos = [random.randint(0, size-1), random.randint(0, size-1)]

    def is_dirty(self, pos):
        x, y = pos
        return self.grid[x][y] == 1

    def clean(self, pos):
        x, y = pos
        self.grid[x][y] = 0

    def get_state(self):
        return (tuple(map(tuple, self.grid)), tuple(self.agent_pos))

# ---------------------------
# Base Agent
# ---------------------------
class Agent:
    def _init_(self):
        self.score = 0

    def act(self, env):
        raise NotImplementedError

# ---------------------------
# Simple Reflex Agent
# ---------------------------
class SimpleReflexAgent(Agent):
    def act(self, env):
        if env.is_dirty(env.agent_pos):
            env.clean(env.agent_pos)
            self.score += 10
            return "Suck"
        else:
            env.agent_pos[random.choice([0, 1])] += random.choice([-1, 1])
            env.agent_pos[0] = max(0, min(env.size-1, env.agent_pos[0]))
            env.agent_pos[1] = max(0, min(env.size-1, env.agent_pos[1]))
            self.score -= 1
            return "Move"

# ---------------------------
# Model-Based Agent
# ---------------------------
class ModelBasedAgent(Agent):
    def _init_(self, size):
        super()._init_()
        self.visited = set()
        self.size = size

    def act(self, env):
        pos = tuple(env.agent_pos)
        if env.is_dirty(pos):
            env.clean(pos)
            self.visited.add(pos)
            self.score += 10
            return "Suck"
        else:
            x, y = pos
            moves = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
            random.shuffle(moves)
            for nx, ny in moves:
                if 0 <= nx < self.size and 0 <= ny < self.size and (nx, ny) not in self.visited:
                    env.agent_pos = [nx, ny]
                    self.score -= 1
                    return "Move"
            env.agent_pos[random.choice([0, 1])] += random.choice([-1, 1])
            env.agent_pos[0] = max(0, min(env.size-1, env.agent_pos[0]))
            env.agent_pos[1] = max(0, min(env.size-1, env.agent_pos[1]))
            self.score -= 1
            return "Move"

# ---------------------------
# Goal-Based Agent
# ---------------------------
class GoalBasedAgent(Agent):
    def _init_(self, env):
        super()._init_()
        self.env = env

    def find_nearest_dirty(self, start):
        q = deque([(start, [])])
        visited = set([start])
        while q:
            pos, path = q.popleft()
            x, y = pos
            if self.env.is_dirty(pos):
                return path
            for nx, ny in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
                if 0 <= nx < self.env.size and 0 <= ny < self.env.size and (nx, ny) not in visited:
                    q.append(((nx, ny), path + [(nx, ny)]))
                    visited.add((nx, ny))
        return []

    def act(self, env):
        pos = tuple(env.agent_pos)
        if env.is_dirty(pos):
            env.clean(pos)
            self.score += 10
            return "Suck"
        else:
            path = self.find_nearest_dirty(pos)
            if path:
                env.agent_pos = list(path[0])
            else:
                env.agent_pos[random.choice([0, 1])] += random.choice([-1, 1])
            env.agent_pos[0] = max(0, min(env.size-1, env.agent_pos[0]))
            env.agent_pos[1] = max(0, min(env.size-1, env.agent_pos[1]))
            self.score -= 1
            return "Move"

# ---------------------------
# Learning Agent (Q-Learning)
# ---------------------------
class LearningAgent(Agent):
    def _init_(self, env, alpha=0.5, gamma=0.9, epsilon=0.2):
        super()._init_()
        self.q = {}
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.env = env

    def get_q(self, state, action):
        return self.q.get((state, action), 0.0)

    def choose_action(self, state):
        actions = ["Up", "Down", "Left", "Right", "Suck"]
        if random.random() < self.epsilon:
            return random.choice(actions)
        q_vals = [self.get_q(state, a) for a in actions]
        max_q = max(q_vals)
        return actions[q_vals.index(max_q)]

    def update_q(self, state, action, reward, next_state):
        max_q_next = max([self.get_q(next_state, a) for a in ["Up", "Down", "Left", "Right", "Suck"]])
        old_q = self.get_q(state, action)
        self.q[(state, action)] = old_q + self.alpha * (reward + self.gamma * max_q_next - old_q)

    def act(self, env):
        state = env.get_state()
        action = self.choose_action(state)
        reward = -1

        if action == "Suck":
            if env.is_dirty(env.agent_pos):
                env.clean(env.agent_pos)
                reward = 10
        else:
            x, y = env.agent_pos
            if action == "Up" and x > 0: x -= 1
            elif action == "Down" and x < env.size-1: x += 1
            elif action == "Left" and y > 0: y -= 1
            elif action == "Right" and y < env.size-1: y += 1
            env.agent_pos = [x, y]

        next_state = env.get_state()
        self.update_q(state, action, reward, next_state)
        self.score += reward
        return action

# ---------------------------
# Visualization
# ---------------------------
def draw_env(env, step, action, agent_type, score):
    plt.clf()
    ax = plt.gca()
    for i in range(env.size):
        for j in range(env.size):
            color = 'red' if env.grid[i][j] == 1 else 'lightblue'
            ax.add_patch(patches.Rectangle((j, env.size-1-i), 1, 1, facecolor=color, edgecolor='black'))
    ax.add_patch(patches.Rectangle((env.agent_pos[1], env.size-1-env.agent_pos[0]), 1, 1, facecolor='black'))
    plt.xlim(0, env.size)
    plt.ylim(0, env.size)
    plt.title(f"{agent_type} | Step: {step}, Action: {action}, Score: {score}")
    plt.pause(0.3)

def run_with_visualization(env, agent, steps=30, agent_type="Agent"):
    plt.figure(figsize=(6,6))
    for step in range(steps):
        action = agent.act(env)
        draw_env(env, step, action, agent_type, agent.score)
    plt.show()

# ---------------------------
# Run Example
# ---------------------------
if _name_ == "_main_":
    env = Environment(size=5, dirt_prob=0.4)

    # agent = SimpleReflexAgent()
    # agent = ModelBasedAgent(env.size)
    # agent = GoalBasedAgent(env)
    agent = LearningAgent(env)

    run_with_visualization(env, agent, steps=30, agent_type=agent._class.name_)