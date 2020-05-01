from covid19_sim import app

# comment experiment

app.config['DEBUG'] = True

if __name__ == "__main__":
    app.run(
        debug = app.config['DEBUG'],
        port = 5000
    )
