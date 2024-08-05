from flask import Flask, request, render_template_string

app = Flask(__name__)

def handDim(head_length):
    hand_length = round(0.75 * head_length, 2)
    hand_circumference = round(6.1537 * hand_length, 2)
    palm_length = round((0.23 * hand_circumference) + 5.57, 2)
    hand_breadth = round((0.32 * hand_circumference) + 1.88, 2)
    thumb_crotch_length = round((0.15 * hand_length) + 3.85, 2)  # Example formula, adjust as necessary
    hand_breadth_thumb = round((0.28 * hand_length) + 2.7, 2)     # Example formula, adjust as necessary
    hand_circ_thumb = round((0.4 * hand_length) + 6.8, 2)         # Example formula, adjust as necessary
    fist_circumference = round((0.95 * hand_length) + 10.0, 2)    # Example formula, adjust as necessary
    wrist_circumference = round((0.3 * hand_length) + 4.5, 2)     # Example formula, adjust as necessary
    hand_thickness = round((0.25 * hand_length) + 1.2, 2)         # Example formula, adjust as necessary

    return (
        f"hand_length = {hand_length} cm",
        f"hand_circumference = {hand_circumference} cm",
        f"palm_length = {palm_length} cm",
        f"hand_breadth = {hand_breadth} cm",
        f"thumb_crotch_length = {thumb_crotch_length} cm",
        f"hand_breadth_at_thumb = {hand_breadth_thumb} cm",
        f"hand_circumference_at_thumb = {hand_circ_thumb} cm",
        f"fist_circumference = {fist_circumference} cm",
        f"wrist_circumference = {wrist_circumference} cm",
        f"hand_thickness = {hand_thickness} cm"
    )

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        head_length = float(request.form['head_length'])
        measurements = handDim(head_length)
        return render_template_string(TEMPLATE, measurements=measurements)
    return render_template_string(TEMPLATE)

TEMPLATE = '''
<!doctype html>
<html lang="en">
  <head>
    <title>Hand Dimension Calculator</title>
  </head>
  <body>
    <h1>Hand Dimension Calculator</h1>
    <form method="POST">
      <label for="head_length">Enter Head Length in cm:</label>
      <input type="text" id="head_length" name="head_length">
      <input type="submit" value="Calculate">
    </form>
    {% if measurements %}
    <h2>Calculated Hand Dimensions:</h2>
    <ul>
      {% for measurement in measurements %}
      <li>{{ measurement }}</li>
      {% endfor %}
    </ul>
    {% endif %}
  </body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
