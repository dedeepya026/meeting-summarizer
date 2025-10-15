import React, { useState } from 'react'
import '../styles/style.css'

export default function Upload() {
  const [file, setFile] = useState(null)
  const [status, setStatus] = useState('')
  const [transcript, setTranscript] = useState('')
  const [summary, setSummary] = useState(null)
  const [loading, setLoading] = useState(false)

  async function handleUpload(e) {
    e.preventDefault()
    if (!file) return alert('Please select an audio file first.')

    setLoading(true)
    setStatus('Uploading and transcribing...')

    try {
      // Step 1: Upload audio to backend for transcription
      const form = new FormData()
      form.append('file', file)

      const res = await fetch('http://localhost:8000/v1/transcribe/', {
        method: 'POST',
        body: form,
      })

      if (!res.ok) throw new Error('Transcription failed.')
      const data = await res.json()

      setTranscript(data.transcript || '')
      setStatus('Transcription done. Generating summary...')

      // Step 2: Send transcript to summarizer API
      const summaryRes = await fetch('http://localhost:8000/v1/summarize/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ transcript: data.transcript }),
      })

      if (!summaryRes.ok) throw new Error('Summary generation failed.')
      const summaryData = await summaryRes.json()

      setSummary(summaryData)
      setStatus('Done ✅')
    } catch (err) {
      console.error(err)
      setStatus('Error: ' + err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="container">
      <h1>🎧 Meeting Summarizer</h1>
      <form onSubmit={handleUpload}>
        <input
          type="file"
          accept="audio/*"
          onChange={(e) => setFile(e.target.files[0])}
        />
        <button type="submit" disabled={loading}>
          {loading ? 'Processing...' : 'Upload & Summarize'}
        </button>
      </form>

      {status && (
        <p style={{ marginTop: '1rem', fontStyle: 'italic' }}>{status}</p>
      )}

      {loading && <div className="loader" style={{ marginTop: '1rem' }}></div>}

      {transcript && (
        <div className="summary-box">
          <h2>📝 Transcript</h2>
          <p>{transcript}</p>
        </div>
      )}

      {summary && (
        <div className="summary-box">
          <h2>📋 Summary</h2>
          <p>{summary.summary}</p>

          {summary.action_items && summary.action_items.length > 0 && (
            <>
              <h3>✅ Action Items</h3>
              <ul>
                {summary.action_items.map((item, i) => (
                  <li key={i}>{item}</li>
                ))}
              </ul>
            </>
          )}
        </div>
      )}
    </div>
  )
}
