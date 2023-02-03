#Created by ChatGPT and Luis Borunda 

import urllib2
import base64
import json
import os
import urllib2
import platform




if send == True:

    # The URL of the DALL-E API endpoint
    url = "https://api.openai.com/v1/images/generations"

    # The description of the image you want to generate
    description = prompt

    # The model to use for image generation
    model = "image-alpha-001"

    # Build the request headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + api_key
    }

    # Build the request data
    data = {
        "model": model,
        "prompt": description
    }

    # Convert the request data to a JSON string
    data = json.dumps(data)

    # Build the request object
    req = urllib2.Request(url, data, headers)

    # Send the request and get the response
    response = urllib2.urlopen(req)

    # Read the response data
    response_data = response.read()

    # Convert the response data from JSON to a Python dictionary
    response_dict = json.loads(response_data)

    # Get the URL of the generated image
    image_url = response_dict["data"][0]["url"]

    # Print the URL of the generated image
    print("Image URL: " + image_url)


    # Identify if working in mac or windows

    if platform.system() == "Windows":
        system = "windows"
    elif platform.system() == "Darwin":
        system = "mac"
    else:
        print("Your operating system is not Windows or Mac.")

    # Save to /user from the URL of the generated image
    url = image_url
    response = urllib2.urlopen(url)


    if system == "mac":
        filename = os.path.expanduser("~/image.jpg")
        with open(filename, "wb") as f:
            f.write(response.read())
        answer = filename

    if system == "windows":
        filename = os.path.expanduser(r"~\image2.jpg")
        with open(filename, "wb") as f:
            f.write(response.read())
        answer = filename



