import requests

class AreaResourceTests():
    def test_make_area_resource_request(self):
        uri = "http://api.football-data.org/v2/areas"
        token = {"X-Auth-Token": "5380111d819c4b0c888404c5b0a8ca2b"}
        response = requests.get(uri, headers=token)
        assert response.status_code == 200
