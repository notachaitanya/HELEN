# HELEN — Personal AI Assistant

Helen is a personal AI assistant project designed to bring together voice interaction, local language models, internet access, and computer vision into one system.

The goal is to build an assistant that can understand user commands, process information, respond naturally, and gradually develop more advanced capabilities through independently developed modules.

Helen is being developed in Python, with a focus on understanding how the different components of an AI assistant work together rather than simply connecting existing tools.

## Project Goals

- **Voice Interaction:** Allow users to communicate with Helen through speech.
- **AI Reasoning:** Use a locally running language model to understand requests and generate responses.
- **Internet Access:** Enable Helen to search for information online and retrieve relevant webpage content. *(Under construction.)*
- **Computer Vision:** Explore visual recognition and person identification through a camera.
- **Personal Memory:** Develop a persistent memory system that can store and retrieve useful information across conversations.
- **Modular Architecture:** Keep each major capability separate so it can be developed, tested, and improved independently.

## Architecture

Helen is organized into modules, each responsible for a different capability.

| Module | Responsibility | Status |
|---|---|---|
| `SOUND` | Voice input and speech output | In development |
| `BRAIN` | Communication with the local language model | In development |
| `INTERNET` | Web search and information retrieval | Under construction |
| `VISION` | Object detection, face detection, and person identification experiments | In development |
| `MEMORY` | Persistent personal memory | Planned |

The `MEMORY` module is a future component and does not yet exist as a separate folder.

### How the Components Work Together

The intended workflow is:

1. Helen receives a spoken command.
2. The voice input is converted into text.
3. The system determines how to handle the request.
4. The AI model generates a response, using internet-retrieved information when required.
5. Helen converts the response into speech and delivers it to the user.

Computer vision and persistent memory will be integrated into this workflow as their implementations develop.

## Technology Stack

The technologies currently explored or used in the project include:

- **Python** — Main programming language.
- **Ollama** — Runs language models locally.
- **DDGS** — Provides general-purpose web search functionality.
- **PyAudio** — Handles audio input and recording.
- **OpenCV** — Provides computer vision and camera access.
- **Ultralytics YOLO** — Used for object and face-detection experiments.

Additional libraries and technologies may be introduced as the project evolves. Each module's README documents its specific dependencies and implementation.

## Repository Structure

```text
HELEN/
│
├── main.py
│
├── BRAIN/
│   └── prefrontalCortex/
│       └── ollamaSend.py
│
├── INTERNET/
│   └── internetSearch.py
│
├── SOUND/
│   ├── listen.py
│   └── speak.py
│
└── VISION/
    ├── trainedModel/
    │   ├── training.py
    │   └── images/
    │
    └── unTrainedModel/
        ├── personsIdentifier.py
        └── yolo11n.pt
```

*Note: Model files and additional generated files may be present in the repository but are omitted here for readability.*

## Module Documentation

Each module has its own README describing its purpose, technologies, implementation, setup instructions, and development progress.

- **BRAIN:** `BRAIN/prefrontalCortex/README.md`
- **INTERNET:** `INTERNET/README.md`
- **SOUND:** `SOUND/README.md`
- **VISION:** `VISION/README.md`

These documents will be updated as the modules evolve.

## Development Philosophy

Helen is being built incrementally. Each module is explored, implemented, tested, and documented before being integrated into the larger system.

The objective is not just to create a voice interface for an existing AI model. It is to understand and develop the orchestration, memory, and interaction systems that make a personal AI assistant useful.

## Current Development Focus

The project is currently focused on developing the foundational components:

- Connecting Python to a locally running language model.
- Building voice input and speech output.
- Experimenting with computer vision and person identification.
- Developing a general-purpose internet search and information retrieval module.

Persistent memory, deeper integration, and additional assistant capabilities will follow as the foundations improve.

## Long-Term Vision

The long-term vision is for Helen to become a personal assistant that can remember relevant information, understand natural voice commands, retrieve information when needed, recognize its environment, and provide a consistent experience across different devices.

This is an ongoing learning and engineering project. Features described as planned or under construction should not be considered fully implemented.
