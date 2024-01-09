# AutoSorter

Auto Organizer is a simple macOS utility that automatically organizes files in your Downloads folder based on their types. It runs in the background, continuously sorting your downloads into predefined categories like Videos, Images, Documents, Applications, and more.

## Features

- **Automatic Organization**: Once activated, Auto Organizer continuously monitors your Downloads folder and organizes files as soon as they are downloaded.
- **Customizable Categories**: Easily customize the file categories by modifying the script to match your preferences.
- **Two Versions Available**:
  - `auto_sorter.py`: Includes a toggleable menu bar app for macOS.
  - `sort_downloads.py`: Direct script execution for one-time organization.

## Usage

### AutoSorter with Menu Bar App

1. Run the `setup.py` script.
```python
python3 setup.py py2app
```
2. Click on the menu bar icon.
3. Toggle "Auto Organizer" to start and stop the automatic organization.

### Direct Script Execution

1. Run the `sort_downloads.py` script directly for one-time organization.

## Customization

### Customize AutoSorter Menu Bar App

Modify the `get_category` function to customize categories and file extensions.
