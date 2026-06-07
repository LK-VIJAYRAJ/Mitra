# Mitra — Compassionate Calendar Companion

Mitra is an **emotion-aware productivity assistant** designed to make calendar management feel more human.  
The project combines a lightweight Tkinter interface with rule-based emotion detection, empathetic response generation, and integration-ready Google Calendar / Gmail modules.

---

## Overview

Mitra helps users enter events in natural language and responds with a context-aware message based on the emotion implied by the text.

Example:
- **"Interview with HR"** → detected as **stress**
- **"Birthday party"** → detected as **joy**
- **"Team meeting"** → detected as **neutral**

The goal of the project is to make routine scheduling feel more supportive, engaging, and personal.

---

## Key Features

- **Emotion-aware event handling** using a simple rule-based NLP approach
- **Empathetic message generation** based on detected emotion
- **Tkinter-based desktop UI** for quick event input and display
- **Google Calendar integration module** for fetching and creating events
- **Gmail integration module** for reading recent email subjects
- **Basic memory/vector store placeholder** to support future semantic retrieval
- **Modular code structure** separated into UI, NLP, helper, API, and memory layers

---

## Project Highlights / Achievements

This project demonstrates several strong implementation achievements:

- Built a **working desktop assistant UI** from scratch using Python and Tkinter.
- Implemented **emotion classification logic** to interpret event text and assign a tone.
- Designed **human-friendly response formatting** so the assistant replies with supportive language.
- Added **Google OAuth-based authentication flow** to support Calendar and Gmail access.
- Created **API wrapper modules** for calendar and email operations, making the project easier to expand.
- Introduced a **memory abstraction layer** that can later be upgraded to a real vector database.
- Kept the codebase **modular and maintainable**, which is a strong base for future AI features.

---

## How It Works

1. The user enters an event in the UI.
2. The text is passed through a rule-based emotion detector.
3. A supportive response is generated according to the detected emotion.
4. The event is displayed in the UI with a timestamp.
5. The event text is also sent to the memory layer for storage hooks.
6. Separate modules are available for Google Calendar and Gmail operations.

---

## Tech Stack

- **Python**
- **Tkinter** for the desktop user interface
- **Google Calendar API**
- **Gmail API**
- **Google OAuth 2.0**
- **Rule-based NLP / text matching**
- **Placeholder vector memory layer** for future expansion

---

## Repository Structure

```text
Mitra-main/
├── main_ui.py          # Tkinter application and event UI
├── emotion_rules.py    # Emotion detection rules
├── helpers.py          # Message formatting helpers
├── memory.py           # Vector memory placeholder
├── calendar_api.py     # Google Calendar integration functions
├── gmail_api.py        # Gmail integration functions
├── google_auth.py      # OAuth credential handling
├── settings.py         # API key placeholders
├── sample_events.txt   # Example event inputs
└── README.md           # Project documentation
```

---

## Core Modules

### `main_ui.py`
Contains the `CalendarApp` class and launches the Tkinter UI.  
It accepts user input, detects emotion, formats the response, and shows the result in the application window.

### `emotion_rules.py`
Implements a simple rule-based function:
- stress-related words → `stress`
- celebration-related words → `joy`
- everything else → `neutral`

### `helpers.py`
Formats the final assistant message using the detected emotion.

### `memory.py`
Provides placeholder functions for:
- storing embeddings
- retrieving similar items

This is useful as a foundation for a future semantic memory / vector search system.

### `google_auth.py`
Handles Google OAuth credential loading and token persistence.

### `calendar_api.py`
Includes functions to:
- fetch upcoming calendar events
- add new calendar events

### `gmail_api.py`
Includes a function to fetch recent Gmail message subjects.

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd Mitra-main
```

### 2. Install dependencies
```bash
pip install google-api-python-client google-auth google-auth-oauthlib google-auth-httplib2
```

If you are running the desktop UI, ensure Python includes Tkinter support.

### 3. Configure Google Cloud credentials
Create a Google Cloud project and enable:
- **Google Calendar API**
- **Gmail API**

Download the OAuth client file and save it as:

```text
credentials.json
```

### 4. First-time authentication
Run the application once so the OAuth flow can generate the token file.

The code stores credentials in:

```text
token.pickle
```

### 5. Update API keys if needed
The `settings.py` file currently contains placeholder values.  
Replace them with valid keys or remove them if your version does not need them.

### 6. Run the app
```bash
python main_ui.py
```

---

## Example Usage

Sample events from `sample_events.txt` include:

- Meeting with manager
- Therapy session
- Birthday party
- Interview with HR

When entered into the UI, each event receives a supportive message based on the detected emotion.

---

## Current Notes

The archive shows a clean prototype with a strong concept and clear modular separation.  
Some modules appear to be designed for a package-based layout, so the import paths may need alignment if you reorganize the files into folders such as `api/`, `utils/`, `nlp/`, and `vector_db/`.

---

## Future Improvements

- Replace rule-based emotion detection with a trained NLP model
- Connect the memory layer to a real vector database
- Trigger actual Google Calendar event creation from the UI
- Add Gmail-based event suggestions and reminders
- Improve UI design with modern widgets and richer event views
- Add persistence for user history and saved preferences

---

## Why This Project Stands Out

Mitra is not just a calendar app. It is an early-stage **emotion-aware productivity assistant** that combines scheduling, email awareness, and supportive communication in a single workflow.  
That makes it a good demonstration of:
- Python application design
- API integration
- UX-focused assistant behavior
- NLP-inspired logic
- Foundation for AI-enhanced productivity tools

---

## License

Add your preferred license here if you plan to publish the project publicly.