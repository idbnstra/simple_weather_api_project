from flask import Flask, request
import os,requests

app = Flask(__name__)

processed_text = ""

@app.route('/', methods =['GET'])
def home():
    construct_url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=605d3c54bdae1d30beb13262cde8a7e5"
    response = requests.get(construct_url)

    list_of_data = response.json()
    
    html_data = f"""
    <form method="POST">
        <input name="text">
        <input type="submit">
    </form>
    <table border="1">
    <tr>
        <td>country</td>
        <td>current city</td>
        <td>coordinate</td>
        <td>temp</td>
        <td>pressure</td>
        <td>humidity</td>
    </tr>
    <tr>

    
        <td>{str(list_of_data['sys']['country'])}</td>
        <td>{str(city)}</td>
        <td>{str(list_of_data['coord']['lon']) + ' '
                    + str(list_of_data['coord']['lat'])}</td>
        <td>{str(list_of_data['main']['temp']) + 'k'}</td>
        <td>{str(list_of_data['main']['pressure'])}</td>
        <td>{str(list_of_data['main']['humidity'])}</td>
    </tr>
    

    </table>
    """
    return html_data

city = "New York"
"""
@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text

city = processed_text
"""
if __name__ == "__main__":
    app.run(port = 8000,debug=True)