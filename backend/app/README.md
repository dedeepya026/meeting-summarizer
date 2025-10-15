# Meeting Summarizer

🎤 **Meeting Summarizer** is a full-stack application that **transcribes meeting audio** and **generates action-oriented summaries** using AI. It is designed to help teams quickly capture key decisions and actionable items from meetings.

---

## 🌟 Features

- **Audio Transcription:** Converts `.mp3` or `.wav` files to text using ASR (Automatic Speech Recognition, e.g., Whisper).  
- **Summary Generation:** Uses Large Language Models (OpenAI GPT) to generate concise summaries and extract action items.  
- **User-Friendly Interface:** Upload audio files and view transcripts, summaries, and action items in a clean React frontend.  
- **Modular Backend:** FastAPI backend with separate services for transcription and summarization.  
- **Cross-Platform Development:** Works locally with Python or Docker for easy setup on any OS.

---

## 🛠️ Technology Stack

- **Backend:** Python, FastAPI, Whisper ASR, OpenAI GPT, Pydantic  
- **Frontend:** React, Vite, JavaScript, CSS  
- **Optional Containerization:** Docker for easy cross-platform execution

---

## 🚀 How It Works

1. **Upload Audio** – Users upload meeting recordings via the frontend.  
2. **Transcription** – The backend transcribes audio into text.  
3. **Summarization** – The transcript is summarized and key action items are extracted using GPT.  
4. **View Results** – Frontend displays the transcript, summary, and action items.

---

## 📁 Project Structure
meeting-summarizer/
├── backend/ # FastAPI backend, ASR and summarization services
├── frontend/ # React + Vite frontend for file upload and display


---

## 🎯 Use Cases

- Remote teams needing quick meeting notes  
- Managers tracking decisions and tasks  
- Educational lectures or seminars summarization  

---

## ⚡ Highlights

- Action-oriented summaries for meetings  
- Modular code structure for easy extensions  
- Can be run locally or in a Docker container  
- Frontend-backend integration with minimal setup

---

## 📌 Notes

- Requires an OpenAI API key for LLM summarization  
- Works offline for transcription with Whisper (local ASR model)  
- Designed to be lightweight and easy to test  

---

> **Meeting Summarizer** is ideal for teams, educators, or anyone who wants to save time on meeting notes and extract actionable items automatically.
