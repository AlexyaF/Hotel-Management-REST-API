from flask_restful import Resource
from models.site import SiteModel

class Sites(Resource):
    def get(self):
        return {'sites':[site.json() for site in SiteModel.query.all()]}
    
class Site(Resource):
    def get(self, url):
        site = SiteModel.find_site(url)
        if site:
            return site.json()
        return {"message":"Site not foud"}, 404

    def post(self, url):
        if SiteModel.find_site(url):
            return {"Message":f"The site '{url}' already exists"}, 400
        else:
            site = SiteModel(url)
            try:
                site.save_site()
                return site.json()
            except Exception as e :
                return {"Message":f"An internal error ocurred trying to create a new site - {e}"},500

    def delete(self, url):
        site = SiteModel.find_site(url)
        if site:
            site.deleted_site()
            return {"message": "Site deleted"}
        else:
            return {"message": "Site not found"}, 404