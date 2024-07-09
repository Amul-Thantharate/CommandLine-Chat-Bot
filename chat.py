from colorama import Fore, Style
import google.generativeai as genai
import typer
from typing import Optional

app = typer.Typer()

@app.command()
def interactive_chat(
    api_key: str = typer.Option(..., help="Your Google API Key"),
    temperature: float = typer.Option(0.7, help="Control Randomness. Defaults to 0.7"),
    max_output_tokens: int = typer.Option(
        150, help="Control length of response. Defaults to 150"
    ),
    top_p: float = typer.Option(0.9, help="Control randomness. Defaults to 0.9"),
    top_k: int = typer.Option(40, help="Control randomness. Defaults to 40"),
):
    """Interactive CLI tool to chat with Google Gemini-1.5-flash model."""

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("models/gemini-1.5-flash")
    typer.echo(
        "Starting interactive chat with Google Gemini-1.5-flash model. Type 'exit' to end the session."
    )
    while True:
        user_input = input(Fore.GREEN + "You: ")
        if user_input.lower() == "exit":
            print(Fore.RED + "Chat ended. 👋👋👋👋👋")
            break
        response = model.generate_content(
            user_input, generation_config={
                "temperature": temperature,
                "max_output_tokens": max_output_tokens,
                "top_p": top_p,
                "top_k": top_k,
            }
        )
        typer.echo(Fore.RED + f"Chatbot: {response.text}")
        typer.echo()

if __name__ == "__main__":
    app()
