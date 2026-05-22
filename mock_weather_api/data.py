"""
Static fixture data for mock weather API, converted for Indian states and cities.
"""

WEATHER_DATA = {
    "jodhpur": {
        "coord": {
            "lon": 73.0,
            "lat": 15.0
        },
        "weather": [
            {
                "id": 800,
                "main": "Clear",
                "description": "clear sky",
                "icon": "01d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 293.15,
            "feels_like": 294.65,
            "temp_min": 291.15,
            "temp_max": 295.15,
            "pressure": 1010,
            "humidity": 40
        },
        "visibility": 10000,
        "wind": {
            "speed": 1.0,
            "deg": 0
        },
        "clouds": {
            "all": 0
        },
        "dt": 1718870000,
        "sys": {
            "type": 1,
            "id": 9000,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200000,
        "name": "Jodhpur",
        "cod": 200
    },
    "maharashtra": {
        "coord": {
            "lon": 75.7,
            "lat": 18.1
        },
        "weather": [
            {
                "id": 802,
                "main": "Clouds",
                "description": "scattered clouds",
                "icon": "03d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 306.15,
            "feels_like": 307.65,
            "temp_min": 304.15,
            "temp_max": 308.15,
            "pressure": 1011,
            "humidity": 47
        },
        "visibility": 9000,
        "wind": {
            "speed": 4.0,
            "deg": 27
        },
        "clouds": {
            "all": 40
        },
        "dt": 1718870010,
        "sys": {
            "type": 1,
            "id": 9001,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200001,
        "name": "Maharashtra",
        "cod": 200
    },
    "arunachal pradesh": {
        "coord": {
            "lon": 78.4,
            "lat": 21.2
        },
        "weather": [
            {
                "id": 500,
                "main": "Rain",
                "description": "light rain",
                "icon": "10d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 304.15,
            "feels_like": 305.65,
            "temp_min": 302.15,
            "temp_max": 306.15,
            "pressure": 1012,
            "humidity": 54
        },
        "visibility": 8000,
        "wind": {
            "speed": 1.0,
            "deg": 54
        },
        "clouds": {
            "all": 75
        },
        "dt": 1718870020,
        "sys": {
            "type": 1,
            "id": 9002,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200002,
        "name": "Arunachal Pradesh",
        "cod": 200
    },
    "vasai-virar": {
        "coord": {
            "lon": 81.1,
            "lat": 24.3
        },
        "weather": [
            {
                "id": 711,
                "main": "Smoke",
                "description": "smoke",
                "icon": "50d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 302.15,
            "feels_like": 303.65,
            "temp_min": 300.15,
            "temp_max": 304.15,
            "pressure": 1013,
            "humidity": 61
        },
        "visibility": 7000,
        "wind": {
            "speed": 4.0,
            "deg": 81
        },
        "clouds": {
            "all": 20
        },
        "dt": 1718870030,
        "sys": {
            "type": 1,
            "id": 9003,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200003,
        "name": "Vasai-Virar",
        "cod": 200
    },
    "meerut": {
        "coord": {
            "lon": 73.8,
            "lat": 17.4
        },
        "weather": [
            {
                "id": 200,
                "main": "Thunderstorm",
                "description": "thunderstorm with light rain",
                "icon": "11d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 300.15,
            "feels_like": 301.65,
            "temp_min": 298.15,
            "temp_max": 302.15,
            "pressure": 1014,
            "humidity": 68
        },
        "visibility": 6000,
        "wind": {
            "speed": 1.0,
            "deg": 108
        },
        "clouds": {
            "all": 90
        },
        "dt": 1718870040,
        "sys": {
            "type": 1,
            "id": 9004,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200004,
        "name": "Meerut",
        "cod": 200
    },
    "uttar pradesh": {
        "coord": {
            "lon": 76.5,
            "lat": 20.5
        },
        "weather": [
            {
                "id": 800,
                "main": "Clear",
                "description": "clear sky",
                "icon": "01d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 298.15,
            "feels_like": 299.65,
            "temp_min": 296.15,
            "temp_max": 300.15,
            "pressure": 1015,
            "humidity": 75
        },
        "visibility": 10000,
        "wind": {
            "speed": 4.0,
            "deg": 135
        },
        "clouds": {
            "all": 0
        },
        "dt": 1718870050,
        "sys": {
            "type": 1,
            "id": 9005,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200005,
        "name": "Uttar Pradesh",
        "cod": 200
    },
    "thane": {
        "coord": {
            "lon": 79.2,
            "lat": 23.6
        },
        "weather": [
            {
                "id": 802,
                "main": "Clouds",
                "description": "scattered clouds",
                "icon": "03d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 296.15,
            "feels_like": 297.65,
            "temp_min": 294.15,
            "temp_max": 298.15,
            "pressure": 1016,
            "humidity": 82
        },
        "visibility": 9000,
        "wind": {
            "speed": 1.0,
            "deg": 162
        },
        "clouds": {
            "all": 40
        },
        "dt": 1718870060,
        "sys": {
            "type": 1,
            "id": 9006,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200006,
        "name": "Thane",
        "cod": 200
    },
    "manipur": {
        "coord": {
            "lon": 81.9,
            "lat": 16.7
        },
        "weather": [
            {
                "id": 500,
                "main": "Rain",
                "description": "light rain",
                "icon": "10d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 294.15,
            "feels_like": 295.65,
            "temp_min": 292.15,
            "temp_max": 296.15,
            "pressure": 1017,
            "humidity": 89
        },
        "visibility": 8000,
        "wind": {
            "speed": 4.0,
            "deg": 189
        },
        "clouds": {
            "all": 75
        },
        "dt": 1718870070,
        "sys": {
            "type": 1,
            "id": 9007,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200007,
        "name": "Manipur",
        "cod": 200
    },
    "tripura": {
        "coord": {
            "lon": 74.6,
            "lat": 19.8
        },
        "weather": [
            {
                "id": 711,
                "main": "Smoke",
                "description": "smoke",
                "icon": "50d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 307.15,
            "feels_like": 308.65,
            "temp_min": 305.15,
            "temp_max": 309.15,
            "pressure": 1018,
            "humidity": 46
        },
        "visibility": 7000,
        "wind": {
            "speed": 1.0,
            "deg": 216
        },
        "clouds": {
            "all": 20
        },
        "dt": 1718870080,
        "sys": {
            "type": 1,
            "id": 9008,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200008,
        "name": "Tripura",
        "cod": 200
    },
    "jabalpur": {
        "coord": {
            "lon": 77.3,
            "lat": 22.9
        },
        "weather": [
            {
                "id": 200,
                "main": "Thunderstorm",
                "description": "thunderstorm with light rain",
                "icon": "11d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 305.15,
            "feels_like": 306.65,
            "temp_min": 303.15,
            "temp_max": 307.15,
            "pressure": 1019,
            "humidity": 53
        },
        "visibility": 6000,
        "wind": {
            "speed": 4.0,
            "deg": 243
        },
        "clouds": {
            "all": 90
        },
        "dt": 1718870090,
        "sys": {
            "type": 1,
            "id": 9009,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200009,
        "name": "Jabalpur",
        "cod": 200
    },
    "nagaland": {
        "coord": {
            "lon": 80.0,
            "lat": 16.0
        },
        "weather": [
            {
                "id": 800,
                "main": "Clear",
                "description": "clear sky",
                "icon": "01d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 303.15,
            "feels_like": 304.65,
            "temp_min": 301.15,
            "temp_max": 305.15,
            "pressure": 1010,
            "humidity": 60
        },
        "visibility": 10000,
        "wind": {
            "speed": 1.0,
            "deg": 270
        },
        "clouds": {
            "all": 0
        },
        "dt": 1718870100,
        "sys": {
            "type": 1,
            "id": 9010,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200010,
        "name": "Nagaland",
        "cod": 200
    },
    "pimpri-chinchwad": {
        "coord": {
            "lon": 82.7,
            "lat": 19.1
        },
        "weather": [
            {
                "id": 802,
                "main": "Clouds",
                "description": "scattered clouds",
                "icon": "03d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 301.15,
            "feels_like": 302.65,
            "temp_min": 299.15,
            "temp_max": 303.15,
            "pressure": 1011,
            "humidity": 67
        },
        "visibility": 9000,
        "wind": {
            "speed": 4.0,
            "deg": 297
        },
        "clouds": {
            "all": 40
        },
        "dt": 1718870110,
        "sys": {
            "type": 1,
            "id": 9011,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200011,
        "name": "Pimpri-Chinchwad",
        "cod": 200
    },
    "amritsar": {
        "coord": {
            "lon": 75.4,
            "lat": 22.2
        },
        "weather": [
            {
                "id": 500,
                "main": "Rain",
                "description": "light rain",
                "icon": "10d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 299.15,
            "feels_like": 300.65,
            "temp_min": 297.15,
            "temp_max": 301.15,
            "pressure": 1012,
            "humidity": 74
        },
        "visibility": 8000,
        "wind": {
            "speed": 1.0,
            "deg": 324
        },
        "clouds": {
            "all": 75
        },
        "dt": 1718870120,
        "sys": {
            "type": 1,
            "id": 9012,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200012,
        "name": "Amritsar",
        "cod": 200
    },
    "meghalaya": {
        "coord": {
            "lon": 78.1,
            "lat": 15.3
        },
        "weather": [
            {
                "id": 711,
                "main": "Smoke",
                "description": "smoke",
                "icon": "50d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 297.15,
            "feels_like": 298.65,
            "temp_min": 295.15,
            "temp_max": 299.15,
            "pressure": 1013,
            "humidity": 81
        },
        "visibility": 7000,
        "wind": {
            "speed": 4.0,
            "deg": 351
        },
        "clouds": {
            "all": 20
        },
        "dt": 1718870130,
        "sys": {
            "type": 1,
            "id": 9013,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200013,
        "name": "Meghalaya",
        "cod": 200
    },
    "telangana": {
        "coord": {
            "lon": 80.8,
            "lat": 18.4
        },
        "weather": [
            {
                "id": 200,
                "main": "Thunderstorm",
                "description": "thunderstorm with light rain",
                "icon": "11d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 295.15,
            "feels_like": 296.65,
            "temp_min": 293.15,
            "temp_max": 297.15,
            "pressure": 1014,
            "humidity": 88
        },
        "visibility": 6000,
        "wind": {
            "speed": 1.0,
            "deg": 18
        },
        "clouds": {
            "all": 90
        },
        "dt": 1718870140,
        "sys": {
            "type": 1,
            "id": 9014,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200014,
        "name": "Telangana",
        "cod": 200
    },
    "gujarat": {
        "coord": {
            "lon": 73.5,
            "lat": 21.5
        },
        "weather": [
            {
                "id": 800,
                "main": "Clear",
                "description": "clear sky",
                "icon": "01d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 298.15,
            "feels_like": 299.65,
            "temp_min": 296.15,
            "temp_max": 300.15,
            "pressure": 1015,
            "humidity": 45
        },
        "visibility": 10000,
        "wind": {
            "speed": 4.0,
            "deg": 45
        },
        "clouds": {
            "all": 0
        },
        "dt": 1718870150,
        "sys": {
            "type": 1,
            "id": 9015,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200015,
        "name": "Gujarat",
        "cod": 200
    },
    "coimbatore": {
        "coord": {
            "lon": 76.2,
            "lat": 24.6
        },
        "weather": [
            {
                "id": 802,
                "main": "Clouds",
                "description": "scattered clouds",
                "icon": "03d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 306.15,
            "feels_like": 307.65,
            "temp_min": 304.15,
            "temp_max": 308.15,
            "pressure": 1016,
            "humidity": 52
        },
        "visibility": 9000,
        "wind": {
            "speed": 1.0,
            "deg": 72
        },
        "clouds": {
            "all": 40
        },
        "dt": 1718870160,
        "sys": {
            "type": 1,
            "id": 9016,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200016,
        "name": "Coimbatore",
        "cod": 200
    },
    "nagpur": {
        "coord": {
            "lon": 78.9,
            "lat": 17.7
        },
        "weather": [
            {
                "id": 500,
                "main": "Rain",
                "description": "light rain",
                "icon": "10d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 304.15,
            "feels_like": 305.65,
            "temp_min": 302.15,
            "temp_max": 306.15,
            "pressure": 1017,
            "humidity": 59
        },
        "visibility": 8000,
        "wind": {
            "speed": 4.0,
            "deg": 99
        },
        "clouds": {
            "all": 75
        },
        "dt": 1718870170,
        "sys": {
            "type": 1,
            "id": 9017,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200017,
        "name": "Nagpur",
        "cod": 200
    },
    "chandigarh": {
        "coord": {
            "lon": 81.6,
            "lat": 20.8
        },
        "weather": [
            {
                "id": 711,
                "main": "Smoke",
                "description": "smoke",
                "icon": "50d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 302.15,
            "feels_like": 303.65,
            "temp_min": 300.15,
            "temp_max": 304.15,
            "pressure": 1018,
            "humidity": 66
        },
        "visibility": 7000,
        "wind": {
            "speed": 1.0,
            "deg": 126
        },
        "clouds": {
            "all": 20
        },
        "dt": 1718870180,
        "sys": {
            "type": 1,
            "id": 9018,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200018,
        "name": "Chandigarh",
        "cod": 200
    },
    "tamil nadu": {
        "coord": {
            "lon": 74.3,
            "lat": 23.9
        },
        "weather": [
            {
                "id": 200,
                "main": "Thunderstorm",
                "description": "thunderstorm with light rain",
                "icon": "11d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 300.15,
            "feels_like": 301.65,
            "temp_min": 298.15,
            "temp_max": 302.15,
            "pressure": 1019,
            "humidity": 73
        },
        "visibility": 6000,
        "wind": {
            "speed": 4.0,
            "deg": 153
        },
        "clouds": {
            "all": 90
        },
        "dt": 1718870190,
        "sys": {
            "type": 1,
            "id": 9019,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200019,
        "name": "Tamil Nadu",
        "cod": 200
    },
    "kerala": {
        "coord": {
            "lon": 77.0,
            "lat": 17.0
        },
        "weather": [
            {
                "id": 800,
                "main": "Clear",
                "description": "clear sky",
                "icon": "01d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 298.15,
            "feels_like": 299.65,
            "temp_min": 296.15,
            "temp_max": 300.15,
            "pressure": 1010,
            "humidity": 80
        },
        "visibility": 10000,
        "wind": {
            "speed": 1.0,
            "deg": 180
        },
        "clouds": {
            "all": 0
        },
        "dt": 1718870200,
        "sys": {
            "type": 1,
            "id": 9020,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200020,
        "name": "Kerala",
        "cod": 200
    },
    "nashik": {
        "coord": {
            "lon": 79.7,
            "lat": 20.1
        },
        "weather": [
            {
                "id": 802,
                "main": "Clouds",
                "description": "scattered clouds",
                "icon": "03d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 296.15,
            "feels_like": 297.65,
            "temp_min": 294.15,
            "temp_max": 298.15,
            "pressure": 1011,
            "humidity": 87
        },
        "visibility": 9000,
        "wind": {
            "speed": 4.0,
            "deg": 207
        },
        "clouds": {
            "all": 40
        },
        "dt": 1718870210,
        "sys": {
            "type": 1,
            "id": 9021,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200021,
        "name": "Nashik",
        "cod": 200
    },
    "pune": {
        "coord": {
            "lon": 82.4,
            "lat": 23.2
        },
        "weather": [
            {
                "id": 500,
                "main": "Rain",
                "description": "light rain",
                "icon": "10d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 294.15,
            "feels_like": 295.65,
            "temp_min": 292.15,
            "temp_max": 296.15,
            "pressure": 1012,
            "humidity": 44
        },
        "visibility": 8000,
        "wind": {
            "speed": 1.0,
            "deg": 234
        },
        "clouds": {
            "all": 75
        },
        "dt": 1718870220,
        "sys": {
            "type": 1,
            "id": 9022,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200022,
        "name": "Pune",
        "cod": 200
    },
    "jharkhand": {
        "coord": {
            "lon": 75.1,
            "lat": 16.3
        },
        "weather": [
            {
                "id": 711,
                "main": "Smoke",
                "description": "smoke",
                "icon": "50d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 307.15,
            "feels_like": 308.65,
            "temp_min": 305.15,
            "temp_max": 309.15,
            "pressure": 1013,
            "humidity": 51
        },
        "visibility": 7000,
        "wind": {
            "speed": 4.0,
            "deg": 261
        },
        "clouds": {
            "all": 20
        },
        "dt": 1718870230,
        "sys": {
            "type": 1,
            "id": 9023,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200023,
        "name": "Jharkhand",
        "cod": 200
    },
    "chennai": {
        "coord": {
            "lon": 77.8,
            "lat": 19.4
        },
        "weather": [
            {
                "id": 200,
                "main": "Thunderstorm",
                "description": "thunderstorm with light rain",
                "icon": "11d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 305.15,
            "feels_like": 306.65,
            "temp_min": 303.15,
            "temp_max": 307.15,
            "pressure": 1014,
            "humidity": 58
        },
        "visibility": 6000,
        "wind": {
            "speed": 1.0,
            "deg": 288
        },
        "clouds": {
            "all": 90
        },
        "dt": 1718870240,
        "sys": {
            "type": 1,
            "id": 9024,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200024,
        "name": "Chennai",
        "cod": 200
    },
    "rajkot": {
        "coord": {
            "lon": 80.5,
            "lat": 22.5
        },
        "weather": [
            {
                "id": 800,
                "main": "Clear",
                "description": "clear sky",
                "icon": "01d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 303.15,
            "feels_like": 304.65,
            "temp_min": 301.15,
            "temp_max": 305.15,
            "pressure": 1015,
            "humidity": 65
        },
        "visibility": 10000,
        "wind": {
            "speed": 4.0,
            "deg": 315
        },
        "clouds": {
            "all": 0
        },
        "dt": 1718870250,
        "sys": {
            "type": 1,
            "id": 9025,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200025,
        "name": "Rajkot",
        "cod": 200
    },
    "puducherry": {
        "coord": {
            "lon": 73.2,
            "lat": 15.6
        },
        "weather": [
            {
                "id": 802,
                "main": "Clouds",
                "description": "scattered clouds",
                "icon": "03d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 301.15,
            "feels_like": 302.65,
            "temp_min": 299.15,
            "temp_max": 303.15,
            "pressure": 1016,
            "humidity": 72
        },
        "visibility": 9000,
        "wind": {
            "speed": 1.0,
            "deg": 342
        },
        "clouds": {
            "all": 40
        },
        "dt": 1718870260,
        "sys": {
            "type": 1,
            "id": 9026,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200026,
        "name": "Puducherry",
        "cod": 200
    },
    "haryana": {
        "coord": {
            "lon": 75.9,
            "lat": 18.7
        },
        "weather": [
            {
                "id": 500,
                "main": "Rain",
                "description": "light rain",
                "icon": "10d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 299.15,
            "feels_like": 300.65,
            "temp_min": 297.15,
            "temp_max": 301.15,
            "pressure": 1017,
            "humidity": 79
        },
        "visibility": 8000,
        "wind": {
            "speed": 4.0,
            "deg": 9
        },
        "clouds": {
            "all": 75
        },
        "dt": 1718870270,
        "sys": {
            "type": 1,
            "id": 9027,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200027,
        "name": "Haryana",
        "cod": 200
    },
    "odisha": {
        "coord": {
            "lon": 78.6,
            "lat": 21.8
        },
        "weather": [
            {
                "id": 711,
                "main": "Smoke",
                "description": "smoke",
                "icon": "50d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 297.15,
            "feels_like": 298.65,
            "temp_min": 295.15,
            "temp_max": 299.15,
            "pressure": 1018,
            "humidity": 86
        },
        "visibility": 7000,
        "wind": {
            "speed": 1.0,
            "deg": 36
        },
        "clouds": {
            "all": 20
        },
        "dt": 1718870280,
        "sys": {
            "type": 1,
            "id": 9028,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200028,
        "name": "Odisha",
        "cod": 200
    },
    "rajasthan": {
        "coord": {
            "lon": 81.3,
            "lat": 24.9
        },
        "weather": [
            {
                "id": 200,
                "main": "Thunderstorm",
                "description": "thunderstorm with light rain",
                "icon": "11d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 300.15,
            "feels_like": 301.65,
            "temp_min": 298.15,
            "temp_max": 302.15,
            "pressure": 1019,
            "humidity": 43
        },
        "visibility": 6000,
        "wind": {
            "speed": 4.0,
            "deg": 63
        },
        "clouds": {
            "all": 90
        },
        "dt": 1718870290,
        "sys": {
            "type": 1,
            "id": 9029,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200029,
        "name": "Rajasthan",
        "cod": 200
    },
    "ladakh": {
        "coord": {
            "lon": 74.0,
            "lat": 18.0
        },
        "weather": [
            {
                "id": 800,
                "main": "Clear",
                "description": "clear sky",
                "icon": "01d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 278.15,
            "feels_like": 279.65,
            "temp_min": 276.15,
            "temp_max": 280.15,
            "pressure": 1010,
            "humidity": 50
        },
        "visibility": 10000,
        "wind": {
            "speed": 1.0,
            "deg": 90
        },
        "clouds": {
            "all": 0
        },
        "dt": 1718870300,
        "sys": {
            "type": 1,
            "id": 9030,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200030,
        "name": "Ladakh",
        "cod": 200
    },
    "madurai": {
        "coord": {
            "lon": 76.7,
            "lat": 21.1
        },
        "weather": [
            {
                "id": 802,
                "main": "Clouds",
                "description": "scattered clouds",
                "icon": "03d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 306.15,
            "feels_like": 307.65,
            "temp_min": 304.15,
            "temp_max": 308.15,
            "pressure": 1011,
            "humidity": 57
        },
        "visibility": 9000,
        "wind": {
            "speed": 4.0,
            "deg": 117
        },
        "clouds": {
            "all": 40
        },
        "dt": 1718870310,
        "sys": {
            "type": 1,
            "id": 9031,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200031,
        "name": "Madurai",
        "cod": 200
    },
    "srinagar": {
        "coord": {
            "lon": 79.4,
            "lat": 24.2
        },
        "weather": [
            {
                "id": 500,
                "main": "Rain",
                "description": "light rain",
                "icon": "10d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 289.15,
            "feels_like": 290.65,
            "temp_min": 287.15,
            "temp_max": 291.15,
            "pressure": 1012,
            "humidity": 64
        },
        "visibility": 8000,
        "wind": {
            "speed": 1.0,
            "deg": 144
        },
        "clouds": {
            "all": 75
        },
        "dt": 1718870320,
        "sys": {
            "type": 1,
            "id": 9032,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200032,
        "name": "Srinagar",
        "cod": 200
    },
    "indore": {
        "coord": {
            "lon": 82.1,
            "lat": 17.3
        },
        "weather": [
            {
                "id": 711,
                "main": "Smoke",
                "description": "smoke",
                "icon": "50d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 302.15,
            "feels_like": 303.65,
            "temp_min": 300.15,
            "temp_max": 304.15,
            "pressure": 1013,
            "humidity": 71
        },
        "visibility": 7000,
        "wind": {
            "speed": 4.0,
            "deg": 171
        },
        "clouds": {
            "all": 20
        },
        "dt": 1718870330,
        "sys": {
            "type": 1,
            "id": 9033,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200033,
        "name": "Indore",
        "cod": 200
    },
    "uttarakhand": {
        "coord": {
            "lon": 74.8,
            "lat": 20.4
        },
        "weather": [
            {
                "id": 200,
                "main": "Thunderstorm",
                "description": "thunderstorm with light rain",
                "icon": "11d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 300.15,
            "feels_like": 301.65,
            "temp_min": 298.15,
            "temp_max": 302.15,
            "pressure": 1014,
            "humidity": 78
        },
        "visibility": 6000,
        "wind": {
            "speed": 1.0,
            "deg": 198
        },
        "clouds": {
            "all": 90
        },
        "dt": 1718870340,
        "sys": {
            "type": 1,
            "id": 9034,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200034,
        "name": "Uttarakhand",
        "cod": 200
    },
    "ranchi": {
        "coord": {
            "lon": 77.5,
            "lat": 23.5
        },
        "weather": [
            {
                "id": 800,
                "main": "Clear",
                "description": "clear sky",
                "icon": "01d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 298.15,
            "feels_like": 299.65,
            "temp_min": 296.15,
            "temp_max": 300.15,
            "pressure": 1015,
            "humidity": 85
        },
        "visibility": 10000,
        "wind": {
            "speed": 4.0,
            "deg": 225
        },
        "clouds": {
            "all": 0
        },
        "dt": 1718870350,
        "sys": {
            "type": 1,
            "id": 9035,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200035,
        "name": "Ranchi",
        "cod": 200
    },
    "delhi": {
        "coord": {
            "lon": 80.2,
            "lat": 16.6
        },
        "weather": [
            {
                "id": 802,
                "main": "Clouds",
                "description": "scattered clouds",
                "icon": "03d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 296.15,
            "feels_like": 297.65,
            "temp_min": 294.15,
            "temp_max": 298.15,
            "pressure": 1016,
            "humidity": 42
        },
        "visibility": 9000,
        "wind": {
            "speed": 1.0,
            "deg": 252
        },
        "clouds": {
            "all": 40
        },
        "dt": 1718870360,
        "sys": {
            "type": 1,
            "id": 9036,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200036,
        "name": "Delhi",
        "cod": 200
    },
    "patna": {
        "coord": {
            "lon": 82.9,
            "lat": 19.7
        },
        "weather": [
            {
                "id": 500,
                "main": "Rain",
                "description": "light rain",
                "icon": "10d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 294.15,
            "feels_like": 295.65,
            "temp_min": 292.15,
            "temp_max": 296.15,
            "pressure": 1017,
            "humidity": 49
        },
        "visibility": 8000,
        "wind": {
            "speed": 4.0,
            "deg": 279
        },
        "clouds": {
            "all": 75
        },
        "dt": 1718870370,
        "sys": {
            "type": 1,
            "id": 9037,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200037,
        "name": "Patna",
        "cod": 200
    },
    "mumbai": {
        "coord": {
            "lon": 75.6,
            "lat": 22.8
        },
        "weather": [
            {
                "id": 711,
                "main": "Smoke",
                "description": "smoke",
                "icon": "50d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 307.15,
            "feels_like": 308.65,
            "temp_min": 305.15,
            "temp_max": 309.15,
            "pressure": 1018,
            "humidity": 56
        },
        "visibility": 7000,
        "wind": {
            "speed": 1.0,
            "deg": 306
        },
        "clouds": {
            "all": 20
        },
        "dt": 1718870380,
        "sys": {
            "type": 1,
            "id": 9038,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200038,
        "name": "Mumbai",
        "cod": 200
    },
    "himachal pradesh": {
        "coord": {
            "lon": 78.3,
            "lat": 15.9
        },
        "weather": [
            {
                "id": 200,
                "main": "Thunderstorm",
                "description": "thunderstorm with light rain",
                "icon": "11d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 290.15,
            "feels_like": 291.65,
            "temp_min": 288.15,
            "temp_max": 292.15,
            "pressure": 1019,
            "humidity": 63
        },
        "visibility": 6000,
        "wind": {
            "speed": 4.0,
            "deg": 333
        },
        "clouds": {
            "all": 90
        },
        "dt": 1718870390,
        "sys": {
            "type": 1,
            "id": 9039,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200039,
        "name": "Himachal Pradesh",
        "cod": 200
    },
    "jaipur": {
        "coord": {
            "lon": 81.0,
            "lat": 19.0
        },
        "weather": [
            {
                "id": 800,
                "main": "Clear",
                "description": "clear sky",
                "icon": "01d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 303.15,
            "feels_like": 304.65,
            "temp_min": 301.15,
            "temp_max": 305.15,
            "pressure": 1010,
            "humidity": 70
        },
        "visibility": 10000,
        "wind": {
            "speed": 1.0,
            "deg": 0
        },
        "clouds": {
            "all": 0
        },
        "dt": 1718870400,
        "sys": {
            "type": 1,
            "id": 9040,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200040,
        "name": "Jaipur",
        "cod": 200
    },
    "west bengal": {
        "coord": {
            "lon": 73.7,
            "lat": 22.1
        },
        "weather": [
            {
                "id": 802,
                "main": "Clouds",
                "description": "scattered clouds",
                "icon": "03d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 301.15,
            "feels_like": 302.65,
            "temp_min": 299.15,
            "temp_max": 303.15,
            "pressure": 1011,
            "humidity": 77
        },
        "visibility": 9000,
        "wind": {
            "speed": 4.0,
            "deg": 27
        },
        "clouds": {
            "all": 40
        },
        "dt": 1718870410,
        "sys": {
            "type": 1,
            "id": 9041,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200041,
        "name": "West Bengal",
        "cod": 200
    },
    "goa": {
        "coord": {
            "lon": 76.4,
            "lat": 15.2
        },
        "weather": [
            {
                "id": 500,
                "main": "Rain",
                "description": "light rain",
                "icon": "10d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 299.15,
            "feels_like": 300.65,
            "temp_min": 297.15,
            "temp_max": 301.15,
            "pressure": 1012,
            "humidity": 84
        },
        "visibility": 8000,
        "wind": {
            "speed": 1.0,
            "deg": 54
        },
        "clouds": {
            "all": 75
        },
        "dt": 1718870420,
        "sys": {
            "type": 1,
            "id": 9042,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200042,
        "name": "Goa",
        "cod": 200
    },
    "dadra and nagar haveli and daman and diu": {
        "coord": {
            "lon": 79.1,
            "lat": 18.3
        },
        "weather": [
            {
                "id": 711,
                "main": "Smoke",
                "description": "smoke",
                "icon": "50d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 297.15,
            "feels_like": 298.65,
            "temp_min": 295.15,
            "temp_max": 299.15,
            "pressure": 1013,
            "humidity": 41
        },
        "visibility": 7000,
        "wind": {
            "speed": 4.0,
            "deg": 81
        },
        "clouds": {
            "all": 20
        },
        "dt": 1718870430,
        "sys": {
            "type": 1,
            "id": 9043,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200043,
        "name": "Dadra and Nagar Haveli and Daman and Diu",
        "cod": 200
    },
    "vadodara": {
        "coord": {
            "lon": 81.8,
            "lat": 21.4
        },
        "weather": [
            {
                "id": 200,
                "main": "Thunderstorm",
                "description": "thunderstorm with light rain",
                "icon": "11d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 295.15,
            "feels_like": 296.65,
            "temp_min": 293.15,
            "temp_max": 297.15,
            "pressure": 1014,
            "humidity": 48
        },
        "visibility": 6000,
        "wind": {
            "speed": 1.0,
            "deg": 108
        },
        "clouds": {
            "all": 90
        },
        "dt": 1718870440,
        "sys": {
            "type": 1,
            "id": 9044,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200044,
        "name": "Vadodara",
        "cod": 200
    },
    "bengaluru": {
        "coord": {
            "lon": 74.5,
            "lat": 24.5
        },
        "weather": [
            {
                "id": 800,
                "main": "Clear",
                "description": "clear sky",
                "icon": "01d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 293.15,
            "feels_like": 294.65,
            "temp_min": 291.15,
            "temp_max": 295.15,
            "pressure": 1015,
            "humidity": 55
        },
        "visibility": 10000,
        "wind": {
            "speed": 4.0,
            "deg": 135
        },
        "clouds": {
            "all": 0
        },
        "dt": 1718870450,
        "sys": {
            "type": 1,
            "id": 9045,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200045,
        "name": "Bengaluru",
        "cod": 200
    },
    "hubli-dharwad": {
        "coord": {
            "lon": 77.2,
            "lat": 17.6
        },
        "weather": [
            {
                "id": 802,
                "main": "Clouds",
                "description": "scattered clouds",
                "icon": "03d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 306.15,
            "feels_like": 307.65,
            "temp_min": 304.15,
            "temp_max": 308.15,
            "pressure": 1016,
            "humidity": 62
        },
        "visibility": 9000,
        "wind": {
            "speed": 1.0,
            "deg": 162
        },
        "clouds": {
            "all": 40
        },
        "dt": 1718870460,
        "sys": {
            "type": 1,
            "id": 9046,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200046,
        "name": "Hubli-Dharwad",
        "cod": 200
    },
    "faridabad": {
        "coord": {
            "lon": 79.9,
            "lat": 20.7
        },
        "weather": [
            {
                "id": 500,
                "main": "Rain",
                "description": "light rain",
                "icon": "10d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 304.15,
            "feels_like": 305.65,
            "temp_min": 302.15,
            "temp_max": 306.15,
            "pressure": 1017,
            "humidity": 69
        },
        "visibility": 8000,
        "wind": {
            "speed": 4.0,
            "deg": 189
        },
        "clouds": {
            "all": 75
        },
        "dt": 1718870470,
        "sys": {
            "type": 1,
            "id": 9047,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200047,
        "name": "Faridabad",
        "cod": 200
    },
    "karnataka": {
        "coord": {
            "lon": 82.6,
            "lat": 23.8
        },
        "weather": [
            {
                "id": 711,
                "main": "Smoke",
                "description": "smoke",
                "icon": "50d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 302.15,
            "feels_like": 303.65,
            "temp_min": 300.15,
            "temp_max": 304.15,
            "pressure": 1018,
            "humidity": 76
        },
        "visibility": 7000,
        "wind": {
            "speed": 1.0,
            "deg": 216
        },
        "clouds": {
            "all": 20
        },
        "dt": 1718870480,
        "sys": {
            "type": 1,
            "id": 9048,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200048,
        "name": "Karnataka",
        "cod": 200
    },
    "agra": {
        "coord": {
            "lon": 75.3,
            "lat": 16.9
        },
        "weather": [
            {
                "id": 200,
                "main": "Thunderstorm",
                "description": "thunderstorm with light rain",
                "icon": "11d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 300.15,
            "feels_like": 301.65,
            "temp_min": 298.15,
            "temp_max": 302.15,
            "pressure": 1019,
            "humidity": 83
        },
        "visibility": 6000,
        "wind": {
            "speed": 4.0,
            "deg": 243
        },
        "clouds": {
            "all": 90
        },
        "dt": 1718870490,
        "sys": {
            "type": 1,
            "id": 9049,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200049,
        "name": "Agra",
        "cod": 200
    },
    "sikkim": {
        "coord": {
            "lon": 78.0,
            "lat": 20.0
        },
        "weather": [
            {
                "id": 800,
                "main": "Clear",
                "description": "clear sky",
                "icon": "01d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 298.15,
            "feels_like": 299.65,
            "temp_min": 296.15,
            "temp_max": 300.15,
            "pressure": 1010,
            "humidity": 40
        },
        "visibility": 10000,
        "wind": {
            "speed": 1.0,
            "deg": 270
        },
        "clouds": {
            "all": 0
        },
        "dt": 1718870500,
        "sys": {
            "type": 1,
            "id": 9050,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200050,
        "name": "Sikkim",
        "cod": 200
    },
    "andhra pradesh": {
        "coord": {
            "lon": 80.7,
            "lat": 23.1
        },
        "weather": [
            {
                "id": 802,
                "main": "Clouds",
                "description": "scattered clouds",
                "icon": "03d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 296.15,
            "feels_like": 297.65,
            "temp_min": 294.15,
            "temp_max": 298.15,
            "pressure": 1011,
            "humidity": 47
        },
        "visibility": 9000,
        "wind": {
            "speed": 4.0,
            "deg": 297
        },
        "clouds": {
            "all": 40
        },
        "dt": 1718870510,
        "sys": {
            "type": 1,
            "id": 9051,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200051,
        "name": "Andhra Pradesh",
        "cod": 200
    },
    "chhattisgarh": {
        "coord": {
            "lon": 73.4,
            "lat": 16.2
        },
        "weather": [
            {
                "id": 500,
                "main": "Rain",
                "description": "light rain",
                "icon": "10d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 294.15,
            "feels_like": 295.65,
            "temp_min": 292.15,
            "temp_max": 296.15,
            "pressure": 1012,
            "humidity": 54
        },
        "visibility": 8000,
        "wind": {
            "speed": 1.0,
            "deg": 324
        },
        "clouds": {
            "all": 75
        },
        "dt": 1718870520,
        "sys": {
            "type": 1,
            "id": 9052,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200052,
        "name": "Chhattisgarh",
        "cod": 200
    },
    "lucknow": {
        "coord": {
            "lon": 76.1,
            "lat": 19.3
        },
        "weather": [
            {
                "id": 711,
                "main": "Smoke",
                "description": "smoke",
                "icon": "50d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 307.15,
            "feels_like": 308.65,
            "temp_min": 305.15,
            "temp_max": 309.15,
            "pressure": 1013,
            "humidity": 61
        },
        "visibility": 7000,
        "wind": {
            "speed": 4.0,
            "deg": 351
        },
        "clouds": {
            "all": 20
        },
        "dt": 1718870530,
        "sys": {
            "type": 1,
            "id": 9053,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200053,
        "name": "Lucknow",
        "cod": 200
    },
    "guwahati": {
        "coord": {
            "lon": 78.8,
            "lat": 22.4
        },
        "weather": [
            {
                "id": 200,
                "main": "Thunderstorm",
                "description": "thunderstorm with light rain",
                "icon": "11d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 305.15,
            "feels_like": 306.65,
            "temp_min": 303.15,
            "temp_max": 307.15,
            "pressure": 1014,
            "humidity": 68
        },
        "visibility": 6000,
        "wind": {
            "speed": 1.0,
            "deg": 18
        },
        "clouds": {
            "all": 90
        },
        "dt": 1718870540,
        "sys": {
            "type": 1,
            "id": 9054,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200054,
        "name": "Guwahati",
        "cod": 200
    },
    "bihar": {
        "coord": {
            "lon": 81.5,
            "lat": 15.5
        },
        "weather": [
            {
                "id": 800,
                "main": "Clear",
                "description": "clear sky",
                "icon": "01d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 303.15,
            "feels_like": 304.65,
            "temp_min": 301.15,
            "temp_max": 305.15,
            "pressure": 1015,
            "humidity": 75
        },
        "visibility": 10000,
        "wind": {
            "speed": 4.0,
            "deg": 45
        },
        "clouds": {
            "all": 0
        },
        "dt": 1718870550,
        "sys": {
            "type": 1,
            "id": 9055,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200055,
        "name": "Bihar",
        "cod": 200
    },
    "punjab": {
        "coord": {
            "lon": 74.2,
            "lat": 18.6
        },
        "weather": [
            {
                "id": 802,
                "main": "Clouds",
                "description": "scattered clouds",
                "icon": "03d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 301.15,
            "feels_like": 302.65,
            "temp_min": 299.15,
            "temp_max": 303.15,
            "pressure": 1016,
            "humidity": 82
        },
        "visibility": 9000,
        "wind": {
            "speed": 1.0,
            "deg": 72
        },
        "clouds": {
            "all": 40
        },
        "dt": 1718870560,
        "sys": {
            "type": 1,
            "id": 9056,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200056,
        "name": "Punjab",
        "cod": 200
    },
    "ludhiana": {
        "coord": {
            "lon": 76.9,
            "lat": 21.7
        },
        "weather": [
            {
                "id": 500,
                "main": "Rain",
                "description": "light rain",
                "icon": "10d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 299.15,
            "feels_like": 300.65,
            "temp_min": 297.15,
            "temp_max": 301.15,
            "pressure": 1017,
            "humidity": 89
        },
        "visibility": 8000,
        "wind": {
            "speed": 4.0,
            "deg": 99
        },
        "clouds": {
            "all": 75
        },
        "dt": 1718870570,
        "sys": {
            "type": 1,
            "id": 9057,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200057,
        "name": "Ludhiana",
        "cod": 200
    },
    "kota": {
        "coord": {
            "lon": 79.6,
            "lat": 24.8
        },
        "weather": [
            {
                "id": 711,
                "main": "Smoke",
                "description": "smoke",
                "icon": "50d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 297.15,
            "feels_like": 298.65,
            "temp_min": 295.15,
            "temp_max": 299.15,
            "pressure": 1018,
            "humidity": 46
        },
        "visibility": 7000,
        "wind": {
            "speed": 1.0,
            "deg": 126
        },
        "clouds": {
            "all": 20
        },
        "dt": 1718870580,
        "sys": {
            "type": 1,
            "id": 9058,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200058,
        "name": "Kota",
        "cod": 200
    },
    "assam": {
        "coord": {
            "lon": 82.3,
            "lat": 17.9
        },
        "weather": [
            {
                "id": 200,
                "main": "Thunderstorm",
                "description": "thunderstorm with light rain",
                "icon": "11d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 295.15,
            "feels_like": 296.65,
            "temp_min": 293.15,
            "temp_max": 297.15,
            "pressure": 1019,
            "humidity": 53
        },
        "visibility": 6000,
        "wind": {
            "speed": 4.0,
            "deg": 153
        },
        "clouds": {
            "all": 90
        },
        "dt": 1718870590,
        "sys": {
            "type": 1,
            "id": 9059,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200059,
        "name": "Assam",
        "cod": 200
    },
    "mizoram": {
        "coord": {
            "lon": 75.0,
            "lat": 21.0
        },
        "weather": [
            {
                "id": 800,
                "main": "Clear",
                "description": "clear sky",
                "icon": "01d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 293.15,
            "feels_like": 294.65,
            "temp_min": 291.15,
            "temp_max": 295.15,
            "pressure": 1010,
            "humidity": 60
        },
        "visibility": 10000,
        "wind": {
            "speed": 1.0,
            "deg": 180
        },
        "clouds": {
            "all": 0
        },
        "dt": 1718870600,
        "sys": {
            "type": 1,
            "id": 9060,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200060,
        "name": "Mizoram",
        "cod": 200
    },
    "madhya pradesh": {
        "coord": {
            "lon": 77.7,
            "lat": 24.1
        },
        "weather": [
            {
                "id": 802,
                "main": "Clouds",
                "description": "scattered clouds",
                "icon": "03d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 306.15,
            "feels_like": 307.65,
            "temp_min": 304.15,
            "temp_max": 308.15,
            "pressure": 1011,
            "humidity": 67
        },
        "visibility": 9000,
        "wind": {
            "speed": 4.0,
            "deg": 207
        },
        "clouds": {
            "all": 40
        },
        "dt": 1718870610,
        "sys": {
            "type": 1,
            "id": 9061,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200061,
        "name": "Madhya Pradesh",
        "cod": 200
    },
    "gwalior": {
        "coord": {
            "lon": 80.4,
            "lat": 17.2
        },
        "weather": [
            {
                "id": 500,
                "main": "Rain",
                "description": "light rain",
                "icon": "10d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 304.15,
            "feels_like": 305.65,
            "temp_min": 302.15,
            "temp_max": 306.15,
            "pressure": 1012,
            "humidity": 74
        },
        "visibility": 8000,
        "wind": {
            "speed": 1.0,
            "deg": 234
        },
        "clouds": {
            "all": 75
        },
        "dt": 1718870620,
        "sys": {
            "type": 1,
            "id": 9062,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200062,
        "name": "Gwalior",
        "cod": 200
    },
    "solapur": {
        "coord": {
            "lon": 73.1,
            "lat": 20.3
        },
        "weather": [
            {
                "id": 711,
                "main": "Smoke",
                "description": "smoke",
                "icon": "50d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 302.15,
            "feels_like": 303.65,
            "temp_min": 300.15,
            "temp_max": 304.15,
            "pressure": 1013,
            "humidity": 81
        },
        "visibility": 7000,
        "wind": {
            "speed": 4.0,
            "deg": 261
        },
        "clouds": {
            "all": 20
        },
        "dt": 1718870630,
        "sys": {
            "type": 1,
            "id": 9063,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200063,
        "name": "Solapur",
        "cod": 200
    },
    "lakshadweep": {
        "coord": {
            "lon": 75.8,
            "lat": 23.4
        },
        "weather": [
            {
                "id": 200,
                "main": "Thunderstorm",
                "description": "thunderstorm with light rain",
                "icon": "11d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 300.15,
            "feels_like": 301.65,
            "temp_min": 298.15,
            "temp_max": 302.15,
            "pressure": 1014,
            "humidity": 88
        },
        "visibility": 6000,
        "wind": {
            "speed": 1.0,
            "deg": 288
        },
        "clouds": {
            "all": 90
        },
        "dt": 1718870640,
        "sys": {
            "type": 1,
            "id": 9064,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200064,
        "name": "Lakshadweep",
        "cod": 200
    },
    "dhanbad": {
        "coord": {
            "lon": 78.5,
            "lat": 16.5
        },
        "weather": [
            {
                "id": 800,
                "main": "Clear",
                "description": "clear sky",
                "icon": "01d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 298.15,
            "feels_like": 299.65,
            "temp_min": 296.15,
            "temp_max": 300.15,
            "pressure": 1015,
            "humidity": 45
        },
        "visibility": 10000,
        "wind": {
            "speed": 4.0,
            "deg": 315
        },
        "clouds": {
            "all": 0
        },
        "dt": 1718870650,
        "sys": {
            "type": 1,
            "id": 9065,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200065,
        "name": "Dhanbad",
        "cod": 200
    },
    "ghaziabad": {
        "coord": {
            "lon": 81.2,
            "lat": 19.6
        },
        "weather": [
            {
                "id": 802,
                "main": "Clouds",
                "description": "scattered clouds",
                "icon": "03d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 296.15,
            "feels_like": 297.65,
            "temp_min": 294.15,
            "temp_max": 298.15,
            "pressure": 1016,
            "humidity": 52
        },
        "visibility": 9000,
        "wind": {
            "speed": 1.0,
            "deg": 342
        },
        "clouds": {
            "all": 40
        },
        "dt": 1718870660,
        "sys": {
            "type": 1,
            "id": 9066,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200066,
        "name": "Ghaziabad",
        "cod": 200
    },
    "allahabad": {
        "coord": {
            "lon": 73.9,
            "lat": 22.7
        },
        "weather": [
            {
                "id": 500,
                "main": "Rain",
                "description": "light rain",
                "icon": "10d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 294.15,
            "feels_like": 295.65,
            "temp_min": 292.15,
            "temp_max": 296.15,
            "pressure": 1017,
            "humidity": 59
        },
        "visibility": 8000,
        "wind": {
            "speed": 4.0,
            "deg": 9
        },
        "clouds": {
            "all": 75
        },
        "dt": 1718870670,
        "sys": {
            "type": 1,
            "id": 9067,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200067,
        "name": "Allahabad",
        "cod": 200
    },
    "kolkata": {
        "coord": {
            "lon": 76.6,
            "lat": 15.8
        },
        "weather": [
            {
                "id": 711,
                "main": "Smoke",
                "description": "smoke",
                "icon": "50d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 307.15,
            "feels_like": 308.65,
            "temp_min": 305.15,
            "temp_max": 309.15,
            "pressure": 1018,
            "humidity": 66
        },
        "visibility": 7000,
        "wind": {
            "speed": 1.0,
            "deg": 36
        },
        "clouds": {
            "all": 20
        },
        "dt": 1718870680,
        "sys": {
            "type": 1,
            "id": 9068,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200068,
        "name": "Kolkata",
        "cod": 200
    },
    "raipur": {
        "coord": {
            "lon": 79.3,
            "lat": 18.9
        },
        "weather": [
            {
                "id": 200,
                "main": "Thunderstorm",
                "description": "thunderstorm with light rain",
                "icon": "11d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 305.15,
            "feels_like": 306.65,
            "temp_min": 303.15,
            "temp_max": 307.15,
            "pressure": 1019,
            "humidity": 73
        },
        "visibility": 6000,
        "wind": {
            "speed": 4.0,
            "deg": 63
        },
        "clouds": {
            "all": 90
        },
        "dt": 1718870690,
        "sys": {
            "type": 1,
            "id": 9069,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200069,
        "name": "Raipur",
        "cod": 200
    },
    "kanpur": {
        "coord": {
            "lon": 82.0,
            "lat": 22.0
        },
        "weather": [
            {
                "id": 800,
                "main": "Clear",
                "description": "clear sky",
                "icon": "01d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 303.15,
            "feels_like": 304.65,
            "temp_min": 301.15,
            "temp_max": 305.15,
            "pressure": 1010,
            "humidity": 80
        },
        "visibility": 10000,
        "wind": {
            "speed": 1.0,
            "deg": 90
        },
        "clouds": {
            "all": 0
        },
        "dt": 1718870700,
        "sys": {
            "type": 1,
            "id": 9070,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200070,
        "name": "Kanpur",
        "cod": 200
    },
    "hyderabad": {
        "coord": {
            "lon": 74.7,
            "lat": 15.1
        },
        "weather": [
            {
                "id": 802,
                "main": "Clouds",
                "description": "scattered clouds",
                "icon": "03d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 301.15,
            "feels_like": 302.65,
            "temp_min": 299.15,
            "temp_max": 303.15,
            "pressure": 1011,
            "humidity": 87
        },
        "visibility": 9000,
        "wind": {
            "speed": 4.0,
            "deg": 117
        },
        "clouds": {
            "all": 40
        },
        "dt": 1718870710,
        "sys": {
            "type": 1,
            "id": 9071,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200071,
        "name": "Hyderabad",
        "cod": 200
    },
    "bangalore": {
        "coord": {
            "lon": 77.4,
            "lat": 18.2
        },
        "weather": [
            {
                "id": 500,
                "main": "Rain",
                "description": "light rain",
                "icon": "10d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 299.15,
            "feels_like": 300.65,
            "temp_min": 297.15,
            "temp_max": 301.15,
            "pressure": 1012,
            "humidity": 44
        },
        "visibility": 8000,
        "wind": {
            "speed": 1.0,
            "deg": 144
        },
        "clouds": {
            "all": 75
        },
        "dt": 1718870720,
        "sys": {
            "type": 1,
            "id": 9072,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200072,
        "name": "Bangalore",
        "cod": 200
    },
    "ahmedabad": {
        "coord": {
            "lon": 80.1,
            "lat": 21.3
        },
        "weather": [
            {
                "id": 711,
                "main": "Smoke",
                "description": "smoke",
                "icon": "50d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 297.15,
            "feels_like": 298.65,
            "temp_min": 295.15,
            "temp_max": 299.15,
            "pressure": 1013,
            "humidity": 51
        },
        "visibility": 7000,
        "wind": {
            "speed": 4.0,
            "deg": 171
        },
        "clouds": {
            "all": 20
        },
        "dt": 1718870730,
        "sys": {
            "type": 1,
            "id": 9073,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200073,
        "name": "Ahmedabad",
        "cod": 200
    },
    "kalyan-dombivli": {
        "coord": {
            "lon": 82.8,
            "lat": 24.4
        },
        "weather": [
            {
                "id": 200,
                "main": "Thunderstorm",
                "description": "thunderstorm with light rain",
                "icon": "11d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 295.15,
            "feels_like": 296.65,
            "temp_min": 293.15,
            "temp_max": 297.15,
            "pressure": 1014,
            "humidity": 58
        },
        "visibility": 6000,
        "wind": {
            "speed": 1.0,
            "deg": 198
        },
        "clouds": {
            "all": 90
        },
        "dt": 1718870740,
        "sys": {
            "type": 1,
            "id": 9074,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200074,
        "name": "Kalyan-Dombivli",
        "cod": 200
    },
    "andaman and nicobar islands": {
        "coord": {
            "lon": 75.5,
            "lat": 17.5
        },
        "weather": [
            {
                "id": 800,
                "main": "Clear",
                "description": "clear sky",
                "icon": "01d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 293.15,
            "feels_like": 294.65,
            "temp_min": 291.15,
            "temp_max": 295.15,
            "pressure": 1015,
            "humidity": 65
        },
        "visibility": 10000,
        "wind": {
            "speed": 4.0,
            "deg": 225
        },
        "clouds": {
            "all": 0
        },
        "dt": 1718870750,
        "sys": {
            "type": 1,
            "id": 9075,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200075,
        "name": "Andaman and Nicobar Islands",
        "cod": 200
    },
    "jammu and kashmir": {
        "coord": {
            "lon": 78.2,
            "lat": 20.6
        },
        "weather": [
            {
                "id": 802,
                "main": "Clouds",
                "description": "scattered clouds",
                "icon": "03d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 291.15,
            "feels_like": 292.65,
            "temp_min": 289.15,
            "temp_max": 293.15,
            "pressure": 1016,
            "humidity": 72
        },
        "visibility": 9000,
        "wind": {
            "speed": 1.0,
            "deg": 252
        },
        "clouds": {
            "all": 40
        },
        "dt": 1718870760,
        "sys": {
            "type": 1,
            "id": 9076,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200076,
        "name": "Jammu and Kashmir",
        "cod": 200
    },
    "visakhapatnam": {
        "coord": {
            "lon": 80.9,
            "lat": 23.7
        },
        "weather": [
            {
                "id": 500,
                "main": "Rain",
                "description": "light rain",
                "icon": "10d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 304.15,
            "feels_like": 305.65,
            "temp_min": 302.15,
            "temp_max": 306.15,
            "pressure": 1017,
            "humidity": 79
        },
        "visibility": 8000,
        "wind": {
            "speed": 4.0,
            "deg": 279
        },
        "clouds": {
            "all": 75
        },
        "dt": 1718870770,
        "sys": {
            "type": 1,
            "id": 9077,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200077,
        "name": "Visakhapatnam",
        "cod": 200
    },
    "navi mumbai": {
        "coord": {
            "lon": 73.6,
            "lat": 16.8
        },
        "weather": [
            {
                "id": 711,
                "main": "Smoke",
                "description": "smoke",
                "icon": "50d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 302.15,
            "feels_like": 303.65,
            "temp_min": 300.15,
            "temp_max": 304.15,
            "pressure": 1018,
            "humidity": 86
        },
        "visibility": 7000,
        "wind": {
            "speed": 1.0,
            "deg": 306
        },
        "clouds": {
            "all": 20
        },
        "dt": 1718870780,
        "sys": {
            "type": 1,
            "id": 9078,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200078,
        "name": "Navi Mumbai",
        "cod": 200
    },
    "howrah": {
        "coord": {
            "lon": 76.3,
            "lat": 19.9
        },
        "weather": [
            {
                "id": 200,
                "main": "Thunderstorm",
                "description": "thunderstorm with light rain",
                "icon": "11d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 300.15,
            "feels_like": 301.65,
            "temp_min": 298.15,
            "temp_max": 302.15,
            "pressure": 1019,
            "humidity": 43
        },
        "visibility": 6000,
        "wind": {
            "speed": 4.0,
            "deg": 333
        },
        "clouds": {
            "all": 90
        },
        "dt": 1718870790,
        "sys": {
            "type": 1,
            "id": 9079,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200079,
        "name": "Howrah",
        "cod": 200
    },
    "vijayawada": {
        "coord": {
            "lon": 79.0,
            "lat": 23.0
        },
        "weather": [
            {
                "id": 800,
                "main": "Clear",
                "description": "clear sky",
                "icon": "01d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 298.15,
            "feels_like": 299.65,
            "temp_min": 296.15,
            "temp_max": 300.15,
            "pressure": 1010,
            "humidity": 50
        },
        "visibility": 10000,
        "wind": {
            "speed": 1.0,
            "deg": 0
        },
        "clouds": {
            "all": 0
        },
        "dt": 1718870800,
        "sys": {
            "type": 1,
            "id": 9080,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200080,
        "name": "Vijayawada",
        "cod": 200
    },
    "surat": {
        "coord": {
            "lon": 81.7,
            "lat": 16.1
        },
        "weather": [
            {
                "id": 802,
                "main": "Clouds",
                "description": "scattered clouds",
                "icon": "03d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 296.15,
            "feels_like": 297.65,
            "temp_min": 294.15,
            "temp_max": 298.15,
            "pressure": 1011,
            "humidity": 57
        },
        "visibility": 9000,
        "wind": {
            "speed": 4.0,
            "deg": 27
        },
        "clouds": {
            "all": 40
        },
        "dt": 1718870810,
        "sys": {
            "type": 1,
            "id": 9081,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200081,
        "name": "Surat",
        "cod": 200
    },
    "varanasi": {
        "coord": {
            "lon": 74.4,
            "lat": 19.2
        },
        "weather": [
            {
                "id": 500,
                "main": "Rain",
                "description": "light rain",
                "icon": "10d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 294.15,
            "feels_like": 295.65,
            "temp_min": 292.15,
            "temp_max": 296.15,
            "pressure": 1012,
            "humidity": 64
        },
        "visibility": 8000,
        "wind": {
            "speed": 1.0,
            "deg": 54
        },
        "clouds": {
            "all": 75
        },
        "dt": 1718870820,
        "sys": {
            "type": 1,
            "id": 9082,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200082,
        "name": "Varanasi",
        "cod": 200
    },
    "aurangabad": {
        "coord": {
            "lon": 77.1,
            "lat": 22.3
        },
        "weather": [
            {
                "id": 711,
                "main": "Smoke",
                "description": "smoke",
                "icon": "50d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 307.15,
            "feels_like": 308.65,
            "temp_min": 305.15,
            "temp_max": 309.15,
            "pressure": 1013,
            "humidity": 71
        },
        "visibility": 7000,
        "wind": {
            "speed": 4.0,
            "deg": 81
        },
        "clouds": {
            "all": 20
        },
        "dt": 1718870830,
        "sys": {
            "type": 1,
            "id": 9083,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200083,
        "name": "Aurangabad",
        "cod": 200
    },
    "bhopal": {
        "coord": {
            "lon": 79.8,
            "lat": 15.4
        },
        "weather": [
            {
                "id": 200,
                "main": "Thunderstorm",
                "description": "thunderstorm with light rain",
                "icon": "11d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 305.15,
            "feels_like": 306.65,
            "temp_min": 303.15,
            "temp_max": 307.15,
            "pressure": 1014,
            "humidity": 78
        },
        "visibility": 6000,
        "wind": {
            "speed": 1.0,
            "deg": 108
        },
        "clouds": {
            "all": 90
        },
        "dt": 1718870840,
        "sys": {
            "type": 1,
            "id": 9084,
            "country": "IN",
            "sunrise": 1718843516,
            "sunset": 1718891156
        },
        "timezone": 19800,
        "id": 1200084,
        "name": "Bhopal",
        "cod": 200
    }
}
