import weather_etl
import weather_data_requests as weather_req

if __name__ == "__main__":
    weather_req.request_new_weather_data()  # Uncomment to initialize requests

    weather_etl.transform_weather()
