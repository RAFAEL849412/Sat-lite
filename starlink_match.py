import requests
import matplotlib.pyplot as plt
import numpy as np
import time
from skyfield.api import Topos, load  # Correct import
import tempfile

def test_w_sp_py_lib(site_url, file_path, username, password):
    from office365.sharepoint.client_context import ClientContext

    ctx = ClientContext(site_url).with_user_credentials(username, password)
    web = ctx.web.get().execute_query()
    print(web.url)

    file = ctx.web.get_file_by_server_relative_path(file_path).get().execute_query()
    print("File size: ", file.length)
    print("File name: ", file.name)
    print("File url: ", file.serverRelativeUrl)

def download_tle():
    url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=starlink&FORMAT=tle"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for 4xx/5xx status codes
        with open('starlink.tle', 'w') as file:
            file.write(response.text)
        print("TLE data downloaded successfully.")
    except requests.RequestException as e:
        print(f"Error downloading TLE: {e}")

def get_location():
    # Example fixed location: New York (latitude and longitude)
    return Topos(latitude_degrees=40.7128, longitude_degrees=-74.0060)

def config_website():
    try:
        with open('website-config.py', 'r') as file:
            config = file.read()
            print("Website configuration loaded successfully.")
            print(config)
    except FileNotFoundError:
        print("Website configuration file not found.")

def main():
    # Download TLE data (if necessary)
    download_tle()

    # Load TLE data
    satellites = load.tle_file('starlink.tle')

    # Get observer location
    observer_location = get_location()

    # Get timescale
    ts = load.timescale()

    # Get current time
    t = ts.now()

    # Observe each satellite and calculate its position
    for satellite in satellites:
        difference = satellite - observer_location
        topocentric = difference.at(t)

        # Get altitude and azimuth
        alt, az, distance = topocentric.altaz()

        # Check if the satellite is visible (above 40 degrees altitude)
        if alt.degrees > 40:
            print(f"{satellite.name} - Altitude: {alt.degrees:.2f}°, Azimuth: {az.degrees:.2f}°")

            # Plot the satellite's position
            plt.figure(figsize=(6, 6))
            plt.polar([0, np.radians(az.degrees)], [0, 90 - alt.degrees], marker='o')

    plt.show()

    # Call website configuration
    config_website()

if __name__ == "__main__":
    main()
