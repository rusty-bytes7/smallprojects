#this is the main file for the Rusty MDP project
import copy

def main():
    print("Welcome to the Rusty MDP!")
    print("This is a simple implementation of a Markov Decision Process (MDP) in Python.")
    print("Rusty is a virtual pet that has various needs and can perform actions to satisfy those needs.")
    #initialize the MDP components here
    #states
    rusty_states = [#living room states
                    "tired_living_room",
                    "rested_living_room",
                    "hungry_living_room",
                    "fed_living_room",
                    "needs_bathroom_living_room",
                    "relieved_living_room",
                    "wants_attention_living_room",
                    "happy_living_room",
                    #kitchen states
                    "tired_kitchen",
                    "rested_kitchen",
                    "hungry_kitchen",
                    "fed_kitchen",
                    "needs_bathroom_kitchen",
                    "relieved_kitchen",
                    "wants_attention_kitchen",
                    "happy_kitchen",
                    #bedroom states
                    "tired_bedroom",
                    "rested_bedroom",
                    "hungry_bedroom",
                    "fed_bedroom",
                    "needs_bathroom_bedroom",
                    "relieved_bedroom",
                    "wants_attention_bedroom",
                    "happy_bedroom",]
    #actions
    rusty_actions = ["eat", "go_to_bathroom", "play", "sleep", "groom", "wait"]

    #transition model
    def build_rusty_transition_function(states, actions):
        transitions = {}

        for state in states:
            room = state.split('_')[-1]  #'bedroom', 'kitchen', or 'living_room'

            for action in actions:
                key = (state, action)
                next_states = []

                #sleep
                if action == "sleep":
                    if "tired" in state:
                        next_state = state.replace("tired", "rested")
                        next_states.append((next_state, 0.7))  #mostly successful
                        next_states.append((state, 0.3))       #sometimes stays tired
                    else:
                        next_states.append((state, 1.0))

                #eat
                elif action == "eat":
                    if "hungry" in state:
                        next_state = state.replace("hungry", "fed")
                        next_states.append((next_state, 1.0))
                    else:
                        next_states.append((state, 1.0))

                #go_to_bathroom
                elif action == "go_to_bathroom":
                    if "needs_bathroom" in state:
                        next_state = state.replace("needs_bathroom", "relieved")
                        if "bedroom" in state:
                            #penalty: only 30% chance success in bedroom
                            next_states.append((next_state, 0.6))
                            next_states.append((state, 0.4)) #40% chance of failure
                        else:
                            next_states.append((next_state, 1.0))
                    else:
                        next_states.append((state, 1.0))

                #play
                elif action == "play":
                    if "wants_attention" in state:
                        next_state = state.replace("wants_attention", "happy")
                        next_states.append((next_state, 0.8))
                    else:
                        next_states.append((state, 0.2))
                #groom
                elif action == "groom":
                    #rusty just stays in the same state
                    next_states.append((state, 1.0))

                #wait
                elif action == "wait":
                    next_states.append((state, 1.0))


                transitions[key] = next_states

        return transitions


    #reward model
    def build_rusty_reward_function(states, actions, transitions):
        rewards = {}

        for state in states:
            for action in actions:
                next_states = transitions.get((state, action), [])
                for s_prime, prob in next_states:
                    reward = 0

                    #Satisfying hunger
                    if "hungry" in state and action == "eat":
                        reward += 100
                    elif "hungry" in state and action != "eat":
                        reward += -20

                    #Satisfying tiredness
                    if "tired" in state and action == "sleep":
                        reward += 90
                    elif "tired" in state and action != "sleep":
                        reward += -15

                    #Satisfying bathroom needs
                    if "needs_bathroom" in state and action == "go_to_bathroom":
                        if "bedroom" in state:
                            reward += -100 #Penalty for attempting bathroom in bedroom- naughty Rusty!
                        elif "relieved" in s_prime:
                            reward += 30
                    elif "needs_bathroom" in state and action != "go_to_bathroom":
                        reward += -20

                    #Satisfying attention
                    if "wants_attention" in state and action == "play":
                        if "happy" in s_prime:
                            reward += 66
                    elif "wants_attention" in state and action != "play":
                        reward += -25

                    #No particular needs
                    if all(x not in state for x in ["hungry", "tired", "needs_bathroom", "wants_attention"]):
                        if action == "groom":
                            reward += 35

                    #Waiting penalty if Rusty has needs
                    if any(x in state for x in ["hungry", "tired", "needs_bathroom", "wants_attention"]) and action == "wait":
                        reward += -16

                    rewards[(state, action, s_prime)] = reward

        return rewards


    #build the transition and reward functions
    rusty_transition_function = build_rusty_transition_function(rusty_states, rusty_actions)
    rusty_reward_function = build_rusty_reward_function(rusty_states, rusty_actions, rusty_transition_function)

    #value iteration using the transition and reward functions
    gamma = 0.9  #Discount factor

    #utility function for value iteration
    def value_iteration(states, actions, transition_probs, rewards, gamma, threshold=0.01):
        utilities = {s: 0 for s in states}
        while True:
            delta = 0
            new_utilities = copy.deepcopy(utilities)
            for s in states:
                action_values = []
                for a in actions:
                    transitions = transition_probs.get((s, a), [])
                    value = 0
                    for s_prime, prob in transitions:
                        reward = rewards.get((s, a, s_prime), 0)
                        value += prob * (reward + gamma * utilities[s_prime])
                    action_values.append(value)
                if action_values:
                    new_utilities[s] = max(action_values)
                    delta = max(delta, abs(new_utilities[s] - utilities[s]))
            utilities = new_utilities
            if delta < threshold:
                break
        return utilities

    utilities = value_iteration(rusty_states, rusty_actions, rusty_transition_function, rusty_reward_function, gamma)
    rounded_utilities = {k: round(v, 2) for k, v in utilities.items()}
    
    #create the policy based on the utilities
    def extract_policy(states, actions, utilities, transition_probs, rewards, gamma):
        policy = {}
        for s in states:
            best_action = None
            best_value = float("-inf")
            for a in actions:
                value = 0
                for s_prime, prob in transition_probs.get((s, a), []):
                    reward = rewards.get((s, a, s_prime), 0)
                    value += prob * (reward + gamma * utilities[s_prime])
                if value > best_value:
                    best_value = value
                    best_action = a
            policy[s] = best_action
        return policy

    policy = extract_policy(rusty_states, rusty_actions, rounded_utilities, rusty_transition_function, rusty_reward_function, gamma)
    print("Policy:", policy)
    import matplotlib.pyplot as plt

    # Assuming you have your 'utilities' dictionary
    rooms = ["living_room", "kitchen", "bedroom"]
    states_by_room = {room: [] for room in rooms}
    for state in utilities:
        for room in rooms:
            if room in state:
                states_by_room[room].append((state, utilities[state]))

    # Plot utilities per room
    for room in rooms:
        labels = [s[0] for s in states_by_room[room]]
        values = [s[1] for s in states_by_room[room]]
        plt.figure(figsize=(8, 2))
        plt.barh(labels, values)
        plt.title(f"Utility Values in {room.capitalize()}")
        plt.xlabel("Utility")
        plt.tight_layout()
        plt.show()


main()