# Table Data Extractor System

This system is composed of two parts: a server-side API and a client interface. The server handles image processing to extract tables from images and convert them into CSV format using machine learning and OCR technologies. The client-side interface allows users to upload images for processing and retrieve the converted CSV data.

## Features

- **Image Upload**: Clients can upload images of tables which need to be processed.
- **OCR Processing**: Utilizes PaddleOCR to recognize text within tables in images.
- **Data Conversion**: Converts recognized text and structures into CSV format.
- **Server-Client Architecture**: Separates processing and interaction logic allowing scalability.
- **FastAPI**: Provides an easy-to-use API endpoint for image uploading and CSV retrieval.

## Prerequisites

Before running the Python scripts, ensure the following are installed:

- Python 3.7
- numpy==1.19.3
- opencv-python==4.8.1.78
- pandas==1.3.3
- matplotlib==3.4.3
- scikit-image==0.18.3
- scipy==1.7.3
- keras_segmentaion
- paddlepaddle==2.5.1
- paddleocr==2.7.0.2
- tensorflow-gpu==2.4.0
- tensorflow==2.4.1
- keras==2.4.3
- FastAPI
- Uvicorn
- wget
- pydantic

To install the required packages, run:

```bash
pip install -r requiremets.txt
```

## Server Setup

The server script (`server.py`) will start a FastAPI application that waits for image uploads and performs the table data extraction task.

## Client Interaction

The client script (`client.py`) serves as a user interface for the system. It allows users to upload images to the server and receive the extracted data in CSV format.

## Usage Instructions

Start the server:

```bash
python3 server.py
```

The server will be running on http://localhost:9001  
Run the client:
```bash
python3 client.py
```

The client will connect to http://localhost:9002. client can upload images via this endpoint to process them into CSV format.  

## System Workflow  

- The client API receives an image upload via an HTTP POST request.
- The server API accepts the image from the client and processes it.
- The csv_generater function is called within the server script,to extract table data.
- The client receives the CSV file as a response from the server.
- The CSV file is saved in client's system. 

## License
Licensed under the MIT License.
