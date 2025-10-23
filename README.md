# Emotion Detector API

A simple Flask web application that performs emotion detection on text input using Watson NLP services. This project was developed as part of an open courseware assignment to explore integrating natural basic language processing capabilities with a simple web application.

**Note**: This repository was forked from an original courseware template. The following files were provided by the original authors as part of the assignment framework:

*  `templates/index.html` - Web interface template with Bootstrap styling
* `static/mywebscript.js` - Frontend JavaScript for API communication

The core implementation files (`server.py`, `nlp/emotion_detection.py`, `test/test_emotion_detection`) and project documentation were developed as part of the assignment completion.

**!! Access to the watson.labs.skills.network is a dependancy for the emotion_detector function !!**

## Overview

This application analyzes text input and identifies the dominant emotion present in the text. It can detect five primary emotions:
- **Joy** - Happiness, contentment, satisfaction
- **Anger** - Frustration, irritation, rage
- **Disgust** - Revulsion, distaste, aversion
- **Sadness** - Sorrow, melancholy, grief
- **Fear** - Anxiety, worry, apprehension

## Features

- **Web Interface**: Clean, responsive Bootstrap-based UI for text input and results display
- **REST API**: `/emotionDetector` endpoint for programmatic access
- **Real-time Analysis**: Instant emotion detection using Watson NLP services
- **Error Handling**: Graceful handling of invalid input with user-friendly error messages
- **Unit Testing**: Comprehensive test suite to validate emotion detection accuracy

## Project Structure

```
emotion-detector-api/
├── server.py                    # Main Flask application
├── requirements.txt             # Python dependencies
├── nlp/
│   ├── __init__.py             # Package initialization
│   └── emotion_detection.py    # Core emotion detection logic
├── templates/
│   └── index.html              # Web interface template
├── static/
│   └── mywebscript.js          # Frontend JavaScript
├── test/
│   └── test_emotion_detection.py # Unit tests
├── README.md                   # Project documentation
└── LICENSE                     # License file
```

## Technology Stack

- **Backend**: Python 3.x, Flask web framework
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 4.3.1
- **NLP Service**: IBM Watson Natural Language Processing
- **Testing**: Python unittest framework
- **HTTP Client**: Python requests library

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Steve-Glover/emotion-detector-api.git
   cd emotion-detector-api
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python server.py
   ```

5. **Access the application**:
   Open your browser and navigate to `http://localhost:5000`

## Usage

### Web Interface

1. Open the application in your browser
2. Enter text in the input field that you want to analyze
3. Click "Run Sentiment Analysis" button
4. View the emotion analysis results below

### API Endpoint

You can also use the REST API directly:

```bash
curl "http://localhost:5000/emotionDetector?textToAnalyze=I%20am%20so%20happy%20today"
```

**Response Format**:
```json
{
  "anger": 0.005,
  "disgust": 0.002,
  "fear": 0.001,
  "joy": 0.987,
  "sadness": 0.005,
  "dominant_emotion": "joy"
}
```

## API Documentation

### GET /emotionDetector

Analyzes the emotion in the provided text.

**Parameters**:
- `textToAnalyze` (string, required): The text to analyze for emotions

**Response**:
- Success (200): Returns emotion scores and dominant emotion
- Error (200): Returns "Invalid text! Please try again" for invalid input

## Error Handling

The application includes robust error handling:
- **Invalid Text**: Returns user-friendly error message for empty or invalid input
- **API Failures**: Handles Watson NLP service errors gracefully
- **Network Issues**: Manages connection problems with appropriate responses

## Development Notes

This project was created as part of an open courseware assignment with the following learning objectives:
- Implement a Flask web application with proper routing
- Integrate external NLP services for text analysis
- Create a responsive web interface using modern web technologies
- Develop comprehensive unit tests for validation
- Practice error handling


## License

This project is licensed under the terms specified in the LICENSE file.

