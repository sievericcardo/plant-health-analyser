# Plant Health Analyzer

## Overview

The Plant Health Analyzer is a Python project designed to analyze images of plants and determine their health status using multiple Multimodal LLMs. This tool can help to quickly identify sick plants and take appropriate action.

## Project Structure

```
plant-health-analyzer
├── src
│   ├── main.py               # Entry point of the application
│   ├── image_parser.py       # Image loading and preprocessing
│   └── utils
│       └── __init__.py       # Utility functions and constants
├── config
│   └── config.py             # Configuration settings
├── tests
│   ├── __init__.py           # Test organization
│   └── test_image_parser.py   # Unit tests for ImageParser
├── requirements.txt           # Project dependencies
├── .gitignore                 # Files to ignore in version control
└── README.md                  # Project documentation
```

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd plant-health-analyzer
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Prepare a folder containing images of plants you want to analyze.
2. Update the configuration settings in `config/config.py` to specify the path to your images and the model checkpoints.
3. Specify the token creating the appropriate `.env` file in the root directory of the project. You can use the `.env.example` as a template:
4. Run the application:

```bash
python src/main.py --image_folder <path_to_your_image_folder>
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the BSD3 License. See the LICENSE file for more details.
