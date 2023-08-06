from transformers import AutoTokenizer
from auto_gptq import AutoGPTQForCausalLM
import gradio as gr
import logging

logging.basicConfig(level=logging.INFO)
logging.info("Start")


model_name = 'fffrrt/ruGPT-3.5-13B-GPTQ'
model_basename = 'gptq_model-4bit-128g'

tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
model = AutoGPTQForCausalLM.from_quantized(model_name,
        model_basename = model_basename,
        use_safetensors=True,
        trust_remote_code=True,
        device="cuda:0",
        use_triton=False,
        quantize_config=None)


"""def generate_response(text, num_beams, max_new_tokens, do_sample_flag, button_click):
    # Here, "button_click" will contain the event for the button click. 
    # You can ignore it if you don't need any specific functionality on button click.

    encoded_input = tokenizer(text, return_tensors='pt').to('cuda:0')
    output = model.generate(
        **encoded_input,
        num_beams=int(num_beams),
        max_new_tokens=int(max_new_tokens),
        do_sample=do_sample_flag
    )
    return tokenizer.decode(output[0], skip_special_tokens=True)
    num_beams=2,
    do_sample=True,
    max_new_tokens=100"""

# def generate_response(text, num_beams, max_new_tokens, do_sample_flag, button_click):
def generate_response(
    text, 
    num_beams, 
    num_return_sequences, 
    max_new_tokens, 
    repetition_penalty,
    do_sample,     
    button_click
    ):

    encoded_input = tokenizer(text, return_tensors='pt').to('cuda:0')
    output = model.generate(
        **encoded_input,
        num_beams=int(num_beams),
        num_return_sequences=int(num_return_sequences),
        max_new_tokens=int(max_new_tokens),
        repetition_penalty=float(repetition_penalty),
        do_sample=do_sample        
    )
    return tokenizer.decode(output[0], skip_special_tokens=True)


def main():
    textbox = gr.Textbox(placeholder="Введите текст...", label="Your Input", value="""Загадка:
Дом на улице стоит,
Детвора к нему спешит.
Несут тетрадки, книжки
Девчонки и мальчишки.

Ответ:""")
    num_beams_slider = gr.Slider(minimum=1, maximum=10, step=1, label="Num Beams", value=10)
    num_return_sequences_slider = gr.Slider(minimum=1, maximum=10, step=1, label="Num Return Sequences", value=2)
    max_new_tokens_slider = gr.Slider(minimum=10, maximum=800, step=10, label="Max New Tokens", value=50)
    repetition_penalty_slider = gr.Slider(minimum=0.0, maximum=2.0, step=0.1, label="Repetition Penalty", value=2.0)
    do_sample = gr.Checkbox(label="Do Sample", value=True)
    submit_button = gr.Button(label="Submit")

    # Initialize the Gradio interface without immediately launching it
    interface = gr.Interface(
        fn=generate_response,
        inputs=[
            textbox, 
            num_beams_slider, 
            num_return_sequences_slider,
            max_new_tokens_slider, 
            repetition_penalty_slider,
            do_sample, 
            submit_button
            ],
        # inputs=[textbox, num_beams_slider, max_new_tokens_slider, do_sample_flag, stop_seq_textbox, run_button],
        outputs="text",
        live=False,
        allow_flagging="never"
    )

    # Set up the queue with desired parameters
    # For this example, I've set the concurrency_count to 3, meaning it will process up to 3 requests simultaneously.
    # You can adjust this based on your hardware capabilities.
    interface.queue(concurrency_count=3, status_update_rate="auto", api_open=True)

    # Now, launch the interface
    # interface.launch(height=200)
    interface.launch()


if __name__ == "__main__":
    main()
