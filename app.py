from flask import Flask, render_template, request

import requests 

from searcher import Searching

app = Flask(__name__)


searching = Searching()    
    
@app.route('/')
def welcome_page():
    return render_template('hello.html') 

@app.route('/generic_name', methods = ["POST", "GET"])
def generic():
    if request.method == "POST":
        drug_name = request.form['drug_name']
        action = request.form['action']
              
        if action == "reaction":
            drug_list = searching.search_generic_reaction(drug_name)
            if drug_list is None: 
                return render_template('not_found.html')
            return render_template('reactions.html', drugs = drug_list.to_html())
        
        if action == "indication":
            drug_list_indication = searching.search_generic_indication(drug_name)
            if drug_list_indication is None: 
                return render_template('not_found.html')
            return render_template('indications.html', drugs = drug_list_indication.to_html())
        
        if action == "interaction":
            interaction_list = searching.search_generic_interaction(drug_name)
            if interaction_list is None:
                return render_template('not_found.html')
            return render_template('interactions.html', interactions = interaction_list) 
        
    return render_template('form.html', type = "Generic")

@app.route('/brand_name', methods = ["POST", "GET"])
def brand():
    if request.method == "POST":
        drug_name = request.form['drug_name']
        action = request.form['action']
        
        if action == "reaction":
            drug_list = searching.search_brand_reaction(drug_name)
            if drug_list is None: 
                return render_template('not_found.html')
            return render_template('reactions.html', drugs = drug_list.to_html())
        
        if action == "indication":
            drug_list_indication = searching.search_brand_indication(drug_name)
            if drug_list_indication is None: 
                return render_template('not_found.html')
            return render_template('indications.html', drugs = drug_list_indication.to_html())
        
        if action == "interaction":
            interaction_list = searching.search_brand_interaction(drug_name)
            if interaction_list is None: 
                return render_template('not_found.html')
            return render_template('interactions.html', interactions = interaction_list) 
        
    return render_template('form.html', type = "Brand")

if __name__ == '__main__':
    app.run(debug=True)
