from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def translate():
    translated_text = ""
    error = ""

    if request.method == "POST":
        text = request.form.get("text", "").strip()
        source = request.form.get("source", "en")
        target = request.form.get("target", "hi")

        if not text:
            error = "Please enter some text to translate."
        elif source == target:
            translated_text = text
        else:
            try:
                translator = GoogleTranslator(
                    source=source,
                    target=target
                )
                translated_text = translator.translate(text)
            except Exception as e:
                error = f"Translation failed: {e}"

    return render_template(
        "index.html",
        translated_text=translated_text,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)