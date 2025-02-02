# PyDotPattern

PyDotPattern is a Python utility that generates a pattern of dots based on user-selected anchor points and a random selection process. The project uses PyGame for visualization and Numpy for numerical operations.

## Project Description

The utility allows users to select 3 to 6 anchor points on a grid. Once the points are selected, the user can press the start button to begin the simulation. The system will simulate rolling a 6-sided die to randomly select one of the anchor points. A new dot will be placed at the midpoint between the last placed dot and the selected anchor point. The first dot will always be the midpoint between the first and last anchor points.

## Features

- Select 3 to 6 anchor points on a grid.
- Simulate rolling a 6-sided die to select an anchor point.
- Generate dots at the midpoint between the last placed dot and the selected anchor point.
- Visualize the pattern generation using PyGame.

## Requirements

- Python 3.x
- PyGame-CE
- Numpy

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/pydotpattern.git
   ```
2. Navigate to the project directory:
   ```sh
   cd pydotpattern
   ```
3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Run the main script:
   ```sh
   python main.py
   ```
2. Select 3 to 6 anchor points on the grid by clicking on the desired locations.
3. Press the start button to begin the simulation.
4. Watch as the dots are generated and placed on the grid.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [PyGame-CE](https://pypi.org/project/pygame-ce/)
- [Numpy](https://numpy.org/)
