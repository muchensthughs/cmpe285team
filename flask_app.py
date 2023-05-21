from flask import Flask, render_template, request, session, url_for, redirect
import MySQLdb
from config import *
from utils import *
from stock_portfolio import Strategy, create_portfolio, calculate_weekly_trend

app = Flask(__name__)
app.secret_key = 'uihd3453'

db=MySQLdb.connect(MYSQL_HOST,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DB)

@app.route('/', methods=['GET'])
def index():
    if not session.get('username'):
        return render_template('index.html')
    else:
        return redirect(url_for('engine'))

@app.route('/test')
def test():
    return "test"


@app.route('/testmysql')
def testmysql():
    sql = "select * from user limit 1"
    res = executeSql(db, sql)
    return res[0][0]

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    sql = "select * from user where username = '%s' and password = '%s'" % (
        username, password)
    res = executeSql(db, sql)
    if len(res) < 1:
        return render_template('login_failed.html')
    else:
        # save username to session
        session['username'] = username
        # got to page that shows current plan etc.
        return redirect(url_for('engine'))

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))   


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        sql = "insert into user values ('%s', '%s')" % (username, password)
        try:
            executeSql(db, sql)
            db.commit()
        except Exception as e:
            return render_template('signup.html', message='Sign up failed, please try a different combination')
        return render_template('index.html')


# route for the Stock Portfolio Suggestion Engine
@app.route("/engine", methods=["GET", "POST"])
def engine():
    # Check if the request method is POST (form submission)
    if request.method == "POST":
        # Get the investment amount and selected strategies from the form
        investment_amount = float(request.form["investment_amount"])
        strategies = request.form.getlist("strategies")
        strategies_string = str(','.join(strategies))
        print("strategies", strategies_string)
        percentages = request.form.getlist("strategy_percentage")
        percentages = list(map(float, percentages))
        print("percentages", percentages)
        # Create the portfolio and weekly history based on the investment amount and strategies
        portfolio = create_portfolio(investment_amount, strategies, percentages)
        weekly_trend = calculate_weekly_trend(portfolio)

        # Render the portfolio and weekly history data
        return render_template(
            "portfolio_suggestion.html",
            portfolio=portfolio,
            weekly_trend=weekly_trend,
            investment_amount=investment_amount,
            strategies=strategies_string
        )
    # Render form
    return render_template("portfolio_suggestion.html")


# Run the app
if __name__ == "__main__":
    app.run(debug=True, port=8000)
