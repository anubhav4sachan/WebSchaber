# WebSchaber

The WebSchaber is Python3 script which extracts the text and images content on search engine `bing.com`

It helps the user in a way that the user will be getting only meaningful results and images for their search query. It does not download the ad content and hence saving data for the user.

It requests for a search term and creates directory (if not made previously) in the root directory of the script where all the content of the related particular search is stored. This python script will be downloading the hypertext and hyperlink to that text and saving it to a .txt file within the directory made by the script itself. This directory saves the text content as well as the images downloaded using the script.

## Requirements
`1.	Modules:

    a. requests: Used for requesting various content through two possible HTTPS Methods: GET and POST.
                 This project uses GET Method.
        
    b. BeautifulSoup: Used for creating JSON like dictionary using HTML Parser. This project uses bs4.
    
    c. os: Used for checking and making directories.
    
    d. PIL.Image: Used for extracting image content.
    
    e. io.ByteIO: Used for saving the extracted image using the PIL.Image.
 
2.	Internet Connection: Continuous high speed internet connection is required for the proper function of the python script as it           continuously creates the copy of the images to the local machine.
`
## Installation

`pip install webschaber`
