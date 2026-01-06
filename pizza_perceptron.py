import random

class SimpleBrain:
    def __init__(self):
        # 1. WEIGHTS: Initialized randomly
        # In software, these are just float variables.
        self.weight_round = random.uniform(-1, 1)
        self.weight_red   = random.uniform(-1, 1)
        
        # THRESHOLD (Bias): The "trigger point"
        self.threshold = 1.0 
        self.learning_rate = 0.11 # How much we change weights per mistake

    def think(self, is_round, is_red):
        # 2. THE FORMULA (Sum of Inputs * Weights)
        score = (is_round * self.weight_round) + (is_red * self.weight_red)
        
        # 3. THE THRESHOLD CHECK
        if score > self.threshold:
            return 1 # Yes, it's Pizza
        else:
            return 0 # No, not Pizza

    def train(self, is_round, is_red, correct_answer):
        # Make a guess
        guess = self.think(is_round, is_red)
        
        # Calculate Error (Difference between Truth and Guess)
        error = correct_answer - guess
        
        if error != 0:
            # 4. WEAKEN OR STRENGTHEN
            # If error is +1 (Missed a pizza), we add (Strengthen)
            # If error is -1 (False alarm), we subtract (Weaken)
            
            self.weight_round += error * is_round * self.learning_rate
            self.weight_red   += error * is_red   * self.learning_rate
            
            print(f"   Mistake! Adjusting weights... New Round W: {self.weight_round:.2f}, New Red W: {self.weight_red:.2f}")
        else:
            print("   Correct!")

# --- LET'S RUN IT ---

brain = SimpleBrain()

# Training Data: [Round, Red, Is_Pizza?]
dataset = [
    [1, 1, 1], # Pizza (Round, Red) -> YES
    [0, 1, 0], # Apple (Not Round, Red) -> NO
    [1, 0, 0], # Coin (Round, Not Red) -> NO
    [0, 0, 0]  # Rock (Not Round, Not Red) -> NO
]

print("--- Start Training ---")
for epoch in range(5): # Loop through data 5 times
    print(f"Epoch {epoch+1}")
    for data in dataset:
        round, red, answer = data
        print(f" Showing: Round={round}, Red={red}...", end="")
        brain.train(round, red, answer)
    print("-" * 20)

print("\n--- Final Test ---")
print(f"Is a Round, Red object a pizza? AI says: {brain.think(1, 1)}")