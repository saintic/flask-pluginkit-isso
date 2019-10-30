from flask import Flask, render_template_string
from flask_pluginkit import PluginManager

app = Flask(__name__)
app.config.update(
    ISSO_API="/isso/test",
)
plugin = PluginManager(app, plugin_packages=["flask_pluginkit_isso"])


@app.route("/")
def index():
    return render_template_string("""
<html>
    <head>
    </head>
    <body>
        {{ emit_tep("isso_content", title="flask_pluginkit_isso") }}
        {{ emit_tep("isso_script") }}
    </body>
</html>""")


if __name__ == "__main__":
    app.run(debug=True)
