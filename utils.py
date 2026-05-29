from groq import Groq
import streamlit as st
# ---------------------------------------------------
# GROQ CLIENT
# ---------------------------------------------------

client = Groq(
api_key=st.secrets["GROQ_API_KEY"]
)

# ---------------------------------------------------
# GENERATE AI RESPONSE
# ---------------------------------------------------

def generate_resolution(
    query,
    incidents
):

    # ---------------------------------------------------
    # NO MATCH FOUND
    # ---------------------------------------------------

    if len(incidents) == 0:

        return f"""

I could not find any strongly related historical incidents for the reported issue "{query}".

This may indicate that the incident is either new, uncommon, or does not yet have sufficient historical resolution data available in the incident repository. It is recommended to review the application and infrastructure logs manually and engage the relevant support team for further investigation.

"""

    # ---------------------------------------------------
    # BUILD INCIDENT CONTEXT
    # ---------------------------------------------------

    context = ""

    for incident in incidents:

        context += f"""

Incident ID:
{incident['incident_id']}

Title:
{incident['title']}

Description:
{incident['description']}

Resolution:
{incident['resolution']}

Severity:
{incident['severity']}

"""

    # ---------------------------------------------------
    # PROMPT
    # ---------------------------------------------------

    prompt = f"""

You are an enterprise AI Incident Resolution Assistant used by Platform and DevOps teams.

A new production incident has been reported:

"{query}"

Below are similar historical incidents retrieved from the incident knowledge base:

{context}

Your responsibilities:

- Analyze the incident intelligently
- Understand the likely root cause
- Suggest the most practical and feasible resolution
- Sound like an experienced DevOps engineer
- Respond naturally in conversational language
- Mention relevant incident IDs naturally in the response
- Avoid bullet points
- Avoid headings
- Avoid rigid or template-based formatting
- Keep the response concise but intelligent
- If the incidents are weakly related, clearly mention that confidence is lower

Generate a professional natural-language recommendation.

"""

    # ---------------------------------------------------
    # GROQ LLM RESPONSE
    # ---------------------------------------------------

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.4,
        max_tokens=300
    )

    # ---------------------------------------------------
    # RETURN RESPONSE
    # ---------------------------------------------------

    return response.choices[0].message.content