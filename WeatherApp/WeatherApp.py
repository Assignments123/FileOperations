from flask import Flask,request,render_template
from datetime import datetime
import weatherApi


weatherapp = Flask(__name__)

@weatherapp.route('/')
def test():
    data = ""
    return render_template('base.html',data=data)

@weatherapp.route('/weatherbyname',methods=['POST'])
def weatherbyname():
    '''
    The function to get temperature, humidity, winds, cloud, sunrise and sunset time of specific city
    '''
    # appid = os.getenv('APPID')
    city_name = request.form['city_name']
    country_name= request.form['country_name']

    if not city_name.isalpha():
        data = {
            "status":"error",
            "message":"Please enter Characters only"
        }
        return  render_template('base.html',data=data)
    
    if not country_name.isalpha():
        data = {
            "status":"error",
            "message":"Please enter Characters only"
        }
        return  render_template('base.html',data=data)
    # data = request.json 
    # city_name = data['city_name']
    # country_name = data['country_name']

    # unit matric for getting temperature in celcius
    # resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{country_name}&appid={appid}&units=metric').json()
    resp = weatherApi.weatherbyname(city_name,country_name)
    # check if getting correct response or not
    if resp.get('cod')!=200:
        data = "Please provide correct city and country name"
    else:
        print(resp.get('cod'))
        temp = resp.get('main').get('temp')
        humidity = resp.get('main').get('humidity')
        sunriseunix = resp.get('sys').get('sunrise') 
        sunsetunix = resp.get('sys').get('sunset')
        timezone = resp.get('sys').get('timezone')
        windspeed = resp.get('wind').get('speed')
        cloud = resp.get('clouds').get('all')
        
        sunrisetime = datetime.fromtimestamp(sunriseunix,timezone).time()
        sunsettime = datetime.fromtimestamp(sunsetunix,timezone).time()

        data = {
            "status":"success",
            "temperature":temp,
            "humidity": humidity,
            "sunrise":str(sunrisetime),
            "sunset":str(sunsettime),
            "windspeed":windspeed,
            "cloud":cloud
        }

    return  render_template('base.html',data=data,city_name=city_name,country_name=country_name)


@weatherapp.route('/weatherbycoords',methods=['POST'])
def weatherbycoords():
    '''
    The function to get temperature, humidity, winds, cloud, sunrise and sunset time of specific Coordinates
    '''
    # appid = os.getenv('APPID')
    lat = request.form['lat']
    lon = request.form['lon']
    # data = request.json
    # lat =  data['lat']
    # lon = data['lon']
    
    def is_float(string):
        try:
            float(string)
            return True
        except ValueError:
            return False
        
    if is_float(lat) and is_float(lon):

        # if not lat.isnumeric():
        #     data = "Please enter coordinates only"
        #     return  render_template('base.html',data=data)
        
        # if not lon.isnumeric():
        #     data = "Please enter coordinates only"
        #     return  render_template('base.html',data=data)
        # unit matric for getting temperature in celcius
        # url = 'https://api.openweathermap.org/data/2.5/weather?'
        # params = { 
        #     "lat" : lat,
        #     "lon" : lon,
        #     "appid": appid,
        #     "units" : "metric",
        # }
        # resp = requests.get(url,params=params).json()
        resp = weatherApi.weatherbycoords(lat,lon)
        # check if getting correct response or not
        if resp.get('cod')!=200:
            data = "please enter valid coordinates"
        else:
            print(type(resp))
            print(resp)
            temp = resp.get('main').get('temp')
            humidity = resp.get('main').get('humidity')
            sunriseunix = resp.get('sys').get('sunrise') 
            sunsetunix = resp.get('sys').get('sunset')
            timezone = resp.get('sys').get('timezone')
            windspeed = resp.get('wind').get('speed')
            cloud = resp.get('clouds').get('all')
            
            sunrisetime = datetime.fromtimestamp(sunriseunix,timezone).time()
            sunsettime = datetime.fromtimestamp(sunsetunix,timezone).time()
            data = {
                "status":"success",
                "temperature":temp,
                "humidity": humidity,
                "sunrise":str(sunrisetime),
                "sunset":str(sunsettime),
                "windspeed":windspeed,
                "cloud":cloud

            }
        return  render_template('base.html',data=data,lat=lat,lon=lon)
    else:
        data ={
            "status" : "error",
            "message" : "please provide coordinates only"
        }
    return  render_template('base.html',data=data)


@weatherapp.route('/tester')
def tester():
    data = weatherApi.weatherbyname()
    return data


weatherapp.run(debug = True)
