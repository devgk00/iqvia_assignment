import feedparser

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def search_disease():
    if request.method == 'POST':
        try:
            form_data = request.form
            if 'name' not in form_data or 'days' not in form_data:
                raise Exception
            name = form_data['name'].replace(' ', '+')
            url = f"https://clinicaltrials.gov/ct2/results/rss.xml?rcv_d={form_data['days']}&lup_d={form_data['days']}&cond={name}&count=1"
            data = feedparser.parse(url)
            result = {
                "message": "",
                "color": "",
                "title": data.feed.title,
                "link": data.feed.link.replace('/rss.xml', ''),
            }
            if len(data.entries) > 0:
                result['color'] = 'green'
                result["message"] = f"Activity performed on disease: {form_data['name']} in last {form_data['days']} days."
                return render_template('search_disease.html', data=form_data, result=result), 201
            else:
                result["link"] = ""
                result["color"] = "red"
                result["message"] = f"No Activity performed on disease: {form_data['name']} in last {form_data['days']} days."
                return render_template('search_disease.html', data=form_data, result=result), 201
        except Exception as error:
            return render_template('search_disease.html', error=str(error)), 404
    else:
        return render_template('search_disease.html'), 200


if __name__ == '__main__':
    app.run()
