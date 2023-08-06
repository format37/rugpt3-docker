from gradio_client import Client

client = Client("http://localhost:7860/")
text = """Загадка:
Дом на улице стоит,
Детвора к нему спешит.
Несут тетрадки, книжки
Девчонки и мальчишки.

Ответ:"""
result = client.predict(
				text,	# str in 'Your Input' Textbox component
				10,	# int | float (numeric value between 1 and 10) in 'Num Beams' Slider component
				2,	# int | float (numeric value between 1 and 10) in 'Num Return Sequences' Slider component
				50,	# int | float (numeric value between 10 and 800) in 'Max New Tokens' Slider component
				2,	# int | float (numeric value between 0.0 and 2.0) in 'Repetition Penalty' Slider component
				True,	# bool in 'Do Sample' Checkbox component
				"",	# str in 'parameter_6' Button component
				api_name="/predict"
)
print(result)