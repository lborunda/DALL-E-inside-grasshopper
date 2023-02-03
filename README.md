# DALL-E-inside-grasshopper
Python script to input prompts and output images (URL) in Rhino/Grasshopper. Created entirely using ChatGPT.

Image Generation with OpenAI DALL-E API
This code was created by ChatGPT and Luis Borunda, and is based on the work of Juan Pablo Arango. It uses the OpenAI DALL-E API to generate an image based on a textual description.

Requirements
A valid OpenAI API key
Ladybug to load "LBImageViewer" component

Usage
Replace api_key in the code with your own OpenAI API key.
Run the code, providing the desired description of the image as the prompt.
The code will print the URL of the generated image.
The script saves the URL to "image.jpg" in /user directory

Note
You can load the image with the "LBImageViewer" component connecting the "answer" output
Be sure to review and comply with the OpenAI API terms and conditions when using the DALL-E API.
