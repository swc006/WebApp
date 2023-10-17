from flask import Flask, render_template_string, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('base.html')

@app.route('/Datasets/Heart_Disease')  # Web address
def datasets_heartdisease():
    # You can pass any required variables as keyword arguments here, if needed
    return render_template('heartdisease.html')


@app.route('/page1/sub2')
def page1_sub2():
    return render_template_string('''
        <div class="container">
            <h1>This is Sub-page 1.2</h1>
        </div>
    ''')

@app.route('/page2/sub1')
def page2_sub1():
    return render_template_string('''
        <div class="container">
            <h1>This is Sub-page 2.1</h1>
        </div>
    ''')

@app.route('/page2/sub2')
def page2_sub2():
    return render_template_string('''
        <div class="container">
            <h1>This is Sub-page 2.2</h1>
        </div>
    ''')


if __name__ == '__main__':
    app.run(debug=True)
