# Fuzzy Self-Driving Car Simulator

## Overview
The Fuzzy Self-Driving Car Simulator is a project designed to simulate the decision-making processes of an autonomous vehicle using fuzzy logic. The simulator emulates real-world driving conditions, focusing on the development and optimization of fuzzy rules to manage obstacles and control speed effectively.

## Features
- **Fuzzy Logic-Based Decision Making**: Implements fuzzy logic principles to handle uncertainties and imprecise information, allowing the car to make human-like decisions in various driving scenarios.
- **Obstacle Avoidance**: The simulator is equipped with advanced fuzzy rules that enable the car to detect and avoid obstacles dynamically, ensuring safe navigation through complex environments.
- **Speed Control**: The system adjusts the car's speed in response to changing road conditions, obstacles, and other vehicles, mimicking real-time decision-making in autonomous driving.
- **Simulation of Various Driving Conditions**: The simulator can be configured to test the self-driving car in different environmental conditions, such as rainy weather, traffic congestion, and varying road types.

## Project Structure
- `fuzzy_logic.py`: Contains the implementation of the fuzzy logic system, including the definition of fuzzy sets and rules.
- `car_simulation.py`: The main simulation script that integrates fuzzy logic with the car's sensors and actuators.
- `obstacle_detection.py`: Module responsible for detecting obstacles in the car's path and triggering the appropriate fuzzy rules.
- `speed_control.py`: Manages the car's speed based on inputs from the environment, utilizing fuzzy logic to maintain safe and efficient driving.
- `environment.py`: Defines the simulation environment, including road layouts, weather conditions, and other vehicles.
