


import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager


def scrape_data():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    #pass through url
    url="https://redplanetscience.com/"
    browser.visit(url)

    html=browser.html
    webpage=BeautifulSoup(html,'html.parser')


    # lets grab the most recent news article
    most_recent_title=webpage.find_all('div',class_='content_title')
    most_recent_title=most_recent_title[0].text
    most_recent_title

    #Lets grab the 'paragraph' for that article
    most_recent_title_paragraph=webpage.find_all('div',class_='article_teaser_body')
    most_recent_title_paragraph=most_recent_title_paragraph[0].text
    most_recent_title_paragraph


    # # Featured Image Section

    #lets pass through our new url to then grab the featured mars image.
    #pass through our new url which will be re-directed to in chrome pop up window
    url_2="https://spaceimages-mars.com"
    browser.visit(url_2)

    html=browser.html
    imagepage=BeautifulSoup(html,'html.parser')



    #lets grab the main featured image for Mars
    featured_image_url=browser.links.find_by_partial_href('featured')
    featured_image_url=featured_image_url['href']
    featured_image_url


    # # Mars Facts Section
    # 


    #pass through our new url which will be re-directed to in chrome pop up window
    url_3="https://galaxyfacts-mars.com"



    table=pd.read_html(url_3)
    mars_earth_comparison=table[0]
    mars_earth_comparison



    #express the data from the table as an HTML Table String. WE ADDED MORE PERAMETERS TO MAKE OUR TABLE PRETTIER
    mars_earth_compare_string=mars_earth_comparison.to_html(header = False, index = False, classes= "table table-striped") 
    mars_earth_facts=mars_earth_compare_string.replace('\n','')
    mars_earth_facts


    # # Mars Hemispheres Section

    # * Click on the link to the hemispheres in the chrome pop-up windown in order to find the image url
    #to the full resolution image.
    #For Cerebrus Hemisphere
    url_4="https://marshemispheres.com/cerberus.html"
    browser.visit(url_4)

    html=browser.html
    mars_hemispheres=BeautifulSoup(html,'html.parser')

    mars_hemispheres_images=browser.links.find_by_partial_href('.jpg')
    cerebrus_img=mars_hemispheres_images['href']
    cerebrus_img


    # * Click on the link to the hemispheres in the chrome pop-up windown in order to find the image url
    #to the full resolution image.
    #For Schiaparelli Hemisphere 
    url_5="https://marshemispheres.com/schiaparelli.html"
    browser.visit(url_5)

    html=browser.html
    mars_hemispheres=BeautifulSoup(html,'html.parser')

    mars_hemispheres_images=browser.links.find_by_partial_href('enhanced')
    schiap_img=mars_hemispheres_images['href']
    schiap_img


    # * Click on the link to the hemispheres in the chrome pop-up windown in order to find the image url
    #to the full resolution image.
    #For Syrtis Major Hemisphere
    url_6="https://marshemispheres.com/syrtis.html"
    browser.visit(url_6)

    html=browser.html
    mars_hemispheres=BeautifulSoup(html,'html.parser')


    mars_hemispheres_images=browser.links.find_by_partial_href('enhanced')
    syrtmaj_img=mars_hemispheres_images['href']
    syrtmaj_img



    # * Click on the link to the hemispheres in the chrome pop-up windown in order to find the image url
    #to the full resolution image.
    #For Valles Marineris Hemisphere
    url_7="https://marshemispheres.com/valles.html"
    browser.visit(url_7)

    html=browser.html
    mars_hemispheres=BeautifulSoup(html,'html.parser')

    mars_hemispheres_images=browser.links.find_by_partial_href('enhanced')
    valmar_img=mars_hemispheres_images['href']
    valmar_img


    #Go back to main "https://marshemispheres.com/" page in chrome pop-up window which shows all four hemipheres 
    #scraping titles
    url_8="https://marshemispheres.com/"
    browser.visit(url_8)

    html=browser.html
    hemisphere_titles=BeautifulSoup(html,'html.parser')

    #scrape titles and clean them to drop "Enhanced"
    #Scraping for Cerberus Hemisphere Title
    titles_mars_hemispheres=hemisphere_titles.find_all('h3')
    cerberus_title=titles_mars_hemispheres[0].text
    cerberus_title

    cleaned_cerberus=cerberus_title.replace('Enhanced', '')
    cleaned_cerberus_title=cleaned_cerberus.strip(' ')
    cleaned_cerberus_title

    #Scraping for Schiaparelli Hemisphere Title
    titles_mars_hemispheres=hemisphere_titles.find_all('h3')
    schiap_title=titles_mars_hemispheres[1].text
    schiap_title

    cleaned_schiap=schiap_title.replace('Enhanced','')
    cleaned_schiap_title=cleaned_schiap.strip(' ')
    cleaned_schiap_title

    #Scraping for Syrtis Major Hemisphere Title
    titles_mars_hemispheres=hemisphere_titles.find_all('h3')
    syrtmaj_title=titles_mars_hemispheres[2].text
    syrtmaj_title

    cleaned_syrtmaj=syrtmaj_title.replace('Enhanced','')
    cleaned_syrtmaj_title=cleaned_syrtmaj.strip(' ')
    cleaned_syrtmaj_title

    #Scraping for Valles Marineris Hemisphere Title
    titles_mars_hemispheres=hemisphere_titles.find_all('h3')
    valmar_title=titles_mars_hemispheres[3].text
    valmar_title

    cleaned_valmar=valmar_title.replace('Enhanced','')
    cleaned_valmar_title=cleaned_valmar.strip(' ')
    cleaned_valmar_title



    mars_hemispheres_list=[]
    mars_hems_dict={
        "title": cleaned_cerberus_title, 
        "img_url": cerebrus_img
        
    }
    mars_hemispheres_list.append(mars_hems_dict)
    mars_hems_dict={
        "title": cleaned_schiap_title , 
        "img_url": schiap_img
        
    }
    mars_hemispheres_list.append(mars_hems_dict)
    mars_hems_dict={
        "title": cleaned_syrtmaj_title , 
        "img_url": syrtmaj_img
        
    }
    mars_hemispheres_list.append(mars_hems_dict)
    mars_hems_dict={
        "title": cleaned_valmar_title , 
        "img_url": valmar_img
        
    }
    mars_hemispheres_list.append(mars_hems_dict)

    mars_hemispheres_list

    mars_data = {
        "latest_mars_article": most_recent_title,
        "latest_article_par" : most_recent_title_paragraph,
        "mars_feat_img" : featured_image_url,
        "mars_earth_table": mars_earth_facts,
        "hems_titles_imgs" : mars_hemispheres_list

    }

    browser.quit()

    return(mars_data)


