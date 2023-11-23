from flask import jsonify, request
from flask.views import MethodView
from flask_smorest import Blueprint

from countries import data

blp = Blueprint("countries", __name__)

@blp.route("/")
class IndexClass(MethodView):
    def get(self):
        return {"message": "Welcome to the countries api. Use the /countries endpoint"}

@blp.route("/countries")
class CountriesClass(MethodView):
    # READ ALL
    def get(self):
        return jsonify(data), 200
    
    # CREATE ONE - PUT TRY EXCEPT HERE - USE ASSERT TO CHECK DATA TYPES HERE
    def post(self):
        country_data = request.form.get("country")
        population_data = request.form.get("population")
        new_country = {"country": country_data, "population": population_data}
        data.append(new_country)
        return {
            "message": "New country added. Please make GET request to the /countries endpoint.",
            "details": new_country
            }

@blp.route("/countries/<string:country_name>")
class CountryClass(MethodView):
    # GET ONE
    def get(self, country_name):
        for country in data:
            if country_name == country["country"]:
                return country

    # UPDATE ONE - PUT TRY EXCEPT HERE - USE ASSERT TO CHECK DATA TYPES HERE
    def put(self, country_name):
        country_data = request.form.get("country")
        population_data = request.form.get("population")
        for country in data:
            if country_name == country["country"]:
                country["country"] = country_data
                country["population"] = population_data
                return {"message": "Country updated. Please make GET request to the /countries endpoint."}

    # DELETE ONE
    def delete(self, country_name):
        for country in data:
            if country_name == country["country"]:
                country["country"] = None
                country["population"] = None
                return {"message": "country deleted"}