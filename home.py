import gradio as gr
import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyCyGBa2I6Y_fsqXXpdk-JYK3Z5TPMM4Bgo")
generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 20000,
    }
def gemini_chat(message,history):
    response = chat.send_message(message)
    return response.text

model = genai.GenerativeModel(model_name="gemini-pro",
                                  generation_config=generation_config)

chat = model.start_chat()

iface = gr.ChatInterface(
    fn=gemini_chat,
    chatbot=gr.Chatbot(height=500),
    submit_btn='Generate',
    title='Kudos AI',
    analytics_enabled= True,
    textbox= gr.Textbox(
        placeholder='Message Kudo',
        scale=7
    ),

)

if __name__ == '__main__':
    iface.launch(share=True)