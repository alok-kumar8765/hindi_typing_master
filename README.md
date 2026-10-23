# Hindi Typing Master

A GUI-based desktop application built with Python and Tkinter designed for practicing and measuring Hindi typing speed and accuracy. Supports both modern Unicode (**Mangal**) and legacy non-Unicode (**Kruti Dev**) font modes.

---

## Key Features

- **Dual Mode Support**:
  - **Mangal / Unicode**: For standard Unicode typing (e.g., InScript, Remington Unicode).
  - **Kruti Dev**: For legacy Kruti Dev 010 font typing.
- **Difficulty Levels**: Three preset difficulty levels (**Easy**, **Medium**, **Hard**) with different lengths and complex Hindi paragraphs.
- **Real-Time Performance Metrics**:
  - **WPM** (Words Per Minute)
  - **CPM** (Characters Per Minute)
  - **Accuracy** (%)
  - **Error Count**
  - **Elapsed Time**
- **Live Text Highlighting**: Color-coded feedback as you type (Green for correct characters, Red with underline for mistakes).
- **Keyboard Shortcuts**: Quick keys to start and reset tests without using the mouse.

---

## Requirements & Prerequisites

### System Requirements
- Operating System: Windows, macOS, or Linux
- Python Version: Python 3.x

### Mandatory Font for Kruti Dev Mode
If you plan to practice in **Kruti Dev** mode, ensure that the **Kruti Dev 010** font is installed on your operating system. Otherwise, the characters will display as standard Latin ASCII letters (`Hkkjr...`).

---

## Getting Started

### Installation

1. Ensure Python 3 is installed on your system. You can verify this by running:
   ```bash
   python --version
   ```

2. Clone or download this repository to your local machine.

3. No third-party pip packages are required! The application relies strictly on Python standard libraries (`tkinter`, `random`, `time`).

### Running the Application

Execute the Python script directly from your terminal or command prompt:

```bash
python hindi_typing_master.py
```

---

## How to Use

1. **Select Font Mode**: Choose between `Mangal / Unicode` or `Kruti Dev` using the dropdown menu.
2. **Select Difficulty**: Choose `Easy`, `Medium`, or `Hard`.
3. **Start Test**: Click the **▶ START TEST** button or press **`F5`**.
4. **Type**: Click into the lower blue box (cursor auto-focuses) and start typing the paragraph displayed in the practice area.
5. **View Results**: The test completes automatically once you finish typing the paragraph, displaying your final WPM, CPM, and Accuracy.

### Keyboard Shortcuts
- **`F5`**: Start / Restart Test
- **`Escape`**: Reset Test

---

## Pros, Cons & Limitations

### Pros
- **Zero Dependencies**: Built strictly using built-in Python modules (`tkinter`, `ttk`, `time`, `random`), making deployment effortless without running `pip install`.
- **Dual Layout/Font Capability**: Accommodates both government/official Unicode (Mangal) test standards and legacy typing test formats (Kruti Dev).
- **Clean Responsive UI**: Clear distinction between practice paragraph and typing area, with fixed height constraints ensuring UI stability across screen resizes.
- **Real-time Feedback**: Color-coded highlights give instantaneous visual feedback on visual accuracy.

### Cons
- **Re-rendering Overhead**: Rebuilding and inserting formatted text into the Tkinter text widget every 150ms (`update_highlight`) can lead to slight UI stutter on low-spec systems or very fast typing speeds.
- **No Character Backspace Lock**: Allows unrestricted backspacing and corrections anywhere in the entry box, which does not mirror strict exam environments where backspacing may be disabled.
- **Hardcoded Practice Texts**: Paragraphs are stored directly inside Python dictionary structures. Adding new texts requires modifying source code rather than editing an external file (e.g., JSON or TXT).

### Limitations
- **Unicode Conjunct Character Matching**: Simple character-by-character comparison (`typed[i] == current_text[i]`) does not account for complex Unicode grapheme clusters, matras, or complex ligatures, which can lead to false error flags during intermediate IME composition steps.
- **No Performance Persistence**: Results are not saved to a local database or log file; once the window is closed or reset, past performance metrics are lost.
- **Font Dependency**: Native system fonts must be pre-installed; Tkinter cannot dynamically embed or bundle custom TTF font files at runtime.

---

## License

This project is open-source and free to use for personal or educational purposes.