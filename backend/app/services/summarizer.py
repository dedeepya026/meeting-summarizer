from openai import OpenAI
from app.config import settings


client = OpenAI(api_key=settings.OPENAI_API_KEY)


PROMPT_SYSTEM = (
    "You are a meeting summarizer. Output JSON only with keys: 'summary', 'decisions', 'action_items', 'open_questions'.\n"
    "For action_items use format: [task] — Owner: [name or 'TBD'] — Due: [date or 'TBD']"
)


PROMPT_USER = (
    "Summarize the following transcript. Be concise (3-5 sentences for summary). Extract key decisions and action items."
)




def generate_summary(transcript_text: str) -> dict:
    messages = [
        {"role": "system", "content": PROMPT_SYSTEM},
        {"role": "user", "content": PROMPT_USER + "\n\n" + transcript_text},
    ]
    resp = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=messages,
    temperature=0.0,
    max_tokens=800
    )
    # response text
    content = None
    if hasattr(resp, 'choices'):
        content = resp.choices[0].message['content']
    else:
        content = resp['choices'][0]['message']['content']


    # try to parse JSON from the assistant content
    import json
    try:
        parsed = json.loads(content)
    except Exception:
    # If model did not return pure JSON, attempt to extract JSON substring
        import re
        m = re.search(r"\{.*\}", content, re.S)
        if m:
            parsed = json.loads(m.group(0))
        else:
            parsed = {"summary": content, "decisions": [], "action_items": [], "open_questions": []}
    return parsed