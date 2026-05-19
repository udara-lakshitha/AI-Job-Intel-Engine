from pydantic import BaseModel
from google import genai
from google.genai import types

class JobProfile(BaseModel):
    title: str
    company: str
    skills: list[str]
    experience_required: str

async def extract_job_details(html_txt: str) -> JobProfile:
    client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))
    prompt = "review the incoming unstructured text and extract the specific metrics mapped out in the data fields"
    configurations = types.GenerateContentConfig(
        response_mime_type =  "application/json",
        response_schema = JobProfile,
        system_instruction = prompt
    )
    response = await client.aio.models.generate_content(
        model="gemini-2.5-flash",
        contents = html_txt,
        config = configurations
    )
    return response.parsed