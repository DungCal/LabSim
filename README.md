# LabSim: Learning Project Based on IsaacLab

## Overview

This project is a learning-focused clone of [IsaacLab](https://github.com/isaac-sim/IsaacLab), created to understand and practice robotic simulation and reinforcement learning concepts. It follows the structure and patterns of IsaacLab while providing a space for experimentation and learning.

**Learning Objectives:**

- Understanding NVIDIA Isaac Sim's robotics simulation capabilities
- Learning reinforcement learning implementation with various frameworks (skrl, RL Games, RSL-RL)
- Practicing robotic environment design and configuration
- Exploring both joint space and operational space control concepts

**Acknowledgment:**
This project is based on [IsaacLab](https://github.com/isaac-sim/IsaacLab) and is created purely for learning purposes. All credit for the original design and architecture goes to the IsaacLab developers.
## Prerequisites and Installation

1. Install Isaac Lab by following the [installation guide](https://isaac-sim.github.io/IsaacLab/main/source/setup/installation/index.html).
   We recommend using the conda installation method.

2. Clone this learning repository:
   ```bash
   git clone https://github.com/DungCal/LabSim.git
   cd LabSim
   ```

3. Install the packages in development mode:
   ```bash
   # use 'PATH_TO_isaaclab.sh|bat -p' instead of 'python' if Isaac Lab is not installed in Python venv or conda
   python -m pip install -e source/LabSim
   python -m pip install -e source/LabSim_tasks
   ```

## Learning Path

This repository is structured to help understand various aspects of robotics simulation and RL:

### 1. Basic Environment Verification

First, verify that everything is set up correctly:
```bash
# List available environments
python scripts/list_envs.py

# Try a basic test with random actions
python scripts/random_agent.py --task=LabSim-Reach-Franka-v0
```

### 2. Understanding Different Control Methods

Available test environments:
- Joint Position Control: `LabSim-Reach-Franka-v0`
- Inverse Kinematics (Absolute): `LabSim-Reach-Franka-IK-Abs-v0`
- Inverse Kinematics (Relative): `LabSim-Reach-Franka-IK-Rel-v0`
- Operational Space Control: `LabSim-Reach-Franka-OSC-v0`

### 3. Training with Different RL Frameworks

Try training with various RL frameworks:
```bash
# Training with skrl
python scripts/skrl/train.py --task LabSim-Reach-Franka-v0 --algorithm PPO --num_envs 2

# Training with RL Games (if available)
python scripts/rl_games/train.py --task LabSim-Reach-Franka-v0 --num_envs 2
```

### 4. Project Structure Study

The repository follows IsaacLab's structure for learning purposes:
```
source/
├── LabSim/            # Core functionality (similar to IsaacLab)
├── LabSim_tasks/      # Environment implementations
└── LabSim_assets/     # Robot and scene assets
```

## Educational Focus Areas

1. **Environment Design**
   - Understanding Gymnasium environment registration
   - Learning robot state and action spaces
   - Implementing reward functions

2. **Control Methods**
   - Joint space control implementation
   - Inverse kinematics solutions
   - Operational space control

3. **RL Integration**
   - Working with different RL frameworks
   - Understanding policy training
   - Hyperparameter tuning

## Development Setup

### IDE Setup (Recommended)

To set up VSCode for development:

1. Press `Ctrl+Shift+P`
2. Select `Tasks: Run Task`
3. Run `setup_python_env`
4. Provide the absolute path to your Isaac Sim installation when prompted

This creates a `.python.env` file in `.vscode` with proper Python paths for intelligent code suggestions.

### Code Formatting

We maintain IsaacLab's code quality standards using pre-commit:

```bash
# Install pre-commit
pip install pre-commit

# Run formatting
pre-commit run --all-files
```

## Troubleshooting

### Pylance Missing Indexing

If VSCode's Pylance has indexing issues, add to `.vscode/settings.json`:
```json
{
    "python.analysis.extraPaths": [
        "<path-to-ext-repo>/source/LabSim"
    ]
}
```

### Pylance Memory Issues

If Pylance crashes due to memory, exclude unused Omniverse packages in `.vscode/settings.json`:
```json
// Example packages to exclude:
"<path-to-isaac-sim>/extscache/omni.anim.*"         // Animation packages
"<path-to-isaac-sim>/extscache/omni.kit.*"          // Kit UI tools
"<path-to-isaac-sim>/extscache/omni.graph.*"        // Graph UI tools
"<path-to-isaac-sim>/extscache/omni.services.*"     // Services tools
```

## Disclaimer

This is a learning project that mimics IsaacLab's structure. It is not intended for production use but rather as a tool for understanding robotics simulation and reinforcement learning concepts.

## License

This project is licensed under the BSD-3-Clause License, following IsaacLab's licensing terms.
```