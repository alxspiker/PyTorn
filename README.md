# PyTorn

A Python-based Android browser app for Torn.com with API integration and userscript support.

## Description

PyTorn is a specialized Android browser application built with Python that enhances the Torn.com gaming experience. It features seamless Torn API integration for real-time alerts and player data, alongside a customized browser for Torn.com navigation. The app's unique userscript manager supports both JavaScript and Python scripting, allowing users to create powerful automation tools and UI enhancements with the simplicity of Python coding.

## Features

- **Torn API Integration**: Real-time alerts, player stats, faction info, and more
- **Custom Browser**: Optimized for Torn.com with specialized navigation
- **Userscript Manager**: Support for both JavaScript and Python scripts
- **Python-to-DOM Bridge**: Easily manipulate page elements using Python

## Project Structure

```
pytorn/
├── app/
│   ├── main.py              # Main application entry point
│   ├── api/                 # Torn API integration
│   ├── browser/             # WebView and browser components
│   ├── script_manager/      # Script management functionality
│   └── ui/                  # UI components and screens
├── assets/                  # Images, icons, and other assets
├── scripts/                 # Default/example scripts
├── docs/                    # Documentation
├── tests/                   # Test files
└── buildozer.spec           # Buildozer configuration for Android packaging
```

## Development Status

This project is currently in early development. Contributions and suggestions are welcome!

## Getting Started

See the [documentation](docs/getting_started.md) for setup and development instructions.