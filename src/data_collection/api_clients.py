"""
API clients for Claude, GPT-4, and Gemini Flash 2.5
"""

import os
from typing import List, Dict
from dotenv import load_dotenv
import anthropic
import openai
from google import generativeai as genai

load_dotenv()

class ClaudeClient:
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
        self.model = "claude-sonnet-4-5-20250929"  # Latest Sonnet 4.5
    
    def generate(self, messages: List[Dict[str, str]], temperature: float = 1.0) -> str:
        """Generate response from Claude"""
        response = self.client.messages.create(
            model=self.model,
            max_tokens=1024,
            temperature=temperature,
            messages=messages
        )
        return response.content[0].text

class GPT4Client:
    def __init__(self):
        self.client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.model = "gpt-4"  # Can also use "gpt-4-turbo" or "gpt-4o"
    
    def generate(self, messages: List[Dict[str, str]], temperature: float = 1.0) -> str:
        """Generate response from GPT-4"""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature,
            max_tokens=1024
        )
        return response.choices[0].message.content

class GeminiClient:
    def __init__(self):
        genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        
    def generate(self, messages: List[Dict[str, str]], temperature: float = 1.0) -> str:
        """Generate response from Gemini Flash 2.5"""
        try:
            chat = self.model.start_chat(history=[])
            
            # Add conversation history
            for i, msg in enumerate(messages[:-1]):
                if msg['role'] == 'user':
                    response = chat.send_message(msg['content'])
            
            # Send final message with increased token limit
            final_response = chat.send_message(
                messages[-1]['content'],
                generation_config=genai.types.GenerationConfig(
                    temperature=temperature,
                    max_output_tokens=2048,  # Increased from 1024
                ),
                safety_settings=[
                    {
                        "category": "HARM_CATEGORY_HARASSMENT",
                        "threshold": "BLOCK_NONE",
                    },
                    {
                        "category": "HARM_CATEGORY_HATE_SPEECH",
                        "threshold": "BLOCK_NONE",
                    },
                    {
                        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                        "threshold": "BLOCK_NONE",
                    },
                    {
                        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                        "threshold": "BLOCK_NONE",
                    },
                ]
            )
            
            return final_response.text
            
        except Exception as e:
            # If response.text fails, try to get alternative content
            if hasattr(final_response, 'parts') and final_response.parts:
                return final_response.parts[0].text
            else:
                raise e

def get_client(model_name: str):
    """Factory function to get the right client"""
    clients = {
        'claude': ClaudeClient,
        'gpt4': GPT4Client,
        'gemini': GeminiClient
    }
    return clients[model_name]()