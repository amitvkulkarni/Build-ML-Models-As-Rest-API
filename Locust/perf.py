import time
import json
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 3)

       
    @task(1)
    def testFlask(self):
        load = {
        "radius_mean": 13.54,
        "texture_mean": 14.36,
        "perimeter_mean": 87.46,
        "area_mean": 566.3,
        "smoothness_mean": 0.09779,
        "compactness_mean": 0.08129,
        "concavity_mean": 0.06664,
        "concave points_mean": 0.04781,
        "symmetry_mean": 0.1885,
        "fractal_dimension_mean": 0.05766,
        "radius_se": 0.2699,
        "texture_se": 0.7886,
        "perimeter_se": 2.058,
        "area_se": 23.56,
        "smoothness_se": 0.008462,
        "compactness_se": 0.0146,
        "concavity_se": 0.02387,
        "concave points_se": 0.01315,
        "symmetry_se": 0.0198,
        "fractal_dimension_se": 0.0023,
        "radius_worst": 15.11,
        "texture_worst": 19.26,
        "perimeter_worst": 99.7,
        "area_worst": 711.2,
        "smoothness_worst": 0.144,
        "compactness_worst": 0.1773,
        "concavity_worst": 0.239,
        "concave points_worst": 0.1288,
        "symmetry_worst": 0.2977,
        "fractal_dimension_worst": 0.07259}
        myheaders = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        self.client.post("/predict", data= json.dumps(load), headers=myheaders)
                

    # @task
    # def testFastAPI(self):
    #     self.client.post("/predict", data = json.dumps(load), headers=self)

