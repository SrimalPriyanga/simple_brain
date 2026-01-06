# The Perceptron: From 1958 Theory to Python Code

This repository contains a practical, scratch-built implementation of the Perceptron algorithm, inspired by Frank Rosenblatt's groundbreaking 1958 paper, **"The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain."**

The goal of this project is to demystify how early Artificial Intelligence was conceptualized as a biological learning process rather than rigid logic, and to demonstrate these mechanics using simple Python code.

## 🧠 Theoretical Background

In 1958, Frank Rosenblatt proposed a radical shift in how we view computing. Rather than treating the brain as a logic machine (storing files and rules), he theorized it as a probabilistic system that learns through **connection strength**.

Key concepts from the paper implemented here:

* **Connectionism:** Information is stored in the *weights* of connections between neurons, not in specific memory cells.
* **The Learning Algorithm:** The system starts with random connections. When it makes a mistake, it adjusts (strengthens or weakens) the weights of the active inputs to correct future errors.
* **Thresholds:** A neuron only "fires" (outputs a decision) if the sum of its weighted inputs exceeds a specific threshold.

## 🍕 The "Pizza Detector" Implementation

To demonstrate Rosenblatt's theory, this repository includes a `pizza_perceptron.py` script. It trains a single neuron to distinguish "Pizza" from other objects based on two sensory inputs.

### How the Code Maps to Theory

| Rosenblatt's Concept | In Python Code | Description |
| --- | --- | --- |
| **Synaptic Weights** | `self.weight_round`, `self.weight_red` | Variables that determine importance of inputs. |
| **Sensory Units (S-Points)** | `is_round`, `is_red` | Input data (0 or 1) simulating retina sensors. |
| **Response Unit (R-Unit)** | `def think(self)` | The decision-making function. |
| **Threshold** | `if score > self.threshold:` | The activation barrier for a "Yes" decision. |
| **Reinforcement** | `+= error * learning_rate` | Strengthening or weakening connections based on error. |

### The Logic

The brain utilizes a simple mathematical formula to mimic the biological process described in the paper:

```python
Output = (Input_A * Weight_A) + (Input_B * Weight_B)

```

If the `Output > Threshold`, the Perceptron fires (returns 1). If the guess is wrong, the weights are mathematically adjusted via the **Backpropagation** of error (the "Learning" phase).

## 🚀 How to Run

1. Clone this repository:
```bash
git clone https://github.com/yourusername/perceptron-demo.git

```


2. Run the script (No external libraries required):
```bash
python pizza_perceptron.py

```



## 📊 Sample Output

You will see the "Brain" evolve from making random guesses to perfect accuracy over 5 epochs (learning cycles):

```text
--- Start Training ---
Epoch 1
 Showing: Round=1, Red=1...   Mistake! Adjusting weights...
 Showing: Round=0, Red=1...   Correct!
...
Epoch 5
 Showing: Round=1, Red=1...   Correct!
 
--- Final Test ---
Is a Round, Red object a pizza? AI says: 1

```

## 📚 References

* **Original Paper:** Rosenblatt, F. (1958). *The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain.* Psychological Review, 65(6), 386–408. [Link to Paper](https://www.ling.upenn.edu/courses/cogs501/Rosenblatt1958.pdf)

---

*This project is for educational purposes to illustrate the fundamentals of Neural Networks.*