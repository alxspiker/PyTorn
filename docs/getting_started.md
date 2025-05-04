# Getting Started with PyTorn

This guide will help you set up your development environment and get started with PyTorn development.

## Prerequisites

- Python 3.7 or higher
- Git
- Android SDK and NDK (for Android deployment)

## Setting Up Development Environment

### 1. Clone the Repository

```bash
git clone https://github.com/alxspiker/PyTorn.git
cd PyTorn
```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment:

- On Windows: `venv\Scripts\activate`
- On macOS/Linux: `source venv/bin/activate`

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Buildozer (for Android builds)

```bash
pip install buildozer
```

## Running the Application

### On Desktop (Development Mode)

PyTorn is built with Kivy, which allows it to run on desktop for development purposes. To run the application:

```bash
python -m app.main
```

### Building for Android

Before building for Android, make sure you have the Android SDK and NDK installed. Buildozer will help with this process if you don't have them already.

```bash
buildozer android debug
```

This command will build a debug APK that you can install on your Android device for testing.

## Project Structure

- `app/main.py`: Main application entry point
- `app/api/`: Torn API integration
- `app/browser/`: WebView and browser components
- `app/script_manager/`: Script management functionality
- `app/ui/`: UI components and screens
- `assets/`: Images, icons, and other assets
- `scripts/`: Default/example scripts
- `docs/`: Documentation
- `tests/`: Test files

## Developing

### Adding a New Feature

1. Create a new branch: `git checkout -b feature/your-feature-name`
2. Make your changes
3. Test thoroughly
4. Commit your changes: `git commit -m "Add your feature description"`
5. Push to the branch: `git push origin feature/your-feature-name`
6. Create a Pull Request

## Torn API Usage

PyTorn uses the Torn API to fetch player data and other information. To use the API:

1. Get your API key from [Torn](https://www.torn.com/preferences.php#tab=api)
2. Enter it in the app settings

For development, you can set your API key in the code:

```python
from app.api.torn_api import TornAPI

api = TornAPI()
api.set_api_key('YOUR_API_KEY')
player_data = api.get_player()
```

## Creating Userscripts

PyTorn supports two types of userscripts:

### JavaScript Userscripts

These are similar to traditional userscripts used with extensions like Tampermonkey or Greasemonkey. They run directly in the browser context.

Example JavaScript userscript structure:

```javascript
// ==UserScript==
// @name        Script Name
// @description Script Description
// @match       https://www.torn.com/*
// @version     1.0
// @author      Your Name
// ==UserScript==

(function() {
    'use strict';
    
    // Your code here
    
})();
```

### Python Userscripts

PyTorn's unique feature is the ability to write userscripts in Python, which are then translated to work with the browser.

Example Python userscript structure:

```python
def on_page_load(context):
    """Function called when a page loads."""
    # Your code here
    
# Register the main entry point
register_handler('page_load', on_page_load)
```

## Getting Help

If you have questions or run into issues, please [open an issue](https://github.com/alxspiker/PyTorn/issues/new) on GitHub.